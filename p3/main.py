#open the output file
#create a funtion to append a user input to the output file
#integrate the function

def input_line():
    while True:
        line = input("Enter line: ")
        with open("mylife.txt", "a") as source_file:
            source_file.write(line)
            again = input("Are there more lines y/n? ")
            if again.lower == "y":
                continue
            elif again.lower =="n":
                break
            else:
                print("Invalid answer!")
                break
                