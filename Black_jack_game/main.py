import random
from art import logo 

### returns game_end bool
def checkStat(user, cardlist: list)-> bool:
    score = sum(cardlist)
    if(score == 21):
        print(f"{user} Win!")
        return True
    elif(score < 21):
        return False
    else:
        if(cardlist.count(11)):
            ## has aces/
            index = cardlist.index(11)
            cardlist[index] = 1
            checkStat(user,cardlist)
            return False
        else:
            print("You lose!")
            return True






cards = [11,11,11,11,11,2,3,4,5,6,7,8,9,10,10,10,10]

playGame = input(str(print("Do you want to play a game of Blackjack? Type 'y' or 'n':")))

if(playGame == 'y'):
    print(logo)
    user_cards = random.choices(cards,k=2)
    dealer_cards = random.choices(cards,k=1)

    

    game_end = False
    ## Check the Status
    game_end = checkStat("You", cardlist= user_cards)
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Dealer's first cards {dealer_cards[0]}")


    while not game_end:
        command = input(str(print("Type 'y' to get another card, type 'n' to pass:"))).lower()
        if(command == 'y'):
            user_cards.append(random.choice(cards))
            game_end = checkStat("You", cardlist= user_cards)
        elif(command == 'n'):
            while(sum(dealer_cards) < 17):
                dealer_cards.append(random.choice(cards))            
            game_end = checkStat("Dealer", cardlist= dealer_cards)    
            if(game_end == False):
                if(sum(user_cards)> sum(dealer_cards)):
                    print("You Won!")
                elif(sum(user_cards)< sum(dealer_cards)):
                    print("You lose!")
                else:
                    print("Draw")
            game_end = True
        print(f"Dealer's cards {dealer_cards}, score: {sum(dealer_cards)}")    
        print(f"Your cards {user_cards}, score: {sum(user_cards)}")                    
else:
    print("Another time!")
        

            












