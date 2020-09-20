from random import choice
import random
  
def get_bot_response(user_response):
   

#add monthly practice by week and give suggestions on what todo!
 bot_response_week_1 = ["Upwnward dog for 20 minutes, don't hold your breath!", "Forward bend sequence ending in parchimotanasana. These poses heal the nervous system.", "1 hour long savasana, nothing better for the mind."] 
 bot_response_week_2 = ["Start with a strong standing pose sequence", "Back-bend sequence on a chair" ,"Upward dog on a rope wall! Be sure to work on arms before starting."]
 bot_response_week_3 = ["10 sun salutations to get you started", "Tree pose for balance! Do all balancing poses you can remeber", "Incorporate twists today!"]
 bot_response_week_4 = ["Hand stand sequence", "Shoulder stand and forearm balance! Yay it will be so fun!", "Hang on a sling for a few mintes and realign the spinal column!"]

# i will need more than one elif if the user inputs an anwer what will the response be? choose from the lists
 if user_response == "forward bends":
    return choice(bot_response_week_1)
 elif user_response == "back bends":
    return choice(bot_response_week_2)
 elif user_response == "standing poses":
    return random.choice(bot_response_week_3)
 elif user_response == "inversions":
    return choice(bot_response_week_4)    
 else:
    return "For help with that pose, you should come to class! Let's practice together!"   

print("Namaste. Sit quietly in a comfortable position and chant om 3 times, notice the effect on your body.")

print ("Let me help you get started with some ideas for poses today. You can type: forward bends, back bends, standing poses, inversions...")



while True:
 user_response = input("Enter the type of pose you would like to practice, and I can suggest a sequence! Om ")
 if user_response == "done":
  break


 bot_response = get_bot_response(user_response)
 print(bot_response)