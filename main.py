import os
from datetime import datetime
import re

my_folder_path = "/Users/shanemitnick/Desktop/ComEdToBeRenamed"

'''
Data Structure :
String : (String, String)
"Utility Name" : "Regex to identify file format", "Regex to extract SA number".
'''
import os
from datetime import datetime
import re

my_folder_path = "/Users/shanemitnick/Desktop/ComEdToBeRenamed"


utility_regex = {
    ## Add More Regex Strings to include more file renaming functionality
    "Comed": ("^AI[0-9]{8}_[0-9]{6,10}.csv$", r'\_(.+?)\.'),

}


def get_new_name(name, regex):
    """Return the new name of the file, formatted in this way: "XXXXXXXXXX_MMDDYYYYTTTT.csv"

    >>> get_new_name("AI00000001_123456789.csv")
    '123456789_111220201649.csv'

    >>> get_new_name("AI00000002_123456.csv")
    '0000123456_111220201650.csv'

    >>> get_new_name("TestFile.csv")
    This is not a standard ComEd file. Keeping the same name.
    'TestFile.csv'

    This function will take a name of a file and create the new comed file with the format below
    'accountnumber_datetime'
    :param name: String,  name of the file that is to be changed
    :return: the new formatted file name
    """

    # Use RegEx to see if given filename is in

    if re.match(regex[0], name) is None:
        print("This is not a standard ComEd file. Keeping the same name.")
        return name

    # If we are here, can be certain file is in format of: "AI########_XXXXXXXXXX.csv"
    # Isolate the account number using the Account Number Regex String
    a_n = re.findall(regex[1], name)[0]

    date_text = datetime.now().strftime("%m%d%Y%H%M")

    return "{}_{}.csv".format(a_n.zfill(10), date_text)


def run(path):
    """
    This function will loop through the given file path and attempt
    to change the names of all the files in that file path.
    :param path: The folder of ComEd files to be renamed.
    :return: None, Renamed files in the given folder path, and a log of files not renamed if any exist.
    """
    try:
        files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    except FileNotFoundError:
        print("This file path does not exist. Please try a different file path.")
    else:
        for file in files:
            new_name = get_new_name(file, utility_regex["Comed"])
            if new_name not in os.listdir(path):
                os.rename(os.path.join(path, file), os.path.join(path, new_name))
                print("File", file, "has been renamed to:", new_name)
            else:
                print("Duplicate file name, skipping over file:", file)


run(my_folder_path)

# to be used for doc-testing
# TODO: Get around "dynamic" file naming (set datetime somehow)
"""
if __name__ == "__main__" and False:
    import doctest
    doctest.testmod()
"""
utility_regex = {
    "Comed": ("^AI[0-9]{8}_[0-9]{6,10}.csv$", r"\_(.+?)\."),
    "Shane": ("^SU[0-9]{6,10}_Ticket[0-9]{3}.csv", r"\SU(.+?)\_")
}


def find_format(filename):
    """
    Here we will use our defined utility_regex dictionary to determine what Utili`ty sent the given file.
    The result will be the regex needed to extract the SA number.
    :param filename: The file name to be renamed
    :return: The Regex that will extract the Account Number
    """
    for utility in utility_regex:
        match = re.match(utility_regex[utility][0], filename)
        if match is not None:
            print("Format detected: " + utility)
            return utility_regex[utility][1]

    # if we are here, there are no matches in the known Utility RegEx
    print("No Utility file format detected.")
    return None


def get_new_name(name):
    """Return the new name of the file, formatted in this way: "XXXXXXXXXX_MMDDYYYYTTTT.csv"

    >>> get_new_name("AI00000001_123456789.csv")
    '123456789_111220201649.csv'

    >>> get_new_name("AI00000002_123456.csv")
    '0000123456_111220201650.csv'

    >>> get_new_name("TestFile.csv")
    This is not a standard ComEd file. Keeping the same name.
    'TestFile.csv'

    :param name: String,  name of the file that is to be changed
    :return: String, the new formatted file name
    """
    # grabbing regex to extract Service Account from given file
    regex = find_format(name)
    if regex is None:
        print(name + " is not a file format that is known. Keeping the same name.")
        return name

    # Isolate the account number using the Account Number Regex String
    a_n = re.findall(regex, name)[0]

    date_text = datetime.now().strftime("%m%d%Y%H%M")

    return "{}_{}.csv".format(a_n.zfill(10), date_text)


def run(path):
    """
    This function will loop through the given file path and attempt
    to change the names of all the files in that file path.
    :param path: The folder of ComEd files to be renamed.
    :return: None, Renamed files in the given folder path, and a log of files not renamed if any exist.
    """
    try:
        files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    except FileNotFoundError:
        print("This file path does not exist. Please try a different file path.")
    else:
        for file in files:
            new_name = get_new_name(file)
            if new_name not in os.listdir(path):
                os.rename(os.path.join(path, file), os.path.join(path, new_name))
                print("File", file, "has been renamed to:", new_name)
            else:
                print("Duplicate file name, skipping over file:", file)


run(my_folder_path)
