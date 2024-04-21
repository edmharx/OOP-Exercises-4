#open the output file
#create a funtion to append a user input to the output file
#integrate the function

def input_line():
    while True:
        line = input("Enter line: ")
        enter_line = line+("\n") #puts the new input on another line
        with open("mylife.txt", "a") as source_file:
            source_file.write(enter_line)
            again = input("Are there more lines y/n? ")
            if again.lower() == "y":
                continue
            elif again.lower() == "n":
                break
            else:
                print("Invalid answer!")
                break

input_line()