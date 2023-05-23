import re

data = input("Please enter the ISBN number: ")
regex = r'ISBN\s\d{3}[-.]?\d[-.]?\d{3}[-.]?\d{5}[-.]?\d'

with open("test.txt", "r") as x:
    ISBN_numbers = x.read()
    equivalent = re.findall(regex, ISBN_numbers)
    
    for match in equivalent:
        if data == match:
            print(match)
            
            
    
    