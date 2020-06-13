import random
import time
import os

Clear = lambda: os.system("cls")
competitor_list = ["Rahma Erickson",
                   "Aran Matthews",
                   "Aiysha Pierce",
                   "Nikita Sanchez",
                   "Faisal Hook",
                   "Presley England",
                   "Calvin Pitt",
                   "Aubrey Lees",
                   "Kayson North",
                   "Evie Clay",
                   "Benedict Hills",
                   "Nina Morgan",
                   "Iylah Ramirez",
                   "Amman Bradford",
                   "Anna Chung",
                   "Byron Oconnor",
                   "Elsie-Mae Huber",
                   "Manraj Wilcox",
                   "Keira Cano",
                   "Carmel Burrows",
                   "Hebe Wilkes",
                   "Lilly-Grace Chen",
                   "Franklin Wills",
                   "Buddy Hodge",
                   "Anabelle Mcdougall",
                   "Alayah Stein",
                   "Tabatha Nieves",
                   "Yvette Holloway",
                   "Imaan Langley",
                   "Marley Allison",
                   "Franky James",
                   "Ebonie Bailey",
                   "Sammy Curry",
                   "Eilidh Serrano",
                   "Herman Hancock",
                   "Charleigh Penn",
                   "Thomas Foster",
                   "Kyla Rice",
                   "Tianna Herman",
                   "Wanda Mccaffrey",
                   "Danyaal Browning",
                   "Jayden Pollard",
                   "Yusha Anthony",
                   "Gerald Brock",
                   "Lennon Draper",
                   "Jaime Seymour",
                   "Akbar Yu",
                   "Kester Drummond",
                   "Vicky Crossley",
                   "Osian Sykes",
                   "Finnlay Mackay",
                   "Sherry Leech",
                   "Kanye Suarez",
                   "Sila Rosales",
                   "Nazia Gilmore",
                   "Aditi Swift",
                   "Aayush Massey",
                   "Sidney Terry",
                   "Eoin West",
                   "Zander Jimenez",
                   "Daisy-Mae Cotton",
                   "Romeo Richmond",
                   "Della Carr",
                   "Brenna Kirby",
                   "Vera Short",
                   "Dario Person",
                   "Briana Pace",
                   "Gina Cline",
                   "Hussain Knights",
                   "Amelia-Mae Rhodes",
                   "Jayda Busby",
                   "Aadam Hamilton",
                   "Ilyas Ireland",
                   "Dina Hunter",
                   "Aiesha Nicholls",
                   "Ridwan Trevino",
                   "Huw Schmidt",
                   "Zachery Millington",
                   "Tracy Hirst",
                   "Elly Mccarthy",
                   "Dawn Vickers",
                   "Lexi-May Hewitt",
                   "Janet Hogan",
                   "Kenzie Harrison",
                   "Jayne Redmond",
                   "Hibba Johnston",
                   "Archie Rossi",
                   "Ritik Daugherty",
                   "Rhiana Rooney",
                   "Fatma Beard",
                   "Allen Potts",
                   "Jaydn Kirkpatrick",
                   "Jamie-Leigh Clarkson",
                   "Caspar Hobbs",
                   "Greg Gallagher",
                   "Arwa Mcknight",
                   "Imaani Haney",
                   "Fynley Rosario",
                   "Bear French",
                   "Pooja Kaur"]

runners = []
Stage1Obs = {"1.1": ["Quad Steps", "Tweleve Timbers", "S Run", "Hill Climb"],
             "1.2": ["Giant Cycle", "Rolling Log", "Giant Swing", "Cargo Gate"],
             "1.3": ["Rope Glider", "Music Box", "Quad Poles"],
             "1.4": ["Jumping Spider", "Bouncing Spider", "Jump Hang", "Lightning Bolts"],
             "1.5": ["Half Pipe Attack", "Sonic Curve", "Coin Flip", "Curved Bungee Bridge"],
             "1.6": ["Warped Wall", "Mega Wall", "Great Wall", "Crooked Wall"],
             "1.7": ["Spinning Bridge", "Broken Bridge", "Flying Chute", "Fishbone"],
             "1.8": ["LumberJack Climb", "Spider Climb", "Jumping Bars to Victory"]}

