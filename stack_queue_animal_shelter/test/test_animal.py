import pytest 
from animal import Animal, AnimalShelter




shelter = AnimalShelter()


def test_dequeue_no_pref():
    shelter = AnimalShelter()
    shelter.enqueue({'species': 'dog', 'name': 'Buddy'})
    shelter.enqueue({'species': 'cat', 'name': 'Whiskers'})
    assert shelter.dequeue() == {'species': 'dog', 'name': 'Buddy'}
    assert shelter.dequeue() == {'species': 'cat', 'name': 'Whiskers'}




def test_empty_shelter():
    empty_shelter = AnimalShelter()
    
    assert empty_shelter.dequeue("dog")== None
    

def test_dequeue_oldest():
    shelter = AnimalShelter()
    shelter.enqueue({'species': 'dog', 'name': 'Buddy'})
    shelter.enqueue({'species': 'cat', 'name': 'Whiskers'})
    assert shelter.dequeue('rabbit') == {'species': 'dog', 'name': 'Buddy'}