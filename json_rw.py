
# Online Python - IDE, Editor, Compiler, Interpreter
import json


def gp_the_str(og_string):
    local_dict = {}
    digi_list = []
    non_digi_list = []
    temp_str = og_string[0]  # Initialise the temp str with 1st char
    n = 1  # n starts from 1 so that n can compare with n-1 (the previous char)

    while n < len(og_string):  # not n <= bcz out of range
        if og_string[n].isdigit() ^ og_string[n-1].isdigit():  # If new type coming
            if og_string[n-1].isdigit():
                digi_list.append(temp_str)
            else:
                non_digi_list.append(temp_str)
            temp_str = ''  # flush the temp str
        temp_str = temp_str + og_string[n]
        n = n+1

    # add the final temporary string to the according list
    if og_string[n-1].isdigit():
        digi_list.append(temp_str)
    else:
        non_digi_list.append(temp_str)

    # serve the lists
    local_dict["characters"] = non_digi_list
    local_dict["numbers"] = digi_list
    print(local_dict)
    return local_dict


# if __name__ == '__main2__':
# data.append(data)


filename = 'TheseVeggies.json'

with open(filename, encoding = 'utf-8') as TheseVeggies:  # File opened
    json_obj = json.load(TheseVeggies)  # File parsed ( json.loads(read(opened_file)) )

for i in range (len(json_obj['ocrResults'])):
    result = json_obj['ocrResults'][i]['text']
    json_obj['ocrResults'][i]['elements'] = gp_the_str(result)

with open(filename, 'w', encoding = 'utf-8') as TheseVeggies:
    json.dump(json_obj, TheseVeggies, sort_keys = True, indent = 3)  # parse the python as json object
