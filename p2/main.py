#read datas from students.txt
#compare all the gwa(values)
#print the name(keys) and gwa(values) of the student with the highest gwa

directory = (r"students.txt")
def highest_gwa(directory):
    with open(directory, "r") as source_file:
        data = source_file.read()
        data_dict = eval(data)


highest_gwa(directory)