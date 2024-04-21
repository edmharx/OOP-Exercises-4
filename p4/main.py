#create source txt file
#create two functions to apply for the integers
#input the results into their respective txt files


def square_cube():
    with open("integers.txt", "r") as source_file:
        for line in source_file:
            if int(line) % 2 == 0: #for even numbers
                square_root = line ** 2
                with open("double.txt", "a") as squared_output:
                    squared_output.write(square_root)
            else:
                cube_root = line ** 3 #for odd numbers
                with open("triple.txt", "a") as cube_output:
                    cube_output.write(cube_root)
            