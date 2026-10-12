"""
Lab 02: Data Structures and OOP
File: lab02_data_structures_oop.py

Codes in this file (in order):
  1. list_methods      - append, insert, remove, pop, sort, sorted, extend...
  2. tuple_methods     - count, index, (50,) vs (50)
  3. dict_methods      - get, update, pop, setdefault, items
  4. set_operations    - add, remove, discard, & | -
  5. comprehensions    - list and dict comprehensions, word frequency
  6. KnowledgeBase     - class with dict of facts
  7. AIModel           - class variable vs instance variable
  8. Agent / ReflexAgent - inheritance with super()
  9. Dataset           - __str__, __len__, __getitem__
  10. SimpleStack       - push, pop, peek
"""

# ---------- LIST ----------
lst = [3, 1, 2]
lst.append(4)
lst.insert(0, 9)
lst.remove(1)            # removes FIRST occurrence only
x = lst.pop()            # removes and returns last
lst.extend([7, 8])
lst.sort()               # changes lst in place
new = sorted(lst)        # returns a new list
lst.reverse()
print(lst.index(7), lst.count(7), len(lst), max(lst), min(lst), sum(lst))
c = lst.copy()
lst.clear()

# ---------- TUPLE ----------
tp = (10, 20, 10)
print(tp.count(10), tp.index(20))     # only these two methods
print(type((50,)))                    # tuple
print(type((50)))                     # int

# ---------- DICT ----------
d = {"a": 1, "b": 2}
print(d.get("z", 0))                  # default if missing
d.update({"c": 3})
d.pop("a")
print(d.keys(), d.values(), d.items())
d.setdefault("k", 100)
for k, v in d.items():
    print(k, v)

# ---------- SET ----------
A = {"dog", "cat"}
B = {"dog", "bird"}
A.add("fish")
A.remove("fish")         # error if missing
A.discard("zzz")         # no error if missing
print(A & B)             # intersection
print(A | B)             # union
print(A - B)             # difference

# ---------- COMPREHENSIONS ----------
squares = [x ** 2 for x in range(1, 6)]
preds = [-1, 2, 3]
pos = [p for p in preds if p > 0]
scores = [50, 80, 100]
mx = max(scores)
norm = [s / mx for s in scores]
names = ["Ali", "Sara"]
marks = [80, 90]
dct = {n: m for n, m in zip(names, marks)}

# ---------- WORD FREQUENCY ----------
text = "the cat and the dog"
freq = {}
for w in text.split():
    freq[w] = freq.get(w, 0) + 1

# ---------- CLASSES ----------
class KnowledgeBase:
    def __init__(self):
        self.facts = {}
    def add_fact(self, key, value):
        self.facts[key] = value
    def get_fact(self, key):
        return self.facts.get(key, "Unknown")

class AIModel:
    model_count = 0                       # class variable (shared)
    def __init__(self, name):
        self.name = name                  # instance variable
        AIModel.model_count += 1
    def __str__(self):
        return f"Model: {self.name}"

class Agent:
    def __init__(self, name):
        self.name = name
    def act(self):
        return "No action"

class ReflexAgent(Agent):                 # inheritance
    def __init__(self, name, rule):
        super().__init__(name)
        self.rule = rule
    def act(self):                        # overriding
        return f"{self.name} follows {self.rule}"

class Dataset:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return f"Dataset({len(self.data)} items)"
    def __len__(self):
        return len(self.data)
    def __getitem__(self, i):
        return self.data[i]

class SimpleStack:
    def __init__(self):
        self._data = []
    def push(self, x):
        self._data.append(x)
    def pop(self):
        if not self._data:
            return "Stack is empty!"
        return self._data.pop()
    def peek(self):
        return self._data[-1] if self._data else None
    def is_empty(self):
        return len(self._data) == 0
    def size(self):
        return len(self._data)
