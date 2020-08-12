import json
class Drives:
    def __init__(self, cvd_disk_file):
        with open(cvd_disk_file, "r", encoding="utf-8-sig") as f:
            self.files = json.load(f)
        self.dir = self.files
    def info(self, file):
        '''
Инфа файлов и папок
"[.]"    - текущая папка
"?[:/]*" - от корня
else     - от текущей папки
'''
        file = file.replace("\\", "/")
        if file == ".":
            return self.dir
        elif file[1] == ":":
            file = list(file)
            file.pop(1)
            file = ''.join(file)
            d = self.files
            for dir in file.split("/"):
                if d["type"] in ["directory", "super", "drive"]:
                    d = d["content"][dir]
                else:
                    raise NotADirectoryError('/'.join(file.split("/")[:-1]) + " not a directory")
            return d
        else:
            d = self.dir
            for dir in file.split("/"):
                if d["type"] in ["dir", "super", "drive"]:
                    d = d["content"][dir]
                else:
                    raise NotADirectoryError('/'.join(file.split("/")[:-1]) + " not a directory")
            return d
    def read(self, file):
        return self.info(file)["content"]
    def chdir(self, dir):
        self.dir = self.info(dir)
    def listdir(self, dr="."):
        return list(self.read(dr).keys())
                
            
