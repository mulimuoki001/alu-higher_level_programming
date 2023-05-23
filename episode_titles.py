import re
episode_titles ='''The Originals S01E01:Always and Forever
The Originals S01E02:House of rising son
The Originals S01E03:Tangled up in blue
The Originals S01E04:Girl in new orleans
The Originals S01E05:Siiners and saints
The Originals S01E06:Fruit of the poisoned tree
The Originals S01E07:Bloodletting
The Originals S01E08:The river in reverse
The Originals S01E09:Reigning pain in new orleans
The Originals S01E10:The casket girls
The Originals S01E11:Apres moi, le deluge
The Originals S01E12:Dance back from the grave
The Originals S01E13:Cresent city
The Originals S01E14:Long way back from hell
The Originals S01E15:Le grand guignol
The Originals S01E16:farewell to storyville
The Originals S01E17:Moon over bourbon street 
The Originals S01E18:The big uneasy
The Originals S01E19:An unblinking death
The Originals S01E20:A closer walk with thee
The Originals S01E21:The battle of new orleans
The Originals S01E22:From  a cradle to a grave
The Originals S02E01:Rebirth
The Originals S02E02:Alive and kicking
The Originals S02E03:Every mother's son
The Originals S02E04:Live and let die
The Originals S02E05:Red door
The Originals S02E06:Wheel inside the wheel
The Originals S02E07:Chasing the devil's tail
The Originals S02E08:The brothers that care forgot
The Originals S02E09:The map of moments
The Originals S02E10:Gonna set your flag on fire
The Originals S02E11:Brotherhood of the damned
The Originals S02E12:Sanctuary
The Originals S02E13:The devil is damned
The Originals S02E14:I love you, goodbye
The Originals S02E15:They all asked for you
The Originals S02E16:Save my soul
The Originals S02E17:Exquisite corpse
The Originals S02E18:Night has a thousand eyes
The Originals S02E19:When the levee breaks
The Originals S02E20:City beneath the sea
The Originals S02E21:Fire with fire
The Originals S02E22:Ashes to ashes
'''
regular_expression = r'\w+\w+:\w+\s\w+\w+\w+'
regex = re.findall(regular_expression, episode_titles)
for x in regex:
    print(x)