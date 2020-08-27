import os,sys
import time
#bebas mengubah AI ini
#tools ini hanya untuk bersenang senang
#ubah nama,umur sesuai dengan nama anda
nama = "Ascen'gi"
umur = 12
p = "#scx: "
def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)

i=input("@you: ")
if("hallo" in i):
    print(p,"hai")

elif("halo" in i):
    print(p,"hai",nama)

elif("siapa namamu" in i):
    print(p,"nama saya adalah scx system")

elif("keluar" in i):
    os.system('clear')

elif("exit" in i):
    os.system('clear')

elif("siapa namaku" in i):
    print(p,"nama anda adalah",nama,"dan umur anda",umur,"tahun")

elif("apa kemampuanmu" in i):
    print("silahkan anda lihat sendiri di daftar kemampuan.txt")

elif("hack" in i):
    hack=input("masukan email dari akun yang ingin di hack: ")
    print("proses...")
    time.sleep(3600)

elif("siapa pacarmu" in i):
    print(p,"saya tidak punya pacar")

elif("kamu cowok apa cewek" in i):
    print(p,"saya robot")

elif("di mana rumah kamu" in i):
    print(p,"saya tinggal di terminal anda")

else:
    print("maaf saya tidak paham")
    print("tolong tambahkan program agar saya paham")

time.sleep(2)
restart()