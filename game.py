import random

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

user_card_list=[]
computer_card_list=[]
for number in range(2):
    user_card_list.append(deal_card())
    computer_card_list.append(deal_card())

def calculate_score(cards):
    if len(cards)==2 and sum(cards)==21:
        return 0
    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)    
    return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Is a Draw!"
    elif computer_score==0:
        return "Computer's Black Jack! You lose"  
    elif user_score==0:
        return "Black Jack! You win :) "
    elif user_score>21:
        return "Your score Over 21. You lose"
    elif computer_score>21:
        return "Computer score Over 21. You Win"  
    elif computer_score>user_score:
        return "Computer Win!"      
    else:
        return "You Win !"    
                  

user_wanna_continue = True

while user_wanna_continue:
    user_score = calculate_score(user_card_list)
    computer_score = calculate_score(computer_card_list)
    print(f"Your Cards are :{user_card_list} and Score:{user_score}" )
    print(f"Computer's First Hands :{computer_card_list[0]}" )
    if user_score==0 or computer_score==0 or user_score>21:
        user_wanna_continue=False
    else:    
        user_reply = input("Do you wanna continue playing blackjack? Type 'y' to continue and 'n' to exit :")
        if user_reply=='y':
            user_card_list.append(deal_card())
        else:
            user_wanna_continue=False    
        
while computer_score !=0 or computer_score<17:
    computer_card_list.append(deal_card())
    computer_score = calculate_score(computer_card_list)
    

print(f"Your Final cards are :{user_card_list} and Score:{user_score}" )
print(f"Computer's Final Hands :{computer_card_list} and Score:{computer_score} " )
print(compare(user_score,computer_score))