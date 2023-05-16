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
        self.queue = Queue()


    def enqueue(self, animal):
        """
        Enqueues an animal in the shelter.
        Args:
            animal (Animal): The animal to enqueue.
        Raises:
            TypeError: If the argument is not an Animal object.
        """
        if animal['species'] != 'dog' and animal['species'] != 'cat':
            raise ValueError('Invalid animal species')
        self.queue.enqueue(animal)

    def dequeue(self, pref=None):
        """
        Removes and returns a dog or cat from the animal shelter.
        Args:
            pref: a string representing the preferred species to dequeue. If not specified or not a valid
                  species ('dog' or 'cat'), the animal that has been waiting in the shelter the longest
                  is returned.
        Returns:
            A dictionary with 'species' and 'name' keys representing the dequeued animal, or None if no
            animal of the preferred species is available.
        """
        if pref is None or (pref != 'dog' and pref != 'cat'):
            # Dequeue the animal that has been waiting in the shelter the longest
            return self.queue.dequeue()
        else:
            # Dequeue the first animal of the preferred species found in the queue
            temp_queue = Queue()
            result = None
            while not self.queue.is_empty():
                animal = self.queue.dequeue()
                if animal['species'] == pref:
                    result = animal
                    break
                else:
                    temp_queue.enqueue(animal)
            while not temp_queue.is_empty():
                self.queue.enqueue(temp_queue.dequeue())
            return result
            

# shelter = AnimalShelter()

# shelter.enqueue(Animal('dog', 'Buddy'))
# shelter.enqueue(Animal('dog', 'Max'))
# shelter.enqueue(Animal('cat', 'Fluffy'))
# shelter.enqueue(Animal('cat', 'Whiskers'))

