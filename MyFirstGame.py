print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old.")

is_older = age >= 13
if age >= 13:
    print("You are old enough to play!")

    Wants_to_Play = input("Are you ready to play?").lower()
    if Wants_to_Play == "yes":
        print("Let's get started!")
        left_or_right = input("First choice... Left or Right (left/right)? ")

        if left_or_right == "right":
            ans = input("Bad choice. You have died of Dysentery on the Oregon Trail.")

        if left_or_right == "left":
            print("You have chosen wisely. You are now on the path to lost city of Atlantis... You come to a "
                  "river.")
            ans = input("Do you swim across or look for a bridge?(swim/bridge)? ")

            if ans == "swim":
                print("You are more brave than wise.. You nearly drowned and lost 5 health points but you made "
                      "it. "
                      "On the other side of the river you find two paths. One leading up the mountain or down into "
                      "the valley.")

                ans = input("Which do you choose(Up/straight)? ")

                if ans == "straight":
                    print("You walk through the valley and come within sight of the Golden Gates of Atlantis, "
                          "but are bitten by a snake. Game over.")

            if "up" == ans:
                print("You climb ladder until it ends on the edge of a cliff.")
                ans = input("Continue climbing freehand or turn back(climb/back)? ")

                if ans == "back":
                    print("Sometimes the path of least resistance is the most dangerous.. In your case it is at "
                          "least. You slip, fall and die...")

                if ans == "climb":
                    print("You risked everything on this journey. Your courage never wavered and you have reached "
                          "the Golden Gates. Welcome to Atlantis!")

            elif ans == "bridge":
                print("You walk upstream for some time, finding apples along the way. Plus 5 health gained as you "
                      "snack. You come to an old looking bridge")

                ans = input(
                    "Do you attempt to cross the decaying bridge or keep going upstream another?(cross/going)? ")

                if ans == "going":
                    print("You continue up the stream for days, eventually dying of exhaustion.")

                if ans == "cross":
                    print("Your bravery has not come without a cost. You dropped all your apples and lost 3 health "
                          "points crossing.")
                    ans = input("Do you continue with the stream or follow the jungle path?(stream/jungle)? ")

                    if ans == "stream":
                        print("You weren't brave enough to take on this adventure so your journey ends here.")

                    if ans == "jungle":
                        print("After walking through the dense jungle, fighting off bugs and vines you reach tall "
                              "golden gates. Your intelligence and perseverance were well worth the journey. Welcome "
                              "to Atlantis!")

    else:
        print("Get out of here then!")
else:
    print("You are not old enough to play...")

'''
string "Hello", 'Hi', "89" Things you want to print out
int  8, 7, -9, 100000. These are integer
float .89, 6.9, 4.8. integer with decimals
bool True or False statements. Uppercase is very important
'''
