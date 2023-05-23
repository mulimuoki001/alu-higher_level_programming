import re 

twitter_handles = input("Enter Twitter Handles: ") or '''
@WhimsicalWanderer
@ElectricDreamer
@MidnightWhisper
@SunnySideUp
@PixelEnthusiast
@ChaosMagnet
@T
brianmuli
_elvin
grace.com'''


regular_expression = r'@\w+'

regex = re.findall(regular_expression, twitter_handles)
for x in regex:
    print(x)