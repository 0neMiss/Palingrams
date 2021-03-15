"""
Loads a file as a list
 
Arguments:
    * Text file name (and directory path, if needed)
Exceptions:
    *IOError if filename not found.
Returns:
    *A list of all words in a text file in lower case.
Requires:
    *import sys
"""
import sys

def load(file):
    try:
        with open(file) as in_file:
            res = in_file.read().strip().split('\n')
            res = [x.lower() for x in res]
            return set(res)

    except IOError as e:
        print(f"{e}\nError Opening{file}. Terminating program.")
        sys.exit(1)
