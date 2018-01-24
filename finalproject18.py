import sys,time,random
#this imports different modules to python so that i can use them later

typing_speed = 100 #wpm
#defines the speed in which the screen will type in words per minute
def slow_type(t): #t will be the word or string that you are trying to have python write
    for l in t: #l will be the letter(s) in the word or phrase that's being printed
        sys.stdout.write(l)
        #sys.stdout.write is a file-like object, and calling the 'write' function will let you print whatever string is provided
        sys.stdout.flush()
        #this flushes out the buffer and allows you to see the output of the function immediately
        time.sleep(random.random()*10.0/typing_speed)
    print('') #this prints whatever is inside the string
#this is a new function that i'm creating to make the story seem like the user is watching the narrator write it

class Character(object): #this is the beginning of a class that i named 'CHaracters' because it contains the main characters in my game (and the show)
    def __init__(self, name, surname, age, personality, looks):
        #whatever is in the parentheses is what i'm going to have to define in the class and assign a variable so that later i can actually use it
        #when creating different objects in the class, what you're assigning to each specific variable must go in the same order, or it won't turn out to be the way you want it to be
        self.town = 'Riverdale' #name of the town (universal)
        self.name = name #name of each character
        self.surname = surname #last name of each character
        self.age = age #age of each character
        self.personality = personality #their personality
        self.looks = looks #what they look like
#this is a human class that was created, including the name of the town, name and surname of the character, their age, what their personality is like, and what they look like

jughead = Character('Jughead', 'Jones', '16', ('smart, determined, introverted, intuitive, thinking, judging, kind of impulsive, can be caring, lonely, knack for morality and lost causes, not very trusting at first, nostalgic, self-imposing'), ('black hair, blue/green eyes, and I always wear my hat'))
#the first class is Jughead Jones
#all the information listed is in the same order that is in when the class is defined

veronica = Character('Veronica', 'Lodge', '16', ('determined, extroverted, intuitive, thinking, perception, calm, sassy, maybe a little emotionally detached, likes aruging (especially winning the arguments)'), ('dark brown/black hair', 'brown eyes'))
#second class is Veronica Lodge

betty = Character('Betty', 'Cooper', '16', ('extroverted, intuitive, feeling, judging, turbulent, led by feelings/judgement, girl-next-door type, nice, determined'), ('blonde hair, blue eyes'))
#third is Betty Cooper

archie = Character('Archie', 'Andrews', '16', ('determined, extroverted, sensing, feeling, judging, impulsive, trusting, heart over head, wants to be my best self'), ('red head, brown/hazel eyes, he is fit/muscular, and he play football'))
#last but not least is Archie Andrews

slow_type("""

MAKE SURE TO TYPE IN ALL LOWER CASE

""")


while True:
    slow_type("Hello. Would you like to play my game? ")
    answer = input() #allows the user to input a specific answer
    print('your answer was', answer)
    if answer == 'yes':
        slow_type("Great! Let's get started! ")
        break
        #not having anything after this option allows python to continue going through the code
    elif answer == 'no':
        slow_type("Oh, okay )): Maybe next time :/ ")
        sys.exit() #this will exit the game if they say that they don't want to play the game
    if answer != 'yes' or 'no':
        print("Sorry, I need a valid answer\n")
        continue


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
answer1 = input() #basically the same as the first one and every other one

if answer1 == 'yes':
    slow_type("Alright, but just know, whatever you learn here, you MUST keep a secret. \n")
elif answer1 == 'no':
    slow_type("Okay, come back if you change your mind. ")
    sys.exit()
else:
    print("Sorry, I don't recognize that command\n")
    #continue
    #***************************

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

