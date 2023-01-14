import sys

class UniqueException(Exception): ...
# this exception should not be raised

def Only(*exceptions):
    exc_info = sys.exc_info()
    if exc_info[0] in exceptions:
        return exc_info[0] # guaranteed to be catched
    return UniqueException
    # returns a unique exception so that it is uncatchable
