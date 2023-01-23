# Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:

    def check_for_ace(self, card):
        if card.value == 1:  # added another equals sign
            return True
        else:  # added colon/maybe fixed indentation check orig
            return False

    def highest_card(self, card1, card2):  # added comma and dif to def
        if card1.value > card2.value:  # fixed indentation
            return card1  # added 1 to card
        else:
            return card2

    def cards_total(self, cards):  # fixed indentation
        total  # create list of 3 or 4 cards in test
        for card in cards:
            total += card.value
            return (f"You have a total of" + {total})
