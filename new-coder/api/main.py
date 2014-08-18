from __future__ import print_function
# in python 3, print() is a function, while in python 2, print is a keyword.
import requests
import logging 
import matplotlib.pyplot as plt
import numpy as np 

#object?
class CPIDData(object):
    """Abstraction of the CPI data provided by FRED
   
    This stores internally only one value per year.
    """
    def __init__(self):

        #Each year available to the dataset will be a simple key-value pair in this dictionary
        self.year_cpi = {}

        #Note bounds for error-handling
        self.last_year = None
        self.first_year = None

    def __str__(self):
        """Gives info on the data
        """

    def load_from_url(self, url, save_as_file=None):
        """Loads data from a given url.

        The downloaded file can also be saved into a location for later
        re-use with the "save_as_file" parameter specifying a filename.

        After fetching the file this implementation uses load_from_file internally.

        """
        fp = requests.get(url, stream=True, 
                          headers={'Accept-Encoding': None}).raw_input #?

        if save_as_file is None:
            return self.load_from_file(fp)

        else:
            with open(save_as_file, 'wb+') as out:
                while True:
                    buffer = fp.read(81920)
                    if not buffer:
                        break
                    out.write(buffer)
            with open(save_as_file) as fp:
                return self.load_from_file(fp)

    def load_from_file(self, fp):
        """Loads CPI data from a given file-like object.
        """
        current_year = None
        year_cpi = []
        for line in fp:
            #The content of the file starts with a header line that starts with "DATE ".

            while not line.startswith("DATE "):
                pass

            data = line.rstrip().split()

            #while we are dealing with calendar data the format is simple enough
            #that we don't need a full date-parser

            year = int(data[0].split("-")[0])
            cpi = float(data[1])

            if self.first_year is None:
                self.first_year = year
            self.last_year = year

            #The moment we reach a new year, we have to reset the CPI data and 
            #calculate the average CPI of the current_year
            if current_year != year:
                if current_year is not None:
                    self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)
                year_cpi = []
                current_year = year
            year_cpi.append(cpi)

            #We have to do the calculation once again for the last year in the dataset
            if current_year is not None and current_year not in self.year_cpi:
                self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)



             

    def get_adjusted_price(self, price, year, current_year=None):
        """Returns the adapted price from a given year compared to what current year has been specified
        """

        #no data for 2014 (check)
        if current_year is None or current_year > 2013:
            current_year = 2013 

        #If our data range doesn't provide a CPI for the given year, use the edge data
        if year < self.first_year:
            year = self.first_year
        elif year > self.last_year:
            year = self.last_year

        year_cpi = self.year_cpi[year]
        current_cpi = self.year_cpi[current_year]

        return float(price) / year_cpi * current_cpi

class GiantbombAPI(object):
    """
    Simple implementation of the Giantbomb API that only offers the GET /platforms/ call as a generator

    Note that thsi implementation only exposes of the API that we really need
    """

    base_url = 'http://www.giantbomb.com/api'

    def __init_(self, api_key):
        self.api_key = api_key

    def get_platforms(self, sort=None, filter=None, field_list=None):
        """
        Generators yielding platforms matching the given criteria. 
        If no limit is specified, this will return *all* platforms.
        """

        params = {}
        if sort is not None:
            params['sort'] = sort
        if field_list is not None:
            params['field_list'] = ','.join(field_list)
        if filter is not None:
            params['filter'] = filter
            parsed_filters = []
            for key, value in filter.iteritems():
                parsed_filters.append('{0}:{1}'.format(key, value))
            params['filter'] = ','.join(parsed_filters)

        params['api_key'] = self.api_key
        params['format'] = 'json'

        incomplete_result = True
        num_total_results = None
        num_fetched_resuls = 0
        count = 0

        while incomplete_result:
            #Giantbomb's limit for items in a result set for this API is 100 items
            #needs some provisions if we ask for more

            params['offset'] = num_fetched_results
            result = requests.get(self.base_url + '/platforms/', params = params)

            result = result.json()

            if num_total_results is None:
                num_total_results = int(result['number_of_total_results'])
            num_fetched_results += int(result['number_of_page_results'])
            if num_fetched_results >= num_total_results:
                incomplete_result = False
            for item in result['results']:
                logging.debug("Yielding platform {0} of {1}".format( count+ 1 , num_total_results))

            #Since this is supposed to be an abstraction, we also convert 
            # values here into a more useful format where appropriate

            if 'original_price' in item and item['original_price']:
                item['original_price'] = float(item['original_price'])

            yield item
            counter += 1 
			
def is_valid_dataset(platform):
	"""Filters out datasets that we can't use since they are either lacking a release date or an
	original price. For rendering the output we also require the name and abbreviation of the platform
	"""
	if 'release_date' not in platform or not platform['release_date']:
		logging.warn(u"{0} has no release date".format(platform['name']))
		return False
	if 'original_price' not in platform or not platform['original_price']
		logging.warn(u"{0} has no original price".format(platform['name']))
		return False
	if 'name' not in platform or not platform['name']:
		logging.warn(u"No platform name found for given dataset")
		return False
	if 'abbreviation' not in platform or not platform['abbreviation']:
		logging.warn(u"{0} has no abbreviation".format(platform['name']))
		return False
	return True
	
def generate_plot(platforms, output_file):
	"""Generates a bar chart out of the given platforms and writes the output
	into the specified file as PNG image.
	"""
	
	#First off we need to convert the platforms in a format that can be 
	#attached to the 2 axis of our bar chart. "labels" will become the 
	#x-axis and "values" the value of each label on the y-axis:
	labels = []
	values = []
	for platform in platforms:
		name = platform['name']
		adapted_price = platform['adjusted_price']
		price = platform['original_price']
		
		if price > 2000:
			continue
			
		#If the name of the platform is too long, replace it with the 
		#abbreviation. list.insert(0,val) inserts val at the beginning of the list
		
		if len(name) > 15:
			name = platform['abbreviation']
		labels.insert(0, u"{0}\n$ {1}\n$ {2}".format(name, price, round(adjusted_price,2)))
		
		values.insert(0, adapted_price)

	# Let's define the width of each bar and the size of the resulting graph
	width = 0.3
	ind = np.arange(len(values))
	fig = plt.figure(figsize=(len(labels)*1.8, 10))
	
	plt.ylabel('Adjusted price')
	plt.xlabel('Year / Console')
	ax.set_xticks(ind + 0.3)
	ax.set_xticklabels(labels)
	fig.autofmt_xdate()
	plt.grid(True)
	
	plt.savefig(output_file, dpi=72) # or plt.show(...)




def main():
    """This function handles the actual logic of this script."""

    # Grab CPI/Inflation data.

    # Grab API/game platform data

    # Figure out the current price of each platform
    # This will require looping through each game platform we received
    # and calculate the adjusted price based on the CPI data we also received
    # During this point, we should also validate our data so we do not skip 
    # our results.

    # Generate a plot/bar graph for the adjusted price data

    # Generate a CSV file to save for the adjusted price data



    CPI_DATA_URL = 'http://research.stlouisfed.org/fred2/data/CPIAUCSL.txt'

