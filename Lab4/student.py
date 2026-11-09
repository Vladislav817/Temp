import math


# === ЗАДАЧА 1 ===
class Wallet:
    def __init__(self, initial_balance):
        if initial_balance > 0:
            self._balance = initial_balance  # Ваш код
        else:
            self._balance = 0

    def deposit(self, amount):
        if amount <=0:
            return False  # Ваш код
        self._balance = self._balance + amount
        return True

    def withdraw(self, amount):
        if amount <=0:
            return False
        if self._balance < amount:
            return False
        self._balance = self._balance - amount
        return True  # Ваш код

    def get_balance(self):
        return self._balance  # Ваш код


# === ЗАДАЧА 2 ===
class Triangle:
    def __init__(self, a, b, c):
        self.a  = a  
        self.b  = b  
        self.c  = c  
  
    def perimeter(self):
        return self.a + self.b + self.c
    def __str__ (self):
        return f"Triangle {self.a}" 


class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r  


def calculate_total_perimeter(shapes):
    calk = 0 
    for i in shapes:
        calk = calk + i.perimeter()
    return calk

# === ЗАДАЧА 3 ===
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            x = self.x + other.x
            y = self.y + other.y
            v = Vector2D(x, y)
            return v
        return NotImplemented
        
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x = self.x * other
            y = self.y * other
            v = Vector2D(x, y)
            return v
        return NotImplemented

    
    def __eq__(self, other):
        if isinstance(other, Vector2D):
            if self.x != other.x:
                return False
            if self.y != other.y:
                return False
            return True
        return NotImplemented

    
    def __hash__(self):
        return hash((self.x, self.y)) 

   
    def __repr__(self):
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return f"({self.x}, {self.y})"


# === ЗАДАЧА 4 ===
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_bonus(self):
        return self.base_salary * 0.10


class Manager(Employee):
    pass  # Ваш код


if __name__=="__main__":
    
    v1 = Vector2D(1, 2)
    v2 = Vector2D(3, 4)
    print(v1)
    print(v1 + v2)          # (4, 6)
    print(v1 * 3)           # (3, 6)
    print(v1 == (1, 2))  # NE
    print(v1 == Vector2D(1, 2))  # True
    print({v1, Vector2D(1, 2)})  # один элемент

    