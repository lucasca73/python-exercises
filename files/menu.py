
class MenuOption():
    def __init__(self, text, callback):
        self.text = text
        self.callback = callback

class Menu():
    def __init__(self, name='Menu'):
        self.options = []
        self.name = name

    def add(self, text, call):
        opt = MenuOption(text, call)
        self.options.append(opt)
        
    def select(self, index):
        if index >= 0:
            self.options[index].callback()
        else:
            print('invalid input')

    def show(self):
        while(True):

            #Clear terminal
            print(chr(27) + "[2J")

            # Show menu
            print('\n -- %s -- ' % self.name)
            for (ind, opt) in enumerate(self.options):
                print('{} - {}'.format(ind, opt.text) )
            
            # Handling select on menu
            try:
                opt = input('Select your option: ')
                self.select(opt)
            except IndexError:
                print('\n :) invalid input range')
            except KeyboardInterrupt:
                print('\n')
                break
            # except NameError:
            #     print('uai', opt)
            #     print('\n :) invalid input type')
