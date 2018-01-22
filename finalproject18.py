import os,sys,time,random

typing_speed = 200 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

class Character(object):
    def __init__(self, name, surname, age, personality, looks):
        self.town = 'Riverdale'
        self.name = name
        self.surname = surname
        self.age = age
        self.personality = personality
        self.looks = looks

jughead = Character('Jughead', 'Jones', '17', ('smart, determined, introverted, intuitive, thinking, judging, kind of impulsive, can be caring, lonely, knack for morality and lost causes, not very trusting at first, nostalgic, self-imposing'), ('black hair, blue/green eyes, and I always wear my hat'))

veronica = Character('Veronica', 'Lodge', '17', ('determined, extroverted, intuitive, thinking, perception, calm, sassy, maybe a little emotionally detached, likes aruging (especially winning the arguments)'), ('dark brown/black hair', 'brown eyes'))

betty = Character('Betty', 'Cooper', '17', ('extroverted, intuitive, feeling, judging, turbulent, led by feelings/judgement, girl-next-door type, nice, determined'), ('blonde hair, blue eyes'))

archie = Character('Archie', 'Andrews', '17', ('determined, extroverted, sensing, feeling, judging, impulsive, trusting, heart over head, wants to be my best self'), ('red head, brown/hazel eyes, fit/muscular, and I play football'))

slow_type("""

MAKE SURE TO TYPE IN ALL LOWER CASE

""")

slow_type("Hello. Would you like to play my game? ")
answer = input()
print('your answer was', answer)

if answer == 'yes':
    slow_type("Great! Let's get started! ")
# elif answer == 'no':
else:
    slow_type("Oh, okay )): Maybe next time :/ ")
    sys.exit()

slow_type(f"""
Hey, what's up, my name is {jughead.name} {jughead.surname}, and I'm {jughead.age} years old. I'm from Rockaway, New York.
Our story is about a town, a small town, and the people in the town.
From a distance, it presents itself like so many other small towns all over the world.
Safe
Decent
Innocent
Get closer, and you'll start to see the shadows that lie underneath. Our town is {jughead.town}, and our story starts, I guess, over the summer
"""
)

slow_type("Would you like to learn our story? ")
answer1 = input()

if answer1 == 'yes':
    slow_type("Alright, but just know, whatever you learn here, you MUST keep a secret. \n")
elif answer1 == 'no':
    slow_type("Okay, come back if you change your mind. ")
    sys.exit()
else:
    slow_type("Sorry, I don't recognize that")

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

while True:
    answer2 = input('type secrets to look at the secrets you have learned or type continue to keep going ')
    secrets = []
    if answer2 == 'secrets':
        secrets.append('Death of Jason Blossom')
        print(secrets)
        print('\n\n')
        continue
    elif answer2 == 'continue':
        break
    else:
        print("Sorry, I do not recognize that command\n")
        continue

slow_type(f"""
Here is where I introduce you to another few characters in my story, {veronica.name} {veronica.surname}, her mom, Hermione Lodge, and her dad, Hiram Lodge.
Some say that Veronica has a not-so-good reputation, but as we go through the story, I'll let you built your own opinion. For now, I'll give you some background to the family, and maybe even some of their secrets...

They lived in New York City, but they recently moved due to some... well... complications. Veronica wanted to start fresh and reinvent herself, as she used to be a 'mean girl' at her old school.
the girl in the popular clique that had {veronica.looks}, and she was pretty and rich, and everyone wanted to be her.

Her mother is quite interesting, being the love interest of both Mr. Lodge and Mr. Andrews while they were in high school. Now, she is helping him run his business and criminal empire while he is behind bars

Her father on the other hand, Hiram Lodge, is a complicated man. While being the richest man in Riverdale, he is a criminal. He's cheated people out of their money and even made some families go bankrupt.
Right now, he's in jail for fraud and embezzlement, but I heard he's coming back to Riverdale soon.

NEW SECRETS ADDED INTO INVENTORY

""")

while True:
    answer3 = input('type secrets to look at the secrets you have learned or type continue to keep going ')
    secrets = []
    if answer3 == 'secrets':
        secrets.append("Death of Jason Blossom")
        print(secrets[0])
        secrets.append("History to Veronica Lodge")
        print(secrets[1])
        secrets.append("Hiram Lodge and his activities")
        print(secrets[2])
        secrets.append("Hermione Lodge helping Hiram keep his criminal empire going")
        print(secrets[3])
        print('\n\n')
        continue
    elif answer3 == 'continue':
        break
    else:
        print('Sorry, I do not recognize that command\n')
        continue