Stage2Obs = {"2.1": ["DownHill Jump", "Stick Slider", "Slider Drop", "Rope Maze"],
             "2.2": ["Salmon Ladder", "Double Salmon Ladder", "Swap Salmon Ladder", "Up Down Salmon Ladder"],
             "2.3": ["Unstable Bridge", "Wave Runner", "Seperated Bridge", "Deja Vu"],
             "2.4": ["Balance Tank", "Butterfly Wall", "Swing Surfer", "Conveyor Belt"],
             "2.5": ["Metal Spin", "Wing Nut Alley", "Roulette Row", "Double Metal Spin"],
             "2.6": ["Wall Life", "Water Walls", "Rotating Walls", "Triple Brick Climb"]}

Stage3Obs = {"3.1": ["Rumbling Dice", "Roulette Cylinder", "Peg Boards", "Drum Hopper"],
             "3.2": ["DoorKnob Grasper", "DoorKnob Arch", "Ring Toss", "KeyLock Hang"],
             "3.3": ["Floating Boards", "Jumping Bar", "Globe Grasper", "Devil Steps"],
             "3.4": ["Ultimate Cliffhanger", "Devils Cliffside", "Crazy Cliffhanger", "Shin Cliffhanger"],
             "3.5": ["Broken Heart", "Rope Grasper", "Curved Body Prop", "Pole Grasper"],
             "3.6": ["Hang Climb", "Vertical Limit", "Area 51", "Peg Cloud"],
             "3.7": ["Spider Flip", "Time Bomb", "Pipe Slider", "Devil Swing"],
             "3.8": ["Pipe Slider", "Flying Bars", "Gliding Ring", "Flying Ring"]}

Stage4Obs = {"4.1": ["Spider Climb", "Brick Climb", "Salmon ladder", "G-Rope"],
             "4.2": ["Salmon Ladder", "G-Rope", "Net Climb", "LumberJack Climb"],
             "4.3": ["G-Rope"]}
Cleared = []
MovingOn = []
Failed = []

print("How many runners? (1-100)")
amount_of_people = input()
int_amount = int(amount_of_people)

if int_amount > 100:
    print("Too many")

elif int_amount < 1:
    print("Too low")

