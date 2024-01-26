import sys


def create_dct(data_lst):
    dct = {
        elem.split(" = ")[0] : {
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
    html = "<!DOCTYPE html><html lang='en'><head><title>Periodic Table</title></head><body><table>"
    for r in range(7):
        row = "<tr>"
        for c in range(18):
            elem, info = find_elem(r, c, dct)
            if elem is not None:
                cell = "<td style='border: 1px solid black; padding:10px'>"
                cell += f"<h4>{elem}</h4>"
                cell += "<ul>"
                cell += f"<li>No {info['number']}</li>"
                cell += f"<li>{info['small']}</li>"
                cell += f"<li>{info['molar']}</li>"
                cell += f"<li>{len(info['electron'].split(' '))} electron(s)</li>"
                cell += "</ul>"
                cell += "</td>"
            else:
                cell = "<td></td>"
            row += cell
        row += "</tr>"
        html += row
    html += "</table></body></html>"
    with open("periodic_table.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
