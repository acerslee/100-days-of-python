# with open("my_file.txt") as file:
#     content = file.read()
#     print(contents)

# Different modes
# r - read only
# w - write (overwrite everything in file)
# a - append (add onto the file)

with open("my_file.txt", mode="w") as file:
    file.write("\nI also know Javascript")

# If you set mode to "w" and execute a non-existing file, this command will create that new file for you
with open("new_file.txt", mode="w") as writeFile:
    writeFile.write("New text.")
