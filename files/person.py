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
        return 'person_{}.txt'.format(cpf)

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
