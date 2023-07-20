#TODO: create a letter using starting_letter.txt

#for each name in invited-names.txt
#Replace the [name] placeholder with the actual name
#Save the letter as in the folders: "Ready to Send"

with open("./inputs/letters/starting_letter.txt", mode="w") as file:
    file.write("Hello my name is Alex. \nIt's nice to meet you!")

with open("./inputs/names/invited_names.txt", mode="w") as file:
    file.write("Grape Watermelon Custard Strawberry Chocolate")

with open("./inputs/names/invited_names.txt", mode="r") as file:
    names = file.read()
    print(names)

arr = names.split(' ')

for name in arr:
    with open(f"./outputs/ReadyToSend/invited_{name}.txt", mode="w") as file:
        file.write(f"Hi I am {name}, nice to meet you too!")