from twttr import shorten

def test_short():
    assert shorten("hello")=="hll"
    assert shorten("twitter")=="twttr"
    assert shorten("What is your name ?")=="Wht s yr nm ?"
    assert shorten("twittr")=="twttr"
    assert shorten("h@llo")=="h@ll"
    assert shorten("itter")=="ttr"


