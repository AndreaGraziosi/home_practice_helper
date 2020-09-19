from random import choice
import random
  
def week_of_the_month(user_response):
   

#add monthly practice by week
 bot_response_week_1 = ["downward dog", "uttanasana", "savasana"] 
 bot_response_week_2 = ["locust", "back-bend on a chair" ,"upward dog"]
 bot_response_week_3 = ["warrior 1","tree pose", "half moon", "chair pose"]
 bot_response_week_4 = ["head stand", "shoulder stand", "head stand"]

#more than one elif statement; each statement representing a possible input for the week of the month
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

print("What kind of poses would you like to practice at home today?")

print ("Let me help you get started, you can type: forward bends, back bends, standing poses, inversions...")



while True:
 user_response = input("Enter the type of pose you would like to practice: ")
 if user_response == "stop":
  break


 bot_response = week_of_the_month(user_response)
 print(bot_response)