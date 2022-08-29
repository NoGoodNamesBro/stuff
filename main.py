inventory = {
    "gold":1,
    "sliver":13,
}
GOBLIN_HIT = False
sword = False
ALIVE = True

def print_inv():
    for k,v in inventory.items():
        print("{}: {}".format(k,v))
        
        
def print_output(decision):
    choice = 'i'
    while choice =='i':
        choice = input("{} [y/n] \nEnter i to see inventory".format(decision)).lower()
        if choice =="i":
            print_inv()
    if choice in ["y","yes"]:
        return True
    return False

def battle(sword):
    global ALIVE
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("  Fighting...")
    print("  If the goblin hits higher then you, you will die")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if sword:
        my_hit = random.randint(3,10)
    else:
        my_hit = random.randint(1,5)
        
    GOBLIN_HIT = random.randint(1,5)
    print("YOU HIT FOR {} DAMAGE".format(my_hit))
    print("GOBLIN FOR {} DAMAGE".format(GOBLIN_HIT))
    if my_hit > 5:
        print("YOU WIN THE BATTLE")
    elif my_hit < 6:
        if GOBLIN_HIT > my_hit:
            print("YOU LOSE")
            ALIVE = False
        elif my_hit == GOBLIN_HIT:
            print("YOU ESCAPE")
        elif my_hit > GOBLIN_HIT:
            print("YOU WIN")
       

def game():
    global inventory
    global sword
    global ALIVE
    print("~~~~~~~~~~~~~~~")
    print("WELCOME TO THE ADVENTURE")
    print("~~~~~~~~~~~~~~~")
    stage.wait(3)
    print("YOU ENTER A CAVE AND YOU SEE A SWORD ON THE GROUND")
    if print_output("PICK IT UP?"):
        rand = random.randint(1,100)
        if rand < 0:
            print("YOU PICKED IT UP")
            inventory["RUSTY SWORD"] = 1
        else:
            print("THERE WAS A DEADLY BUG PROTECTING THE SWORD")
            stage.wait(3)
            print("IT BIT YOU AND YOU DIED")
            quit()
    else:
        print("YOU LEAVE THE RUSTY SWORD")
        
    stage.wait(3)
    print("YOU SEE A SHINY OBJECT")
    if print_output("GO TOWARD IT?"):
        print("IT TURNS OUT TO BE A GOBLIN WITH A GOLD BELT BUCKLE")
    else:
        print("YOU STAY AWAY FROM THE OBJECT BUT THE OBJECT GOES TO YOU")
        
    if print_output("DO YOU ATTACK?"):
        if "RUSTY SWORD" in list(inventory.keys()):
            print("YOU LUNGE TOWARD THE GOBLIN")
            battle(sword)
            
        else:
            print("YOU ATTACK WITH NO WEAPON")
    else:
        print("YOU TRY TO AVOD IT BUT IT SHOOTS AN ARROW AT YOU")
        print("YOU DIED")
        ALIVE = False

def game2():
    global inventory
    global sword
    global ALIVE
    print("NEXT CHAPTER")
    print("YOU EXIT THE CAVE")
    stage.wait(3)
    print("YOU HEAD HOME AND SEE THAT THE ROYAL GUARD IS AT SOMEONE'S DOOR STEP")
    stage.wait(3)
    if print_output("DO YOU TALK TO THE GUARDS?"):
        print("THEY SAY FOR WINDING UP IN THE KING'S BUSSNESS THEY WILL KILL YOU AND YOU DIE")
        ALIVE = False
    

def main():
    global ALIVE
    while ALIVE:
        game()
        game2()
    print("***THE END***")

main()



