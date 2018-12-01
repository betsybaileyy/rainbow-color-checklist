from os import system, name

red      = "\033[1;31m"
green    = "\033[0;32m"

checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[int(index)] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("   {}     {}".format(index, list_item)) #!!
        index += 1

def mark_completed(index):
    checklist[index] = '√' + checklist[index]
    print(checklist[index])
def unmark_completed(index):
    checklist[int(index)] = checklist[int(index)].replace('√', '')
    print(checklist[index])

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

def select(function_code):
    if function_code == "C":
        input_item = user_input( red + "Input item to add to the list: " + green)
        create(input_item)
        print("\n   " + red + "YOUR LIST" + green + "\n index#  item")
        list_all_items()

    elif function_code == "R":
        item_index = user_input("What is the index number of the item you would like to examine? ")
        print(read(int(item_index)))

    elif function_code == "U":
        item_index = user_input("What is the index number of the item you would like to update? ")
        input_item = input("What item would you like to replace it with? ")
        update(item_index, input_item)
        list_all_items()

    elif function_code == "M":
        item_index = user_input("What is the index number of the item you would like to check as complete? ")
        mark_completed(int(item_index))
        list_all_items()

    elif function_code == "UC":
        item_index = user_input("What is the index number of the item you would like to uncheck as complete? ")
        unmark_completed(int(item_index))
        list_all_items()

    elif function_code == "D":
        index = int(user_input("What is the index number of the item you would like to delete? "))
        destroy(index)
        list_all_items()

    elif function_code == "P":
        list_all_items()

    # else:
    #     print("Unknown Option")
    return True

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)
    mark_completed(0)
    list_all_items()

    select("C")

    list_all_items()

    select("R")

    list_all_items()

    user_value = user_input("Please Enter a value:")
    print(user_value)

# test()
# mark_completed(index)
print( red + "\nWelcome to your Christmas Wishlist! \nThis thing will come in handy before Santa and his reindeer come to see you. Let's get started." + green + "\nThis list has lots of ways to help you get your wishlist get orginized before it goes to the North Pole! \nLet's look at them: ")
selection = user_input
select(selection)

running = True
while running:
    selection = user_input("\nC = Create New Item \nR = Examine One Item \nP = Display List \nU = Update Spefic Item \nM = Check Item Off List \nUC = Uncheck Item on List \nD = Delete an Item from your List" + red + "\n\nHow would you like to proceed?" + green + " Input: ")
    clear()
    running = select(selection)
