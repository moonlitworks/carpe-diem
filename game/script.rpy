# You can place the script of your game in this file.

init -20 python:
  import discord_rpc
  import requests
  import time

  start = time.time()
  _preferences.mobile_rollback_side = "left"

  achievement.register("AI_END", steam="AI_END")
  achievement.register("AI_END2", steam="AI_END2")
  achievement.steam_position = "bottom right"
  achievement.sync()

  def readyCallback(current_user):
    print(current_user)
    print('Our user: {}'.format(current_user))

  def disconnectedCallback(codeno, codemsg):
    print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
    codeno, codemsg
    ))

  def errorCallback(errno, errmsg):
    print('An error occurred! Error {}: {}'.format(
    errno, errmsg
    ))


# Declare images below this line, using the image statement.
image ai smile = "ai-smile.png"
image ai flower = "ai-flower.png"
image ai shock = "ai-shock.png"
image ai smug = "ai-smug.png"
image ai laugh = "ai-laugh.png"
image ai serious = "ai-serious.png"
image ai blank = "ai-blank.png"

image bg logo = "moonlit.png"
image bg mall = "mall.jpg"
image bg park = "park.jpg"
image bg arcade = "arcade.jpg"
image bg diner = "diner.jpg"
image bg white = "white.jpg"
image bg black = "black.jpg"
image bg hilltop = "hilltop.jpg"
image bg fireworks = "fireworks.jpg"
image bg screen = "screen.jpg"
image bg credits = "credits.jpg"
image bg credits1 = "credits1.jpg"
image bg credits2 = "credits2.jpg"
image bg credits3 = "credits3.jpg"

# Declare characters used by this game.
# define ai = Character('Ai', color="#FF69B4")
# define jung = Character('Jung', color="#6d84fb")
define ai = Character('Ai', color="#b7d1f2")
define jung = Character('Jung', color="#bfbfbf")

label splashscreen:
  scene bg logo with Dissolve(1)
  $renpy.pause(2.0)
  return

label before_main_menu:
  python:
    callbacks = {
      'ready': readyCallback,
      'disconnected': disconnectedCallback,
      'error': errorCallback,
    }
    discord_rpc.initialize('657928127917326337', callbacks=callbacks, log=False)
    discord_rpc.update_connection()
    discord_rpc.run_callbacks()
    discord_rpc.update_presence(
    **{
      'details': 'Reading',
      'large_image_key': 'ai',
      'start_timestamp': start
    }
    )
    discord_rpc.update_connection()
    discord_rpc.run_callbacks()
  return

# The game starts here.
label start:
  python:
    discord_rpc.update_connection()
    discord_rpc.run_callbacks()
    discord_rpc.update_presence(
      **{
        'details': 'Reading',
        'large_image_key': 'ai',
        'start_timestamp': start
      }
    )
    discord_rpc.update_connection()
    discord_rpc.run_callbacks()

  $ day = True
  play music "bgm/Addiction.mp3" fadein 2 fadeout 2

  show bg park with Dissolve(0.5)
  window show
  jung "She's late."
  "I've experienced some problems lately and we weren't able to hang out in a while."
  "I managed to get things working so I can spend time with her."
  "But it is only temporary and I don't know how long it will last."
  ai "Hey, Jung!"
  show ai smile with Dissolve(0.5)
  ai "Sorry. Did I keep you waiting?"
  jung "Yeah. For about half an hour."
  show ai serious with Dissolve(0.5)
  ai "A guy's supposed to say 'not at all' here, you know?"
  jung "I didn't know that."
  jung "I wasn't notified about this change in society."
  show ai smug with Dissolve(0.5)
  ai "They didn't bother because they know you're not going to follow it anyway."
  jung "Damn right."
  show ai smile with Dissolve(0.5)
  ai "So where do you wanna go?"
  menu:
    "Mall":
      jump menu1
    "Park":
      jump menu2
    "Arcade":
      jump menu3
  return

