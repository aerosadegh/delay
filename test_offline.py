##   Test Delay in offline mode  (data with time)
from delay import Delay
from termcolor import colored
from random import randrange, choice, seed
import datetime 

print("\n\n$$$$$$$$$$$     OFFLINE MODE      $$$$$$$$$$$\n\n")
# Test Delay in offline mode

seed(123456)
prev = False

def sig_gen(prev):
    c = [prev]*2 + [not prev]
    return choice(c)


def random_date(start,l):
    current = start
    while l >= 0:
        tdl = datetime.timedelta(seconds=randrange(1,7))
        #print(tdl)
        current = current + tdl
        yield current
        l-=1


data = []
startDate = datetime.datetime(2019, 9, 20,13,00)

for x in random_date(startDate,20):
    prev = sig_gen(prev)
    data.append((x, prev))


delay_offline = Delay(delay_on=3, delay_off=4)
for t, d in data:
    inp = d
    out = delay_offline(d, t.timestamp())
    color = "green" if inp == out else "grey"
    on_c = "on_white" if inp == out else "on_red"   
    conn = " ---------- " if inp == out else " ----/---- " 
    print(colored(str(d) + conn + str(out) , color, on_c, attrs=['bold']))
    print("$$"*20)
    print()