slow_type(f"""
Now brace yourself, as the story is about to take off...

HERMIONE: While the apartment is small, it is the only piece of property in my name an not your father's.

SMITHERS: Ms. Hermione! Welcome home!

HERMIONE: Smithers! Oh, you are a sight for sore eyes.

SMITHERS: How was the ride?

HERMIONE: No traffic, thank God. Smithers, I'd like to introduce you to my daughter, Veronica.

SMITHERS: It's a pleasure, miss.

VERONICA: Hi.

SMITHERS: I'll get the bags.

HERMIONE: Would you?

SMITHERS: Oh, and would you like some menus, ma'am, so you can order in?

HERMIONE: Oh, no. I have been craving one of Pop Tate's cheeseburgers since noon. Is his Chock'lit Shoppe still open?

VERONICA: What is a Chock'lit Shoppe and why does it sell burgers?

... she was the new mystery, because with her will come trouble and even more secrets...

----------------------------------------------------------------------------------------------------------------------------------------------------

It's about time to introduce some more characters before we move on, and they are {betty.name} {betty.surname} and {archie.name} and {archie.surname}.

{betty.name} has {betty.looks} and has that girl-next-door type personality, but don't underestimate her... or it will come back to bite you...
Anyways, like everyone else here, she's {betty.age}, and she lives next to {archie.name} {archie.surname}.

{archie.name} {archie.surname} is {archie.age}. He has {archie.looks}, and is pretty much the guy everyone aims to be. Attractive, musculoar, football jock.

There's also Kevin Keller, the sheriff's son, who is also one of Betty's best friends.
Some secrets will be within the next part, so keep an eye out for them (or ***).

KEVIN: Are you excited? Nervous?

BETTY: Both. I haven't seen him all summer.

KEVIN: Which is why nerves are acceptable, but we agreed, Betty It's time. You like him, he likes you.

BETTY: Well, then why, Kevin, hasn't he ever said or done anything?  ***

KEVIN: Because Archie's swell, but like most millennial straight guys, he needs to be told what he wants. So tell him, finally.

BETTY: Well, we'll see. I mean, it depends.

KEVIN: Oh, my God!

BETTY: What?

KEVIN: Game-changer. Archie got hot! He's got abs now. Six more reasons for you to take that ginger bull by the horns tonight.

----------------------------------------------------------------------------------------------------------------------------------------------------

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
        secrets.append("Archie is unsure how he feels about Betty")
        print(secrets[4])
        print('\n\n')
        continue
    elif answer3 == 'continue':
        break
    else:
        print('Sorry, I do not recognize that command\n')
        continue


slow_type(f"""
You always hear people say
'Time goes by so fast at your age.'
'One summer can change everything.'

But, wow. You never realise how true it is until everything in your life turns upside down.

BETTY: How was working for your dad?

ARCHIE: It was pouring concrete, every day, all day long. To pass time, I would start composing these poems, in my head. And at night, I'd go home, I'd write them down,

BETTY: You don't even like reading poetry.

ARCHIE: They weren't poems, they were song lyrics. *** And working on them made me feel like...

BETTY: What, Archie?

ARCHIE: It made me feel like I'd finally broken through to something real. About my life and what I should be trying to do with it. Music. Starting this year, tomorrow.

BETTY: Amazing. Will you ask Ms. Grundy to tutor you?

ARCHIE: I'm not sure, maybe.

BETTY: What about football? Can you do both?

ARCHIE: I'll try out, at least. I haven't even told my dad yet, but I'm waiting until I have things more figured out. For now, you're the only person I'm telling.

BETTY: Okay. Um...also I've been thinking about us, Archie, and our friendship, and how it's time we...

VERONICA: I called in an order, for Lodge?

POP: Two burgers, yeah, almost ready, but you gotta wait.

VERONICA (to ARCHIE and BETTY): Hi

ARCHIE: Hey.

----------------------------------------------------------------------------------------------------------------------------------------------------

""")

slow_type("Would you like to continue to learn our story? ")
answer4 = input()

if answer4 == 'yes':
    slow_type("Great! On with the story! \n")
elif answer4 == 'no':
    slow_type("Okay, come back if you change your mind. ")
    sys.exit()
else:
    slow_type("Sorry, I don't recognize that")

slow_type(f"""
Now, this is where things pick up. Essentially, from here, Veronica, Betty, and Archie exchange a few words about the food and they introduce themselves to each other.
It turns out that Betty is Veronica's peer mentor for the first day of school, and that is where the drama starts.

{betty.name} gets home from Pop's and her mother is 'explaining' (more like lecturing) how important school is, and how she needs to keep up her grades and her character, participate in
extracurriculars and athletics... the normal spiel that parents go on about school.

ALICE: Betty. You've accomplished so much so far, I don't want anything jeopardizing that. I mean, just think of your poor sister. She was such a shining star before she let that Blossom boy ruin her.***

BETTY: Mom, I'm not Polly.

ALICE: You missed curfew last night.

BETTY: By seven minutes. I was with Archie, who has red hair, yes, but is nothing like Jason Blossom.

ALICE: Oh, but sweetie, all boys are like Jason Blossom.***

----------------------------------------------------------------------------------------------------------------------------------------------------

(at school)


BETTY(to VERONICA): So, I usually start off my tours with a little history and context. Riverdale High first opened its doors in 1941 and-

VERONICA: And hasn't been redecorated since, apparently. Honestly, I feel like I'm wandering through the lost epilogue of Our Town. So what's the social scene like here? Any night clubs?

KEVIN: A strip club called the Ho Zone and a tragic gay bar called Innuendo. Friday nights, football games and then tailgate parties at the Mallmart parking lot.
Saturday night is movie night, regardless of what's playing at the Bijou, and you better get there early, because we don't have reserved seating in Riverdale.
And Sunday nights Thank God for HBO.

Here, at Riverdale, we have many people of many talents, and Josie and the Pussycats just so happen to be the most up-and-coming acts in the town.
Josie, the lead singer, is the mayor's daughter. Currently, they're building their own image and reputation. After winning Rockland County's Battle of the Bands last year,
they've been a force to be reckoned with. Building on that success, they continue to tell stories with the songs that they write for the people of the town.

Oh, and of course there's the Back-to-School - semiformal dance this weekend. Veronica is new, so of course she doesn't know about {betty.name} and {archie.name}. While they aren't dating, they are endgame.
BUT! I think I heard that the dance might be cancelled because of what happened to Jason. But they're going to tell us at thr assembly.

VERONICA: Who's Jason and what happened to him?

(at the assembly)

CHERYL: Thank you for that moment of silence. Many of you were lucky enough to have known my brother personally. Each and every one of you meant the world to Jason.
I loved my brother. He was and always will be my soulmate. So I speak with the confidence only a twin could have Jason wouldn't want us to spend the year mourning. Jason would want us to move on with our lives.
Which is why I've asked the School Board not to cancel the Back-to-School semiformal. But rather, to let us use it as a way to heal, collectively, and celebrate my brother's too, too short life on this mortal coil.
Thank you all.


After the assembly, Archie caught up with Ms. Grundy to talk about the music he'd been writing, and possibly a few other things.

MS. GRUNDY: They're Very real, very personal.

ARCHIE: I took your advice and wrote them down. Polished them. But I was wondering maybe if you could help me

MS. GRUNDY: With what, Archie?

ARCHIE: You went to Juilliard, Ms. Grundy. There is no one else in Riverdale I can take lessons from. Believe me, I've looked.

MS. GRUNDY: Well, I don't think that's a good idea. I don't think we should be alone together. If this is you trying to restart something that never should've started in the first

ARCHIE: No, it's not. It is about the music. But it's also... Come on, I need to be able to talk about what happened with someone. We heard what we heard and afterwards, we didn't do anything. We didn't say anything.

MS. GRUNDY: We heard fireworks.

ARCHIE: Who's lighting fireworks at 6:00 in the morning?

MS. GRUNDY: How would we explain why we were together at Sweetwater River at 6:00 a.m. on the Fourth of July? ... And you're right. We didn't say anything. We're both going to have to live with that choice.
Do you understand? I think you should pursue your music, but not with me. ***

----------------------------------------------------------------------------------------------------------------------------------------------------

At about lunch-time, everyone is sitting outside and enjoying themselves back on the first day of school.

VERONICA: What are we doing?

BETTY: Listening to one of Archie's songs.

KEVIN: I thought we were going to have to pretend to like it, but it's actually really good.

VERONICA: Wait, that was you singing? Something you wrote?

ARCHIE: It's rough.

BETTY: No, it's great.

VERONICA: It's incredible, actually, the little snippet I heard. Is that your thing? Music? Are you doing something with that?

ARCHIE: Yeah, that's the plan. So how's your first day going? Good? Not to be a complete narcissist, but I thought people would be more-

KEVIN: Obsessed with you? Any other year, you'd be trending number one, for sure. This year, though, it's all about Cheryl trying to win the Best Supporting Psycho Oscar for her role as
Riverdale High's bereaved Red Widow.

ARCHIE: Hey, I should go. I got that meeting with Grundy and then football tryouts, so.

VERONICA: You play football, too? What don't you do?

KEVIN: Before you ask, Blue Jasmine, no, she has not invited him to the dance yet

BETTY: Not yet, and don't talk about Archie.

CHERYL: Veronica Lodge, I'd heard whisperings. I'm Cheryl Blossom, may I sit? Betty, would you mind? So, what are you three hens gossiping about?
Archie's Efron-esque emergence from the chrysalis of puberty?

VERONICA: Extracurriculars. Weatherbee wants me to sign up for a few.

CHERYL: Cheerleading. You must. I'm senior captain of the River Vixens.

KEVIN: Is cheerleading still a thing?

CHERYL: Is being the Gay Best Friend still a thing? Some people say it's retro, I say it's eternal and iconic.

VERONICA: At Spence, I sat at the top of the Elites' pyramid. I'm in. Betty, you're trying out, too.

CHERYL: Of course, anyone's welcome to try out, but Betty's already got so much on her plate right now and being a Vixen is kind of a full-time thing.
But open to all!

VERONICA: Go ahead and hate on cheerleading, but if Hipster Prince Harry-

BETTY: I'd love to be a cheerleader. It would look great on my college applications. But last year, when I tried out, Cheryl said I was too fat.

VERONICA: Well, you're a total smoke show now. I mean it. As hot and as smart as you are, you should be the Queen Bey of this drab hive.
Look, if you want to be a River Vixen, I'll help you prep. I have moves.

BETTY: Okay. You know what? Show me your moves.

----------------------------------------------------------------------------------------------------------------------------------------------------

""")

while True:
    answer5 = input('type secrets to look at the secrets you have learned or type continue to keep going ')
    secrets = []
    if answer5 == 'secrets':
        secrets.append("Death of Jason Blossom")
        print(secrets[0])
        secrets.append("History to Veronica Lodge")
        print(secrets[1])
        secrets.append("Hiram Lodge and his activities")
        print(secrets[2])
        secrets.append("Hermione Lodge helping Hiram keep his criminal empire going")
        print(secrets[3])
        secrets.append("Archie is unsure how he feels about Betty")
        print(secrets[4])
        secrets.append("Archie has an aspiring music career and writes his own songs")
        print(secrets[5])
        secrets.append("Polly (Betty's older sister) dated Jason he went missing")
        print(secrets[6])
        secrets.append("Alice had this bad view of the Blossom family because of Jason and Polly together")
        print(secrets[7])
        secrets.append("During the summer, on the night of Jason Blossom's murder, Archie and Ms. Grundy were together")
        print(secrets[8])
        secrets.append("Hermione and Fred dated in high school before she left Fred for Hiram and eventually married him")
        print(secrets[9])
        secrets.append("After Hiram was incarcerated, Hermoine and Veronica lost a lot of money because the main income source was from Hiram")
        print(secrets[10])
        secrets.append("Hiram Lodge ran his empire based on illegal activities concering money (fraud, exploiting people, etc)")
        print(secrets[11])
        print('\n\n')
        continue
    elif answer5 == 'continue':
        break
    else:
        print('Sorry, I do not recognize that command\n')
        continue

slow_type(f"""

Meanwhile, Fred Andrews and Hermione Lodge engaged in an interaction.


FRED: Hermione Lodge. Well, my day just got a lot more interesting.

HERMIONE: Hello, Fred. How are you?

FRED: Surprised. Can I get you anything? Would you like a water?

HERMIONE: A job. I saw on your website that you are looking for a seasonal hire, someone to help with the books?

FRED: Yeah, my guy's on paternity leave.

HERMIONE: You know, I think my daughter's going to school with your son, isn't that funny? We'll have to tell them that we knew each other, that we even dated, for a little while. Well, at least until I-

FRED: Chose the rich kid.***

HERMIONE: ... How's Mary doing?

FRED: She's in Chicago. We split up. We're civil. How about you? How are you holding up? Really?

HERMIONE: I have a little money saved. *** I was praying that someone in Riverdale, maybe an old friend, would be willing to give me the benefit of the doubt.

FRED: If it were up to me.

HERMIONE: Isn't it up to you? It's your company.

FRED: Well, I have clients. I can't very well have Hermione Lodge, the wife of Hiram Lodge, on trial for fraud and embezzlement***, balancing my books. Can I?

HERMIONE: I suppose you can't.

----------------------------------------------------------------------------------------------------------------------------------------------------

While not as interesting as two high school sweethearts reuniting, Veronica and Betty were trying out for the cheerleading. But, Cheryl is the senior captain of the team and her brother
dated Betty's sister before he went missing, so things were bound to get messy.

Unimpressed, Cheryl dismissed their audition and questioned {betty.name} about her sister and how she was treated by Jason. After a minute of firing insults to each other's siblings, Cheryl
accepts {veronica.name} to the RIver Vixens, but {veronica.name} wasn't going to have it.

CHERYL: Better luck next time Betty.

VERONICA: Wait, what? Why? Because you couldn't bully Betty into being like you?

CHERYL: I need girls with fire on my squad.

VERONICA: I know what you need, Cheryl, because I know who you are. You would rather people fear than like you, so you traffic in terror and intimidation.
You're rich, so you've never been held accountable, but I'm living proof. That certainty, that entitlement you wear on your head like a crown? It won't last.
Eventually, there will be a reckoning. Or... maybe that reckoning is now. And maybe, that reckoning is me. Betty and I come as a matching set. You want one, you take us both.
You wanted fire? Sorry, Cherrybombshell, my specialty's ice.

(walking outside during the football tryouts)

BETTY: Hey, {veronica.name}, why did why did you defend me? I know the crowd you ran with in New York. Why are you being so nice?

VERONICA: When my father got arrested, it was the worst thing ever. All these trolls started writing horrible things about us.
We'd get letters and e-mails saying that my dad was a thief, my mom was a clueless socialite, and that I was the spoiled rich-bitch ice princess.
And what hurt the most about it was the things the trolls were writing were true... I was like Cheryl. I was worse than Cheryl.
So, when my mom said we were moving to Riverdale, I made a pact with myself to use this as an opportunity to become maybe, hopefully, a better version of myself. ***

BETTY: That's a lot of pressure. When Polly and Jason got together It meant everything to her and nothing to him, and things got super intense and weird and toxic and my mom turned on Polly.
Said Polly wasn't her daughter anymore, said all these awful things to her. Jason hurt Polly, but it's my mom who broke her.

VERONICA: Archie! (to BETTY) You're so doing this.

BETTY: What?

VERONICA: Slaying your dragons, Betty Cooper, one by one. (to ARCHIE, who is approaching them) Hi, Teen Outlander.

ARCHIE: Hey. Nice outfits.

VERONICA: Betty here has something she wants to ask you about the Back-to-School dance.
Go on, Betty, ask.

BETTY: I was wondering if you wanted to come with both of us.

ARCHIE: Huh?

VERONICA: What?

BETTY: It's your first dance at Riverdale. You should have someone to go with, even if it's just a friend.

VERONICA: I mean, I'd love to.

ARCHIE: I'm not really in the headspace for a dance.

BETTY: Oh. That's okay.

VERONICA: Totally unacceptable, Archie. We need an escort. Take a break from being a tortured musical genius and come spend a blissful evening with not one, but two newly-minted River Vixens.
We'll text you time and place.

ARCHIE: Okay. Yeah, okay. Bye.

BETTY and VERONICA: Bye.

----------------------------------------------------------------------------------------------------------------------------------------------------

(at Betty's house after tryouts)

BETTY: Hey Mom, guess what.

ALICE: What is that?

BETTY: I made the cheerleading squad.

ALICE: Cheryl Blossom's cheerleading squad? After what Jason did to Polly? No, I'm sorry. I won't allow it. Take that off right now.

BETTY: No.

ALICE: What did you say to me?

BETTY: I do everything for everyone. Everything to be perfect. The perfect daughter, the perfect sister, the perfect student. Can't I do this one thing just for me?

ALICE(as BETTY is trying to leave the room): Wait.

BETTY: Get out of my way.

ALICE: Where are you going?

BETTY: To buy a dress. Because guess what? I'm also gong to the dance with Archie. And Veronica.

ALICE: Wait, Hermione Lodge's daughter?

BETTY: She's actually really nice. And trying to be a good person.

ALICE: You think so? You think she's going to be your friend? Let me tell you something. Girls like Cheryl and Veronica Lodge, they don't like girls like us.

BETTY: I don't want to hear it, Mom. It's happening. I'm going.***

----------------------------------------------------------------------------------------------------------------------------------------------------

""")

slow_type("Are you enjoying this so far? ")
answer6 = input()

if answer6 == 'yes':
    slow_type("Great! I'm glad. Now, onto the rest of the story. \n")
elif answer6 == 'no':
    slow_type("Oh, okay. I'm sorry. But just wait! It gets better! ")
else:
    slow_type("Sorry, I don't recognize that")

while True:
    answer7 = input('type secrets to look at the secrets you have learned or type continue to keep going ')
    secrets = []
    if answer7 == 'secrets':
        secrets.append("Death of Jason Blossom")
        print(secrets[0])
        secrets.append("History to Veronica Lodge")
        print(secrets[1])
        secrets.append("Hiram Lodge and his activities")
        print(secrets[2])
        secrets.append("Hermione Lodge helping Hiram keep his criminal empire going")
        print(secrets[3])
        secrets.append("Archie is unsure how he feels about Betty")
        print(secrets[4])
        secrets.append("Archie has an aspiring music career and writes his own songs")
        print(secrets[5])
        secrets.append("Polly (Betty's older sister) dated Jason he went missing")
        print(secrets[6])
        secrets.append("Alice had this bad view of the Blossom family because of Jason and Polly together")
        print(secrets[7])
        secrets.append("During the summer, on the night of Jason Blossom's murder, Archie and Ms. Grundy were together")
        print(secrets[8])
        secrets.append("Hermione and Fred dated in high school before she left Fred for Hiram and eventually married him")
        print(secrets[9])
        secrets.append("After Hiram was incarcerated, Hermoine and Veronica lost a lot of money because the main income source was from Hiram")
        print(secrets[10])
        secrets.append("Hiram Lodge ran his empire based on illegal activities concering money (fraud, exploiting people, etc)")
        print(secrets[11])
        secrets.append("Veronica reveals how she was in New York and why she's in Riverdale")
        print(secrets[12])
        secrets.append("Betty's inner rebel shows in the defiance against her mother")
        print(secrets[13])
        print('\n\n')
        continue
    elif answer7 == 'continue':
        break
    else:
        print('Sorry, I do not recognize that command\n')
        continue


slow_type(f"""
FRED: I, um I got a call from your coach today. He's under the impression that you can't play varsity football because I'm making you work for me. Which is odd,
because you made it seem like you couldn't work for me because you were playing football. So my first question is Who are you lying to? Me or your coach?

ARCHIE: Neither. Both. Dad. I want to study music, I want to write music.***

FRED: Football takes you to college. College takes you to business school.

ARCHIE: Business school, and that takes me right back here. To work for you in Riverdale.

FRED: Not for me, with me. And eventually for yourself, son. The company would be yours.

ARCHIE: No disrespect, Dad, but I don't want it.

FRED: Three months ago, you did. What happened?

ARCHIE: I've changed. Everything's changed. This summer-

FRED: This summer what? That's it? We don't talk anymore?

ARCHIE: Dad.

FRED: I would never force you to play football. I don't care if you play football. And you don't have to work with me or for me, ever again.
But some advice, man-to-man? These decisions that you're making now, son, they have consequences. They go on to form who you are and who you'll become.
Whatever you decide, be confident enough in it that you don't have to lie.

----------------------------------------------------------------------------------------------------------------------------------------------------

As the night went on and more secrets were spilt, there was something more interesting brewing.

(at the dance)

VERONICA: Well, it's not the Met Ball.

BETTY: Hey (to ARCHIE).When do you have to let Coach Clayton know about football?

ARCHIE: This weekend.

VERONICA: Guys, can't we just liberate ourselves from the tired dichotomy of jock/artist? Can't we, in this post James Franco world, be all things at once?

ARCHIE: I've been working on it, Veronica.

VERONICA: Work faster. I'm getting punch. (whispering to BETTY) You got this.

BETTY: It's about following your heart, right? What does your heart say? Music or football?

ARCHIE: Betty, will you give me one minute? And I promise, when I get back, I'll be a much better date, okay? I have a plan.

KEVIN(out of nowhere): Betty, you will not believe who just propositioned me in the bathroom.
Give you a hint his name may be Moose, but I'd describe a certain appendage of his as horse-like.

ARCHIE(after he got back, to BETTY): Wanna dance?

BETTY: Yeah. Did that go okay?

ARCHIE: Yeah, yes. I'll study with Ms. Grundy before school, football practice after school, and work with my dad on the weekends. It's going to be nuts.

BETTY: So long as you don't give up your passion... um Now that I'm a River Vixen and you're gonna be on varsity football, I have this fantasy of us as a power couple,
or maybe even just a couple.

ARCHIE: Betty

BETTY: Is that so impossible to imagine?

CHERYL(at a distance away from BETTY and ARCHIE) Make sure those two turtledoves come to my after-party. Veronica too. I'm in the mood for chaos.

----------------------------------------------------------------------------------------------------------------------------------------------------

Hey, just so you know, there are quite some secrets in your inventory so far!!!
""")

while True:
    answer8 = input('type secrets to look at the secrets you have learned or type continue to keep going ')
    secrets = []
    if answer8 == 'secrets':
        secrets.append("Death of Jason Blossom")
        print(secrets[0])
        secrets.append("History to Veronica Lodge")
        print(secrets[1])
        secrets.append("Hiram Lodge and his activities")
        print(secrets[2])
        secrets.append("Hermione Lodge helping Hiram keep his criminal empire going")
        print(secrets[3])
        secrets.append("Archie is unsure how he feels about Betty")
        print(secrets[4])
        secrets.append("Archie has an aspiring music career and writes his own songs")
        print(secrets[5])
        secrets.append("Polly (Betty's older sister) dated Jason he went missing")
        print(secrets[6])
        secrets.append("Alice had this bad view of the Blossom family because of Jason and Polly together")
        print(secrets[7])
        secrets.append("During the summer, on the night of Jason Blossom's murder, Archie and Ms. Grundy were together")
        print(secrets[8])
        secrets.append("Hermione and Fred dated in high school before she left Fred for Hiram and eventually married him")
        print(secrets[9])
        secrets.append("After Hiram was incarcerated, Hermoine and Veronica lost a lot of money because the main income source was from Hiram")
        print(secrets[10])
        secrets.append("Hiram Lodge ran his empire based on illegal activities concering money (fraud, exploiting people, etc)")
        print(secrets[11])
        secrets.append("Veronica reveals how she was in New York and why she's in Riverdale")
        print(secrets[12])
        secrets.append("Betty's inner rebel shows in the defiance against her mother")
        print(secrets[13])
        secrets.append("Archie tells his dad about him wanting to pursue a music carrer")
        print(secrets[14])
        print('\n\n')
        continue
    elif answer8 == 'continue':
        break
    else:
        print('Sorry, I do not recognize that command\n')
        continue

slow_type(f"""

After the dance, Cheryl and her following MADE SURE that EVERYONE from the school was at this afterparty-type thing.

CHERYL: It's game time at Chez Blossom, kiddies. We're going old-school tonight. Seven Minutes in Heaven. Who wants to tryst in the Closet of Love first? My vote is "A" for Archie.
Anyone care to second it?

ARCHIE: Wait, actually-

REGGIE: Yes, Andrews! Yes.

CHERYL: All right.cGather round, kids. Let's see who's riding the ginger stallion tonight.

REGGIE: Oh, no way!

CHERYL: It's clearly pointing to- the new girl. This should be fun.

VERONICA: Um I'm not doing this.

CHERYL: That's up to you. But, if you don't, house rules decree the hostess gets to take your turn.

VERONICA(in a closet with Archie): I know her brother died and everything, but Cheryl Blossom truly is the antichrist.

ARCHIE: So, uh, do you miss New York?

VERONICA: It's been less than a week. But yes.

ARCHIE: Six minutes, twenty seconds.

VERONICA: Okay.

ARCHIE: Your turn. Ask me a deep, probing question - to kill time.

VERONICA: It looked like you and Betty were having fun at the dance.

ARCHIE: Definitely. We've been friends forever. My turn.

VERONICA: I didn't ask my question yet. Is that all it is? Just friends?

ARCHIE:We're not just friends, we're best friends. My turn. Did you have a boyfriend in New York?

VERONICA: No. My turn. Could it ever possibly become something more?

ARCHIE: Are you asking for Betty or for yourself?

VERONICA: For Betty, and you didn't answer my question.

BETTY: I have never felt Whatever it is I'm supposed to feel with Betty.

VERONICA: Have you felt it, though? With anyone?

ARCHIE: Yeah. This summer. Have you?

VERONICA: Maybe once. You're a little more dangerous than you look, aren't you? All boy-next-door-ish?

ARCHIE: You have no idea.

VERONICA: Your turn. Ask me a question, Archie. Ask me anything you want. (getting closer and closer to ARCHIE) We shouldn't do this.

ARCHIE: We definitely shouldn't do this. ***

REGGIE: Nailed it. Yes.

VERONICA: Where's Betty?

CHERYL: She spiraled and fled. Between us, she's a lot more high-strung than she looks.

ARCHIE: Crap. Betty's cell is off.

VERONICA: I'm getting an Uber.

ARCHIE: Can I come with you? We should probably try to find her.

VERONICA: Believe me! The last thing Betty wants is us tracking her down together. We messed up.

----------------------------------------------------------------------------------------------------------------------------------------------------

HERMIONE: Hey, you're home early. How was the dance?

VERONICA: It was fine. I mean, it's not the Met Ball or anything

HERMIONE: Tell me about it. You can cheer me up.

VERONICA: I'm super tired, Mom.

HERMIONE: Is everything okay? Ronnie, what is it?


It was midnight, and my old friend Archie Andrews arrived at the one place in town that was still open. He was looking for the girl next door. Instead, he found me.


ARCHIE: Hey, Pop. Betty hasn't come in tonight, has she?

POP: Nope. Just the night hawks in tonight.

ARCHIE: Thanks. Uh, can I sit, Jughead?

ME: If you want.

ARCHIE: What are you working on?

ME: My novel. It's about this summer, and Jason Blossom.

ARCHIE: Seventeen years old and how will he be remembered? As captain of the water polo team?

ME: The Aquaholics? Considering how he died, probably not.

ARCHIE: No, what I mean is...was he doing everything he was supposed to do, everything he wanted. I mean, did he even know what that was?

ME: Coach Clayton was in here talking to Pop Tate. Varsity, huh? That make you, what, Mr. Popular Football God now?

ARCHIE: No. In fact, I'm kind of terrified I lost my best friend tonight.

ME: If you mean Betty, whatever happened, just talk to her. You know, it'd go a long way. Would've gone a long way with me.


So, after that was said, Arche was on his way to go find his girl, and I was left on ly own once again. I don't mind though...
it can be quite fun listening to people when they don't think anyone is listening.

Anyways, back to {archie.name} and {betty.name} in front of her house.

BETTY: I'm not going to ask what you did with Veronica at Cheryl's. But I'm asking you now, right now, if you love me, Archie.
Or even like me?

ARCHIE: Of course I love you, Betty. But I can't give you the answer you want.

BETTY: Why?

ARCHIE: You are so perfect. I've never been good enough for you. I'll never be good enough for you.***


And so, it wasn't one heart that broke that night. It was two. And the night was far from over.
""")

slow_type("Are you enjoying the story? We're almost at the end! ")

answer9 = input()

if answer9 == 'yes':
    slow_type("Great! The ending is definitely the best part!  \n")
elif answer9 == 'no':
    slow_type("Awww )): Just hang on a little bit longer! The ending is probably the best  ")
else:
    slow_type("Sorry, I don't recognize that")

while True:
    answer10 = input('type secrets to look at the secrets you have learned or type continue to keep going ')
    secrets = []
    if answer10 == 'secrets':
        secrets.append("Death of Jason Blossom")
        print(secrets[0])
        secrets.append("History to Veronica Lodge")
        print(secrets[1])
        secrets.append("Hiram Lodge and his activities")
        print(secrets[2])
        secrets.append("Hermione Lodge helping Hiram keep his criminal empire going")
        print(secrets[3])
        secrets.append("Archie is unsure how he feels about Betty")
        print(secrets[4])
        secrets.append("Archie has an aspiring music career and writes his own songs")
        print(secrets[5])
        secrets.append("Polly (Betty's older sister) dated Jason he went missing")
        print(secrets[6])
        secrets.append("Alice had this bad view of the Blossom family because of Jason and Polly together")
        print(secrets[7])
        secrets.append("During the summer, on the night of Jason Blossom's murder, Archie and Ms. Grundy were together")
        print(secrets[8])
        secrets.append("Hermione and Fred dated in high school before she left Fred for Hiram and eventually married him")
        print(secrets[9])
        secrets.append("After Hiram was incarcerated, Hermoine and Veronica lost a lot of money because the main income source was from Hiram")
        print(secrets[10])
        secrets.append("Hiram Lodge ran his empire based on illegal activities concering money (fraud, exploiting people, etc)")
        print(secrets[11])
        secrets.append("Veronica reveals how she was in New York and why she's in Riverdale")
        print(secrets[12])
        secrets.append("Betty's inner rebel shows in the defiance against her mother")
        print(secrets[13])
        secrets.append("Archie tells his dad about him wanting to pursue a music carrer")
        print(secrets[14])
        secrets.append("Veronica and Archie kiss")
        print(secrets[15])
        secrets.append("Archie shows some vulnerability and insecurity")
        print(secrets[16])
        print('\n\n')
        continue
    elif answer10 == 'continue':
        break
    else:
        print('Sorry, I do not recognize that command\n')
        continue


slow_type(f"""

(in the forest)

MOOSE: For the record, I'm not gay.

KEVIN: Obviously not, Moose. You're on the football team. But if you were gay, what would you like to do?

MOOSE: Everything but kiss.

KEVIN: I love a good closet case. So, let's start with skinny-dipping and then see what happens?  And I... uh...

MOOSE: Dude, are you okay?

KEVIN: ...Oh, my God...it's Jason. He was shot.***



By morning, everyone would be talking, texting, and posting about it. We'd all be feeling it. That the world around us had changed, maybe forever.
That Riverdale wasn't the same town as before. That it was a town of shadows and secrets now.

On Monday, the autopsy on Jason's body would take place.

And on Tuesday, halfway through fifth period, the first arrest would be made.
""")


slow_type("This is the end of the story! Did you enjoy it?")
answer11 = input()

if answer11 == 'yes':
    slow_type("Great!I'm glad!  \n")
elif answer11 == 'no':
    slow_type("Awww )): I'm sorry! But hey, you got through it ¯\_(ツ)_/¯  ")
else:
    slow_type("Sorry, I don't recognize that")

while True:
    answer12 = input('type secrets to look at the secrets you have learned or type continue to keep going ')
    secrets = []
    if answer12 == 'secrets':
        secrets.append("Death of Jason Blossom")
        print(secrets[0])
        secrets.append("History to Veronica Lodge")
        print(secrets[1])
        secrets.append("Hiram Lodge and his activities")
        print(secrets[2])
        secrets.append("Hermione Lodge helping Hiram keep his criminal empire going")
        print(secrets[3])
        secrets.append("Archie is unsure how he feels about Betty")
        print(secrets[4])
        secrets.append("Archie has an aspiring music career and writes his own songs")
        print(secrets[5])
        secrets.append("Polly (Betty's older sister) dated Jason he went missing")
        print(secrets[6])
        secrets.append("Alice had this bad view of the Blossom family because of Jason and Polly together")
        print(secrets[7])
        secrets.append("During the summer, on the night of Jason Blossom's murder, Archie and Ms. Grundy were together")
        print(secrets[8])
        secrets.append("Hermione and Fred dated in high school before she left Fred for Hiram and eventually married him")
        print(secrets[9])
        secrets.append("After Hiram was incarcerated, Hermoine and Veronica lost a lot of money because the main income source was from Hiram")
        print(secrets[10])
        secrets.append("Hiram Lodge ran his empire based on illegal activities concering money (fraud, exploiting people, etc)")
        print(secrets[11])
        secrets.append("Veronica reveals how she was in New York and why she's in Riverdale")
        print(secrets[12])
        secrets.append("Betty's inner rebel shows in the defiance against her mother")
        print(secrets[13])
        secrets.append("Archie tells his dad about him wanting to pursue a music carrer")
        print(secrets[14])
        secrets.append("Veronica and Archie kiss")
        print(secrets[15])
        secrets.append("Archie shows some vulnerability and insecurity")
        print(secrets[16])
        secrets.append("Kevin and Moose accidentally find Jason's body in the river, and find that he was shot")
        print(secrets[17])
        print('\n\n')
        continue
    elif answer12 == 'exit':
        break

        print('Sorry, I do not recognize that command\n')
        break