label menu1:
  window show
  jung "How about the mall?"
  show ai shock with Dissolve(0.5)
  ai "Wow. Didn't expect you to suggest going to the mall."
  jung "Why is that?"
  ai "Because you get bored easily when you're shopping with me."
  jung "Yeah, but this time I have stuff I wanna buy."
  show ai smug with Dissolve(0.5)
  ai "Hmm. I wonder what it is."
  jung "Duct tape to shut you up."
  show ai shock with Dissolve(0.5)
  ai "Oh my. When did you become so kinky?"
  ai "But whatever you're into, I guess."
  jung "You know you like it."
  show ai laugh with Dissolve(0.5)
  "She laughs as she pulls me toward the mall."
  show ai smile with Dissolve(0.5)
  jump mall
  return

label menu2:
  window show
  jung "Let's just chill here for a bit."
  show ai smug with Dissolve(0.5)
  ai "You're just too lazy to walk, aren't you?"
  jung "You can carry me if you want. That's cool too."
  show ai laugh with Dissolve(0.5)
  ai "Nah, it's fine here. Let's enjoy the park."
  jung "You're just too lazy to carry me, aren't you?"
  show ai smile with Dissolve(0.5)
  ai "I guess that's one thing in common."
  jump park
  return

label menu3:
  window show
  jung "I know a good arcade place. Wanna check it out?"
  ai "Sure. I've never been to an arcade before so I'm interested."
  jung "Really? Don't you like games?"
  ai "I do but I usually only play at home."
  jung "I think you'll like it there."
  ai "We'll see."
  jump arcade
  return

