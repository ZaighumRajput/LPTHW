def scan(string):
    """
    :param argv: takes in a list of arguments
    :then associates certain words with their category
    in particular
    Direction words: north, south, east, west, down, up, left, right, back.
    Verbs: go, stop, kill, eat.
    Stop words: the, in, of, from, at, it
    Nouns: door, bear, princess, cabinet.
    Numbers: any string of 0 through 9 characters.

    so if "south go" is passed
    it returns [('direction', 'north'), ('go', 'verb')]
    """

    #how do we store our lexicon?
    #dictionary
    #which is the key and which is the value?
    lexicon = {
        'north' : 'direction',
        'south' : 'direction',
        'east' : 'direction',
        'west' : 'direction',
        'go' : 'verb',
        'kill' : 'verb',
        'eat' : 'verb',
        'stop' : 'verb',
        'in' : 'stop',
        'of' : 'stop',
        'from' : 'stop',
        'at' : 'stop',
        'it' : 'stop',
        'the': 'stop',
        'door': 'noun',
        'bear' : 'noun',
        'princess' : 'noun',
        'cabinet' : 'noun'

    }
    words = string.split(' ')
    answer = []
    for ele in words:
        try:
            if ele.isdigit():
                answer.append(('number',int(ele)))
            else:
                answer.append((lexicon[ele.lower()],ele))
        except KeyError:
            answer.append(('error',ele))
    return answer

