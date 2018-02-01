import argparse

class coin():
    number_of_sides = 2

    def __init__(self, name, value):
        self.name = name
        self.value = value

    @classmethod
    def display_currency_type(cls):
        print("Coin's number of sides: {}".format(cls.number_of_sides))

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
    c = coin("tc", 100)
    c.display_currency_type()


if __name__ == '__main__':
    main()