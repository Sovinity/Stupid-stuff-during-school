'''

CODE BY THE SOVIET UNION.

Created by MushroomEnder on Jan 7th, on Friday

'''

from colorama import Fore, Back
from time import sleep
import platform as pf
import threading as th
import logging
import random
import math
import json 
import os

# Logging Information

logging.basicConfig (
    filename='mainPythonFile.log', 
    filemode='w', 
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

'''

MAIN FUNCTIONS

'''

def typed(text, /, time_between: float =0.08, clr: bool=False) -> None:
    '''
    Types text to the basic console as if it is being spoken!

    text: Text to speak!

    time_between: The time between each character!

    clr: If the console should be cleared before print!
    '''
    if clr:
        clear()
    for i in text:
        print(i, end="", flush="false")
        sleep(time_between)
    sleep(time_between*3)
    print()

def toBool(string: str) -> bool:
    '''
    Translates normal words into a bool!
    '''
    true_statements = ["yes", "yep", "uh-huh", "yeah", "true", "definitely"]
    false_statements = ["no", "nope", "nuh-uh", "false", "definitely not"]

    string = string.strip(" ")

    if (string.lower() in true_statements):
        return True;
    elif (string.lower() in false_statements):
        return False;
    else:
        raise TypeError("Statement is neither true nor false.")

def question(text: str, /, return_type: type = str, clr: bool = True, enter_text: str = ">>> ") -> any:
    '''
    Asks a basic question in the basic console!

    text: The question to ask the user!

    return_type: The type that is required of the user!

    clr: Clear before asks the question!

    enter_text: The text that goes in the "input()" function
    '''
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
    '''
    Loads the save file!
    '''
    with open("savefile.json", 'r') as s:
        data = json.load(s)
    return data;

def check_if_windows() -> bool:
    '''
    Check if the system is running windows!

    (Because Windows is so specific and it has to be cradled like a wittwe babwy!)
    '''
    if (pf.system().lower() == "windows"):
        return True;
    else:
        return False;   

def clear() -> None:
    '''
    Clear the console! 

    Determines if it is windows, or linux!
    '''
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

    x = ["Hello,", "world", "!"]

    add_spaces(x) -> "Hello, world !"

    '''
    appendable = ""
    for i in array:
        appendable += f"{i} "
    return appendable[:-1]

'''

MAIN CLASSES

'''

class screen:
    '''
    Creates a screen that is manipulateable!

    After text is written to it, it saves it in the content variable,
    so you can mess with the variable, and update the screen!
    '''
    def __init__(self, initial:list=[], /, max:int = None):
        self.content = initial
        # print(max)
        if (max != None) and (max <= 0): raise ValueError("Max has to be greater than one.")
        self.max = max

    @property
    def content(self):
        return self._content;
    
    @content.setter
    def content(self, setValue, /, update:bool=True):
        self._content = setValue;
        if update:
            self.update()
    
    def update(self):
        '''
        Updates the screen with the current information!
        '''
        clear()
        if self.max:
            while len(self.content) > self.max:
                self.content.pop(0)
        for i in self.content:
            print(i)
        
    def typed(self, text: str, time_between:float=0.08, clr:bool=False):
        '''
        Write text to the shell as if it was speech!

        text: The text spoken to the screen!

        time_between: the amount of time between each character!

        clr: If it should clear the screen before speech!
        '''
        self.update()
        if clr:
            self.clear()
        for i in text:
            print(i, end="", flush="false")
            sleep(time_between)
        self.append(text)
        sleep(time_between*3)
        print()
    
    def clear(self):
        '''
        Clears the screen, and updates!
        '''
        self.content = []
        self.update()
    
    def append(self, screen_item: str, insertion_placement: int = None):
        '''
        Add something to the screen!
        If no insertion placement is given, it will place it at the end.
        '''
        if insertion_placement == None:
            self.content.append(screen_item)
        else:
            self.content.insert(insertion_placement, screen_item)
        self.update()


class shell(screen):
    def __init__(self, shell_func, start_content:list = [], /, beckon_text: str = "--\nPY >>> ", clr_constantly: bool = False, max:int=None):
        self.beckon_text = beckon_text
        self.clr = clr_constantly
        self.shell_func = shell_func
        self.max = max
        super().__init__(start_content, max)
    
    def solve_shell(self, /, args=[], clr:bool=False):
        '''
        Run your function with the shell!

        This shell object is passed to it as the first parameter!
        Returns the return value of your function as well!

        def your_func(shell_object, args)
        '''
        if clr:
            clear()
        return self.shell_func(self, args)

    def beckon(self):
        '''
        
        Returns a list of 3 similar values from the shell.

        x: Stripped lower case letters
        y: A list structured like this: [<first word: str>, <main body text: str>, <flags: list>]
        z: The raw input string

        '''
        z = str(input(self.beckon_text)).strip(" ")
        y = z.split(" ")
        x = z.lower()
        flags = []

        b = False
        for count,i in enumerate(y):
            if i[0] == "-":
                b = True
                break 
        
        if b:
            for i in y[count][1:]:
                flags.append(i)
            y.pop(count)
        y = [y[0], add_spaces(y[1:]), flags]

        return [x, y, z];


class neo_number:
    '''
    A number with a max and a minimum!
    You can even make it wrap back and forth through
    the min and max!
    '''
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

def theCalvinFunction(shell_class) -> None:
    '''
    IT'S YA BOI KEVIN BACON
    '''
    shell_class.typed("**** it's ya boi, kevin bacon")

def helloWorld(shell_class: shell) -> None:
    '''
    Sing the beautiful song "hello world" by Louie Zong!

    https://www.youtube.com/watch?v=Yw6u6YkTgQ4
    '''
    try:
        shell_class.typed("Hello World", 0.1)
        sleep(1)
        shell_class.typed("Programmed to work and not to feel.", 0.1)
        sleep(1)
        shell_class.typed("Not even sure that this is real.", 0.1)
        sleep(1)
        shell_class.typed("Hello World", 0.3)
        sleep(3)
    except KeyboardInterrupt:
        shell_class.typed("\nWhy are you stopping me?", 0.04)

def theReaperFunction(shell_class: shell, pick: int = 3, type_rest: float = 0.04):
    '''
    Talk to the man death himself!
    '''
    if (pick == 0):
        shell_class.typed(random.choice(
            [
                "You called?", 
                "Yeah, I'm here, why?", 
                "Suprise, I am in fact, not dead.", 
                "Probably had to poke around your code to find this."
            ]), type_rest)
    elif (pick == 1):
        shell_class.typed(random.choice(
            [
                "Hacker Online", 
                "SGFja2VyIE9ubGluZQ==", 
                "48 61 63 6b 65 72 20 4f 6e 6c 69 6e 65", 
                "01001000 01100001 01100011 01101011 01100101 01110010 00100000 01001111 01101110 01101100 01101001 01101110 01100101", 
                "Looking for the hivemind?"
            ]), type_rest)
    else:
        shell_class.typed(random.choice(
            [
                "Did you seriously just call my function raw?", 
                "Not even an variable? How rude.", 
                "Seriously, use some arguments why don't you?"
            ]), type_rest)

def hackerAlert(shell_class: shell):
    shell_class.typed(random.choice(
        [
            "Oh no, not a hacker!", 
            "What, a hacker, where!?", 
            "Ahhh, everybody run there's a hacker.", 
            "Follow this link for free bitCoin --> https://printer.discord.com"
        ]), 0.04)

def shell_code(shell_class: shell, args: list):
    '''
    This is the main shell area of this code!
    '''
    x,y,z = shell_class.beckon()
    if not "r" in y[2]: 
        shell_class.append(f"> {z}")
    # -----------------------------------
    # Fun Commands
    # -----------------------------------

    successful = True
    
    if (x == "hello world"):
        shell_class.typed("Hey that's my line :/")
        # print(shell_class.content)
    elif ("sing" in x):
        helloWorld(shell_class)
    
    elif (y[0] == "say"):
        if ("c" in y[2]):
            shell_class.clear()

        shell_class.typed(y[1])
    
    elif ("nya" in x):
        shell_class.typed("I wove you~")

    # -----------------------------------
    # HAPPY ABI WABI
    # -----------------------------------

    elif (x[:3] == "uwu"):
        try:
            shell_class.typed("OwO "*int(x[3:]), 0.001)
        except Exception:
            shell_class.typed("owo")
    
    elif (x == "ara ara"):
        shell_class.typed("no stop\n"*2, 0.01)
        shell_class.typed("no stop")
    
    elif ("snuggles" in x) or ("snuggle" in x) or ("cuddle" in x) or ("cuddles" in x):
        shell_class.typed(random.choice(["No Snuggles for you.", "You don't get snuggles.", "I probably should let you, but I won't", "I will give you snuggles :3"]), 0.04)
    
    elif (x == "calvin"):
        theCalvinFunction(shell_class)
    
    # optimizing this for ya
    # ("reaper" in x) or ("death" in x)
    elif (x in ["reaper", "death"]):
        theReaperFunction(shell_class, 0, 0.04)

    elif ("hack" in x):
        hackerAlert(shell_class)
    
    # -----------------------------------
    # Program Commands
    # -----------------------------------

    # C++
    elif (x == "run cplusplus") or (x == "run c++"):
        # with th.Thread(target=CompileC) as nt:
        nt = th.Thread(target=CompileC)
        nt.start()
        # we should put a loading function here so it can show a loading screen in the console while it compiles!


        shell_class.clear()
        while True:
            shell_class.clear()
            shell_class.typed("Compiling...", time_between=0.03)
            if (not nt.is_alive()):
                shell_class.typed("Done!", time_between=0.02)
                break
            shell_class.clear()

        del nt
        RunC()
    
    # Node Javascript
    elif (x == "run node"):
        shell_class.clear()
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
        shell_class.clear()
        shell_class.typed("loading...", time_between=0.02)
        os.system("java java.java")

        
    # -------------------------------------
    # Shell Commands
    # -------------------------------------
    
    elif (x == "clear"):
        shell_class.clear()

    elif y[0] in ["console", "cn", "c"]:
        newY = ""
        iterable = list(y[1:]) 
        for i in iterable:
            newY += f"{i} "
        os.system(newY)

    elif (x ==  "quit") or (x == "exit"):
        return 1;
    else:
        shell_class.typed("I don't understand :/")
        successful = False 
    
    if not "r" in y[2]:
        try:
            shell_class.content.pop(-2)
            if (successful):
                shell_class.append(f"> {Fore.GREEN}{z} {Fore.WHITE}", -1)
            else:
                shell_class.append(f"> {Fore.RED}{z} {Fore.WHITE}", -1)
        except IndexError:
            pass

if (__name__ == "__main__"):
    newShell = shell(shell_code, [], max=8)
    while True:
        try:
            exit_code = newShell.solve_shell()
            if exit_code == 1:
                break
        except KeyboardInterrupt:
            typed("\nExitting...")
            break