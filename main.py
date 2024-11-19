#THE GAME
import random

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   # print(color.BOLD + 'Hello, World!' + color.END)


def combat(p1,enem):
    while True:
        while True:
            opt = int(
                input(
                    "Narrator: QUICK WHAT ARE YOU GONNA DO!!"+color.GREEN+
                    "\n1: Shoot to the head\n2: Shoot to the chest\n3: Try to talk\nChooe!:"+color.END
                ))
            if opt == 1:
                dmg = random.randint(1, 3)
                p1["attack"] = dmg + 2
                enem["health"] -= p1["attack"]

                enem["attack"] = dmg-1
                p1["health"] -= enem["attack"]

                print("You shoot at the head!", p1["attack"], "<-- was your dmg")
                print("Enemy Attack! it does!",enem["attack"], " of dmg!")

            elif opt == 2:
                dmg = random.randint(1, 2)
                p1["attack"] = dmg + 1
                enem["health"] -= p1["attack"]

                enem["attack"] = dmg - 1
                p1["health"] -= enem["attack"]

                print("You shoot at the head!", p1["attack"], "<-- was your dmg")
                print("Enemy Attack! it does!", enem["attack"], " of dmg!")

            elif opt == 3:
                print(
                    "------You try to talk, but the enemy shoot you in the face!------")
                print("------------------YOU ARE DEAD SPACE-COWBOY!---------------")
                print("------------------------GAME OVER!-------------------\n"
                      "-----------------SEE YOU LATER SPACE-COWBOY!---------------")
                break

            if p1["health"] <= 0:
                print("------------------YOU ARE DEAD SPACE-COWBOY!---------------")
                break

            if enem["health"] > 0:
                print("The enemy is still standing with",enem["health"],
                      "health left!")
                print("This is you health Watch out!", p1["health"])
            else:
                print("The enemy is defeated!")
                return


        restart = int(
            input("Do you want to repeat the fight?\n1: Yes\n2: No\nChoose!: "))
        if restart != 1:
            print("-----See you later, space cowboy!------")
            exit()




