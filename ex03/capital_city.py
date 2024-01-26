import sys


def find_capital(state):
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
    state_abr = states.get(state, None)
    if state_abr is not None:
        capital = capital_cities[state_abr]
        print(capital)
    else:
        print("Unknown state")


def main():
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        find_capital(arg)


if __name__ == "__main__":
    main()
