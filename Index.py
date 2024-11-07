file = open("my_txt", "w")
file.write("Hello World")
file.write("My name is lara")
file.write("I am 25 years old")
file.close()    

text = open("my_txt", "a")
text.write("I am a python programmer")
text.write("I am a 18 years old")
text.write("I love Coding")
text.close()

try:
    file = open("my_txt", "r")
    print(file.read())
except:
    print("File not found")
finally:
    file.close()