stt = True
while stt:
    inve = []
    enemy1 = {"health":10, "attack":2}
    enemy2 = {"health":10, "attack":2}
    FinalBoss_Health = {"health":20, "attack":3}
    p1 = {"health": 10, "attack": 0}

    with open("output.txt", "w") as file:

        print(color.BOLD+ color.GREEN + "------Welcome To Space-Cowboy!!------" + color.END)

        print(color.YELLOW + "This is a demo, There is just one mission!\n " + color.END)
        print(color.RED + "----IMPORTANT!----\nUse the terminal the biggest you can for a better experience."+color.END)

        cho = int(input(color.GREEN+"1: Start!\n2: Exit\nChoose!: "+color.END))

        if cho == 1:
            print(color.BOLD+"\nNarrator: "+color.END,"It is a dark night, it is drizzling in the streets of Neon-Heaven,\n"
                  "You are driving your car, you get to the destination, your friend Franky told you\n"
                "about this place, The best fixer in town he said.")

            print("\nNarrator: You made your way to get to the 3rd floor, the second door to the right, that was what Franky told you\n"
                  "You knock the door 3 times.... No answer...")
            cho = int(input("\nNarrator: Do you want to knock again?"+color.GREEN + "\n1:Yes!\n2:Nope!\nChoose!:"+color.END))
            if cho == 1:
                print("\nNarrator: You knock one more time.... and finally someone open the door!\n"
                  "It is a beautiful woman!, and when you are about to say something\n"
                  "You get interrupted by a small man with a cybernetic eye, and a robotic hand, he is counting credits"
                  "\n\nSmall man: So you are the Cowboy Franky talked about, so tell me choom ")
                Name = input("What is your name Space-Cowboy? ")

                print("\nJax: Oh hi",color.YELLOW+ Name + color.END, "my name is Jax I am the best fixer from this heavenly city")
                print("I'm gonna be quick choom!, I have a job for you if you want it of course....")
                print("\nJax: The job is simple, just an extraction, there is this man who his kid got lost, or kidnap,\n"
                      "I don't really know, the point is that he need someone to retrieve the kiddo, it should be an easy job.\n")
                cho = int(input(
                    "Jax: So what do you say choom?"+color.GREEN+"\n1:Yes, I'll do it!\n2:F#$k you!\nChoose!: "+color.END))

                if cho == 1:
                    print("\nJax: Aight!, let me give you the deets!.......")
                    print("\nNarrator: The fixer give you the details about the mission, then you get out the building\n"
                          "get into your car, and drive your way over your objective......")
                    print(color.YELLOW + "\nMission 1: The lost child!" + color.END)

                    print("\nNarrator: You get to your objective, it is and old house, a few miles outside the city\n"
                          "You park on the next street so nobody will suspect, before you start walking to the house\n"
                          "You open your trunk, and you see your equipment there, a full stack of weapons and tools\n"
                          "Just what any Space-Cowboy need, you know this is a quick job, that's what Jax told you\n"
                          "So you decide to choose from your 3 favorite weapons...... ")

                    cho = int(input(color.GREEN+"1:Revolver.\n2:Shotgun\n3:Rifle\nChoose your weapon!: "+color.END))
                    if cho == 1:
                        print("Excellent choice! you will have more rounds and speed but less damage! ")
                        inve.append("revolver")
                        p1["attack"] += 2
                    elif cho == 2:
                        print("Good one!, you'll have less rounds but more power! ")
                        inve.append("shotgun")
                        p1["attack"] += 3
                    else:
                        print(
                            "The good old rifle! you'll have more damage per shot! but just one round! use it with wisdom! ")
                        inve.append("rifle")
                        p1["attack"] += 4

                    print("\n"+color.BLUE+Name+color.END, ":Alright, Show Time!! \n")
                    print("Narrator: You walk close to the house, you start to asset the house, looking for any choom\n"
                          "who want to make your work harder, but you can see anything...")
                    print(
                        "\nNarrator: You see two options.\n"
                        +color.GREEN +"Option 1: Go trough the front door and see what happen. \n"
                        "Option 2: Surround the house and go through the back door."+color.END)

                    while stt:
                        opt = int(input("\nNarrator: Wat are you gonna do ? "))
                        if opt == 1:
                            print(
                                "\nNarrator: You open the front door, and walk slowly, with your "" on your hand, you are ready for anything!\n"
                                "At least that's what you think, you hear something to your right, it is a man, with a machinegun, and he is ready to shoot!!")
                            combat(p1,enemy1)
                            p1["health"] = 10
                            print("\nNarrator: The shooting alert everyone who was on that house, now you hear steps coming to you!.\n"
                                  "A second person shows with a sword, you don't have time to think, you need to act!")
                            opt = int(input("\nWhat are you gonna do!... \n"
                                    +color.GREEN+"1:Hide behind the wall and wait for her!\n"
                                    "2:Run to confront him face to face!\n"
                                    "Chooe!:"+color.END))
                            if opt == 1:
                                print("\nYou hide in the corner and wait for him to show up and.. ")

                                combat(p1,enemy2)
                                p1["health"] = 10
                                print("\nNarrator: After the fight, you see a mysterious person runing towards the basemant!\n"
                                      "you go behind, you kick the door! and rush down!, you see a the mysterious figure, but... it is not\n"
                                      "trying to kill you, it's not even looking your way.. it is talking to someone.. to a kid...")


                                opt = int(input("\nWhat do you want to do?\n"+color.GREEN+"1: Shoot in the back!\n2: Talk to the mysterious person.\nChoose!: "+color.END))
                                if opt == 1:
                                    print("\nNarrator: You shoot in the back....")
                                    print("\nkid: MOOOOOMMMYYYYYYYY!!!!!!!!!!!" )
                                    print("\nNarrator: You inspect the body, it was a woman, it was the kid's mother..\n"
                                          "with her last words, she said..... ")
                                    print("\nPam: I....love.....you............................")
                                    print("\nNarrator: You take the kid back to the fixer to collect your reward...\n"
                                          "When you arrived you notice there is another man with Jax..\n"
                                          "\nJax: Heeheeee I knew you could do the job! this is Ewyn the kids daddy.\n"
                                          "\nEwyn: Thanks for your exceptional job!, she was a inconvenience, I will give you something extra!\n"
                                          "Now kid lets GO!!! and STOP CRYING!!! ")
                                    print("\nNarrator: You get your bounty, but the question is, was it really worth it??")

                                    print("\n---------------See you Next time Space-Cowboy!----------------")
                                    print(color.YELLOW+"-------------------------GAME OVER!-------------------------"+color.END)
                                    stt = False

                                else:
                                    print("\nNarrator: You wait a moment and hear what are they saying.. ")
                                    print("\nPam: It is ok baby! we are gonna be fine!!, we will go to te beach after this night! don't worry!\n"
                                          "(The kid is crying softly.. he is scare.. ")
                                    print("\nPam: So Ewyn hired you right?, I know why you are here, look I'm not gonna try to convence you\n"
                                          "But trust me when I say he is a MONSTER!, I will not let you take my son to him!!, he want to\n"
                                          "to some experiments with him!, He is special! and I will protect him! with my life!!  ")
                                    opt = int(input("\nNarrator: You just have 2 options."+color.GREEN+"\n1:Fight!\n2:Spare her life and let her go!\nChoose!:"+color.END))
                                    if opt == 1:
                                        print("\nPam: alright then.. let's do this... (She takes her son into a room and close the door.")
                                        combat(p1,FinalBoss_Health)
                                        print("\nNarrator: She is defeated, she lay in the floor, and blood is coming out of her chest...\n"
                                              "The door opens...")
                                        print("\nkid: MOOOOOMMMYYYYYYYY!!!!!!!!!!!\n"
                                              "\nNarrator: With her last words....")
                                        print("\nPam: I....love.....you............................")
                                        print("\nNarrator: You take the kid back to Jax to collect your reward...\n"
                                              "When you arrived you notice there is another man with Jax..\n"
                                              "\nJax: Heeheeee I knew you could do the job! this is Ewyn the kid daddy.\n"
                                              "\nEwyn: Thanks for your exceptional job!, she was a.... inconvenience, I will give you something extra!\n"
                                              "Now kid lets GO!!! and STOP CRYING!!!  ")
                                        print("\nKid: NOOOOOOOOOOOOOooooooooooooooooooo!!!!")

                                        print("\nNarrator: You get your bounty, but the question is, was it really worth it??\n")
                                        print("\n-------------------------TO BE CONTINUE!-------------------------")
                                        print("------------------See you Next time Space-Cowboy!----------------")
                                        print(color.YELLOW+"-------------------------GAME OVER!-------------------------"+color.END)
                                        stt = False
                                    else:
                                        print(Name,"Go...")
                                        print("\nPam: Thank you, you have no idea how much this means to me...\n"
                                              "Take care....\n"
                                              "\nNarrator: She takes the kid and leave....\n"
                                              "\nNarrator: You drive back to Jax house.")
                                        print("\nJax: Well is it done?.. is it right?... oh noo... we are doom now choom.\n"
                                              "\nNarrator: A big truck arrived, 4 armed men get out from the car, behind them one more\n"
                                              "one with a suit and long hair...")
                                        print("\nEwyn: So.. where is my kid Jax?..\n"
                                              "\nJax: eeEe...(He is afraid)\n"
                                              "\nEwyn: Well that is a shame.. kill him..(BOOOOM)\n"
                                              "\nNarrator: Jax is in the floor, he is dead, Ewyn's men take you down, and put a gun in your head.\n"
                                              "\nEwyn: I guess you where hired for the job but. let me guess, she convinece you right?\n"
                                              "Look, I'm not a monster.. I just didn't kike Jax, but you, I heard about you.I'm gonna\n"
                                              "give you one more chance, you gonna give me that little monster back! or your head is next!\n "
                                              "There is not options here!, you are my employee now!")
                                        print("\nNarrator: They leave and left you there..... You stand up, it is a rainy night, and you have work to do.")
                                        print("\n---------Doing the right thing in this city looks like a crime, but what kind of person are you Space-Cowboy?-----")

                                        print("-----------------------TO BE CONTINUE!-----------------------")
                                        print("\n---------------See you Next time Space-Cowboy!----------------")
                                        print(color.YELLOW+"-------------------------GAME OVER!-------------------------"+color.END)
                                        file.write("CONGRATS! YOU GOT THE TRUE ENDING!")
                                        stt = False
                            else:
                                print("You run to try to hit him to save bullets!, but she has a sword and stab you in the cest!!\n")
                                print(color.RED + "------------------YOU ARE DEAD SPACE-COWBOY!---------------" + color.END)
                                print("-------------GAME OVER! SEE YOU LATER SPACE-COWBOY!-------------")
                                stt = False
                        else:
                            print("\nNarrator: You go to the back door.. You try to open it but it is close from the other side...\n")
                else:
                    print("Jax: You chose the wrong fight choom!!!!!")
                    print(
                        "Narrator: The women rise her cybernetic leg and it transform into a machinegun, which use to shoot you!")
                    print("-------------YOU ARE DEAD SPACE-COWBOY!----------")
                    print("------------------------GAME OVER!-------------------\n"
                          "-----------------SEE YOU LATER SPACE-COWBOY!---------------")
                    stt = False
            else:
                restart = int(
                    input("Are you sure?\n1: Yes\n2: No\nChoose!: "))
                if restart == 1:
                    print("\nNarrator: Alright time to go home Space-Cowboy!\n")
                    print("------------------------GAME OVER!-------------------\n"
                          "-----------------SEE YOU LATER SPACE-COWBOY!-----------11----")
                    stt = False








        else:
            print("------------------------GAME OVER!-------------------\n"
                  "-----------------SEE YOU LATER SPACE-COWBOY!---------------")
            stt=False