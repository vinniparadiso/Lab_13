#Vinni, Sarah, Breanna
import dbm
db1=dbm.open("swift", "c")
db1["taylor.jpeg"]="Taylor Swift"
db1["guitar.jpeg"]="Taylor Swift playing guitar."
db1["mic.jpeg"]="Taylor Swift holding her mic."
db1["eras.jpeg"]="Taylor Swift on tour."
db1["dance.jpeg"]="Taylor Swift dancing."

for item in db1:
    print(item, db1[item])
