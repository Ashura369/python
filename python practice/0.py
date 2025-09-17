class person:
      def __init__(self, name, age, height, location):
            self.name = name
            self.age = age
            self.height = height
            self.location = location


name = input('NAME: ')
age = int(input('AGE: '))
height = float(input('HEIGHT: '))
location = input('LOCATION: ')

p1 = person(name, age, height, location)

print(f"""
    NAME : {p1.name}
    AGE : {p1.age}
    HEIGHT : {p1.height}
    LOCATION : {p1.location}
""")