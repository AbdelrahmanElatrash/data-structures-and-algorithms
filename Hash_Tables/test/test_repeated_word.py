import pytest
from ..repeated_word import split_ , repeated_word , list_word ,count_word


str_1="Once upon a time, there was a brave princess who..."
str_2="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
str_3="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn't know what I was doing in New York..."

def test_repeated_world():
    assert repeated_word(str_1)== "a"
    assert repeated_word(str_2)== "it"
    assert repeated_word(str_3)== "summer"
    
def test_word_count():
      assert count_word(str_1) == {'once': 1, 'upon': 1, 'a': 2, 'time': 1, 'there': 1, 'was': 1, 'brave': 1, 'princess': 1}

      assert count_word(str_2) == {'it': 10, 'was': 11, 'the': 14, 'best': 1, 'of': 12, 'times': 2, 'worst': 1, 'age': 2, 'wisdom': 1, 'foolishness': 1, 'epoch': 2, 'belief': 1, 'incredulity': 1, 'season': 2, 'light': 1, 'darkness': 1, 'spring': 1, 'hope': 1, 'winter': 1, 'despair': 1, 'we': 4, 'had': 2, 'everything': 1, 'before': 2, 'us': 2, 'nothing': 1, 'were': 2, 'all': 2, 'going': 2, 'direct': 2, 'to': 1, 'heaven': 1, 'other': 1, 'way': 1, '–': 1, 'short': 1, 'period': 2, 'so': 1, 'far': 1, 'like': 1, 'present': 1, 'that': 1, 'some': 1, 'its': 2, 'noisiest': 1, 'authorities': 1, 'insisted': 1, 'on': 1, 'being': 1, 'received': 1, 'good': 1, 'evil': 1, 'superlative': 1, 'degree': 1, 'comparison': 1}
      assert count_word(str_3) == {'it': 1, 'was': 2, 'a': 1, 'queer': 1, 'sultry': 1, 'summer': 2, 'the': 2, 'they': 1, 'electrocuted': 1, 'rosenbergs': 1, 'and': 1, 'i': 2, "didn't": 1, 'know': 1, 'what': 1, 'doing': 1, 'in': 1, 'new': 1}
      
      
      
def test_list_word():
    assert list_word(str_1)=={'a'}
    assert list_word(str_2)=={'its', 'was', 'all', 'we', 'of', 'the', 'period', 'were', 'going', 'direct', 'before', 'us', 'in', 'times', 'had', 'it', 'or', 'age', 'epoch', 'for', 'season'}
    assert list_word(str_3)=={'i', 'the', 'was', 'summer'}
    