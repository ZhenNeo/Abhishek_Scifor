import random

WHEN = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
WHO = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
NAME = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']

def line_story():
    when = random.choice(WHEN)
    who = random.choice(WHO)
    name = random.choice(NAME)

    story = f"{when}, {who} named {name}"
    return story

for i in range(15):
    story = line_story()
    print(f"{i+1} : {story}")