def main():
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]
    data_dct_tmp = {}
    for musician, date in d:
        data_dct_tmp.setdefault(date, []).append(musician)
    data_dct = {
        key: " ".join(value)
        for key, value in data_dct_tmp.items()
    }
    for date, musician in data_dct.items():
        print(f"{date} : {musician}")


if __name__ == "__main__":
    main()
