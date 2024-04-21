#open the output file
#create a funtion to append a user input to the output file
#loop if there are more input
#break if there are no more input
#loop to input question when invalid answer

def input_line():
    resume = True
    while resume:
        line = input("Enter line: ")
        enter_line = line+("\n") #puts the new input on another line
        with open("mylife.txt", "a") as source_file:
            source_file.write(enter_line)
            while resume:
                again = input("Are there more lines y/n? ")
                if again.lower() == "y":
                    break
                elif again.lower() == "n":
                    print ("Sure!")
                    resume = False #breaks the two while loops
                else:
                    print("Invalid answer! Please type y/n only.")
                    continue

input_line()