# try :
#     file = open ('file.txt')
#
# except FileNotFoundError :
#     file = open ("file.txt", "w")
#     file.write("after exception")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print ("File was closed.")

# Height = float (input ("What is your Height in meters : "))
# Weight = float (input ("What is your Weight in KG : "))
# if Height > 3 :
#     raise  ValueError ("Human Height can not exceed 3 meters")
# if Weight < 40 :
#     raise  ValueError ("Adult Weight  can not be less than 40")
# else :
#     BMI =  Weight / Height ** 2
#
#     print (BMI)

dic = {
    "wy": "88d0",
    "nedw": 8388
}
import json

with open ("file.json", "r") as file :
    data = json.load(file)
    data.update(dic)
with open ("file.json", "w") as file :
     json.dumps(data,file, indent=4)