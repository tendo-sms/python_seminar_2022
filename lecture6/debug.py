inputdata = {}
with open("debug_input.txt", encoding="utf_8") as f:
    for line in f:
        if "=" in line:
            split_line = line.split("=")
            inputdata[split_line[0]] = split_line[1].strip()

# TITLE
print(inputdata.get("TITLE"))

# DATA TYPE
print(inputdata.get("DATA TYPE"))

# OWNER
print(inputdata.get("OWNER"))

# LONGDATE
print(inputdata.get("LONGDATE"))
