'''

CODE BY THE SOVIET UNION.

Created by MushroomEnder on Jan 7th, on Friday

'''

from time import sleep
import platform as pf
import threading as th
import random
import math
import json 
import os

'''

MAIN FUNCTIONS

'''

def typed(text, /, time_between: float =0.08, clr: bool=False) -> None:
    for i in text:
        print(i, end="", flush="false")
        sleep(time_between)
    sleep(time_between*3)
    print()

def toBool(string: str) -> bool:
    true_statements = ["yes", "yep", "uh-huh", "yeah", "true", "definitely"]
    false_statements = ["no", "nope", "nuh-uh", "false", "definitely not"]

    if (string.lower() in true_statements):
        return True;
    elif (string.lower() in false_statements):
        return False;
    else:
        raise TypeError("Statement is neither true nor false.")

def question(text: str, /, return_type: type = str, clr: bool = True, enter_text: str = ">>> ") -> any:
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

def load_save() -> dict:
    with open("savefile.json", 'r') as s:
        data = json.load(s)
    return data;

def check_if_windows() -> bool:
    if (pf.system().lower() == "windows"):
        return True;
    else:
        return False;   

def clear() -> None:
    if (pf.system().lower() == "windows"):
        os.system("cls")
    elif (pf.system().lower() == "linux"):
        os.system("clear")
'''

BASIC METHODS

'''

def CompileC() -> None:
    '''

    Compile the C++ code.

    '''
    os.system("clang++ cplusplus.cpp -orun.exe")

def RunC() -> None:
    '''

    Run the C++ code. 

    '''
    os.system("./run.exe")

def add_spaces(array: tuple) -> None:
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
            
def helloWorld() -> None:
    try:
        typed("Hello World", 0.1)
        sleep(1)
        typed("Programmed to work and not to feel.", 0.1)
        sleep(1)
        typed("Not even sure that this is real.", 0.1)
        sleep(1)
        typed("Hello World", 0.3)
        sleep(3)
        clear()
    except KeyboardInterrupt:
        typed("\nWhy are you stopping me?", 0.04)

'''

MAIN CLASSES

'''

class screen:
    def __init__(self, initial:list=[]):
        self.content = initial 

    @property
    def content(self):
        return self._content;
    
    @content.setter
    def content(self, setValue, /, update:bool=True):
        self._content = setValue;
        if update:
            self.update()
    
    def update(self):
        clear()
        for i in self.content:
            print(i)
        
    def typed(self, text: str, time_between:float=0.08, clr:bool=False):
        self.update()
        if clr:
            self.content = []
        for i in text:
            print(i, end="", flush="false")
            sleep(time_between)
        self.content.append(text)
        self.update()
        sleep(time_between*3)
        print()
    
    def clear(self):
        self.content = []


class shell(screen):
    def __init__(self, shell_func, start_content:list = [], /, beckon_text: str = "--\nPY >>> ", clr_constantly: bool = False):
        self.beckon_text = beckon_text
        self.clr = clr_constantly
        self.shell_func = shell_func
        super().__init__(start_content)
    
    def solve_shell(self, clr:bool=False):
        if clr:
            clear()
        self.shell_func(self)

    def beckon(self):
        '''
        
        Returns a list of 3 similar values from the shell.

        x: Stripped lower case letters
        y: A list structured like this: [<first word>, <second word>]
        z: The raw input string

        '''
        z = str(input(self.beckon_text)).strip(" ")
        y = z.split(" ")
        if (len(y) > 1):
            temp = add_spaces(y[1:])
            y = [y[0], temp]
        x = z.lower()
        return [x, y, z];


