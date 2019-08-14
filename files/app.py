from car import Car
from person import Person
from menu import Menu

def leave():
    raise KeyboardInterrupt



def car_menu():

    cars = Menu('Cars Menu')

    # Setting up menu
    cars.add('add car', add_car)
    cars.add('search car', search_car)
    cars.add('remove car', remove_car)
    cars.add('Back', leave )

    cars.show()

def add_car():
    print('Adding new car...')
    plate = raw_input('type a plate: ')
    model = raw_input('type a model: ')
    print('typed: %s' % plate)
    new_car = Car(plate, model)
    new_car.save()

def remove_car():
    print('removing a car...')
    plate = raw_input('type a plate number: ')
    ld_car = Car.load(plate)
    if ld_car:
        print('Found => ', ld_car.plate, ld_car.model)
        decision = raw_input('remove? (y/n): ')
        if decision == 'y' or decision == 'Y':
            ld_car.remove()

def search_car():
    print('searching a car...')
    plate = raw_input('type a plate number: ')
    ld_car = Car.load(plate)
    if ld_car:
        print('Found => ', ld_car.plate, ld_car.model)
    else:
        print('Car not found')




def person_menu():

    p_menu = Menu('Person Menu')

    # Setting up menu
    p_menu.add('add person', add_per)
    p_menu.add('search person', search_per)
    p_menu.add('remove person', remove_per)
    p_menu.add('Back', leave )

    p_menu.show()

def add_per():
    print('Adding new person...')
    cpf = raw_input('type a cpf: ')
    name = raw_input('type a name: ')

    obj = Person(cpf, name)
    obj.save()


def remove_per():
    print('removing a person...')
    cpf = raw_input('type a cpf number: ')
    load = Person.load(cpf)
    if load:
        print('Found => ', load.cpf, load.name)
        decision = raw_input('remove? (y/n): ')
        if decision == 'y' or decision == 'Y':
            load.remove()


def search_per():
    print('searching a person...')
    plate = raw_input('type a cpf number: ')
    load = Person.load(plate)
    if load:
        print('Found => ', load.cpf, load.name)
    else:
        print('Person not found')

root = Menu()

root.add('car menu', car_menu)
root.add('person menu', person_menu)
root.add('Quit', leave)

root.show()