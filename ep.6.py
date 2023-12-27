class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def get_name(self):
        return f"My name is {self.name}."

    def get_age(self):
        return f"I am {self.age} years old."

    def get_occupation(self):
        return f"I work as a {self.occupation}."

# person
person1 = Person("Thamthanaphat", 23, "data analytics")

# print
print(person1.get_name())        # ผลลัพธ์: My name is Thamthanaphat.
print(person1.get_age())         # ผลลัพธ์: I am 23 years old.
print(person1.get_occupation())  # ผลลัพธ์: I work as a data analytics.
