
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
from re import sub
import zlib
from datetime import date

today = str(date.today())
today = today.replace("-","")
ip = input("IP: ")
discord_user = input("DISCORD USER: ")
subscription = input("SUBSCRIPTION TYPE: ")
if subscription == "week" or subscription == "month":
    subscription = subscription+today


string = ip+"-"+discord_user
string = string.encode()

def obscure(data):
    return b64e(zlib.compress(data,9)).decode()

with open("db.txt","a") as file:
    print(obscure(string))
    file.write(str(obscure(string))+subscription+"\n")