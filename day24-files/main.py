# with open("my_file.txt") as file:
#     content = file.read()
#     print(contents)

# with open("my_file.txt", mode="a") as file:
#     file.write("\nThis is a new text")

# If you set mode to "w" and execute a non-existing file, this command will create that new file for you
with open("new_file.txt", mode="w") as writeFile:
    writeFile.write("New text.")
