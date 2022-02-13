############### Blackjack Project #####################



from art import logo
from replit import clear
import random


print(logo)

def deal_cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """"Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)


def compare(user_score, computer_score):
  if computer_score == user_score:
    return "Draw"
  elif computer_score == 0:
      return "You lost, Computer has Blackjack! "
  elif user_score == 0:
      return "You Won!! BlackJack! "   
  elif computer_score > 21:
      return "You Win, Computer over 21"
  elif user_score > 21:
      return "You lose, over 21"
  elif user_score > computer_score:
    return "You Win"
  else:
    return "You lose"
    
def play_game():
  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}  Current Score: {user_score} ")
    print(f"Computer's First Card: {computer_cards[0]}  ")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
      print("Your score is over 21, you lose! ")
    else:
      user_should_deal = input("Type 'y' to get another card or type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_cards())
      else:
        is_game_over = True


  while computer_score != 0 and computer_score < 21:
    computer_cards.append(deal_cards())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards} \nYour final Score: {user_score} ")
  print(f"Computer's final hand: {computer_cards} \nComputer final Score: {computer_score} ")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
