import random

characters = {"Alice in wonderland": "fantasy world", "Spider man": "strong", "Cinderella": "kind and generous",
              "Sponge bob": "positive and funny", "Maleficent": "sometimes cruel", "James bond": "charming and clever",
              "Harry potter": "magic mind person", "Bill gates": "tech savvy", "Albert Einstein": "good at physics",
              "Issac Newton": "alone and creative", "Leonardo da Vinci": "passionate painter and amazing creator",
              "Marco Polo": "interested in travelling", "Abraham Lincoln": "strategical person", }
print("\033[35mHello dear user!, welcome to match_character app:)\nby asking \033[1;0m 5 questions or less "
      "\033[36m we are going to find some characters that have something in common with you!\033[33m \nthis is just for fun, nothing more."
      "\n\033[1;32mhope you enjoy it:)")

x = []
random_choicer_pack = []

for i in range(5):
    random_choicer = random.choice(list(characters.values()))
    random_choicer_pack.append(random_choicer)

    if random_choicer_pack.count(random_choicer) >= 2:
        continue
        
    answer = input(f"\033[36mare you {random_choicer}? type yes or no")
    if answer == "yes":
        print(f"\033[35m Wow!so maybe you have something in common with \033[0;35m {list(characters.keys())[list(characters.values()).index(random_choicer)]}")
        print(f"\033[0m for more information, check it out here: https://en.wikipedia.org/wiki/{list(characters.keys())[list(characters.values()).index(random_choicer)]}")
        x.append(list(characters.keys())[list(characters.values()).index(random_choicer)])
        break

    else:
        print("\033[0m ok!give me another try!")
        continue

if len(x) == 0:
    print("\033[33m sorry! seems that our database is not enough for you"),
    inputer = input("\033[0m you can add your iconic character to our database.would you like to continue adding?(yes/no)")
    if inputer == "yes":
        i = input("your iconic character is:")
        i2 = input(f"and the bold personality in {i} is:")
        characters[i] = i2
        print("\033[32m Successfully done!")