fd =  "mytext1"
fd2 = "mytext2"
file = open(fd,'w')
name = input("enter your name/n")
file.write(name)
file.close()
file = open(fd,'r')
name2= file.read()
print(name2)
file2 = open(fd2,'w')
file2.write(name2)
file2.close()
file2.open(fd2,'r')
name3 = file2.read()
file2.close()
print(name3)


