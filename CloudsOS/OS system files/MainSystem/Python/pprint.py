import tkinter
window = False
label = None
wd = None
def init_print(tk, lb):
    global wd, label
    wd = tk
    label = lb
    window = True
    
def print(*text, sep=' ', end='\n'):
    assert window, "Print не инициализирован init_print(tk, label)"
    label["text"] = label["text"] + sep.join(text) + end