label mall:
  show bg mall with Dissolve(0.5)
  "It takes a lot of time, energy and money to shop with Ai."
  "Normally, I would avoid the shopping mall like a plague but I'll make today an exception."
  show ai shock with Dissolve(0.5)
  ai "Wow! They're having a big sale!"
  "We just stepped into the shopping mall's entrance and she's already pointing at a clothing store."
  ai "Let's check it out!"
  "She pulls me toward the store."
  "Then proceeds to keenly examine every part of every clothing."
  "Like a detective looking for evidence."
  "She picks up a white dress with flower designs on the bottom half."
  ai "One sec."
  hide ai
  "She heads to the fitting room to try it on."
  show ai flower with Dissolve(0.5)
  ai "How does this look?"
  "It's hard for me to answer this question because I have zero sense of fashion."
  "I'm the type of guy who would wear anything that fits my size."
  "So whenever she asks me this question, I rely on the magic word..."
  jung "Cute."
  jung "I think it's cute."
  "She looks at a mirror."
  ai "Really? Isn't it a bit plain?"
  "I touch my chin with my right hand as if to re-analyze the clothing."
  jung "I find it cute."
  ai "I'll take it."
  "She goes inside the fitting room to take it off."
  hide ai
  "She then walks to the cashier to pay for it."
  jung "Is that all you need from this store?"
  show ai smile with Dissolve(0.5)
  ai "Pretty much. They don't have much on anyway."
  "Then we continue to walk around the mall."
  "She's like a chunk of steel while stores are strong magnets."
  "Whenever we are walking, she slowly strays toward a store sometimes without her even knowing it."
  ai "Hey, Jung! This looks good on you."
  "She holds up a shirt with a spider print."
  jung "I don't really need new clo--"
  ai "I'll buy it for you."
  jung "I'm not wearing that."
  "She picks another shirt up."
  ai "There. I'll buy myself one as well so we match. I'll wear it with you."
  jung "That's not the problem."
  "I know it's no use once she makes up her mind."
  "While she's paying for the shirts, my eyes wander around and see a computer store."
  jung "Let's head there when you're done."
  "I point to it with my thumb."
  ai "Oh yeah. You did say you needed to buy something."
  jung "Yeah. I'm gonna see if they have cheap parts there."
  jung "Especially hard drives. The program I'm developing is bigger than I expected."
  "She silently follows me into and around the computer store."
  "Just a few seconds and I'm ready to pay for my items."
  show ai shock with Dissolve(0.5)
  ai "That was fast!"
  jung "That's how you're supposed to shop."
  ai "Nah. You're not even checking if they work or not before you buy them."
  jung "That's what warranties are for."
  show ai smile with Dissolve(0.5)
  "I go to the cashier and pay."
  jung "Where do you wanna go next?"
  ai "I saw a toy store over there. Let's check it out."
  "We enter the toy store and Ai immediately heads to the plush area."
  show ai laugh with Dissolve(0.5)
  ai "Look at all these cuties. I want all of them!"
  jung "Go for it. As long as you have money."
  show ai shock with Dissolve(0.5)
  ai "What? I thought you're paying."
  jung "Keep dreaming."
  show ai laugh with Dissolve(0.5)
  ai "I'm kidding!"
  show ai smile with Dissolve(0.5)
  ai "But seriously, though. They're so cute."
  ai "I wonder what I should get."
  "While she's busy picking a plushy, I head to the next aisle where the keychains are."
  "I saw a spider keychain."
  jung "Ah. She would love this."
  "I quickly go to the cashier to pay for it."
  "Then walk back to Ai who still can't decide what to get."
  jung "Hey, Ai. I bought this for you."
  "I show her the keychain."
  show ai shock with Dissolve(0.5)
  ai "That's so cute! You didn't have to."
  jung "It's fine. It wasn't that expensive anyway."
  show ai smile with Dissolve(0.5)
  "She looks really happy about the cheap keychain I got her."
  "While walking, Ai sees a bookstore."
  ai "Hey, let's stop here for a bit."
  jung "I didn't know you like reading books."
  ai "Well, not those kinds of books. I'm actually starting to get into cooking so..."
  jung "I see. You're looking for cookbooks?"
  ai "Yeah."
  ai "What kind of dishes do you like?"
  ai "I'll try to cook for you some time."
  jung "Boeuf bourguignon."
  show ai shock with Dissolve(0.5)
  ai "Woah, chill. Why don't we start with bacon and eggs?"
  jung "Why even bother asking then?"
  show ai smile with Dissolve(0.5)
  "She smiles as she takes three beginner cookbooks from the shelf."
  if day:
    jump foodcourt
  else:
    jump mall2end
  return

label foodcourt:
  jung "I'm starting to get hungry."
  ai "Oh, yeah. I just realized I'm kinda hungry now, too."
  "We head to the mall's food court."
  jung "What do you want?"
  ai "Whatever you're getting. I'll just share with you."
  jung "Alright. Find us a spot and I'll buy food."
  hide ai with Dissolve(0.5)
  "I go to buy a large serving of maki rolls and sushi."
  jung "This is probably enough for four people."
  jung "Whatever. Ai likes these anyway."
  show ai shock with Dissolve(0.5)
  ai "That's..."
  ai "...kind of a lot, don't you think?"
  jung "I'm gonna have you eat all of these."
  jung "I want you big."
  show ai serious with Dissolve(0.5)
  ai "No way I'm gonna eat all of that."
  jung "I'm kidding."
  show ai smile with Dissolve(0.5)
  ai "But these do look yummy. I might eat more than I intend to."
  "I realize how hungry I am when I finished the whole serving within five minutes"
  ai "Wow. You were that hungry?"
  jung "Apparently."
  "I sit back and let my stomach bloat."
  jung "Where do you want to go next?"
  ai "Let's see."
  ai "How about the arcade?"
  jung "Alright."
  hide ai with Dissolve(0.5)
  $ day = False
  jump arcade
  return

