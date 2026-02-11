import pyfiglet
import os
from termcolor import colored
import sys
import time
import threading

os.system('clear')

def loading_animation():
    # Spinner အတွက် အသုံးပြုမယ့် character များ
    chars = ["/", "-", "\\", "|"]
    print("Starting Server Wait... ", end="")
    os.system('clear')

    # ၅ စက္ကန့်လောက် လည်နေအောင် လုပ်ထားတာပါ
    end_time = time.time() + 5
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f"\rStarting Server Wait... {char}")
            sys.stdout.flush()
            time.sleep(0.1)

# Animation ကို run မည်
loading_animation()

print ("\n")
print ("\n")
colorname = colored(input("\nEnter UserName ==> "),color="red") #username

def bf ():
	os.system ("clear")
	gun = colored ("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⢈⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢤⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⠐⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠺⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⠟⢁⣴⣷⣦⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠛⡆⠀⠉⠛⠻⠿⠿⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣴⣿⡦⠀⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⣿⡿⠁⠀⠘⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[version 1.0.0]
⠀⣰⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠻⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""",color="red")


def TextCounter(): # No1 Menu
	os.system ("clear")
	text_figlet = pyfiglet.figlet_format ("Text Counter",font = "slant")
	text_counter = colored (text_figlet, color = "yellow")
	print (text_counter)
	TextCount = colored("Text Counter : ",color = "green")
	colorTextCounter = input (f"{TextCount}")
	print (len(colorTextCounter))


bestcoder = pyfiglet.figlet_format ("Best Coder",font = "script") #banner
colorbanner = colored(bestcoder, color= "magenta") #banner

Textcounter = colored("[1] TextCounter",color = "red") #1
font =colored("[2] Banner font",color = "red") #2
About = colored("[3] About",color = "red") #3
Exit = colored ("[4] Exit",color = "red") #4

linebanner = ("=================================================================")
linecolorbanner = colored (linebanner,color = "cyan")
versioncolor = colored("vesion1.0.0",color = "red")
welcome = colored ("Welcome", color = "blue")
choicemenu = colored ("[CHOICEMEN] ==> ", color = "green")

print (linecolorbanner)
print (linecolorbanner)
print (colorbanner)
print (f"   {welcome} -- ({colorname})                           	{versioncolor}")
print (linecolorbanner)
print (linecolorbanner)
print ("")
print (Textcounter)
print ("")
print (font)
print ("")
print (About)
print ("")
print (Exit)
print ("")
choice_menu = input (f"{choicemenu}")
if choice_menu == "1":
	TextCounter ()
elif choice_menu == "2":
	bf ()
elif choice_menu == "3":
	pass
elif choice_menu == "4":
	print (f"Thank ...{username}")
else:
	print ("You choice Menu number , Error Code")


