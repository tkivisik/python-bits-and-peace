import argparse

def main():
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



if __name__ == '__main__':
    main()