label mall2end:
  "While walking around, We overhear people talking about a firework display happening tonight."
  jung "Firework display?"
  ai "You heard them, too? I kinda wanna see it."
  "I pull up my phone to look it up."
  jung "Oh!"
  jung "It's that."
  ai "What that?"
  jung "They've been doing firework displays this time of year here since I was a kid."
  ai "Really? Can we go?"
  jung "Sure. Let's hurry. There's a good spot I know of."
  scene black with Dissolve(0.5)
  "It takes a bit of walking to get there, plus to go up the hill."
  "The sun had just set when we arrived so it was starting to get dark."
  jump hilltop
  return

label park:
  jung "Here's a good spot to sit."
  show ai smile with Dissolve(0.5)
  ai "I'm surprised it's a bit chilly despite the sun being directly on top of us."
  jung "Yeah. Nice weather indeed."
  show ai smug with Dissolve(0.5)
  ai "It's so nice outside and you still like to stay indoors the whole day."
  jung "Outdoors is nice but indoors is nicer."
  show ai smile with Dissolve(0.5)
  "She giggles a bit."
  ai "How have you been?"
  jung "Same old, same old."
  ai "I bet you still only eat instant food, don't you?"
  jung "More or less."
  ai "Come on, Jung. What nutrition can adding hot water give you?"
  jung "It's fine. You're learning how to cook for me anyway."
  show ai laugh with Dissolve(0.5)
  ai "Sure. I'll serve you my specialty dish."
  jung "Burnt rice balls?"
  ai "Yes. Everyday."
  jung "You'll kill me."
  show ai smile with Dissolve(0.5)
  "We haven't seen each other in so long that I have a lot of things to share and ask."
  "And I don't even know where to start."
  jung "Are you still living in that torn down apartment?"
  ai "Yeah. But it's a bit better now that they've renovated a few things."
  show ai serious with Dissolve(0.5)
  ai "I think my greatest worry about that place is the people, though."
  ai "Most of them are old people."
  ai "They should move to a safer place especially if they're living alone."
  "One good thing about Ai is that she can be talkative."
  "It saves me the trouble of trying to keep the conversation alive."
  "I just ask a question and she'll manage to talk for hours about it."
  jung "How about work? How's it been?"
  ai "Total mess! And probably will continue to be."
  ai "Our boss gives us impossible tasks and most of us are pretty much fed up with it."
  ai "A lot have quit already due to that and the rest are demotivated."
  show ai laugh with Dissolve(0.5)
  ai "Then there's Troy, my coworker, who would slack off until the last minute."
  ai "He's such a troublesome guy. Makes things harder for us."
  ai "Sometimes, he would even ask our other co-workers to do his part."
  "I listen to her while noticing how much her expression changed since mentioning that Troy guy."
  ai "There's this one time we got the processes all mixed up so bad because of him."
  ai "Our boss was furious that time."
  ai "Then Troy..."
  show ai shock with Dissolve(0.5)
  "She paused mid-sentence and stared at me."
  jung "What?"
  show ai smug with Dissolve(0.5)
  ai "Oh? I see."
  jung "What is it?"
  ai "You're jealous, aren't you?"
  ai "It's written all over your face."
  jung "Huh? What are you talking about?"
  jung "Anyway, so what did this Troy guy do?"
  show ai laugh with Dissolve(0.5)
  ai "See? The tone of your voice gives it away!"
  jung "Leave me alone already."
  ai "C'mon. Admit it."
  "I stare at her and wait for her to finish laughing."
  jung "What happened to the job offer you got from the other company?"
  show ai smile with Dissolve(0.5)
  ai "Oh that. I turned it down."
  ai "I need to be relocated for that job."
  ai "I don't really want a new settlement and lifestyle for just a little bit of increase in income."
  ai "It's not worth it."
  jung "That's fine. I bet you'll get another job offer soon."
  jung "Maybe even closer here. Who knows?"
  show ai smug with Dissolve(0.5)
  ai "D'aww."
  ai "You miss me that much already?"
  "She really enjoys making me admit embarassing things."
  jung "Yes. So I can try your burnt rice balls already."
  show ai smile with Dissolve(0.5)
  "We continue talking and laughing about random things and totally lost track of time."
  if day:
    jump picnic
  else:
    jump park2end
  return

