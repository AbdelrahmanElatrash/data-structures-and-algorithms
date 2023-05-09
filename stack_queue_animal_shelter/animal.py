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
        self.dog_stack = []
        self.cat_stack = []
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
            self.dog_stack.append(animal)
        elif animal.species == 'cat':
            self.cat_stack.append(animal)

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
            if not self.dog_stack:
                return None
            # Move all the dogs to the cat stack until we find the first dog
            while self.dog_stack:
                self.cat_stack.append(self.dog_stack.pop())
                if self.cat_stack[-1].species == 'dog':
                    return self.cat_stack.pop()
        elif pref == 'cat':
            if not self.cat_stack:
                return None
            # Move all the cats to the dog stack until we find the first cat
            while self.cat_stack:
                self.dog_stack.append(self.cat_stack.pop())
                if self.dog_stack[-1].species == 'cat':
                    return self.dog_stack.pop()
        else:
            # If neither dog nor cat is preferred, return whichever animal has been waiting the longest
            if not self.dog_stack:
                return self.cat_stack.pop() if self.cat_stack else None
            if not self.cat_stack:
                return self.dog_stack.pop() if self.dog_stack else None
            if self.dog_stack[-1].timestamp < self.cat_stack[-1].timestamp:
                return self.dog_stack.pop()
            else:
                return self.cat_stack.pop()
        return None