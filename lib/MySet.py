class MySet:
    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
    
    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)

# Bonus method
    def clear(self):
        self.dictionary.clear()
        return self
    
    def __str__(self):
        return f"MySet: {set(self.dictionary.keys())}"

set = MySet([1, 2, 3, 3])
print(set)  
set.add(4)
print(set)  
set.delete(2)
print(set) 
print(set.has(1)) 
print(set.size())  
set.clear()
print(set)  
