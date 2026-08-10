import random

def welcome():
    print("="*30)
    print("WELCOME TO  THE PYTHON ADVENTURE RPG")
    print("="*30)

    name=input("Enter your name:")
    return name



def choose_character(player_name):
    print("\n Choose your character")
    print("1.Knight")
    print("2.Archer")
    print("3.Mage")

    choice=int(input("Enter your choice:"))

    if choice==1:
        player={"name":player_name,
         "class":"Knight",
         "health":120,
         "attack":20,
         "gold":50,
         "xp":0,
         "level":1
         }

    elif choice==2:
        player = {
            "name": player_name,
            "class": "Archer",
            "health": 100,
            "attack": 25,
            "gold": 50,
            "xp": 0,
            "level": 1
        }

    else:
        player = {
            "name": player_name,
            "class": "Mage",
            "health": 80,
            "attack": 35,
            "gold": 50,
            "xp": 0,
            "level": 1
        }

    return player




def show_stats(player):
    print("\n=============PLAYER STATS=============")
    print("Name:",player["name"])
    print("Class:",player["class"])
    print("Health:",player["health"])
    print("Attack:",player["attack"])
    print("Gold:",player["gold"])
    print("XP: ",player["xp"])
    print("Level:",player["level"])
    print("=======================================")


def main_menu(player):
    while True:
        print("\n========MAIN MENU========")
        ch=int(input("Enter your choice\n 1.Explore\n 2.View stats\n 3.Exit"))
        if ch==1:
            explore(player)
        elif ch==2:
            show_stats(player)
        elif ch==3:
            game_over(player)
            break
        else:
            print("Invalid choice!")


def explore(player):
    print("\n=====You Start Exploring=====")
    event=random.randint(1,3)
    if event==1:
        print("An enemy appeared")
        enemy=create_enemy()
        battle(player,enemy)
    elif event==2:
        gold=random.randint(10,30)
        print("YOU FOUND A TRESURE CHEST")
        print("gold found",gold)

        player["gold"]+=gold
    else:
        print("NOTHING HAPPENED")

def create_enemy():
    enemy_choice =random.randint(1,3)
    if enemy_choice==1:
        goblin={
            "name":"Goblin",
            "health":50,
            "attack":10,
            "gold":20,
            "xp":10
        }
        return goblin
    elif enemy_choice==2:

        dragon={
            "name":"dragon",
            "health":200,
            "attack":35,
            "gold":100,
            "xp":50
        }
        return dragon
    else:

        skeleton={
            "name":"skeleton",
            "health":100,
            "attack":20,
            "gold":40,
            "xp":25
        }
        return skeleton
        


def battle(player,enemy):
        while player["health"]>0 and enemy["health"]>0:
            print("\n=====BATTLE=====")
            print("Enemy:",enemy["name"])
            print("Your Health:",player["health"])
            print("Enemy Health:",enemy["health"])
            
            ch=int(input("Enter your choice:\n 1.Attack\n 2.Run\n"))
            if ch==1:
                enemy["health"]-=player["attack"]
                print(f"you attacked the{enemy['name']}:")
                print(f"{enemy['name']} lost {player['attack']} health")
                if enemy['health']<=0:
                   print(f"You defeated the {enemy['name']}!")
                   player["gold"]+=enemy["gold"]
                   player["xp"]+=enemy["xp"]
                   print(f"You earned {enemy['gold']} gold!")
                   print(f"You earner{enemy['xp']} XP!")

                   print("\n*****LEVEL UP*****")
                   print("Level:",player["level"])
                   print("Attack:",player["attack"])
                   print("Health:",player["health"])

                   break
                   

            
                player["health"]-=enemy["attack"]
                print(f"{enemy['name']} attacked you")
                print(f"you lost {enemy['attack']} health")
                if player['health']<=0:
                    game_over(player)
                    break

            elif ch==2:
                print("You ran away!")
                break
            
            else:
                print("Invalid Choice")





def game_over(player):
    print("\n========== GAME OVER ==========")
    print("Player Name :", player["name"])
    print("Class       :", player["class"])
    print("Level       :", player["level"])
    print("XP          :", player["xp"])
    print("Gold        :", player["gold"])
    print("Thank you for playing!")
    print("===============================")


def main():
    print("\n========PYTHON RPG GAME========")
    player_name = welcome()
    player = choose_character(player_name)
    main_menu(player)



main()