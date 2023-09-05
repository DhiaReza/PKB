import math
import os 
file_input = open("test_data4.txt","r")
file_output = open("output.txt","a")
type = file_input.readline()
try:
    type=int(type)
except:
    print("File yang dibuka tidak sesuai dengan format yang diminta.")
    exit()
if type>=1 and type<=4:
    pass
else:
    print("File yang dibuka tidak sesuai dengan format yang diminta.")
    exit()

def percentage(bobot):
    sum=0
    for i in bobot.keys():
        sum=sum+bobot[i]
    for i in bobot.keys():
        bobot[i]/=sum
    return bobot

if type== 3 or type == 4:
    bobot = {"width":1/4,"length": 1/4,"height":1/4,"lwh":1/4}
    guess = {"width":"Small Leaf","length": "Small Leaf","height":"Small Leaf","lwh":"Small Leaf",}
    arr = ["width","length","height","lwh",]
    barrier = {"width": [3,6],"length": [5,10], "height":[0.3,0.6] , "lwh":[3.5325 , 28.26]}
else:
    bobot = {"width":1/3,"length": 1/3,"lw":1/3}
    guess = {"width":"Small Leaf","length": "Small Leaf","lw":"Small Leaf"}
    arr = ["width","length","lw"]
    barrier = {"width": [3],"length": [5],"lw":[11.775]}

