'''test in online mode'''

from delay import Delay
from termcolor import colored
import time


delay_online = Delay(delay_on=2, delay_off=0)

insec = 2
rep = 2

l = []
l += [False]*10
l += ([True]*insec + [False]*insec) * rep
l += ([True]*2*insec + [False]*2*insec) * rep
l += ([True]*3*insec + [False]*3*insec) * rep
l += ([True]*insec + [False]*insec) * rep
l += ([True]*4*insec + [False]*4*insec) * rep
l += ([True]*5*insec + [False]*5*insec) * rep
l += ([True]*6*insec + [False]*6*insec) * rep

for c in l:
    time.sleep(0.4)
    inp = c
    out = delay_online(c)
    color = "green" if inp == out else "grey"
    on_c = "on_white" if inp == out else "on_red"   
    conn = " ---------- " if inp == out else " ----/---- " 
    print(colored(str(c) + conn + str(out) , color, on_c, attrs=['bold']))
    print("$$"*20)
    print()

