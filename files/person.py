import os

class Person():
    def __init__(self, cpf, name):
        self.cpf = cpf
        self.name = name

    def save(self):
        # opening in overwrite
        with open(Person.file_path(self.cpf), 'w') as file:
            file.write('%s' % self.name)
        print('[Ok!] new Person saved')

    def remove(self):
        if os.path.exists(Person.file_path(self.cpf)):
            os.remove(Person.file_path(self.cpf))
            print("Person removed")
        else:
            print("The file does not exist")

    @staticmethod
    def file_path(cpf):
        return 'db.person_{}'.format(cpf)

    @staticmethod
    def load(cpf):
        # opening in read only
        try:
            with open(Person.file_path(cpf), 'r') as file:
                name = file.readline()
                loaded = Person(cpf, name)
                return loaded
        except:
            print('could not find Person with cpf %s...' % cpf)
            return None

        return None



class PersonCar():
    def __init__(self, cpf, plate):
        self.cpf = cpf
        self.plate = plate

    def save(self):
        # opening in overwrite
        with open(PersonCar.file_path(self.cpf, self.plate), 'w') as file:
            file.write('ok')
        print('[Ok!] new PersonCar saved')

    def remove(self):
        path = PersonCar.file_path(self.cpf, self.plate)
        if os.path.exists(path):
            os.remove(path)
            print("PersonCar removed")
        else:
            print("The file does not exist")

    @staticmethod
    def file_path(cpf, plate):
        return 'db.buy_{}_{}'.format(cpf, plate)

    @staticmethod
    def load(cpf, plate):
        # opening in read only
        try:
            with open(PersonCar.file_path(cpf,plate), 'r') as file:
                loaded = PersonCar(cpf, plate)
                return loaded
        except:
            print('could not find PersonCar')
            return None

        return None
