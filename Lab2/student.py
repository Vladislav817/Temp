def solve(string):
    string = string.replace("vk. com","vk.ru")
    string = string.replace("http"," http")
    url_list = list()
    for line in string.split(" "):

        if line.startswith("t.me"):
            line = "https://" + line
        line = line.replace("vk.com","vk.ru")
        line = line.replace("vk/com","vk.ru")
        line = line.replace("m.vk.ru","vk.ru")
        line = line.replace("fast.vk.ru","vk.ru")
        line = line.replace("m.ok.ru","ok.ru")
        line = line.replace("https//","https://")
        line = line.replace("http://","https://")
        line = line.replace("https:vk","https://vk")
        line = line.replace("httpc","https")
        line = line.replace("Https://","https://")
        if "https://" not in line:
            continue
    
        string_lst = line.split("?")
        url_list.append(string_lst[0].strip(","))
    return url_list



# line = "https://vk.com/wall-207148281_1145 ;  https://vk.com/wall-207148281_1147 ;   https://vk.com/wall-207148281_1151 ; https://vk.com/wall-207148281_1168 ; https://vk.com/wall-207148281_1169"
# output = [
# "https://vk.ru/wall-207148281_1145",
# "https://vk.ru/wall-207148281_1147",
# "https://vk.ru/wall-207148281_1151",
# "https://vk.ru/wall-207148281_1168",
# "https://vk.ru/wall-207148281_1169"]
if __name__ == "__main__":
    line =  "https://vk.com/club145371898?w=wall-145371https://vk.com/club145371898?w=wall-145371898_4153 898_4154"
    output = [
        "https://vk.ru/club145371898",
        "https://vk.ru/club145371898"
        ]


    print(solve(line))
    print(output)



# print(line.split(" "))