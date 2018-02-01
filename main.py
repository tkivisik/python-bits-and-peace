import argparse

class coin():
    number_of_sides = 2     # Class variable

    def __init__(self, name, value):
        self.name = name
        self.value = float(value)

    # Method
    def change_value(self, percentage):
        self.value = self.value + self.value*percentage/100

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
    parser = argparse.ArgumentParser(description='This appears before usage.' ,epilog="This appears after usage. All arguments starting with a dash are considered optional.")

    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--test', action='store_true', help="args.test will be set to True")
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print args.accumulate(args.integers)
    print args.test


def main():
    c = coin("tc", 7)
    c.show_number_of_sides()
    c.change_value(-50)
    print c.value
    print repr(c)
    print c


if __name__ == '__main__':
    main()