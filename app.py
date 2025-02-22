try :
    file = open ('file.txt')

except FileNotFoundError :
    file = open ("file.txt", "w")
    file.write("after exception")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print ("File was closed.")
