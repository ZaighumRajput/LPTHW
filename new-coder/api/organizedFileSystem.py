"""To keep my filesystem organized

"""
import os


def initializeFileStructure():
    """This function makes the skeleton folder structure

    """	
    os.mkdir("masterRoot")
    os.mkdir("inbox")
    os.chdir("MasterRoot")
    filesInRoot = ["currentlyWorkingOn", "projects", "utilities"]
    for fileNames in filesInRoot:
        os.mkdir(fileNames)

def activeMonitoring():
    """This function should check file structure for any rules that are being broken
    1. Files have meaningful names
    2. file names aren't too big
    3. currentlyWorkingOn and Inbox don't have more than 5 files.
    4. files in inbox are not more than 2 weeks old.

    """


def copy():
    """Duplicate one file structure from one computer to another and/or cloud

    """

def backup():
    """Should zip, encrypt, and save the entire file system
    """