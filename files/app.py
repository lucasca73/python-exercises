class MenuOption():
    def __init__(self, text, callback):
        self.text = text
        self.callback = callback

class Menu():
    def __init__(self):
        self.options = []

    def add(self, text, call):
        opt = MenuOption(text, call)
        self.options.append(opt)
        
    def select(self, index):
        if index >= 0:
            self.options[index].callback()
        else:
            print('invalid input')

    def show(self):
        print(' -- Menu -- ')
        for (ind, opt) in enumerate(self.options):
            print('{} - {}'.format(ind, opt.text) )



def leave():
    print('Bye!')
    raise KeyboardInterrupt

def add_car():
    print('add new car')

def remove_car():
    print('remove car')

def search_car():
    print('search car')

def add_person():
    print('add new person')

def remove_person():
    print('remove person')

def search_person():
    print('search person')

menu = Menu()

menu.add('add car', add_car)
menu.add('add person', add_person)
menu.add('Quit', leave)

while(True):
    print('\n')
    menu.show()
    try:
        opt = input('Select your option: ')
        menu.select(opt)
    except IndexError:
        print('\n :) invalid input range')
    except NameError:
        print('\n :) invalid input type')
    except KeyboardInterrupt:
        print('\n')
        break


# input('')
# with open('file.txt')