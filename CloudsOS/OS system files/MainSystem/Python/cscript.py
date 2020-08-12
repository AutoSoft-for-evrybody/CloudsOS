def run(code):
    comands = code.split(";")
    i = 0
    while(i < len(comands)):
        comands[i] = comands[i].strip("\n")
        i+=1
    del i
    for cmd in comands:
        compile(cmd.strip(" "))
def compile(cmd):
    # cmd - строка вида say("привет!")
    if (cmd.startswith("say")):
        params = cmd[4:].split(",")
        i = 0
        while(i < len(params)):
            params[i] = params[i].strip(" ")
            i+=1
        del i
        print(params[0].strip("\""))
    # Сам придумал но ты можешь помочь в некоторых понятаих