class neo_number:
    def __init__(self, initial: float, /, min:float=None, max:float=None, wrap: bool = True):
        self._number = initial
        if (max <= min and not (min or max) == None):
            raise ValueError("The minimum cannot be greater than or equal to the maximum.")
        else:
            self.min = min 
            self.max = max
        if (max or min) == None:
            self.wrap = False
        else:
            self.wrap = wrap
    
    @property
    def Number(self) -> float:
        return self._number;

    @Number.setter
    def Number(self, newNumber) -> Number:
        self._number = newNumber
        if (self.max != None) and (self.Number > self.max):
            if self.wrap:
                #Method 3 (Logical Mathematical version, extracting the percentage, and multiplies it against the full width between the min and the max)
                # x = ((self.Number - self.max) / (self.max-self.min))
                # y = x - (math.floor(x))
                # self.Number = self.min+round((self.max-self.min)*y, (len(str(self.Number))))

                # Method 4 (uses the negative space of the percentage)
                
                # Get the amount of times that the value is over the maximum
                x = ((self.Number - self.min) / (self.max-self.min))

                # Floor it, and find how many times it loops over the maximum (It's floored because that little 
                # extra bit that wasn't floored will stay. It's similar to the previous method of using the 
                # percentage, but it does it the opposite way so it is accurate and doesn't use the percentage)
                # honestly way too complicated to explain
                y = (math.floor(x))*(self.max-self.min)

                # then subtract that value, leaving that small percentage left that did not go over the maximum.
                self.Number = self.Number - y

            else:
                self.Number = self.max
        if (self.min != None) and (self.Number < self.min):
            if self.wrap:
                # Method 3
                # x = ((self.Number - self.min) / (self.max-self.min))
                # y = abs(x - (math.floor(x)))
                # self.Number = self.min+round((self.max-self.min)*y, (len(str(self.Number))))

                # Method 4
                x = ((self.Number - self.max) / (self.max-self.min))

                y = (math.ceil(x)*(self.max-self.min))

                self.Number = self.Number - y

                # Just sitting here coding this, thinking, "I need to watch SAO again."
            else:
                self.Number = self.min
        return self.Number

def theCalvinFunction() -> None:
    print("**** it's ya boi, kevin bacon")

def theReaperFunction(pick: int = 3, type_rest: float = 0.04):
    if (pick == 0):
        typed(random.choice(
            [
                "You called?", 
                "Yeah, I'm here, why?", 
                "Suprise, I am in fact, not dead.", 
                "Probably had to poke around your code to find this."
            ]), type_rest)
    elif (pick == 1):
        typed(random.choice(
            [
                "Hacker Online", 
                "SGFja2VyIE9ubGluZQ==", 
                "48 61 63 6b 65 72 20 4f 6e 6c 69 6e 65", 
                "01001000 01100001 01100011 01101011 01100101 01110010 00100000 01001111 01101110 01101100 01101001 01101110 01100101", 
                "Looking for the hivemind?"
            ]), type_rest)
    else:
        typed(random.choice(
            [
                "Did you seriously just call my function raw?", 
                "Not even an variable? How rude.", 
                "Seriously, use some arguments why don't you?"
            ]), type_rest)

def hackerAlert():
    typed(random.choice(
        [
            "Oh no, not a hacker!", 
            "What, a hacker, where!?", 
            "Ahhh, everybody run there's a hacker.", 
            "Follow this link for free bitCoin --> https://printer.discord.com"
        ]), 0.04)

def shell_code(shell_class: shell):
    x,y,z = shell_class.beckon()

    # -----------------------------------
    # Fun Commands
    # -----------------------------------

    if (x in ["test neonumber", "test neo number"]):
        test_neo_number()
    
    elif (x == "hello world"):
        shell_class.typed("Hey that's my line :/")
        # print(shell_class.content)
    elif ("sing" in x):
        helloWorld()
    
    elif (y[0] == "say"):
        if (y[1].find("-c") != -1):
            # print(y[1].find("-c"))
            y[1] = y[1].replace("-c", "")
            clear()
            

        typed(y[1])
    
    elif ("nya" in x):
        typed("I wove you~")

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
    
    # optimizing this for ya
    # ("reaper" in x) or ("death" in x)
    elif (x in ["reaper", "death"]):
        theReaperFunction(0, 0.04)

    elif ("hack" in x):
        hackerAlert()
    
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
        return 1;
    else:
        typed("I don't understand :/")

if (__name__ == "__main__"):
    newShell = shell(shell_code, [])
    while True:
        try:
            exit_code = newShell.solve_shell()
            if exit_code == 1:
                break
        except KeyboardInterrupt:
            typed("\nExitting...")
            break