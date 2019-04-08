fd = "hello.txt"
file = open(fd, 'a')
file.write("\nvenkat")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
