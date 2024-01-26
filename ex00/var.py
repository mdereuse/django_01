def my_var():
    var0 = 42
    var1 = "42"
    var2 = "quarante-deux"
    var3 = 42.0
    var4 = True
    var5 = [42]
    var6 = {42: 42}
    var7 = (42, )
    var8 = set()
    for var in locals().values():
        print(f"{var} est de type {type(var)}")


if __name__ == "__main__":
    my_var()
