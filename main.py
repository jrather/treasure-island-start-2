print('''
*******************************************************************************
              _
               //
              //
           __/(
       _.~-a  ~-.
      {_____)    `.           _..=~~~~=._
            ~-_    \      _.=~           '=.
               \    `._.=~            .=.   :=._
                -         __         (   \   : \)
                 ~.      (  }       (     |   : :
                   `:     \ \        \    |\   ; :
                     \     \ }        \   / |  ;  }
                      `-.__//__.==~~=._\ (_/  ;  ;
                          //           | |/  ;  ;
                         {{       _____|_/ ;   ;        *     ___
                          `      ---- _=.=`   ~ _____   ||*    ____
                                  __:='    .='     ___\\||/___
      "Parasaurolophus"       ..:~____.==''

*******************************************************************************
''')
print("Welcome to Dinosaur Island.")
print("Your mission is to find the legendary Indominus Rex and tame him!.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("The aging ferry pulls up to the dock and passengers disembark. You walk down the creaking, wooden pier and onto land. The silence is eerie, except for screams in the distance. Something has happened.")
step1 = input("Do you go left or right? ")

if step1 == ("left") or step1 == ("Left"):
  print("A pterodactyl swoops down and carries you away to its lair. When you arrive there, massive jaws filled with sharp teeth clamp down on you - game over.")
elif step1 == ("right") or ("Right"):
  print("You make your way down a walkway covered in broken concrete and you arrive at a large steel door. A button is located on one side of the door.") 
  step2 = input("Do you press it? Yes or No? ")
  if step2 == ("yes") or step2 == ("Yes"):
    print("The door slides open with a metallic shriek. A velociraptor jumps out of the shadows and eats you. Game over.")
  else:
    print("Wise move. As you walk away, something on the other side of that door snarls and scrapes its claws against metal. You round a corner see a set of mysterious looking stairs leading down into a dark, underground pit. ")
    step3 = input("Do you go down the stairs? Yes or No? ")
    if step3 == ("No") or step3 == ("no"):
      print("Scary flying shark appears behind you and eats you! Game Over")
    else: 
      print("You find an abandoned Model XK-992 Dinosaur Stun Gun! It appears to still be in working condition, too. You breathe a sigh of relief now that you have a way to defend yourself. But oh NO! IDOMINUS appears behind you!!! ROOOARRRRRRRRR!!! You raise the stun gun to fire. ")
      step4 = input("Do you aim at his legs, or at his head? ")
      if step4 == ("His legs") or step4 == ("his legs") or step4 == ("legs") or step4 == ("Legs"):
        print("It didn't work! He shrugs off the hit and giant jaws clamp down on you - game over.")
      elif step4 == ("His head") or step4 == ("Head") or step4 == ("head") or step4 == ("his head"):
        print("A bolt of lighting leaps out of the gun, singing the air as it makes contact. The giant dino ROARRS loudly, but then passes out and falls to the ground. You win!!!")
  