else:
    for _ in range(int_amount):
        new_competitor = random.choice(competitor_list)
        competitor_list.remove(new_competitor)
        runners.append(new_competitor)

    Current1dot1 = random.choice(Stage1Obs["1.1"])
    Current1dot2 = random.choice(Stage1Obs["1.2"])
    Current1dot3 = random.choice(Stage1Obs["1.3"])
    Current1dot4 = random.choice(Stage1Obs["1.4"])
    Current1dot5 = random.choice(Stage1Obs["1.5"])
    Current1dot6 = random.choice(Stage1Obs["1.6"])
    Current1dot7 = random.choice(Stage1Obs["1.7"])
    Current1dot8 = random.choice(Stage1Obs["1.8"])

    Current2dot1 = random.choice(Stage2Obs["2.1"])
    Current2dot2 = random.choice(Stage2Obs["2.2"])
    Current2dot3 = random.choice(Stage2Obs["2.3"])
    Current2dot4 = random.choice(Stage2Obs["2.4"])
    Current2dot5 = random.choice(Stage2Obs["2.5"])
    Current2dot6 = random.choice(Stage2Obs["2.6"])

    Current3dot1 = random.choice(Stage3Obs["3.1"])
    Current3dot2 = random.choice(Stage3Obs["3.2"])
    Current3dot3 = random.choice(Stage3Obs["3.3"])
    Current3dot4 = random.choice(Stage3Obs["3.4"])
    Current3dot5 = random.choice(Stage3Obs["3.5"])
    Current3dot6 = random.choice(Stage3Obs["3.6"])
    Current3dot7 = random.choice(Stage3Obs["3.7"])
    Current3dot8 = random.choice(Stage3Obs["3.8"])

    Current4dot1 = random.choice(Stage4Obs["4.1"])
    Current4dot2 = random.choice(Stage4Obs["4.2"])
    Current4dot3 = random.choice(Stage4Obs["4.3"])
    print(runners)

    input("Press Enter to Continue")
    Clear()

    for _ in runners:
        Current_Runner = random.choice(runners)

        Fail = random.randint(1, 10)

        if Fail == 1:
            TimeUp = random.randint(1, 80)
            if TimeUp == 80:
                Run = f"{Current_Runner} timed up on {Current1dot1}"
                Failed.append(Run)
            else:
                Run = f"{Current_Runner} failed {Current1dot1}"
                Failed.append(Run)
        else:

            Fail = random.randint(1, 9)

            if Fail == 1:
                TimeUp = random.randint(1, 70)
                if TimeUp == 70:
                    Run = f"{Current_Runner} timed up on {Current1dot2}"
                    Failed.append(Run)
                else:
                    Run = f"{Current_Runner} failed {Current1dot2}"
                    Failed.append(Run)
            else:

                Fail = random.randint(1, 8)

                if Fail == 1:
                    TimeUp = random.randint(1, 60)
                    if TimeUp == 60:
                        Run = f"{Current_Runner} timed up on {Current1dot3}"
                        Failed.append(Run)
                    else:
                        Run = f"{Current_Runner} failed {Current1dot3}"
                        Failed.append(Run)
                else:

                    Fail = random.randint(1, 7)

                    if Fail == 1:
                        TimeUp = random.randint(1, 50)
                        if TimeUp == 50:
                            Run = f"{Current_Runner} timed up on {Current1dot4}"
                            Failed.append(Run)
                        else:
                            Run = f"{Current_Runner} failed {Current1dot4}"
                            Failed.append(Run)
                    else:

                        Fail = random.randint(1, 6)

                        if Fail == 1:
                            TimeUp = random.randint(1, 40)
                            if TimeUp == 40:
                                Run = f"{Current_Runner} timed up on {Current1dot5}"
                                Failed.append(Run)
                            else:
                                Run = f"{Current_Runner} failed {Current1dot5}"
                                Failed.append(Run)
                        else:

                            Fail = random.randint(1, 5)

                            if Fail == 1:
                                TimeUp = random.randint(1, 30)
                                if TimeUp == 30:
                                    Run = f"{Current_Runner} timed up on {Current1dot6}"
                                    Failed.append(Run)
                                else:
                                    Run = f"{Current_Runner} failed {Current1dot6}"
                                    Failed.append(Run)
                            else:

                                Fail = random.randint(1, 4)

                                if Fail == 1:
                                    TimeUp = random.randint(1, 20)
                                    if TimeUp == 20:
                                        Run = f"{Current_Runner} timed up on {Current1dot7}"
                                        Failed.append(Run)
                                    else:
                                        Run = f"{Current_Runner} failed {Current1dot7}"
                                        Failed.append(Run)
                                else:

                                    Fail = random.randint(1, 3)

                                    if Fail == 1:
                                        TimeUp = random.randint(1, 10)
                                        if TimeUp == 20:
                                            Run = f"{Current_Runner} timed up on {Current1dot8}"
                                            Failed.append(Run)
                                        else:
                                            Run = f"{Current_Runner} failed {Current1dot8}"
                                            Failed.append(Run)
                                    else:
                                        Run = f"{Current_Runner} Cleared Stage 1"
                                        Cleared.append(Run)
                                        MovingOn.append(Current_Runner)

    print("These People Cleared Stage 1")
    print(", ".join(MovingOn))
    print()
    print("These People Failed")
    print(", ".join(Failed))
    print()
    print(MovingOn)
    runners.clear()
    input("Press Enter to Continue")
    Clear()
    Cleared.clear()
    Failed.clear()

    for _ in MovingOn:
        Current_Runner = random.choice(MovingOn)
        runners.append(Current_Runner)
    MovingOn.clear()
    for _ in runners:

        Current_Runner = random.choice(runners)

        Fail = random.randint(1, 8)

        if Fail == 1:
            TimeUp = random.randint(1, 60)
            if TimeUp == 60:
                Run = f"{Current_Runner} timed up on {Current2dot1}"
                Failed.append(Run)
            else:
                Run = f"{Current_Runner} failed {Current2dot1}"
                Failed.append(Run)
        else:

            Fail = random.randint(1, 7)

            if Fail == 1:
                TimeUp = random.randint(1, 50)
                if TimeUp == 50:
                    Run = f"{Current_Runner} timed up on {Current2dot2}"
                    Failed.append(Run)
                else:
                    Run = f"{Current_Runner} failed {Current2dot2}"
                    Failed.append(Run)
            else:

                Fail = random.randint(1, 6)

                if Fail == 1:
                    TimeUp = random.randint(1, 40)
                    if TimeUp == 40:
                        Run = f"{Current_Runner} timed up on {Current2dot3}"
                        Failed.append(Run)
                    else:
                        Run = f"{Current_Runner} failed {Current2dot3}"
                        Failed.append(Run)
                else:
                    Fail = random.randint(1, 5)

                    if Fail == 1:
                        TimeUp = random.randint(1, 30)
                        if TimeUp == 30:
                            Run = f"{Current_Runner} timed up on {Current2dot4}"
                            Failed.append(Run)
                        else:
                            Run = f"{Current_Runner} failed {Current2dot4}"
                            Failed.append(Run)
                    else:

                        Fail = random.randint(1, 4)

                        if Fail == 1:
                            TimeUp = random.randint(1, 20)
                            if TimeUp == 20:
                                Run = f"{Current_Runner} timed up on {Current2dot5}"
                                Failed.append(Run)
                            else:
                                Run = f"{Current_Runner} failed {Current2dot5}"
                                Failed.append(Run)
                        else:

                            Fail = random.randint(1, 3)

                            if Fail == 1:
                                TimeUp = random.randint(1, 10)
                                if TimeUp == 10:
                                    Run = f"{Current_Runner} timed up on {Current2dot6}"
                                    Failed.append(Run)
                                else:
                                    Run = f"{Current_Runner} failed {Current2dot6}"
                                    Failed.append(Run)
                            else:
                                Run = f"{Current_Runner} Cleared Stage 2"
                                Cleared.append(Run)
                                MovingOn.append(Current_Runner)
    print("These People Cleared Stage 2")
    print(", ".join(MovingOn))
    print()
    print("These People Failed")
    print(", ".join(Failed))
    print()
    print(MovingOn)
    runners.clear()
    input("Press Enter to Continue")
    Clear()
    Cleared.clear()
    Failed.clear()

    for _ in MovingOn:
        Current_Runner = random.choice(MovingOn)
        runners.append(Current_Runner)
    MovingOn.clear()
    for _ in runners:
        MovingOn.clear()

    for _ in runners:
        Current_Runner = random.choice(runners)

        Fail = random.randint(1, 10)

        if Fail == 1:
            Run = f"{Current_Runner} failed {Current3dot1}"
            Failed.append(Run)
        else:

            Fail = random.randint(1, 9)

            if Fail == 1:
                Run = f"{Current_Runner} failed {Current3dot2}"
                Failed.append(Run)
            else:

                Fail = random.randint(1, 8)

                if Fail == 1:
                    Run = f"{Current_Runner} failed {Current3dot3}"
                    Failed.append(Run)
                else:

                    Fail = random.randint(1, 7)

                    if Fail == 1:
                        Run = f"{Current_Runner} failed {Current3dot4}"
                        Failed.append(Run)
                    else:

                        Fail = random.randint(1, 6)

                        if Fail == 1:
                            Run = f"{Current_Runner} failed {Current3dot5}"
                            Failed.append(Run)
                        else:

                            Fail = random.randint(1, 5)

                            if Fail == 1:
                                Run = f"{Current_Runner} failed {Current3dot6}"
                                Failed.append(Run)
                            else:

                                Fail = random.randint(1, 4)

                                if Fail == 1:
                                    Run = f"{Current_Runner} failed {Current3dot7}"
                                    Failed.append(Run)
                                else:

                                    Fail = random.randint(1, 3)

                                    if Fail == 1:
                                        Run = f"{Current_Runner} failed {Current3dot8}"
                                        Failed.append(Run)

                                    else:
                                        Run = f"{Current_Runner} Cleared Stage 1"
                                        Cleared.append(Run)
                                        MovingOn.append(Current_Runner)
    print("These People Cleared Stage 3")
    print(", ".join(MovingOn))
    print()
    print("These People Failed")
    print(", ".join(Failed))
    print()
    print(MovingOn)
    runners.clear()
    input("Press Enter to Continue")
    Clear()
    Cleared.clear()
    Failed.clear()

    for _ in MovingOn:
        Current_Runner = random.choice(MovingOn)
        runners.append(Current_Runner)
    MovingOn.clear()

    for _ in runners:
        Current_Runner = random.choice(runners)

        Fail = random.randint(1, 3)

        if Fail == 1:
            Run = f"{Current_Runner} timed up on {Current4dot1}"
            Failed.append(Run)
        else:

            Fail = random.randint(1, 3)

            if Fail == 1:
                Run = f"{Current_Runner} Timed up on {Current4dot2}"
                Failed.append(Run)
            else:

                Fail = random.randint(1, 3)

                if Fail == 1:
                    Run = f"{Current_Runner} timed up on {Current4dot3}"
                    Failed.append(Run)
                else:
                    Run = f"{Current_Runner} Achieved Total Victory"
                    Cleared.append(Run)
                    MovingOn.append(Current_Runner)
    print("These People Achieved Total Victory")
    print(", ".join(MovingOn))
    print()
    print("These People Failed")
    print(", ".join(Failed))
    input("Press Enter to quit")