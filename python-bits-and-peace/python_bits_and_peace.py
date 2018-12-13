import os
import logging
import argparse
import module_one

class Coin():
    number_of_sides = 2     # Class variable

    def __init__(self, name, value, test):
        self.name = name
        self.value = value
        self.test = test


    # Method
    def change_value(self, percentage):
        self.value = self.value + self.value*percentage/100

    def dangerous_function(self):
        logging.warning('Dangerous function was just run')

    @classmethod
    def show_number_of_sides(cls):
        print("Coin's number of sides: {}".format(cls.number_of_sides))

    def __repr__(self):
        unambiguous = "Coin {}, {}, n sides: {}".format(self.name, self.value, self.number_of_sides)
        return unambiguous
    
    def __str__(self):
        human_readable = "This is an amazing coin named {}, it's value is {} and it has {} side(s)".format(self.name, self.value, self.number_of_sides)
        return human_readable


def parse_command_line():
    parser = argparse.ArgumentParser(description='This appears before usage.',
        epilog="This appears after usage. All arguments starting with a dash are considered optional.")

    parser.add_argument('name', type=str, help='sets a name for a coin')
    parser.add_argument('value', type=float, help='sets a value for a coin')
    parser.add_argument('--test', action='store_true', help="args.test will be set to True")

    args = parser.parse_args()

    logging.debug('Parsed {}'.format(args))
    return args


def main():
    logfile_path = os.path.join(os.path.dirname(__file__), "python_bits_and_peace.log")
    logging.basicConfig(filename=logfile_path,level=logging.DEBUG, format="%(asctime)s\t%(levelname)s\t%(message)s")
    logging.info('Program started')

    args = parse_command_line()

    c = Coin(args.name, args.value, args.test)
    c.show_number_of_sides()
    c.change_value(-50)
    c.dangerous_function()

    logging.info('Program finished')

    module_one.function_one()


if __name__ == '__main__':
    main()
