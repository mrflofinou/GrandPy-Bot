"""This file contains custom exceptions"""

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class GoogleError(Error):
    """Exception raised if Google maps don't find results."""
    pass

class QueryEmptyError(Error):
    """Exception raised if the user query is empty."""
    pass

class WikipediaResultError(Error):
    """Exception raised if Wikipedia don't find results."""
    pass
