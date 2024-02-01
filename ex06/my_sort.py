def get_key_by_value(dct, value):
    keys = []
    for k, v in dct.items():
        if v == value:
            keys.append(k)
    return keys


def main():
    d = {
        'Hendrix': '1942',
        'Allman': '1946',
        'King': '1925',
        'Clapton': '1945',
        'Johnson': '1911',
        'Berry': '1926',
        'Vaughan': '1954',
        'Cooder': '1947',
        'Page': '1944',
        'Richards': '1943',
        'Hammett': '1962',
        'Cobain': '1967',
        'Garcia': '1942',
        'Beck': '1944',
        'Santana': '1947',
        'Ramone': '1948',
        'White': '1975',
        'Frusciante': '1970',
        'Thompson': '1949',
        'Burton': '1939',
    }
    year_lst = list(set(d.values()))
    sorted_year_lst = sorted(year_lst)
    big_musician_lst = []
    for year in sorted_year_lst:
        musician_lst = get_key_by_value(d, year)
        big_musician_lst.extend(sorted(musician_lst))
    for m in big_musician_lst:
        print(m)


if __name__ == "__main__":
    main()
