import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('number', help='input number', type=float)
    return parser.parse_args()


def format_price(price=None):
    if not isinstance(price, float):
        return None
    if price == int(price):
        return '{:,.2f}'.format(price).replace('.00', '').replace(',', ' ')
    else:
        return '{:,.2f}'.format(price).replace(',', ' ')


if __name__ == '__main__':
    args = create_parser()

    print(format_price(args.number))
