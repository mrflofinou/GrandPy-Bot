from .stopwords import stopword


def parserkiller(query):
    """
    This function parse a sentence with the help of stop words
    The result will be use for the APIs
    """
    query_splited = query.lower().split()
    result_parser = [word for word in query_splited if word not in stopword]
    return ' '.join(result_parser)
