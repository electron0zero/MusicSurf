import os
os.system('python -m pip install termcolor')
from termcolor import colored
print(colored('helloworld', 'red'))
try:
    i = 1 / 0
except Exception as ex:
    print(colored('exception r:' + str(ex), "red"))
