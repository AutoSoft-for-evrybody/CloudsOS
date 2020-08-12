import json
import os
f = input("file.cvd: ")
with open(f, "r", encoding="utf-8-sig") as f:
            files = json.load(f)

def opn(files, n, location=""):
    if (files["type"] in ["super", "dir", "drive"]):
        os.mkdir(location + "/" + n)
        for k, v in files["content"].items():
            print(k)
            opn(v, k, location + "/" + n)
    elif (files["type"] == "file"):
        with open(location + "/" + k, "w") as file:
            file.write(files["content"])
opn(files, "drives", os.curdir)
    
