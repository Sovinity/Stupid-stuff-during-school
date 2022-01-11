'''

CODE BY THE SOVIET UNION.

Created by MushroomEnder on Jan 7th, on Friday

'''

from time import sleep
import platform as pf
import threading as th
import random
import os

'''

MAIN FUNCTIONS

'''

def typed(text, /, time_between: float =0.08, clr: bool=False):
    for i in text:
        print(i, end="", flush="false")
        sleep(time_between)
    sleep(time_between*3)
    print()

def toBool(string: str):
    true_statements = ["yes", "yep", "uh-huh", "yeah", "true"]
    false_statements = ["no", "nope", "nuh-uh", "false"]

    if (string.lower() in true_statements):
        return True;
    elif (string.lower() in false_statements):
        return False;
    else:
        raise TypeError("Statement is neither true nor false.")

def question(text: str, /, return_type: type = str, clr: bool = True, enter_text: str = ">>> "):
    typed(text)
    while True:
        x = input(enter_text)

        try:
            if (return_type == bool):
                y = toBool(x)
            else:
                y = return_type(x)
            if clr: clear()

            return y;
        except Exception:
            typed(f"That was not an accepted type. This is the required type: {return_type}")

def check_if_windows():
    if (pf.system().lower() == "windows"):
        return True;
    else:
        return False;   

def clear():
    if (pf.system().lower() == "windows"):
        os.system("cls")
    elif (pf.system().lower() == "linux"):
        os.system("clear")
'''

BASIC METHODS

'''

def CompileC():
    '''

    Compile the C++ code.

    '''
    os.system("clang++ cplusplus.cpp -orun.exe")

def RunC():
    '''

    Run the C++ code. 

    '''
    os.system("./run.exe")

def add_spaces(array: tuple):
    '''

    String up an array by adding spaces in between.

    '''
    appendable = ""
    for i in array:
        appendable += f"{i} "
    return appendable[:-1]

def test_neo_number():
    initial = question("What is the initial value?", float, False)
    maximum = question("What is the max?", float, False)
    minimum = question("What is the min?", float, False)
    wrap = question("Should it wrap?", bool, False)
    nn = neo_number(initial, minimum, maximum, wrap)

    while (True):
        x = question("", str, False)

        if (x == "add"):
            nn.set_number(nn.Number+question("by how much?", float, False))
        elif (x == "multiply"):
            nn.set_number(nn.Number+question("by how much?", float, False))
        elif (x == "print"):
            print(nn.Number)
        elif (x == "exit"):
            return;

'''

MAIN CLASSES

'''
# Class still under development 

class neo_number:
    def __init__(self, initial: float, /, min:float=None, max:float=None, wrap: bool = True):
        self.Number = initial
        if (max <= min):
            raise ValueError("The minimum cannot be greater than or equal to the maximum.")
        else:
            self.min = min 
            self.max = max
            if (max or min) == None:
                self.wrap = False
            else:
                self.wrap = wrap
    
    def evaluate(self):
        if (self.max != None):
            if (self.Number > self.max):
                if self.wrap:
                    self.Number = self.min + (abs(self.Number)%(self.max-self.min))
                else:
                    self.Number = self.max
        if (self.min != None):
            if (self.Number < self.min):
                if self.wrap:
                    self.Number = self.max - (abs(self.Number)%(self.max-self.min))
                else:
                    self.Number = self.min
        return self.Number
    
    def set_number(self, number):
        self.Number = number 
        self.evaluate()

    # def add(self, other_num):
    #     newValue = self.Number + other_num
    #     if (newValue > self.max):
    #         newValue = newValue % ()

def theCalvinFunction():
    print("**** it's ya boi, kevin bacon")

try:
    if (__name__ == "__main__"):
        typed("hello world", time_between=0.1)
        while True:
            # this code is temporary for now. I'm going to make a method to ask for user input that is better and more precise.
            z = str(input("PY >>> ")).strip(" ")
            y = z.split(" ")
            if (len(y) > 1):
                temp = add_spaces(y[1:])
                y = [y[0], temp]
            x = z.lower()

            # -----------------------------------
            # Fun Commands
            # -----------------------------------

            if (x in ["test neonumber", "test neo number"]):
                test_neo_number()
            
            elif (x == "hello world"):
                typed("Hey that's my line :/")
            
            elif (y[0] == "say"):
                if (y[1].find("-c")):
                    y[1] = y[1].replace("-c", "")
                    clear()

                typed(y[1])

            # -----------------------------------
            # HAPPY ABI WABI
            # -----------------------------------

            elif (x[:3] == "uwu"):
                try:
                    typed("OwO "*int(x[3:]), 0.001)
                except Exception:
                    typed("owo")
            
            elif (x == "ara ara"):
                typed("no stop\n"*2, 0.01)
                typed("no stop")
            
            elif ("snuggles" in x) or ("snuggle" in x) or ("cuddle" in x) or ("cuddles" in x):
                typed(random.choice(["No Snuggles for you.", "You don't get snuggles.", "I probably should let you, but I won't", "I will give you snuggles :3"]), 0.04)
            
            elif (x == "calvin"):
                theCalvinFunction()

            # -----------------------------------
            # Program Commands
            # -----------------------------------

            # C++
            elif (x == "run cplusplus") or (x == "run c++"):
                # with th.Thread(target=CompileC) as nt:
                nt = th.Thread(target=CompileC)
                nt.start()
                # we should put a loading function here so it can show a loading screen in the console while it compiles!


                clear()
                while True:
                    typed("Compiling...", time_between=0.03)
                    if (not nt.is_alive()):
                        typed("Done!", time_between=0.02)
                        break
                    clear()

                del nt
                RunC()
            
            # Node Javascript
            elif (x == "run node"):
                clear()
                if (check_if_windows()):
                    # subprocess.call('node node.js', shell=True)
                    # %SystemRoot%\system32\WindowsPowerShell\\v1.0\powershell.exe 
                    os.system('%SystemRoot%\system32\WindowsPowerShell\\v1.0\powershell.exe node node.js')
                else:
                    os.system("node node.js")
            
            # C Sharp
            elif (x == "run c#") or (x == "run csharp"):
                os.system("clear && echo loading... && csharp csharp.cs")
            
            # Java
            elif (x == "run java"):
                clear()
                typed("loading...", time_between=0.02)
                os.system("java java.java")

                
            # -------------------------------------
            # Shell Commands
            # -------------------------------------
            
            elif (x == "clear"):
                clear()

            elif y[0] in ["console", "cn", "c"]:
                newY = ""
                iterable = list(y[1:]) 
                for i in iterable:
                    newY += f"{i} "
                os.system(newY)

            elif (x ==  "quit") or (x == "exit"):
                os.system("exit")
            else:
                typed("I don't understand :/")
except KeyboardInterrupt:
    typed("\nExitting...")