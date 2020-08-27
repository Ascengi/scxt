import os,sys
import time

def ret():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)

print("masukan password jika anda memiliki tools ini")
password = "Daisha"
def main():
    inp=input("masukan password: ")
 
    if(inp ==  password):
        print("Berhasil login")
        sys.exit()

    else:
        ret()

try:
    main()
except keyboardInterput:
    os.system('clear')
    restart()