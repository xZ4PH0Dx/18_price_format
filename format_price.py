import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('number', help='input number')
    return parser.parse_args()


def format_price(price=None):
    if isinstance(price, bool):
        return None
    try:
        price = float(price)
    except (TypeError, ValueError):
        return None
    if round(price, 2).is_integer():
        return '{:,.0f}'.format(price).replace(',', ' ')
    else:
        return '{:,.2f}'.format(price).replace(',', ' ')


if __name__ == '__main__':
    args = create_parser()

    print(format_price(args.number))
