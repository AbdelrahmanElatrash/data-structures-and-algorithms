from queue import Queue

class Animal:
    def __init__(self, species, name):
        """
        Initializes an Animal object.
        Args:
            species (str): The species of the animal.
            name (str): The name of the animal.
        """
        self.species = species
        self.name = name

class AnimalShelter:
    def __init__(self):
        """
        Initializes an AnimalShelter object.
        """
        self.dog_queue = Queue()
        self.cat_queue = Queue()
        self.timestamp = 0

    def enqueue(self, animal):
        """
        Enqueues an animal in the shelter.
        Args:
            animal (Animal): The animal to enqueue.
        Raises:
            TypeError: If the argument is not an Animal object.
        """
        if not isinstance(animal, Animal):
            raise TypeError("Argument must be an Animal object.")
        animal.timestamp = self.timestamp
        self.timestamp += 1
        if animal.species == 'dog':
            self.dog_queue.enqueue(animal)
        elif animal.species == 'cat':
            self.cat_queue.enqueue(animal)

    def dequeue(self, pref):
        """
        Dequeues an animal from the shelter.
        Args:
            pref (str): The preferred species of animal to dequeue.
        Returns:
            Animal: The dequeued animal, or None if no animal of the preferred species is available.
        Raises:
            ValueError: If the preferred species is not 'dog' or 'cat'.
        """
        if pref not in ['dog', 'cat']:
            raise ValueError("Preferred species must be 'dog' or 'cat'.")
        if pref == 'dog':
            if self.dog_queue.is_empty():
                return None
            return self.dog_queue.dequeue()
        elif pref == 'cat':
            if self.cat_queue.is_empty():
                return None
            return self.cat_queue.dequeue()
        else:
            # If neither dog nor cat is preferred, return whichever animal has been waiting the longest
            if self.dog_queue.is_empty():
                return self.cat_queue.dequeue() if not self.cat_queue.is_empty() else None
            if self.cat_queue.is_empty():
                return self.dog_queue.dequeue() if not self.dog_queue.is_empty() else None
            dog_front_timestamp = self.dog_queue.peek().timestamp
            cat_front_timestamp = self.cat_queue.peek().timestamp
            if dog_front_timestamp < cat_front_timestamp:
                return self.dog_queue.dequeue()
            else:
                return self.cat_queue.dequeue()
            

# shelter = AnimalShelter()

# shelter.enqueue(Animal('dog', 'Buddy'))
# shelter.enqueue(Animal('dog', 'Max'))
# shelter.enqueue(Animal('cat', 'Fluffy'))
# shelter.enqueue(Animal('cat', 'Whiskers'))

