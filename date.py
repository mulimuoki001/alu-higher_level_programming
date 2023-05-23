import re

date_regex = r'\d{2}[-]\w+[-]\d{4}'

with open("test.txt", "r") as date_data:
    date_info = date_data.read()
    date_match =re.findall(date_regex, date_info)
    for x in date_match:
        if x :
            print(x)
        else:
            print("Date not Found")