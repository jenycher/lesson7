# Задача 1
#Создайте класс Animal с методом make_sound(). Затем создайте несколько дочерних классов
# (например, Dog, Cat, Cow), которые наследуют Animal, но изменяют его поведение
# (метод make_sound()). В конце создайте список содержащий экземпляры этих животных и
# вызовите make_sound() для каждого животного в цикле.

class animal():
    def make_sound(self):
        pass
class Dog(animal):
    def make_sound(self):
        print("гав")
class Cat(animal):
    def make_sound(self):
        print("мяу")

class Cow(animal):
    def make_sound(self):
        print("мууу")

dog = Dog()

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.make_sound()