count=0
for line in file_input:
    line = line.replace(",",".")
    line = line.replace("\n","")
    line = line.split("\t")
    count+=1
    line[0],line[1] = float(line[0]),float(line[1])
    if type == 1 or type == 2:
        if line[0] < barrier["width"][0]:
            guess["width"]="Small Leaf"
        else:
            guess["width"]="Big Leaf"
        if line[1] < barrier["length"][0]:
            guess["length"]="Small Leaf"
        else:
            guess["length"]="Big Leaf"
        lw = math.pi*line[0]*line[1]/4
        line.insert(2,lw)
        if line[2] < barrier["lw"][0]:
            guess["lw"]="Small Leaf"
        else:
            guess["lw"]="Big Leaf"
        wrong_guess = 0
        for i in guess.values():
            if line[3]!=i:
                wrong_guess+=1
        for i in guess.keys():
            if wrong_guess==0: 
                break
            if line[3]==guess[i]:
                bobot[i]=bobot[i]+((1-bobot[i])*0.01)
            else:
                if wrong_guess!=3:
                    bobot[i]=bobot[i]-((bobot[i])*0.067)
                barrier[i][0]=barrier[i][0]-(barrier[i][0]-line[arr.index(i)])*bobot[i]
        bobot=percentage(bobot)
    elif type == 3 :
        line[2] = float(line[2])
        if line[0] < barrier["width"][0]:
            guess["width"]="Small Leaf"
        else:
            guess["width"]="Big Leaf"
        if line[1] < barrier["length"][0]:
            guess["length"]="Small Leaf"
        else:
            guess["length"]="Big Leaf"
        if line[2] < barrier["height"][0]:
            guess["height"]="Small Leaf"
        else:
            guess["height"]="Big Leaf"
        lwh = math.pi*line[0]*line[1]/4*line[2]
        line.insert(3,lwh)
        if line[3] < barrier["lwh"][0]:
            guess["lwh"]="Small Leaf"
        else:
            guess["lwh"]="Big Leaf"
        wrong_guess = 0
        for i in guess.values():
            if line[4]!=i:
                wrong_guess+=1
        for i in guess.keys():
            if wrong_guess==0: 
                break
            if line[4]==guess[i]:
                bobot[i]=bobot[i]+((1-bobot[i])*0.01)
            else:
                if wrong_guess!=4:
                    bobot[i]=bobot[i]-((bobot[i])*0.067)
                barrier[i][0]=barrier[i][0]-(barrier[i][0]-line[arr.index(i)])*bobot[i]
        bobot=percentage(bobot)
    elif type == 4 :
        line[2] = float(line[2])
        if line[0] < barrier["width"][0]:
            guess["width"]="Small Leaf"
        elif line[0]<barrier["width"][1]:
            guess["width"]="Big Leaf"
        else:
            guess["width"]="Very Big Leaf"
        if line[1] < barrier["length"][0]:
            guess["length"]="Small Leaf"
        elif line[1]<barrier["length"][1]:
            guess["length"]="Big Leaf"
        else:
            guess["length"]="Very Big Leaf"
        if line[2] < barrier["height"][0]:
            guess["height"]="Small Leaf"
        elif line[2]<barrier["height"][1]:
            guess["height"]="Big Leaf"
        else:
            guess["height"]="Very Big Leaf"
        lwh = math.pi*line[0]*line[1]/4*line[2]
        line.insert(3,lwh)
        if line[3] < barrier["lwh"][0]:
            guess["lwh"]="Small Leaf"
        elif line[3]<barrier["lwh"][1]:
            guess["lwh"]="Big Leaf"
        else:
            guess["lwh"]="Very Big Leaf"
        wrong_guess = 0
        for i in guess.values():
            if line[4]!=i:
                wrong_guess+=1
        for i in guess.keys():
            if wrong_guess==0: 
                break
            if line[4]==guess[i]:
                bobot[i]=bobot[i]+((1-bobot[i])*0.01)
            else:
                if wrong_guess!=4:
                    bobot[i]=bobot[i]-((bobot[i])*0.067)
                if line[4] == "Small Leaf":
                    if guess[i] == "Big Leaf":
                        barrier[i][0]=barrier[i][0]-(barrier[i][0]-line[arr.index(i)])*bobot[i]
                        barrier[i][1]=barrier[i][1]-(barrier[i][1]-line[arr.index(i)])*bobot[i]*(barrier[i][0]-line[arr.index(i)])/(barrier[i][1]-line[arr.index(i)])
                    if guess[i] == "Very Big Leaf":
                        barrier[i][0]=barrier[i][0]-(barrier[i][0]-line[arr.index(i)])*bobot[i]
                        barrier[i][1]=barrier[i][1]-(barrier[i][1]-line[arr.index(i)])*bobot[i]
                elif line[4] == "Big Leaf":
                    if guess[i] == "Small Leaf":
                        barrier[i][0]=barrier[i][0]-(barrier[i][0]-line[arr.index(i)])*bobot[i]
                        barrier[i][1]=barrier[i][1]-(barrier[i][1]-line[arr.index(i)])*bobot[i]*(barrier[i][0]-line[arr.index(i)])/(barrier[i][1]-line[arr.index(i)])
                    if guess[i] == "Very Big Leaf":
                        barrier[i][0]=barrier[i][0]-(barrier[i][0]-line[arr.index(i)])*bobot[i]*(barrier[i][1]-line[arr.index(i)])/(barrier[i][0]-line[arr.index(i)])
                        barrier[i][1]=barrier[i][1]-(barrier[i][1]-line[arr.index(i)])*bobot[i]
                if line[4] == "Very Big Leaf":
                    if guess[i] == "Small Leaf":
                        barrier[i][0]=barrier[i][0]-(barrier[i][0]-line[arr.index(i)])*bobot[i]
                        barrier[i][1]=barrier[i][1]-(barrier[i][1]-line[arr.index(i)])*bobot[i]
                    if guess[i] == "Big Leaf":
                        barrier[i][0]=barrier[i][0]-(barrier[i][0]-line[arr.index(i)])*bobot[i]*(barrier[i][1]-line[arr.index(i)])/(barrier[i][0]-line[arr.index(i)])
                        barrier[i][1]=barrier[i][1]-(barrier[i][1]-line[arr.index(i)])*bobot[i]
        bobot=percentage(bobot)

print("Selamat Datang di Program Penebak Species Daun")
def Option():
    print("Menu:")
    print("1. Lihat Bobot dan Batas Data")
    print("2. Tebak Species Daun")
    print("3. Keluar")
    print("Option:",end=" ")
