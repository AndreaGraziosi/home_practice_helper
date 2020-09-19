from random import choice
import random
  
def week_of_the_month(user_response):
   

#add monthly practice by week
 bot_response_week_1 = ["downward dog", "forward bend", "savasana"] 
 bot_response_week_2 = ["downward dog", "back-bend" ,"savasana"]
 bot_response_week_3 = ["downward dog","tree pose", "twist", "savasana"]
 bot_response_week_4 = ["downward dog", "inversions", "savasana"]

#more than one elif statement; each statement representing a possible input for the week of the month
 if user_response == "week1":
    return choice(bot_response_week_1)
 elif user_response == "week2":
    return choice(bot_response_week_2)
 elif user_response == "week3":
    return random.choice(bot_response_week_3)
 elif user_response == "week4":
    return choice(bot_response_week_4)    
 else:
    return "refer to: more practice ideas"   

print("Let's plan your practice!")
print ("please enter the week of the month for a list of poses to practice this week.")



while True:
 user_response = input("Example: week1 week2 week3 week4: ")
 if user_response == "no":
  break


 bot_response = week_of_the_month(user_response)
 print(bot_response)