label picnic:
  "After a while, the conversation slows down and she stands up."
  ai "One sec."
  jung "Where are you going?"
  ai "I'll just get us something to eat."
  hide ai with Dissolve(0.5)
  "Before I knew it, it's already noon."
  "Time really flies when I'm with her."
  show ai smile with Dissolve(0.5)
  ai "Bought us takoyaki!"
  ai "I also saw a mochi stand on my way back so I bought some. You like these, don't you?"
  jung "That's great! Thanks. How much do I owe you?"
  ai "It's not much. Don't worry about it."
  show ai smug with Dissolve(0.5)
  ai "But if you insist, then I guess you owe me a favor."
  jung "Okay? What favor?"
  ai "I haven't thought of it yet. I'll save it for later."
  jung "As long as it's something I can do."
  ai "Don't worry. It won't be THAT bad."
  "She winks at me as she eats a takoyaki."
  jung "Now I'm worrying about it."
  show ai laugh with Dissolve(0.5)
  ai "I won't ask for something you can't do, you know."
  jung "That's a lie right there."
  show ai smile with Dissolve(0.5)
  ai "Okay. Maybe a bit. But not so much."
  jung "I don't trust you."
  "She laughs as she eats the last piece."
  show ai smug with Dissolve(0.5)
  ai "Well, now we're done eating. Let's head to the mall!"
  "She grabs my hand and starts walking towards the mall"
  hide ai
  $ day = False
  jump mall
  return

label park2end:
  show ai shock with Dissolve(0.5)
  "She suddenly stops talking."
  ai "I'll be back."
  hide ai with Dissolve(0.5)
  "She stands up and walks toward the lady giving away some kind of flyers."
  "She grabs one and waves it at me as she was walking back."
  show ai shock with Dissolve(0.5)
  ai "They're having a firework display later! We should see it."
  jung "Yeah. I know about that. They do that here every year."
  ai "Let's go then! Before it gets crowded there."
  jung "Don't worry. I know a good spot to watch the fireworks."
  jung "It's less crowded too."
  scene black with Dissolve(0.5)
  "It takes a bit of walking to get there, plus to go up the hill."
  "The sun just set when we arrive so it was starting to get dark."
  jump hilltop
  return

