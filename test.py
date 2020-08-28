import os
import time
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
s = time.strftime("%H.%M.%S")

ss = "hello "
print(s)

print(ss)
speak.Speak(ss)