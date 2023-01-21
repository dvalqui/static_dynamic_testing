### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:


  def check_for_ace(self, card):
    if card.value == 1:
      return True
    else:  #added colon
      return False
   

  def highest_card(self, card1, card2): #added comma and added indentation
    if card1.value > card2.value:
      return card
    else:
      return card2
  


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total