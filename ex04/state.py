import sys


def get_key_by_value(dct, value):
    for k, v in dct.items():
        if v == value:
            return k
    return None


def find_state(capital):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    state_abr = get_key_by_value(capital_cities, capital)
    if state_abr is not None:
        state = get_key_by_value(states, state_abr)
        print(state)
    else:
        print("Unknown capital city")


def main():
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        find_state(arg)


if __name__ == "__main__":
    main()
