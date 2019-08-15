from car import Car
from person import Person, PersonCar
from menu import Menu
import os

def leave():
    raise KeyboardInterrupt



def car_menu():
    global profile
    profile = None

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
    ld = Car.load(plate)
    if ld:
        print('Car with plate already exists...')
    else:
        new_car = Car(plate, model)
        new_car.save()
    _ = raw_input('...')

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
    _ = raw_input('...')


def person_menu():
    global profile
    profile = None
    p_menu = Menu('Person Menu')

    # Setting up menu
    p_menu.add('add person', add_per)
    p_menu.add('person profile', search_per)
    p_menu.add('remove person', remove_per)
    p_menu.add('Back', leave )

    p_menu.show()

def add_per():
    print('Adding new person...')
    cpf = raw_input('type a cpf: ')
    name = raw_input('type a name: ')

    ld = Person.load(cpf)
    if ld:
        print('Person with cpf already exists...')
    else:
        obj = Person(cpf, name)
        obj.save()

    _ = raw_input('...')


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
        person_buy_menu(load)
    else:
        print('Person not found')


global profile
profile = None

def buy_car():
    global profile

    files = [f for f in os.listdir('./db') if os.path.isfile(f)]
    for f in files:
        splited = f.split('_')

    if profile:
        plate = raw_input('type the cars plate: ')
        ld_car = Car.load(plate)
        if ld_car:

            buy = PersonCar.load(profile.cpf, ld_car.plate)
            if buy:
                print('Car is already bought..')
            else:
                buy = PersonCar(profile.cpf, ld_car.plate)
                buy.save()

    _ = raw_input('...')

def remove_car():
    global profile
    if profile:
        plate = raw_input('type the cars plate: ')
        ld_car = Car.load(plate)
        if ld_car:
            buy = PersonCar.load(profile.cpf, ld_car.plate)
            if buy:
                buy.remove()

    _ = raw_input('...')

def my_cars():
    global profile
    if profile:

        files = [f for f in os.listdir('./db') if os.path.isfile(f)]
        for f in files:
            splited = f.split('_')
            if len(splited) == 3 and splited[1] == profile.cpf:
                plate = splited[2]
                ld_car = Car.load(plate)
                if ld_car:
                    print(ld_car.plate, ld_car.model)

    _ = raw_input('...')

def person_buy_menu(person):
    p_menu = Menu('Buy Menu ({})'.format(person.name))
    global profile
    profile = person
    # Setting up menu
    p_menu.add('buy car', buy_car )
    p_menu.add('remove car', remove_car )
    p_menu.add('my cars', my_cars )
    p_menu.add('Back', leave )

    p_menu.show()

root = Menu()

root.add('car menu', car_menu)
root.add('person menu', person_menu)
root.add('Quit', leave)

root.show()