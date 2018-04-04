from .stopwords import stopword


def parserkiller(sentence):
    """
    This function parse a sentence with the help of stop words
    The result will be use for the APIs
    """
    sentence_splited = sentence.lower().split()
    result_parser = [word for word in sentence_splited if word not in stopword]
    return result_parser
