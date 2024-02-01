def create_dct(data_lst):
    dct = {
        elem.split(" = ")[0]: {
                info.split(":")[0]: info.split(":")[1]
                for info in elem.split(" = ")[1].split(", ")
            }
        for elem in data_lst[:-1]
    }
    for key, value in dct.items():
        if key == "Palladium":
            value["electron"] += " 0"
        col = int(value["position"])
        row = len(value["electron"].split(" ")) - 1
        dct[key]["col"] = col
        dct[key]["row"] = row
    return dct


def find_elem(r, c, dct):
    for key, value in dct.items():
        if value["row"] == r and value["col"] == c:
            return key, value
    return None, None


def main():
    with open("periodic_table.txt", "r") as f:
        data = f.read()
    data_lst = data.split("\n")
    dct = create_dct(data_lst)
    html = """<!DOCTYPE html>
<html lang='en'>
    <head>
        <meta charset='utf-8'>
        <title>Periodic Table</title>
    </head>
    <body>
        <table>
    """
    template = """
                <td style='border: 1px solid black; padding:10px'>
                    <h4>{elem}</h4>
                    <ul>
                        <li>No {number}</li>
                        <li>{small}</li>
                        <li>{molar}</li>
                        <li>{electron} electron(s)</li>
                    </ul>
                </td>
    """
    for r in range(7):
        row = """
            <tr>"""
        for c in range(18):
            elem, info = find_elem(r, c, dct)
            if elem is not None:
                cell = template.format(
                    elem=elem,
                    number=info['number'],
                    small=info['small'],
                    molar=info['molar'],
                    electron=len(info['electron'].split(' '))
                )
            else:
                cell = """
                <td></td>
                """
            row += cell
        row += """
            </tr>"""
        html += row
    html += """
        </table>
    </body>
</html>"""
    with open("periodic_table.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
