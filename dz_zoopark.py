#1. Создайте базовый класс `Animal`, который будет содержать общие
# атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`)
# для всех животных.
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для `# make_sound()`).
#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()`
# для каждого животного.
#4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`,
# `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff):
        self.staff.append(staff)
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

# -----------------
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return "Гав!"

    def eat(self):
        return f"{self.name} кушает собачий корм."

class Staff:
    def __init__(self, name, position):
        self.name = name
        self.position = position

# Создаем объект класса Dog
dog = Dog("Жучка", 3, "Йоркширский терьер")
print(dog.make_sound())
print(dog.eat())

#2-----------------------------------------------------------
class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def make_sound(self):
        return "Твит твит!"

    def fly(self):
        return f"{self.name} летает высоко."

class Mammal(Animal):
    def __init__(self, name, age, habitat):
        super().__init__(name, age)
        self.habitat = habitat

    def make_sound(self):
        return "Ррррр!"

    def run(self):
        return f"{self.name} быстро бегает."

class Reptile(Animal):
    def __init__(self, name, age, skin_type):
        super().__init__(name, age)
        self.skin_type = skin_type

    def make_sound(self):
        return "Хшшш!"

    def crawl(self):
        return f"{self.name} ползают по земле."

# Создаем объекты различных подклассов
bird = Bird("Воробей", 1, "Воробьинообразные")
mammal = Mammal("Лев", 5, "Саванна")
reptile = Reptile("Змея", 2, "Кожаный")

# Выводим информацию о животных
print(bird.make_sound())
print(bird.fly())

print(mammal.make_sound())
print(mammal.run())

print(reptile.make_sound())
print(reptile.crawl())

#3-----------------------------------------------------------
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

# Создаем объекты различных подклассов
animals = [Bird("Воробей", 1, "Воробьинообразные"), Mammal("Лев", 5, "Саванна"), Reptile("Змея", 2, "Кожаный")]

# Вызываем функцию для воспроизведения звуков животных
print(f"Звуки животных:")
animal_sound(animals)

#4------------------------------------
zoo = Zoo()

staff = Staff("Елена", "Сотрудник зоопарка")

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_staff(staff)

for animal in zoo.animals:
    print(f"{animal.name} издает звук: {animal.make_sound()}")

for staff in zoo.staff:
    print(f"{staff.name} по должности {staff.position} в зоопарке.")

#Задание 5------------------------------
class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "Zoo Keeper")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        print(f"{self.name} лечит  {animal.name}")

zookeeper = ZooKeeper("Настя")
veterinarian = Veterinarian("Иван")

zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

for staff in zoo.staff:
    if isinstance(staff, ZooKeeper):
        staff.feed_animal(bird)
    elif isinstance(staff, Veterinarian):
        staff.heal_animal(mammal)