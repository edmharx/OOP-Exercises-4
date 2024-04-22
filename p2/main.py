#read datas from students.txt
#compare all the gwa(values)
#print the name(keys) and gwa(values) of the student with the highest gwa

directory = (r"students.txt")
def find_highest_gwa(directory):
    with open(directory, "r") as source_file:
        data = source_file.read()
        data_dict = eval(data)
        highest_gwa = None
        highest_gwa_student = None
        for key, value in data_dict.items():
            float_value = float(value)
            if highest_gwa is None or float_value > float(highest_gwa):
                highest_gwa_student = key
                highest_gwa = value
        return highest_gwa_student, highest_gwa


key, value = find_highest_gwa(directory)
print (f"{key} has the highest GWA with {value}")
