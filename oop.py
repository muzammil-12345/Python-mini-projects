class student:

    clgName = 'ABC College'
    name = 'anonymous'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Adding new student...')

s1 = student()
print(s1.name)