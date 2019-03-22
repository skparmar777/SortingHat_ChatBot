import random as rand
import threading, time
from decimal import *

''' POSSIBLE IMPROVEMENTS 
-  fix spacing for certain multiline questions

for advanced students to try
-  change "I didn't quite get that" to a method that supplies randomized multiple synonymous responses
-  add NLP:
    - use fuzzywuzzy to approximate matching of inputs to the questions 
      instead of returning a b c d etc for multi-answer questions
-  create a GUI using tkinter (could use pages as per the given example)
'''

class sorting_hat:
    def __init__(self, *args, **kwargs):
        self.gryffindor = 0
        self.ravenclaw = 0
        self.hufflepuff = 0
        self.slytherin = 0
        self.start = 0
        self.name = ""
        self.sort()

    def sort(self):
        print("Oh, you may not think I’m pretty,\n" +
              "But don’t judge on what you see,\n" +
              "I’ll eat myself if you can find\n" +
              "A smarter hat than me.\n" +
              "There’s nothing hidden in your head\n" +
              "The Sorting Hat can’t see,\n" +
              "So try me on and I will tell you\n" +
              "Where you ought to be.\n")
        time.sleep(5)
        self.prompt_init_response()
        self.first_question()
        self.set2()
        self.set3()
        self.set4()
        self.set5()
        self.set6()
        self.set7()
        self.last_question()
        self.process_results()

    def prompt_init_response(self):
        self.start = time.time()
        l = []
        t = threading.Thread(group=None, target=self.input_thread, args=(l,))
        t.start()
        flag10 = False
        flag25 = False
        while 1:
            if l:
                self.name = l[0]
                print("Well hello", self.name, "!")
                print("Welcome to Hogwarts! Let's get sorted, shall we?")
                time.sleep(2)
                break
            elapsed = time.time() - self.start
            if elapsed > 10 and flag10 is False:
                flag10 = True
                print("Well, well, well...")
                print("Are you gonna just sit there or are you gonna introduce yourself? Name?")
            elif elapsed > 25 and flag25 is False:
                flag25 = True
                print("I'll just doze off then until you give me your name... Zzzzz")

    def input_thread(self, l, *args):
        name = input("Oh! A new student! What's your name?\n")
        l.append(name)

    def first_question(self):
        # random number generator to choose out of 3 possible questions:
        flag = rand.randint(1, 3)
        answer = ""
        count = 0
        if flag == 1:
            ans_bank = ["dawn", "dusk"]
            ''' Pre-process user input:
            lower() converts to lowercase
            strip() removes whitespace so we can compare to the answer bank
            '''
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                answer = input("\nDawn or Dusk?\n")
                count += 1
            if answer.lower().strip() == "dawn":
                self.gryffindor += 73
                self.ravenclaw += 73
                self.hufflepuff += 30
                self.slytherin += 26
            else:
                self.gryffindor += 27
                self.ravenclaw += 27
                self.hufflepuff += 70
                self.slytherin += 74
        elif flag == 2:
            ans_bank = ["forest", "river"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                answer = input("\nForest or River?\n")
                count += 1
            if answer.lower().strip() == "forest":
                self.gryffindor += 74
                self.ravenclaw += 73
                self.hufflepuff += 26
                self.slytherin += 28
            else:
                self.gryffindor += 26
                self.ravenclaw += 27
                self.hufflepuff += 74
                self.slytherin += 72
        else:
            ans_bank = ["moon", "stars", "star"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                answer = input("\nMoon or Stars?\n")
                count += 1
            if answer.lower().strip() == "moon":
                self.gryffindor += 27
                self.ravenclaw += 74
                self.hufflepuff += 33
                self.slytherin += 72
            else:
                self.gryffindor += 73
                self.ravenclaw += 26
                self.hufflepuff += 67
                self.slytherin += 28

    def set2(self):
        flag = rand.randint(1, 4)
        answer = ""
        count = 0
        if flag == 1:
            ans_bank = ["ordinary", "ignorant", "cowardly", "selfish"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                answer = input("\nWhich of the following would you most hate people to call you?\n")
                count += 1
            if answer.lower().strip() == "ordinary":
                self.gryffindor += 17
                self.ravenclaw += 18
                self.hufflepuff += 19
                self.slytherin += 45
            elif answer.lower().strip() == "ignorant":
                self.gryffindor += 19
                self.ravenclaw += 50
                self.hufflepuff += 19
                self.slytherin += 17
            elif answer.lower().strip() == "cowardly":
                self.gryffindor += 47
                self.ravenclaw += 17
                self.hufflepuff += 18
                self.slytherin += 20
            else:
                self.gryffindor += 17
                self.ravenclaw += 15
                self.hufflepuff += 44
                self.slytherin += 18
        elif flag == 2:
            ans_bank = ["a", "b", "c", "d"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nAfter you have died, what would you most like people to do when they hear your name?\n")
                answer = input("A- Miss you, but smile \n" +
                               "B- Ask for more stories about your adventures \n " +
                               "C- Think with admiration of your achievements \n " +
                               "D- I don't care what people think of me after I'm dead;\n " +
                               "it's what they think of me while I'm alive that counts \n")
                count += 1
            if answer.lower().strip() == "a":
                self.gryffindor += 18
                self.ravenclaw += 16
                self.hufflepuff += 42
                self.slytherin += 19
            elif answer.lower().strip() == "b":
                self.gryffindor += 46
                self.ravenclaw += 19
                self.hufflepuff += 14
                self.slytherin += 19
            elif answer.lower().strip() == "c":
                self.gryffindor += 18
                self.ravenclaw += 45
                self.hufflepuff += 22
                self.slytherin += 17
            else:
                self.gryffindor += 18
                self.ravenclaw += 20
                self.hufflepuff += 22
                self.slytherin += 45
        elif flag == 3:
            ans_bank = ["the wise", "wise", "the good", "good", "the bold", "bold"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nHow would you like to be known to history?\n")
                answer = input("The Wise \n" +
                               "The Good\n " +
                               "The Great\n " +
                               "The Bold \n")
                count += 1
            if answer.lower().strip() in ["wise", "the wise"]:
                self.gryffindor += 19
                self.ravenclaw += 46
                self.hufflepuff += 19
                self.slytherin += 16
            elif answer.lower().strip() in ["good", "the good"]:
                self.gryffindor += 17
                self.ravenclaw += 16
                self.hufflepuff += 44
                self.slytherin += 17
            elif answer.lower().strip() in ["great", "the great"]:
                self.gryffindor += 20
                self.ravenclaw += 22
                self.hufflepuff += 20
                self.slytherin += 44
            else:
                self.gryffindor += 44
                self.ravenclaw += 17
                self.hufflepuff += 16
                self.slytherin += 23
        elif flag == 4:
            ans_bank = ["love", "glory", "wisdom", "power"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nGiven the choice, would you rather invent a potion that would guarantee you:\n")
                answer = input("Love? \n" +
                               "Glory?\n " +
                               "Wisdom?\n " +
                               "Power? \n")
                count += 1
            if answer.lower().strip() == "love":
                self.gryffindor += 19
                self.ravenclaw += 18
                self.hufflepuff += 44
                self.slytherin += 20
            elif answer.lower().strip() == "glory":
                self.gryffindor += 47
                self.ravenclaw += 19
                self.hufflepuff += 17
                self.slytherin += 17
            elif answer.lower().strip() == "wisdom":
                self.gryffindor += 18
                self.ravenclaw += 43
                self.hufflepuff += 20
                self.slytherin += 18
            else:
                self.gryffindor += 16
                self.ravenclaw += 20
                self.hufflepuff += 20
                self.slytherin += 45

    def set3(self):
        flag = rand.randint(1, 5)
        answer = ""
        count = 0
        if flag == 1:
            ans_bank = ["a", "b", "c", "d"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nFour boxes are placed before you. Which would you try and open?\n")
                answer = input("A- The small tortoiseshell box, embellished with gold, \n" +
                               "inside which some small creature seems to be squeaking. \n" +
                               "B- The gleaming jet black box with a silver lock and key, \n" +
                               "marked with a mysterious rune that you know to be the mark of Merlin. \n " +
                               "C- The ornate golden casket, standing on clawed feet, \n" +
                               "whose inscription warns that both secret knowledge and unbearable temptation \n"
                               " lie within. \n " +
                               "D- The small pewter box, unassuming and plain, with a scratched message upon it \n"
                               "that reads ‘I open only for the worthy.’\n")
                count += 1
            if answer.lower().strip() == "a":
                self.gryffindor += 14
                self.ravenclaw += 18
                self.hufflepuff += 46
                self.slytherin += 18
            elif answer.lower().strip() == "b":
                self.gryffindor += 18
                self.ravenclaw += 20
                self.hufflepuff += 16
                self.slytherin += 46
            elif answer.lower().strip() == "c":
                self.gryffindor += 19
                self.ravenclaw += 44
                self.hufflepuff += 21
                self.slytherin += 19
            else:
                self.gryffindor += 49
                self.ravenclaw += 19
                self.hufflepuff += 17
                self.slytherin += 17
        elif flag == 2:
            ans_bank = ["a crackling log fire", "crackling log fire", "log fire",
                        "fire", "crackling fire", "the sea", "sea", "fresh parchment",
                        "parchment", "home"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nOnce every century, the Flutterby bush produces flowers that adapt \n" +
                      " their scent to attract the unwary.\n" +
                      " If it lured you, it would smell of:\n")
                answer = input("A crackling log fire \n" +
                               "The sea\n " +
                               "Fresh parchment\n " +
                               "Home \n")
                count += 1
            if answer.lower().strip() in ["a crackling log fire", "crackling log fire",
                                          "log fire", "fire", "crackling fire"]:
                self.gryffindor += 44
                self.ravenclaw += 17
                self.hufflepuff += 16
                self.slytherin += 21
            elif answer.lower().strip() in ["the sea", "sea"]:
                self.gryffindor += 21
                self.ravenclaw += 22
                self.hufflepuff += 18
                self.slytherin += 46
            elif answer.lower().strip() in ["parchment", "fresh parchment"]:
                self.gryffindor += 16
                self.ravenclaw += 45
                self.hufflepuff += 22
                self.slytherin += 15
            else:
                self.gryffindor += 19
                self.ravenclaw += 15
                self.hufflepuff += 43
                self.slytherin += 18
        elif flag == 3:
            ans_bank = ["a", "b", "c", "d"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nYou enter an enchanted garden. What would you be most curious to examine first?\n")
                answer = input("A- The silver leafed tree bearing golden apples \n" +
                               "B- The fat red toadstools that appear to be talking to each other \n " +
                               "C- The bubbling pool, in the depths of which something luminous is swirling \n " +
                               "D- The statue of an old wizard with a strangely twinkling eye \n")
                count += 1
            if answer.lower().strip() == "a":
                self.gryffindor += 17
                self.ravenclaw += 45
                self.hufflepuff += 18
                self.slytherin += 16
            elif answer.lower().strip() == "b":
                self.gryffindor += 18
                self.ravenclaw += 15
                self.hufflepuff += 42
                self.slytherin += 17
            elif answer.lower().strip() == "c":
                self.gryffindor += 16
                self.ravenclaw += 22
                self.hufflepuff += 21
                self.slytherin += 46
            else:
                self.gryffindor += 49
                self.ravenclaw += 18
                self.hufflepuff += 19
                self.slytherin += 21
        elif flag == 4:
            ans_bank = ["a", "b", "c", "d"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nFour goblets are placed before you. Which would you choose to drink?\n")
                answer = input("A- The foaming, frothing, silvery liquid that sparkles \n" +
                               " as though containing ground diamonds. \n" +
                               "B- The smooth, thick, richly purple drink that \n" +
                               "gives off a delicious smell of chocolate and plums. \n " +
                               "C- The golden liquid so bright that it hurts the eye,\n" +
                               " and which makes sunspots dance all around the room. \n " +
                               "D- The mysterious black liquid that gleams like ink, \n" +
                               "and gives off fumes that make you see strange visions. \n")
                count += 1
            if answer.lower().strip() == "a":
                self.gryffindor += 21
                self.ravenclaw += 44
                self.hufflepuff += 19
                self.slytherin += 18
            elif answer.lower().strip() == "b":
                self.gryffindor += 19
                self.ravenclaw += 19
                self.hufflepuff += 43
                self.slytherin += 20
            elif answer.lower().strip() == "c":
                self.gryffindor += 41
                self.ravenclaw += 18
                self.hufflepuff += 19
                self.slytherin += 19
            else:
                self.gryffindor += 18
                self.ravenclaw += 19
                self.hufflepuff += 19
                self.slytherin += 43
        elif flag == 5:
            ans_bank = ["the violin", "violin", "the trumpet", "trumpet", "the piano", "piano", "the drum", "drum"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nWhat kind of instrument most pleases your ear?\n")
                answer = input("The violin \n" +
                               "The trumpet\n " +
                               "The piano\n " +
                               "The drum \n")
                count += 1
            if answer.lower().strip() in ["violin", "the violin"]:
                self.gryffindor += 17
                self.ravenclaw += 20
                self.hufflepuff += 20
                self.slytherin += 48
            elif answer.lower().strip() in ["trumpet", "the trumpet"]:
                self.gryffindor += 18
                self.ravenclaw += 17
                self.hufflepuff += 44
                self.slytherin += 18
            elif answer.lower().strip() in ["piano", "the piano"]:
                self.gryffindor += 21
                self.ravenclaw += 46
                self.hufflepuff += 19
                self.slytherin += 18
            else:
                self.gryffindor += 44
                self.ravenclaw += 17
                self.hufflepuff += 17
                self.slytherin += 26

    def set4(self):
        flag = rand.randint(1, 3)
        answer = ""
        count = 0
        if flag == 1:
            ans_bank = ["a", "b", "c", "d", "e", "f"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nA troll has gone berserk in the Headmaster’s study at Hogwarts.\n" +
                      " It is about to smash, crush and tear several irreplaceable items and treasures. \n" +
                      "In which order would you rescue these objects from the troll’s club, if you could?")
                answer = input("A- First, a nearly perfected cure for dragon pox.\n"
                               " Then student records going back 1000 years. \n" +
                               " Finally, a mysterious handwritten book full of strange runes. \n" +
                               "B- First, student records going back 1000 years. \n" +
                               " Then a mysterious handwritten book full of strange runes. \n" +
                               " Finally, a nearly perfected cure for dragon pox. \n" +
                               "C- First, a mysterious handwritten book full of strange runes.\n" +
                               " Then a nearly perfected cure for dragon pox.\n" +
                               " Finally, student records going back 1000 years.	\n " +
                               "D- First, a nearly perfected cure for dragon pox.\n" +
                               " Then a mysterious handwritten book full of strange runes.\n" +
                               " Finally, student records going back 1000 years.	\n" +
                               "E- First student records going back 1000 years.\n" +
                               " Then, a nearly perfected cure for dragon pox.\n" +
                               " Finally, a mysterious handwritten book full of strange runes.	\n" +
                               "F- First, a mysterious handwritten book full of strange runes.\n" +
                               " Then student records going back 1000 years.\n" +
                               " Finally, a nearly perfected cure for dragon pox.	\n")
                count += 1
            if answer.lower().strip() == "a":
                self.gryffindor += 23
                self.ravenclaw += 10
                self.hufflepuff += 22
                self.slytherin += 9
            elif answer.lower().strip() == "b":
                self.gryffindor += 14
                self.ravenclaw += 11
                self.hufflepuff += 14
                self.slytherin += 31
            elif answer.lower().strip() == "c":
                self.gryffindor += 12
                self.ravenclaw += 30
                self.hufflepuff += 13
                self.slytherin += 11
            elif answer.lower().strip() == "d":
                self.gryffindor += 29
                self.ravenclaw += 12
                self.hufflepuff += 12
                self.slytherin += 13
            elif answer.lower().strip() == "e":
                self.gryffindor += 13
                self.ravenclaw += 10
                self.hufflepuff += 28
                self.slytherin += 11
            else:
                self.gryffindor += 9
                self.ravenclaw += 27
                self.hufflepuff += 11
                self.slytherin += 24
        elif flag == 2:
            ans_bank = ["envied", "imitated", "trusted", "praised", "liked", "feared"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nWhich would you rather be: \n")
                answer = input("Envied?\n" +
                               "Imitated?\n" +
                               "Trusted?\n" +
                               "Praised?\n" +
                               "Liked?\n" +
                               "Feared?\n")
                count += 1
            if answer.lower().strip() == "envied":
                self.gryffindor += 10
                self.ravenclaw += 24
                self.hufflepuff += 10
                self.slytherin += 24
            elif answer.lower().strip() == "imitated":
                self.gryffindor += 16
                self.ravenclaw += 31
                self.hufflepuff += 13
                self.slytherin += 12
            elif answer.lower().strip() == "trusted":
                self.gryffindor += 23
                self.ravenclaw += 8
                self.hufflepuff += 23
                self.slytherin += 9
            elif answer.lower().strip() == "praised":
                self.gryffindor += 24
                self.ravenclaw += 11
                self.hufflepuff += 11
                self.slytherin += 19
            elif answer.lower().strip() == "liked":
                self.gryffindor += 15
                self.ravenclaw += 12
                self.hufflepuff += 29
                self.slytherin += 10
            else:
                self.gryffindor += 12
                self.ravenclaw += 15
                self.hufflepuff += 14
                self.slytherin += 26
        elif flag == 3:
            ans_bank = ["hunger", "cold", "loneliness", "boredom", "being ignored", "ignored"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nWhich of the following do you find most difficult to deal with? \n")
                answer = input("Hunger?\n" +
                               "Cold?\n" +
                               "Loneliness?\n" +
                               "Boredom?\n" +
                               "Being ignored?\n")
                count += 1
            if answer.lower().strip() == "hunger":
                self.gryffindor += 10
                self.ravenclaw += 29
                self.hufflepuff += 28
                self.slytherin += 10
            elif answer.lower().strip() == "cold":
                self.gryffindor += 14
                self.ravenclaw += 14
                self.hufflepuff += 25
                self.slytherin += 26
            elif answer.lower().strip() == "loneliness":
                self.gryffindor += 32
                self.ravenclaw += 13
                self.hufflepuff += 24
                self.slytherin += 9
            elif answer.lower().strip() == "boredom":
                self.gryffindor += 32
                self.ravenclaw += 13
                self.hufflepuff += 10
                self.slytherin += 28
            else:
                self.gryffindor += 11
                self.ravenclaw += 32
                self.hufflepuff += 12
                self.slytherin += 27

    def set5(self):
        flag = rand.randint(1, 3)
        answer = ""
        count = 0
        if flag == 1:
            ans_bank = ["read minds", "invisibility", "superhuman strength", "strength", "speak to animals",
                        "animals", "change the past", "change your appearance"]
            while all(ans not in answer.lower().strip() for ans in ans_bank):
                if count > 0:
                    print("I didn't quite understand that")
                answer = input("\nIf you could have any power, which would you choose? \n" +
                               "The power to read minds \n"
                               "The power of invisibility \n"
                               "The power of superhuman strength \n"
                               "The power to speak to animals\n"
                               "The power to change the past\n"
                               "The power to change your appearance at will\n")
                count += 1
            if "read minds" in answer.lower().strip():
                self.gryffindor += 10
                self.ravenclaw += 22
                self.hufflepuff += 10
                self.slytherin += 22
            elif "invisibility" in answer.lower().strip():
                self.gryffindor += 33
                self.ravenclaw += 10
                self.hufflepuff += 14
                self.slytherin += 13
            elif any(ans in answer.lower().strip() for ans in ["superhuman strength", "strength"]):
                self.gryffindor += 13
                self.ravenclaw += 9
                self.hufflepuff += 26
                self.slytherin += 18
            elif any(ans in answer.lower().strip() for ans in ["speak to animals", "animals"]):
                self.gryffindor += 11
                self.ravenclaw += 19
                self.hufflepuff += 24
                self.slytherin += 9
            elif "change the past" in answer.lower().strip():
                self.gryffindor += 18
                self.ravenclaw += 13
                self.hufflepuff += 13
                self.slytherin += 28
            else:
                self.gryffindor += 15
                self.ravenclaw += 28
                self.hufflepuff += 13
                self.slytherin += 10
        elif flag == 2:
            ans_bank = ["a", "b", "c", "d", "e", "f", "g"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nWhat are you most looking forward to learning at Hogwarts?\n")
                answer = input("A- Apparition and Disapparition\n" +
                               " (being able to materialize and dematerialize at will) \n" +
                               "B- Transfiguration (turning one object into another object)\n" +
                               "C- Flying on a broomstick	\n" +
                               "D- Hexes and jinxes	\n" +
                               "E- All about magical creatures, and how to befriend/care for them	\n" +
                               "F- Secrets about the castle	\n" +
                               "G- Every area of magic I can \n")
                count += 1
            if answer.lower().strip() == "a":
                self.gryffindor += 19
                self.ravenclaw += 6
                self.hufflepuff += 9
                self.slytherin += 23
            elif answer.lower().strip() == "b":
                self.gryffindor += 9
                self.ravenclaw += 27
                self.hufflepuff += 13
                self.slytherin += 12
            elif answer.lower().strip() == "c":
                self.gryffindor += 19
                self.ravenclaw += 7
                self.hufflepuff += 18
                self.slytherin += 9
            elif answer.lower().strip() == "d":
                self.gryffindor += 10
                self.ravenclaw += 11
                self.hufflepuff += 11
                self.slytherin += 28
            elif answer.lower().strip() == "e":
                self.gryffindor += 9
                self.ravenclaw += 9
                self.hufflepuff += 27
                self.slytherin += 10
            elif answer.lower().strip() == "f":
                self.gryffindor += 24
                self.ravenclaw += 13
                self.hufflepuff += 11
                self.slytherin += 9
            else:
                self.gryffindor += 11
                self.ravenclaw += 27
                self.hufflepuff += 11
                self.slytherin += 10
        elif flag == 3:
            ans_bank = ["centaurs", "goblins", "merpeople", "ghosts", "vampires", "werewolves", "trolls"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nWhich of the following would you most like to study? \n")
                answer = input("Centaurs\n" +
                               "Goblins\n" +
                               "Merpeople\n" +
                               "Ghosts\n" +
                               "Vampires\n" +
                               "Werewolves\n" +
                               "Trolls\n")
                count += 1
            if answer.lower().strip() == "centaurs":
                self.gryffindor += 20
                self.ravenclaw += 19
                self.hufflepuff += 8
                self.slytherin += 8
            elif answer.lower().strip() == "goblins":
                self.gryffindor += 10
                self.ravenclaw += 23
                self.hufflepuff += 9
                self.slytherin += 16
            elif answer.lower().strip() == "merpeople":
                self.gryffindor += 9
                self.ravenclaw += 8
                self.hufflepuff += 20
                self.slytherin += 20
            elif answer.lower().strip() == "ghosts":
                self.gryffindor += 24
                self.ravenclaw += 23
                self.hufflepuff += 8
                self.slytherin += 6
            elif answer.lower().strip() == "vampires":
                self.gryffindor += 9
                self.ravenclaw += 12
                self.hufflepuff += 12
                self.slytherin += 26
            elif answer.lower().strip() == "werewolves":
                self.gryffindor += 22
                self.ravenclaw += 8
                self.hufflepuff += 20
                self.slytherin += 6
            else:
                self.gryffindor += 6
                self.ravenclaw += 8
                self.hufflepuff += 22
                self.slytherin += 19

    def set6(self):
        flag = rand.randint(1, 6)
        answer = ""
        count = 0
        if flag == 1:
            ans_bank = ["a", "b", "c", "d"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nYou and two friends need to cross a bridge guarded by a river troll \n"
                      "who insists on fighting one of you before he will let all of you pass. Do you:\n")
                answer = input(
                    "A- Attempt to confuse the troll into letting all three of you pass without fighting? \n" +
                    "B- Suggest drawing lots to decide which of you will fight?	 \n " +
                    "C- Suggest that all three of you should fight (without telling the troll)?	 \n " +
                    "D- Volunteer to fight?	 \n")
                count += 1
            if answer.lower().strip() == "a":
                self.gryffindor += 20
                self.ravenclaw += 44
                self.hufflepuff += 18
                self.slytherin += 23
            elif answer.lower().strip() == "b":
                self.gryffindor += 16
                self.ravenclaw += 17
                self.hufflepuff += 47
                self.slytherin += 17
            elif answer.lower().strip() == "c":
                self.gryffindor += 18
                self.ravenclaw += 19
                self.hufflepuff += 16
                self.slytherin += 42
            else:
                self.gryffindor += 46
                self.ravenclaw += 19
                self.hufflepuff += 19
                self.slytherin += 18
        elif flag == 2:
            ans_bank = ["a", "b", "c", "d"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nOne of your house mates has cheated in a Hogwarts exam by using a Self-Spelling Quill.\n" +
                      " Now he has come top of the class in Charms, beating you into second place.\n" +
                      " Professor Flitwick is suspicious of what happened. \n" +
                      "He draws you to one side after his lesson and asks you whether or not \n" +
                      "your classmate used a forbidden quill. \n" +
                      "What do you do?\n")
                answer = input(
                    "A- Lie and say you don’t know \n" +
                    " (but hope that somebody else tells Professor Flitwick the truth).\n" +
                    "B- Tell Professor Flitwick that he ought to ask your classmate\n" +
                    " (and resolve to tell your classmate that if he doesn’t tell the truth, you will). \n " +
                    "C- Tell Professor Flitwick the truth. \n" +
                    " If your classmate is prepared to win by cheating, he deserves to be found out. \n" +
                    " Also, as you are both in the same house, any points he loses will be regained by you, \n" +
                    " for coming first in his place. \n " +
                    "D- You would not wait to be asked to tell Professor Flitwick the truth.\n" +
                    " If you knew that somebody was using a forbidden quill, \n" +
                    " you would tell the teacher before the exam started.\n")
                count += 1
            if answer.lower().strip() == "a":
                self.gryffindor += 17
                self.ravenclaw += 14
                self.hufflepuff += 43
                self.slytherin += 18
            elif answer.lower().strip() == "b":
                self.gryffindor += 43
                self.ravenclaw += 16
                self.hufflepuff += 22
                self.slytherin += 14
            elif answer.lower().strip() == "c":
                self.gryffindor += 22
                self.ravenclaw += 45
                self.hufflepuff += 16
                self.slytherin += 19
            else:
                self.gryffindor += 18
                self.ravenclaw += 25
                self.hufflepuff += 19
                self.slytherin += 49
        elif flag == 3:
            ans_bank = ["a", "b", "c", "d"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nA Muggle confronts you and says that they are sure you are a witch or wizard. Do you:\n")
                answer = input("A- Ask what makes them think so? \n" +
                               "B- Agree, and ask whether they’d like a free sample of a jinx? \n " +
                               "C- Agree, and walk away, leaving them to wonder whether you are bluffing? \n " +
                               "D- Tell them that you are worried about their mental health, \n" +
                               "and offer to call a doctor. \n")
                count += 1
            if answer.lower().strip() == "a":
                self.gryffindor += 17
                self.ravenclaw += 45
                self.hufflepuff += 20
                self.slytherin += 17
            elif answer.lower().strip() == "b":
                self.gryffindor += 21
                self.ravenclaw += 17
                self.hufflepuff += 20
                self.slytherin += 41
            elif answer.lower().strip() == "c":
                self.gryffindor += 47
                self.ravenclaw += 21
                self.hufflepuff += 15
                self.slytherin += 23
            else:
                self.gryffindor += 16
                self.ravenclaw += 17
                self.hufflepuff += 45
                self.slytherin += 20
        elif flag == 4:
            ans_bank = ["a", "b", "c", "d"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nWhich nightmare would frighten you most?\n")
                answer = input("A- Standing on top of something very high and realizing suddenly that\n" +
                               " there are no hand- or footholds, nor any barrier to stop you falling.	 \n" +
                               "B- An eye at the keyhole of the dark, windowless room in which you are locked.	 \n " +
                               "C- Waking up to find that neither your friends \n" +
                               " nor your family have any idea who you are.	 \n " +
                               "D- Being forced to speak in such a silly voice that\n" +
                               " hardly anyone can understand you, and everyone laughs at you.	\n")
                count += 1
            if answer.lower().strip() == "a":
                self.gryffindor += 20
                self.ravenclaw += 46
                self.hufflepuff += 18
                self.slytherin += 20
            elif answer.lower().strip() == "b":
                self.gryffindor += 45
                self.ravenclaw += 18
                self.hufflepuff += 17
                self.slytherin += 18
            elif answer.lower().strip() == "c":
                self.gryffindor += 17
                self.ravenclaw += 15
                self.hufflepuff += 45
                self.slytherin += 15
            else:
                self.gryffindor += 18
                self.ravenclaw += 21
                self.hufflepuff += 20
                self.slytherin += 47
        elif flag == 5:
            ans_bank = ["a", "b", "c", "d"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nWhich road tempts you most?\n")
                answer = input("A- The wide, sunny, grassy lane	 \n" +
                               "B- The narrow, dark, lantern-lit alley	\n " +
                               "C- The twisting, leaf-strewn path through woods	 \n " +
                               "D- The cobbled street lined with ancient buildings	\n")
                count += 1
            if answer.lower().strip() == "a":
                self.gryffindor += 18
                self.ravenclaw += 14
                self.hufflepuff += 41
                self.slytherin += 18
            elif answer.lower().strip() == "b":
                self.gryffindor += 19
                self.ravenclaw += 20
                self.hufflepuff += 17
                self.slytherin += 44
            elif answer.lower().strip() == "c":
                self.gryffindor += 44
                self.ravenclaw += 22
                self.hufflepuff += 19
                self.slytherin += 23
            else:
                self.gryffindor += 19
                self.ravenclaw += 43
                self.hufflepuff += 23
                self.slytherin += 14
        elif flag == 6:
            ans_bank = ["a", "b", "c", "d"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                print("\nLate at night, walking alone down the street, you hear a peculiar cry\n"
                      " that you believe to have a magical source. Do you:\n")
                answer = input("A- Proceed with caution,\n" +
                               " keeping one hand on your concealed wand and an eye out for any disturbance?		 \n" +
                               "B- Draw your wand and try to discover the source of the noise?	\n " +
                               "C- Draw your wand and stand your ground? \n " +
                               "D- Withdraw into the shadows to await developments,\n"
                               " while mentally reviewing the most appropriate defensive and offensive spells,\n"
                               " should trouble occur?\n")
                count += 1
            if answer.lower().strip() == "a":
                self.gryffindor += 19
                self.ravenclaw += 17
                self.hufflepuff += 43
                self.slytherin += 21
            elif answer.lower().strip() == "b":
                self.gryffindor += 45
                self.ravenclaw += 21
                self.hufflepuff += 17
                self.slytherin += 19
            elif answer.lower().strip() == "c":
                self.gryffindor += 17
                self.ravenclaw += 19
                self.hufflepuff += 19
                self.slytherin += 42
            else:
                self.gryffindor += 19
                self.ravenclaw += 44
                self.hufflepuff += 21
                self.slytherin += 19

    def set7(self):
        answer = ""
        count = 0

        ans_bank = ["tabby cat", "siamese cat", "ginger cat", "black cat", "white cat",
                    "tawny owl", "screech owl", "brown owl", "snowy owl", "barn owl",
                    "common toad", "natterjack toad", "dragon toad", "harlequin toad", "three toed tree toad"]
        while answer.lower().strip() not in ans_bank:
            if count > 0:
                print("I didn't quite understand that")
            print("\nWhile you are attending Hogwarts, which pet would you choose to take with you? \n")
            answer = input("Tabby cat\n" +
                           "Siamese cat\n" +
                           "Ginger cat\n" +
                           "Black cat\n" +
                           "White cat\n" +
                           "Tawny owl\n" +
                           "Screech owl\n" +
                           "Brown owl\n" +
                           "Snowy owl\n" +
                           "Barn owl\n" +
                           "Commmon toad\n" +
                           "Natterjack toad\n" +
                           "Dragon toad\n" +
                           "Harlequin toad\n" +
                           "Three toed tree toad\n")
            count += 1
        if answer.lower().strip() == "tabby cat":
            self.gryffindor += 9
            self.ravenclaw += 5
            self.hufflepuff += 4
            self.slytherin += 8
        elif answer.lower().strip() == "siamese cat":
            self.gryffindor += 7
            self.ravenclaw += 5
            self.hufflepuff += 5
            self.slytherin += 12
        elif answer.lower().strip() == "ginger cat":
            self.gryffindor += 8
            self.ravenclaw += 5
            self.hufflepuff += 5
            self.slytherin += 11
        elif answer.lower().strip() == "black cat":
            self.gryffindor += 6
            self.ravenclaw += 5
            self.hufflepuff += 5
            self.slytherin += 11
        elif answer.lower().strip() == "white cat":
            self.gryffindor += 6
            self.ravenclaw += 5
            self.hufflepuff += 5
            self.slytherin += 10
        elif answer.lower().strip() == "tawny owl":
            self.gryffindor += 6
            self.ravenclaw += 11
            self.hufflepuff += 5
            self.slytherin += 4
        elif answer.lower().strip() == "screech owl":
            self.gryffindor += 7
            self.ravenclaw += 9
            self.hufflepuff += 4
            self.slytherin += 4
        elif answer.lower().strip() == "brown owl":
            self.gryffindor += 7
            self.ravenclaw += 11
            self.hufflepuff += 5
            self.slytherin += 5
        elif answer.lower().strip() == "snowy owl":
            self.gryffindor += 5
            self.ravenclaw += 7
            self.hufflepuff += 8
            self.slytherin += 5
        elif answer.lower().strip() == "barn owl":
            self.gryffindor += 6
            self.ravenclaw += 11
            self.hufflepuff += 5
            self.slytherin += 5
        elif answer.lower().strip() == "common toad":
            self.gryffindor += 7
            self.ravenclaw += 4
            self.hufflepuff += 12
            self.slytherin += 4
        elif answer.lower().strip() == "natterjack toad":
            self.gryffindor += 6
            self.ravenclaw += 5
            self.hufflepuff += 11
            self.slytherin += 4
        elif answer.lower().strip() == "dragon toad":
            self.gryffindor += 9
            self.ravenclaw += 5
            self.hufflepuff += 7
            self.slytherin += 5
        elif answer.lower().strip() == "harlequin toad":
            self.gryffindor += 6
            self.ravenclaw += 4
            self.hufflepuff += 11
            self.slytherin += 5
        else:
            self.gryffindor += 6
            self.ravenclaw += 7
            self.hufflepuff += 9
            self.slytherin += 5

    def last_question(self):
        # random number generator to choose out of 3 possible questions:
        flag = rand.randint(1, 3)
        answer = ""
        count = 0
        if flag == 1:
            ans_bank = ["black", "white"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                answer = input("\nBlack or White?\n")
                count += 1
            if answer.lower().strip() == "black":
                self.gryffindor += 73
                self.ravenclaw += 29
                self.hufflepuff += 24
                self.slytherin += 72
            else:
                self.gryffindor += 27
                self.ravenclaw += 71
                self.hufflepuff += 76
                self.slytherin += 28

        elif flag == 2:
            ans_bank = ["heads", "tails", "head", "tail"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                answer = input("\nHeads or Tails?\n")
                count += 1
            if answer.lower().strip() in ["heads", "head"]:
                self.gryffindor += 27
                self.ravenclaw += 69
                self.hufflepuff += 74
                self.slytherin += 27
            else:
                self.gryffindor += 73
                self.ravenclaw += 31
                self.hufflepuff += 26
                self.slytherin += 73
        else:
            ans_bank = ["left", "right"]
            while answer.lower().strip() not in ans_bank:
                if count > 0:
                    print("I didn't quite understand that")
                answer = input("Left or Right?")
                count += 1
            if answer.lower().strip() == "left":
                self.gryffindor += 29
                self.ravenclaw += 70
                self.hufflepuff += 29
                self.slytherin += 73
            else:
                self.gryffindor += 71
                self.ravenclaw += 30
                self.hufflepuff += 71
                self.slytherin += 27

    def process_results(self):
        total_points = self.gryffindor + self.ravenclaw + self.hufflepuff + self.slytherin
        points_dict = {self.slytherin: "SLYTHERINNNNN", self.hufflepuff: "HUFFLEPUFFFFF",
                       self.ravenclaw: "RAVENCLAWWWWWW", self.gryffindor: "GRYFFINDORRRRR"}
        max_point = max(self.gryffindor, self.ravenclaw, self.hufflepuff, self.slytherin)
        print("Hmm... very interesting....")
        time.sleep(3)
        print("Better be.....")
        time.sleep(1.5)
        print(points_dict[max_point])
        time.sleep(1.5)
        ans = input("\nWould you like to see your compatibility across each house?\n Y/N")
        if ans.lower().strip() == "y":
            print("Gryffindor: ",
                  Decimal((self.gryffindor / total_points) * 100).quantize(Decimal('.01'), rounding=ROUND_DOWN), "%")
            print("Ravenclaw: ",
                  Decimal((self.ravenclaw / total_points) * 100).quantize(Decimal('.01'), rounding=ROUND_DOWN), "%")
            print("Hufflepuff: ",
                  Decimal((self.hufflepuff / total_points) * 100).quantize(Decimal('.01'), rounding=ROUND_DOWN), "%")
            print("Slytherin: ",
                  Decimal((self.slytherin / total_points) * 100).quantize(Decimal('.01'), rounding=ROUND_DOWN), "%")
        time.sleep(1.5)
        print("\nRun along to your house now and enjoy your time at Hogwarts!")
        exit(1)


sorter = sorting_hat()
