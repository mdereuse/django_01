import sys


def get_key_by_value(dct, value):
    for k, v in dct.items():
        if v == value:
            return k
    return None


def find_capital(state, states, capital_cities):
    state_abr = states[state]
    return capital_cities[state_abr]


def find_state(capital, states, capital_cities):
    state_abr = get_key_by_value(capital_cities, capital)
    return get_key_by_value(states, state_abr)


def find(arg):
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
    arg_lst = [arg.strip() for arg in arg.split(",") if len(arg.strip()) > 0]
    for arg in arg_lst:
        arg_format = arg.lower().title()
        if arg_format in states.keys():
            capital = find_capital(arg_format, states, capital_cities)
            print(f"{capital} is the capital of {arg_format}")
        elif arg_format in capital_cities.values():
            state = find_state(arg_format, states, capital_cities)
            print(f"{arg_format} is the capital of {state}")
        else:
            print(f"{arg} is neither a capital city nor a state")


def main():
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        find(arg)


if __name__ == "__main__":
    main()