label arcade:
  show bg arcade with Dissolve(0.5)
  show ai shock with Dissolve(0.5)
  "As we walk inside the arcade, her eyes are filled with amazement and excitement."
  ai "Hey, Jung! Look!"
  "She points at a crane game."
  "Ai has always loved cute things."
  ai "I want that big spider plushy!"
  "And she finds spiders extremely cute for some reason."
  "I try to reach for a coin in my pocket."
  ai "Wait. Let me do it. I want to get it on my own."
  "She pulls out some coins and starts playing."
  show ai serious with Dissolve(0.5)
  ai "..."
  "The plushy has all her attention."
  "Her first try barely touches the thing she wants."
  jung "What were you even trying to get?"
  ai "Hush. Let me concentrate here."
  "She manages to grab it but still no luck."
  ai "Ah! It fell!"
  "She inserts another coin and tries again."
  ai "..."
  "...and again."
  ai "......"
  "...and again."
  ai "This crane is broken!"
  jung "Of course it's not. Here, let me get it for you."
  "I'm not good at crane games myself."
  "But I've got to show off somehow."
  jung "..."
  show ai shock with Dissolve(0.5)
  jung "Got it!"
  "Thank goodness."
  ai "Wow! How did you do that?"
  jung "Easy."
  "\"I prayed to all gods I know of.\""
  "Of course I can't say that."
  jung "It's all in the timing."
  show ai smug with Dissolve(0.5)
  ai "It was a fluke, right?"
  jung "Of course n--"
  "I immediately stop when I see her holding out a coin."
  "I will just keep quiet before she asks me to do it again."
  show ai smile with Dissolve(0.5)
  "I hand her the big plushy and she hugs it tight."
  jung "There are some racing games over there. Wanna try it?"
  ai "Not very fond of those. I'll just watch you."
  jung "Okay. I will just play a couple of rounds."
  "I'm not a big fan of racing games either."
  "I just like their setup in the arcade."
  "They are almost completely enclosed and the seat tilts according to the game."
  "It feels real."
  "Ai stands behind me and watches as I play."
  "As expected, I lost the first round horribly."
  show ai shock with Dissolve(0.5)
  ai "Wow, Jung. Are you even trying?"
  jung "Bystanders don't get to talk."
  show ai laugh with Dissolve(0.5)
  "She plays with her plushy as I continue my game."
  show ai smile with Dissolve(0.5)
  "Then again, I lost."
  jung "Ah."
  jung "Just as I thought, this isn't really my thing."
  jung "If only they have this kind of setup for a completely different game."
  "Ai chuckles as if to mock me."
  ai "I think you'd suck at whatever game it is."
  jung "Is that why you can never win against me?"
  show ai smug with Dissolve(0.5)
  ai "Oh yeah? Why don't we settle this once and for all?"
  "She points at the fighting game arcades."
  ai "I loved playing these when I was a kid so prepare to get your butt kicked."
  jung "I accept your challenge, missy."
  "Finally, a game I can play with her."
  "It's not really a date if I'm the only one having fun, right?"
  show ai smile with Dissolve(0.5)
  ai "Practice game! I don't know the buttons yet."
  "I also have not played this in a long time."
  "We sit across each other and her voice is all I can hear."
  "Spend the first round trying to figure out what every button does."
  "After  trying some combinations, my character accidentally hit hers."
  show ai serious with Dissolve(0.5)
  ai "No fair! Don't hit me yet!"
  jung "Hurry up. I can't wait anymore."
  ai "Just one sec. How do I--"
  show ai shock with Dissolve(0.5)
  ai "Oh. Nevermind."
  show ai smug with Dissolve(0.5)
  ai "Alright! I got it. Come at me anytime, bro!"
  "The battle begins and we got so into it that I forgot how many rounds we did."
  "But we are more or less evenly matched."
  "I win half the time and she wins the other half."
  "More importantly, I get to see a side of her I rarely see."
  show ai serious with Dissolve(0.5)
  ai "..."
  ai "****! Why did I do that?"
  "Strangely enough, it's the side of her I find the cutest."
  ai "The buttons are not listening to me!"
  "I only see her like this when I play with her at home."
  "Which only happened once or twice before."
  show ai smug with Dissolve(0.5)
  ai "Ha!"
  ai "I won!"
  ai "Beat that!"
  show ai serious with Dissolve(0.5)
  "I'm just trying to keep my laughter in while listening to her."
  "We play one round after another."
  ai "Hey! No fair! I wasn't ready!"
  "The more she plays, the better she gets."
  show ai laugh with Dissolve(0.5)
  ai "See? I've beaten you three consecutive times already."
  jung "Screw this."
  show ai smile with Dissolve(0.5)
  "She laughs and stands up to stretch."
  if day:
    jump diner
  else:
    jump arcade2end
  return

