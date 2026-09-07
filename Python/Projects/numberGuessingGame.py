import random
com = (random.randint(1,100))
tries=0

while True:
    tries+=1
    hum = int(input("GUESS YOUR NUMBER BETWEEN 1-100 :"))
    if hum == com:
        print(f"Congratulations you have won in {tries} tries !")
        break
    elif hum > com:
        print("sorry wrong guess go lower !")
    else:
        print("sorry wrong guess go higher !")






