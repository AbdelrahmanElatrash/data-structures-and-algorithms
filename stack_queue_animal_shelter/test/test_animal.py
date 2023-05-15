import pytest 
from animal import Animal, AnimalShelter


cat1 = Animal("cat", "Whiskers")
dog1 = Animal("dog", "Fido")
cat2 = Animal("cat", "Fluffy")
dog2 = Animal("dog", "Buddy")

shelter = AnimalShelter()


def test_enqueue_dequeue():
    shelter.enqueue(cat1)
    shelter.enqueue(dog1)
    shelter.enqueue(cat2)
    shelter.enqueue(dog2)

    cat = shelter.dequeue("cat")
    assert cat.species == "cat"
    assert cat.name == "Whiskers"

    dog = shelter.dequeue("dog")
    assert dog.species == "dog"
    assert dog.name == "Fido"


def test_enqueue_dequeue_not_animal():
    try:
        animal = shelter.dequeue("")
    except ValueError as e:
        assert str(e)== "Preferred species must be 'dog' or 'cat'."
    
    try:
        hamster=Animal("hamster", "Whiskers")
        animal = shelter.enqueue(hamster)
    except ValueError as e:
        assert str(e)== "Argument must be an Animal object."


def test_empty_shelter():
    empty_shelter = AnimalShelter()
    
    assert empty_shelter.dequeue("dog")== None
    