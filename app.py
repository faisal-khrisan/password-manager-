try :
    file = open ('file.txt')
    content = file.read()
except FileNotFoundError :
    file = open ("fil.txt", "w")
    file.write("after exception")
else:
    content = file.read()
    print(content)
