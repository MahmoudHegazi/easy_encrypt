import random
data = "task_id=1,guest_id=3,code=AH72B"

encryptList = []
salt = random.randint(10000000, 99999999)
lenstr = len(data)

def encrypt():
    random_range = data[1:len(data) - 3]
    the_real_random =  int(random.choice(range(len(random_range))))
    #the_real_random = 2
    #''.join(list1)
    string_list = list(data)
    dumy_value = random.randint(2, 1546458)
    fake_random = int(((lenstr * salt) / 2) + the_real_random)
    string_list.insert(the_real_random, str(dumy_value))    
    string1 = "".join(string_list)
    splited_random_list = string1.split(str(dumy_value))
    part1 = splited_random_list[0]
    part2 = splited_random_list[0]
    encrypted = splited_random_list[0][::-1] + splited_random_list[1][::-1] + "+" + str(fake_random)
    return encrypted
print(encrypt())


def decrypt(req_parameter, salt):
    if "+" not in req_parameter:
        return False
    full_data = req_parameter.split("+")
    fake_random = int(full_data[1])
    lenstr = len(str(full_data[0]))
    formala_num = int((lenstr * salt) / 2)
    the_real_random = int(fake_random - formala_num)
    string_list = list(req_parameter.split("+")[0])
    dumy_value = random.randint(2, 1546458)
    string_list.insert(the_real_random, str(dumy_value))
    string1 = "".join(string_list)
    splited_random_list = string1.split(str(dumy_value))
    return splited_random_list[0][::-1] + splited_random_list[1][::-1]

print(decrypt(encrypt(), salt))
