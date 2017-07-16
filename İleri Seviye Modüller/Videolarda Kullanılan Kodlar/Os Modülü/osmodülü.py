import os
from datetime import datetime


for klasör_yolu,klasör_isimleri,dosya_isimler  in os.walk("C:/Users/user/Desktop"):
    for i in klasör_isimleri:
        if (i.startswith("kr")):
            print(i)







#from datetime import datetime

# print(dir(os))

# print(os.getcwd())

# os.chdir("C:/Users/user/Desktop/")


# print(os.getcwd())


# print(os.listdir())

#os.mkdir("Deneme1")

#os.makedirs("Deneme2/Deneme3")

#os.rmdir("Deneme2/Deneme3")

# os.rename("Deneme1","Deneme2")
# os.removedirs("Deneme2/Deneme3")

# os.rename("test.txt","test2.txt")

# print(os.stat("test2.txt"))

# degistirilme = os.stat("test2.txt").st_mtime

# print(datetime.fromtimestamp(degistirilme))


"""for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("C:/Users/user/Desktop"):


    print("Current Path",klasör_yolu)
    print("Directories",klasör_isimleri)
    print("Dosyalar",dosya_isimleri)
    print("**********************************")"""





