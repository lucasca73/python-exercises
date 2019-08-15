import os

class Car():
    def __init__(self, plate, model):
        self.plate = plate
        self.model = model

    def save(self):
        # opening in overwrite
        with open(Car.file_path(self.plate), 'w') as file:
            file.write('%s' % self.model)
        print('[Ok!] new car saved')

    def remove(self):
        if os.path.exists(Car.file_path(self.plate)):
            os.remove(Car.file_path(self.plate))
            print("Car removed")
        else:
            print("The file does not exist")

    @staticmethod
    def file_path(plate):
        return './db/car_{}'.format(plate)

    @staticmethod
    def load(plate):
        # opening in read only
        try:
            with open(Car.file_path(plate), 'r') as file:
                model = file.readline()
                loaded = Car(plate, model)
                return loaded
        except:
            print('could not find car with plate %s...' % plate)
            return None

        return None
