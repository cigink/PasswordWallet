# Python 3
# this is a test program to store passwords
# By Cigin Koshy
PASSWORDS = {'facebook' : 'Password',
             'gmail' : 'Password2'
             }

import sys
import pyperclip
if len(sys.argv)<2 :
    print ('Using python to copy password')
    sys.exit()

account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print ('Password to account copied to clipboard')
else :
    print ('Account not found')