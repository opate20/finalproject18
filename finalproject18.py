import sys,time,random

typing_speed = 100 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

class Character(object):
    def __init__(self, name, surname, age, personality, looks):
        self.name = name
        self.surname = surname
        self.age = age
        self.personality = personality
        self.looks = looks

town = 'Riverdale'
name = 'Jughead'
surname = 'Jones'
age = 17
personality = 'determined, extroverted, sensing, feeling, judging, impulsive, trusting, heart over head, wants to be my best self, I play football'
looks = 'black hair, blue/green eyes, and I always wear my hat'

slow_type("""

MAKE SURE TO TYPE IN ALL LOWER CASE

""")

answer = slow_type(input("Hello. Would you like to play my game? "))

if answer == 'yes':
    slow_type("Great! Let's get started! ")

else:
    slow_type("Oh, okay )): Maybe next time :/ ")

slow_type(f"""
Hey, what's up, my name is {name} {surname}, and I'm {age} years old. I'm from Rockaway, New York.
Our story is about a town, a small town, and the people in the town.
From a distance, it presents itself like so many other small towns all over the world.
Safe
Decent
Innocent
Get closer, and you'll start to see the shadows that lie underneath. Our town is {town}, and our story starts, I guess, over the summer
"""
)

answer1 = input("Would you like to learn our story? ")

if answer1 == 'yes':
    slow_type("Alright, but just know, whatever you learn here, you MUST keep a secret. ")

else:
    slow_type("Okay, come back if you change your mind. ")

slow_type(f"""
On the Fourth of July, just after dawn, Jason and Cheryl Blossom drove out to Sweetwater River for an early morning boat ride
The next thing we know happened for sure is that Dilton Doiley, who was leading Riverdale's Boy Scout Troop on a bird watching expedition, came upon Cheryl by the river's edge
The Riverdale Police searched Sweetwater River for Jason's body, but never found it.
If he is dead, I hope in those last moments he suffered.
May Jason Blossom burn in hell.

So a week later, the Blossom family buried an empty casket and Jason's death was ruled an accident, as the story that Cheryl told made the rounds.
That she dropped her glove in the water, and Jason reached down to get it, and accidentally tipped the boat, and panicked, and drowned.

As for us, we were still talking about the "July Fourth Tragedy" on the last day of summer vacation, when a new mystery rolled into town.

NEW ITEM IN SECRETS INVENTORY!!!
"""
)

While True:
    answer2 = input('type secrets to look at the secrets you have learned or type continue to keep going ')
    secrets = []
    if answer2 == 'secrets':
        secrets.append('Death of Jason Blossom')
        print(secrets)
        continue
    elif answer2 == 'continue':
        slow_type(f"""
        Brace yourself, as this is story is about to take off...
        """)
        break