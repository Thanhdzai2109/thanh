
def gender(string):
    for i in string.split():
        if(i=="Nam" or i=="nam"):
            return "Nam"
        if(i=="Nữ" or i=="nữ" or i== "nu" or i=="Nu"):
            return "Nữ"
    return "none"

def math(string):
    if gender(string) == "Nam":
        return 170/0.7
    else:
        return 170
print(math("Nam 170 65"))