while True:
    os.system("clear")
    Option()
    option = input()
    if option =="1":
        print(bobot)
        print(barrier)
        x = input("[Press Enter To Continue]")
    elif option =="2":
        while True:
            if type == 1:
                width = input("Lebar Daun: ")
                length = input("Panjang Daun: ")
                try:
                    width = float(width)
                    length = float(length)
                    line =[]
                    line.append(width)
                    line.append(length)
                    if line[0] < barrier["width"][0]:
                        guess["width"]="Small Leaf"
                    else:
                        guess["width"]="Big Leaf"
                    if line[1] < barrier["length"][0]:
                        guess["length"]="Small Leaf"
                    else:
                        guess["length"]="Big Leaf"
                    lw = math.pi*line[0]*line[1]/4
                    line.insert(2,lw)
                    if line[2] < barrier["lw"][0]:
                        guess["lw"]="Small Leaf"
                    else:
                        guess["lw"]="Big Leaf"
                    prob_s = (guess["width"]=="Small Leaf")*bobot["width"] + (guess["length"]=="Small Leaf")*bobot["length"] + (guess["lw"]=="Small Leaf")*bobot["lw"]
                    prob_b = (guess["width"]=="Big Leaf")*bobot["width"] + (guess["length"]=="Big Leaf")*bobot["length"] + (guess["lw"]=="Big Leaf")*bobot["lw"]
                    if prob_s>prob_b:
                        print("Species Daun : Small Leaf")
                    else:
                        print("Species Daun : Big Leaf")
                    x = input("[Press Enter To Continue]")
                    break
                except:
                    print("Data Tidak Valid, Silahkan Masukkan Ulang Data")
                    x = input("[Press Enter To Continue]")
                    continue
            elif type == 2:
                while True:
                    os.system("clear")
                    print("Pilih Jenis Data Yang Ingin Dimasukkan:")
                    print("1. Panjang Daun")
                    print("2. Lebar Daun")
                    opsi = input("Option: ")
                    if opsi == "1":
                        length = input("Panjang Daun: ")
                        try:
                            length = int(length)
                            if length < barrier["length"][0]:
                                print("Species Daun : Small Leaf")
                            else:
                                print("Species Daun : Big Leaf")
                            x = input("[Press Enter To Continue]")
                            break
                        except:
                            print("Data Tidak Valid, Silahkan Masukkan Ulang Data")
                            x = input("[Press Enter To Continue]")
                    elif opsi == "2":
                        width = input("Panjang Daun: ")
                        try:
                            width = int(width)
                            if width < barrier["width"][0]:
                                print("Species Daun : Small Leaf")
                            else:
                                print("Species Daun : Big Leaf")
                            x = input("[Press Enter To Continue]")
                            break
                        except:
                            print("Data Tidak Valid, Silahkan Masukkan Ulang Data")
                            x = input("[Press Enter To Continue]")
                    else:
                        print("Data Tidak Valid, Silahkan Masukkan Ulang Data")
                        x = input("[Press Enter To Continue]")
            elif type == 3:
                width = input("Lebar Daun: ")
                length = input("Panjang Daun: ")
                height = input("Tinggi Daun: ")
                try:
                    width = float(width)
                    length = float(length)
                    height = float(height)
                    line = []
                    line.append(width)
                    line.append(length)
                    line.append(height)
                    if line[0] < barrier["width"][0]:
                        guess["width"]="Small Leaf"
                    else:
                        guess["width"]="Big Leaf"
                    if line[1] < barrier["length"][0]:
                        guess["length"]="Small Leaf"
                    else:
                        guess["length"]="Big Leaf"
                    if line[2] < barrier["height"][0]:
                        guess["height"]="Small Leaf"
                    else:
                        guess["height"]="Big Leaf"
                    lwh = math.pi*line[0]*line[1]/4*line[2]
                    line.insert(3,lwh)
                    if line[3] < barrier["lwh"][0]:
                        guess["lwh"]="Small Leaf"
                    else:
                        guess["lwh"]="Big Leaf"
                    prob_s = (guess["width"]=="Small Leaf")*bobot["width"] + (guess["length"]=="Small Leaf")*bobot["length"] + (guess["height"]=="Small Leaf")*bobot["height"] + (guess["lwh"]=="Small Leaf")*bobot["lwh"]
                    prob_b = (guess["width"]=="Big Leaf")*bobot["width"] + (guess["length"]=="Big Leaf")*bobot["length"] + (guess["height"]=="Big Leaf")*bobot["height"] + (guess["lwh"]=="Big Leaf")*bobot["lwh"]
                    if prob_s>prob_b:
                        print("Species Daun : Small Leaf")
                    else:
                        print("Species Daun : Big Leaf")
                    x = input("[Press Enter To Continue]")
                    break
                except:
                    print("Data Tidak Valid, Silahkan Masukkan Ulang Data")
                    x = input("[Press Enter To Continue]")
                    continue
            elif type == 4:
                width = input("Lebar Daun: ")
                length = input("Panjang Daun: ")
                height = input("Tinggi Daun: ")
                try:
                    width = float(width)
                    length = float(length)
                    height = float(height)
                    line = []
                    line.append(width)
                    line.append(length)
                    line.append(height)
                    if line[0] < barrier["width"][0]:
                        guess["width"]="Small Leaf"
                    elif line[0]<barrier["width"][1]:
                        guess["width"]="Big Leaf"
                    else:
                        guess["width"]="Very Big Leaf"
                    if line[1] < barrier["length"][0]:
                        guess["length"]="Small Leaf"
                    elif line[1]<barrier["length"][1]:
                        guess["length"]="Big Leaf"
                    else:
                        guess["length"]="Very Big Leaf"
                    if line[2] < barrier["height"][0]:
                        guess["height"]="Small Leaf"
                    elif line[2]<barrier["height"][1]:
                        guess["height"]="Big Leaf"
                    else:
                        guess["height"]="Very Big Leaf"
                    lwh = math.pi*line[0]*line[1]/4*line[2]
                    line.insert(3,lwh)
                    if line[3] < barrier["lwh"][0]:
                        guess["lwh"]="Small Leaf"
                    elif line[3]<barrier["lwh"][1]:
                        guess["lwh"]="Big Leaf"
                    else:
                        guess["lwh"]="Very Big Leaf"
                    prob_s = (guess["width"]=="Small Leaf")*bobot["width"] + (guess["length"]=="Small Leaf")*bobot["length"] + (guess["height"]=="Small Leaf")*bobot["height"] + (guess["lwh"]=="Small Leaf")*bobot["lwh"]
                    prob_b = (guess["width"]=="Big Leaf")*bobot["width"] + (guess["length"]=="Big Leaf")*bobot["length"] + (guess["height"]=="Big Leaf")*bobot["height"] + (guess["lwh"]=="Big Leaf")*bobot["lwh"]
                    prob_vb = (guess["width"]=="Very Big Leaf")*bobot["width"] + (guess["length"]=="Very Big Leaf")*bobot["length"] + (guess["height"]=="Very Big Leaf")*bobot["height"] + (guess["lwh"]=="Very Big Leaf")*bobot["lwh"]
                    if prob_s>prob_b and prob_s > prob_vb:
                        print("Species Daun : Small Leaf")
                    elif prob_b>prob_s and prob_b > prob_vb:
                        print("Species Daun : Big Leaf")
                    else:
                        print("Species Daun : Very Big Leaf")
                    x = input("[Press Enter To Continue]")
                    break
                except:
                    print("Data Tidak Valid, Silahkan Masukkan Ulang Data")
                    x = input("[Press Enter To Continue]")
                    continue
            break
    elif option =="3":
        print("Terima Kasih Telah Menggunakan Program Kami")
        print("Semoga Hari Anda Menyenangkan")
        break
    else:
        print("Input Tidak Valid")
        x = input("[Press Enter To Continue]")