import pytest

from ..helpers import parser, stopwords


def test_parser_return_string():
    assert type(parser.parserkiller(' '.join(stopwords.stopword))) == str

def test_parser_return_void_when_only_stop_words():
    assert parser.parserkiller(' '.join(stopwords.stopword)) == ""

def test_parser_return_input_when_no_stop_words():
    assert parser.parserkiller("maison café-turban") == "maison café turban"

def test_parser_return_input_without_stop_words():
    assert parser.parserkiller("La maison de mon oncle est toute petite") == "maison oncle petite"

def test_parser_return_void_when_only_punctuation():
    assert parser.parserkiller("? ! , ' ; :") == ""