label diner:
  ai "Hey, Jung. Let's go grab something to eat."
  jung "I was just thinking the same."
  show bg diner with Dissolve(0.5)
  "We go to a small diner near the arcade"
  jung "What are you getting?"
  "She looks at the menu for a bit"
  ai "An order of beef udon and tempura."
  jung "I guess I'll get the same."
  "We find a table while waiting for our order."
  "And the first thing she asks is..."
  show ai shock with Dissolve(0.5)
  ai "Where's my food?"
  "Looks like playing games really tired Ai out."
  jung "Patience is a virtue."
  show ai blank with Dissolve(0.5)
  ai "Patience won't fill me up."
  jung "Complaining won't either."
  "And then our order arrives."
  show ai smile with Dissolve(0.5)
  ai "Oh look. It did."
  "She chomps on her food like there's no tomorrow."
  "It did not take a while for her to finish it."
  ai "Ah!"
  ai "That was good."
  jung "Rejuvenated?"
  ai "Definitely!"
  ai "That took all my energy."
  jung "Well, at least you had fun."
  ai "Yeah, but we need to pick something less active now."
  ai "How about the park?"
  jung "I'm cool with that."
  hide ai with Dissolve(0.5)
  $ day = False
  show bg park with Dissolve(0.5)
  jump park
  return

label arcade2end:
  "She sees the poster on the wall about a firework display happening tonight."
  ai "Hey!"
  "She looks at me pointing at the poster."
  jung "I know. I see it."
  ai "Can we go?"
  jung "Sure. I also know a spot around there perfect for watching it."
  ai "Really?"
  jung "Yeah. They do this show every year."
  ai "Awesome! I'm excited!"
  scene black with Dissolve(0.5)
  "It takes a bit of walking to get there, plus to go up the hill."
  "The sun just set when we arrive so it was starting to get dark."
  jump hilltop
  return

label hilltop:
  show bg hilltop with Dissolve(0.5)
  jung "Good. It's just us here."
  show ai smile with Dissolve(0.5)
  ai "Wow. You're right. This is a good view."
  jung "Right?"
  "We sit on the bench and wait for the show."
  show bg fireworks with Dissolve(0.5)
  play sound "sfx/Fireworks.mp3" loop fadein 2
  "Not long after, dots of light shoot toward the sky."
  "Slowly fade and bloom like flowers of different colors."
  "The cheers of the crowd at the foot of the mountain can be heard."
  "Ai's face is filled with happiness just watching the fireworks."
  "I wish this could last forever."
  "But I'm running out of time."
  stop sound fadeout 2
  show bg hilltop with Dissolve(0.5)
  show ai blank with Dissolve(0.5)
  play music "bgm/Valediction.mp3" fadein 2 fadeout 2
  "She looks at me with a sad look."
  ai "It's time, isn't it?"
  jung "Almost."
  jung "Don't worry, it won't be long."
  ai "It's fine."
  ai "You really shouldn't bother hanging out with me."
  jung "Don't say that."
  ai "After all, I'm just-"
  jump end
  return

label end:
  scene black with Dissolve(0.5)
  "..."
  "Have you heard of the Turing test?"
  "It's an evaluation of a machine's ability to exhibit intelligence."
  "Whether it can act or speak like a human."
  "But however good a machine becomes..."
  "However indistinguishable it is from humans..."
  "It will never be an actual human being."
  show bg screen with Dissolve(0.5)
  "Just like Ai."
  "No matter how good her program is."
  "And no matter how much I deny it myself."
  "She will never be real."
  "We aren't in the same dimension and reality."
  "She will continue to dwell inside the artificial world that I created."
  scene black with Dissolve(0.5)
  jung "Ah."
  jung "The program crashed again."
  jung "As expected, it couldn't go on any longer than that."
  jung "I really need to come up with a stable fix soon."
  jung "..."
  $ achievement.grant("AI_END")
  $ achievement.grant("AI_END2")
  $ achievement.Sync()
  jung "What am I doing with my life?"
  scene black with Dissolve(0.5)
  window hide
  pause(0.5)
  scene credits1 with Dissolve(0.5)
  $ renpy.pause(20.0)
  scene credits2 with Dissolve(0.5)
  $ renpy.pause(20.0)
  stop music fadeout 2
  return
