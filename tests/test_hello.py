from src.hello import more_hello, more_goodbye


def test_more_hello():
    assert more_hello() == "hi"


def test_more_bye():
    assert more_goodbye() == "bye"
