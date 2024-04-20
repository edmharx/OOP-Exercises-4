#opening of numbers.txt
#creation of the files
#read lines in number.txt
#per line write the number to designated text file

def read_write():
    with open("numbers.txt", "r") as source_file:
        for line in source_file: #loops reading of line
            if int(line) % 2 == 0: #check if integer per line is divisible by 2
                with open("even.txt", "a") as even_output_file:
                    even_output_file.write(line)
            else:
                with open("odd.txt", "a") as odd_output_file:
                    odd_output_file.write(line)

read_write()