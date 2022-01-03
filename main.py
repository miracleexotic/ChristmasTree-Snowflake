import curses
from curses import wrapper
import time
import random

def main(stdscr):

    stdscr.clear()
    
    pad = curses.newpad(101, 101)
    stdscr.refresh()

    try:
        space = 5
        while True:
            for y in range(0, 100):
                for x in range(0, 100):
                    if x == random.randint(0, 100):
                        pad.addstr(y,x, f"{random.choice(['.', '*', 'o'])}")
        
            for i in range(100-30, -1, -1):
                
                # Ref = http://talk-it.biz/wp-content/uploads/2015/01/ASCI_Art4ef4a62daa7be.png
                pad.addstr(i+space+1,15+15, ",")
                pad.addstr(i+space+2,15+14, "_/^\_")
                pad.addstr(i+space+3,15+13, "<     >")
                pad.addstr(i+space+4,15+13, " / - \\   ")
                pad.addstr(i+space+5,15+13, " `/&\\`    ")
                pad.addstr(i+space+6,15+13, ",@.*;@,")
                pad.addstr(i+space+7,15+12, "/_o.I %_\\")
                pad.addstr(i+space+8,15+11, "(`\'--:o(_@;")
                pad.addstr(i+space+9,15+10, "/`;--.,__ `\')")
                pad.addstr(i+space+10,15+9, ";@`o % O,*`\'`&\\")
                pad.addstr(i+space+11,15+8, "(`\'--)_@ ;o %'()\\")
                pad.addstr(i+space+12,15+8, "/`;--._`\'\'--._O\'@;")
                pad.addstr(i+space+13,15+7, "/&*,()~o`;-.,_ `\"\"`)")
                pad.addstr(i+space+14,15+7, "/`,@ ;+& () o*`;-\";\\")
                pad.addstr(i+space+15,15+6, "(`\"\"--.,_0 +% @' &()\\")
                pad.addstr(i+space+16,15+6, "/-.,_    ``''--....-'`)")
                pad.addstr(i+space+17,15+6, "/@%;o`:;'--,.__   __.'\\")
                pad.addstr(i+space+18,15+5, ";*,&(); @ % &^;~`\"`o;@();")
                pad.addstr(i+space+19,15+5, "/(); o^~; & ().o@*&`;&%O\\")
                pad.addstr(i+space+20,15+5, "`\"=\"==\"\"==,,,.,=\"==\"===\"`")
                pad.addstr(i+space+21,15+2, "__.----.(\\-''#####---...___...-----._")
                pad.addstr(i+space+22,15, "'`         \)_`\"\"\"\"\"`                  ")
                pad.addstr(i+space+23,15, "        .--' ')                             ")
                pad.addstr(i+space+24,15, "      o(  )_-\\                             ")
                pad.addstr(i+space+25,15, "        `\"\"\"`  `                         ")

                pad.refresh(i,0, 0,0, 30,99)
                time.sleep(0.1)

            pad.clear()

    except:
        print("[!] terminal size < lines=150,cols=150")


wrapper(main)

