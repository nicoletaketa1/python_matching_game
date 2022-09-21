"""
Program: Project 2
Author: Nicole Taketa
Class: CS 115
Description: This program creates an interactive 5x5 matching game in a graphics window.
"""
from match_graphics import *


def shuffle_cards():
   '''
   Generates a shuffled deck of cards. When done, cards[i][j] is the name
   of the card in row i and column j. It is a 5x5 grid comprised of 12
   card pairs and one extra card.

   :param: None
   :return: list of five nested lists with five items in each list(25 total items)
   '''

   shuffle(images)
   pairs = images[:18]             # picks out first 12 images from shuffled list
   duplicates = images[:18]        # duplicates list of 12 to create pairs
   extra = images[18]              # picks out extra card
   shuffled_cards = pairs + duplicates
  # shuffled_cards.append(extra)        # creates full list of 25
   shuffle(shuffled_cards)             # reshuffles cards

   cards = []
   for i in range(6):
       row = []
       for j in range(6):
           item = shuffled_cards[j]
           row.append(item)
       shuffled_cards = shuffled_cards[6:]  # takes away the first five cards of list so they are not reused
       cards.append(row)  # will end up with a list of five nested lists
   return cards


def show_card(win, card_name, i, j):
    '''
    Shows the card at row i and column j in the 5x5 grid in the window.

    :param win: graphics window
    :param card_name: card associated with (i, j)
    :param i: value of column
    :param j: value of row
    :return: None
    '''
    top_left = Point(XMARGIN + (i * CARD_WIDTH), YMARGIN + (j * CARD_HEIGHT))
    bottom_right = Point(XMARGIN + ((1 + i) * CARD_WIDTH), YMARGIN + ((1 + j) * CARD_HEIGHT))
    rectangle = Rectangle(top_left, bottom_right)
    rectangle.setOutline('Yellow')          # Draws a rectangle with a yellow border of line width 5
    rectangle.setWidth(5)
    rectangle.draw(win)
    # Draw the image for card_name at the center of the rectangle.
    center_x = XMARGIN + ((CARD_WIDTH * i) + (CARD_WIDTH / 2))
    center_y = YMARGIN + ((CARD_HEIGHT * j) + (CARD_HEIGHT / 2))
    card = Image(Point(center_x, center_y), card_name)
    card.draw(win)
    return


def hide_card(win, i, j):
   '''
   Takes the window and cards and hides the card at row i and column j.

   :param win: graphics window
   :param i: value of column
   :param j: value of row
   :return: None
   '''
   top_left = Point(XMARGIN + (i * CARD_WIDTH), YMARGIN + (j * CARD_HEIGHT))
   bottom_right = Point(XMARGIN + ((i + 1) * CARD_WIDTH), YMARGIN + ((j + 1) * CARD_HEIGHT))
   hidden_card = Rectangle(top_left, bottom_right)
   hidden_card.setFill('LightGreen')       # fills card space with light green instead of picture
   hidden_card.setOutline('Yellow')
   hidden_card.setWidth(5)
   hidden_card.draw(win)
   return


def mark_card(win, i, j):
   '''
   Takes the window and cards and marks the card at row i and column j
   with a red X.

   :param win: graphics window
   :param i: value of column
   :param j: value of row
   :return: None
   '''
   top_left = Point(XMARGIN + (i * CARD_WIDTH), YMARGIN + (j * CARD_HEIGHT))
   bottom_right = Point(XMARGIN + ((i + 1) * CARD_WIDTH), YMARGIN + ((j + 1) * CARD_HEIGHT))
   top_right = Point(XMARGIN + (i * CARD_WIDTH) + CARD_WIDTH, YMARGIN + (j * CARD_HEIGHT))
   bottom_left = Point(XMARGIN + (i * CARD_WIDTH), YMARGIN + (j * CARD_HEIGHT) + CARD_HEIGHT)
   line1 = Line(top_left, bottom_right)    # draws line from top left of card to bottom right
   line1.setOutline('red')
   line1.setWidth(6)
   line1.draw(win)
   line2 = Line(top_right, bottom_left)    # draws line from top right of card to bottom left
   line2.setOutline('red')
   line2.setWidth(6)
   line2.draw(win)
   return


def get_col(x):
   '''
   Takes the x-coordinate value and returns the column.
   If the x coordinate is outside the board, returns -1.

   :param x: x-coordinate clicked
   :return: value of column
   '''

   # TODO (Checkpoint B): finish this function as described

   if (0 < x < XMARGIN) or ((BOARD_WIDTH - XMARGIN) < x < BOARD_WIDTH):
       return -1                                   # outside of board
   elif (XMARGIN + CARD_WIDTH) > x > XMARGIN:
       return 0                                    # column 0
   elif (XMARGIN + (CARD_WIDTH * 2)) > x > (XMARGIN + CARD_WIDTH):
       return 1                                    # column 1
   elif (XMARGIN + (CARD_WIDTH * 3)) > x > (XMARGIN + (CARD_WIDTH * 2)):
       return 2                                    # column 2
   elif (XMARGIN + (CARD_WIDTH * 4)) > x > (XMARGIN + (CARD_WIDTH * 3)):
       return 3                                    # column 3
   elif (XMARGIN + (CARD_WIDTH * 5)) > x > (XMARGIN + (CARD_WIDTH * 4)):
       return 4                                    # column 4
   elif (XMARGIN + (CARD_WIDTH * 6)) > x > (XMARGIN + (CARD_WIDTH * 5)):
       return 5


def get_row(y):
   '''
   Takes the y-coordinate value and returns the row.
   If the y-coordinate is outside the board, returns -1.

   :param y: y-coordinate clicked
   :return: value of row
   '''
   if (0 < y < YMARGIN) or ((BOARD_HEIGHT - YMARGIN) < y < BOARD_HEIGHT):
       return -1                                   # outside of board
   elif (YMARGIN + CARD_HEIGHT) > y > YMARGIN:
       return 0                                    # row 0
   elif (YMARGIN + (CARD_HEIGHT * 2)) > y > (YMARGIN + CARD_HEIGHT):
       return 1                                    # row 1
   elif (YMARGIN + (CARD_HEIGHT * 3)) > y > (YMARGIN + (CARD_HEIGHT * 2)):
       return 2                                    # row 2
   elif (YMARGIN + (CARD_HEIGHT * 4)) > y > (YMARGIN + (CARD_HEIGHT * 3)):
       return 3                                    # row 3
   elif (YMARGIN + (CARD_HEIGHT * 5)) > y > (YMARGIN + (CARD_HEIGHT * 4)):
       return 4                                    # row 4
   elif (YMARGIN + (CARD_HEIGHT * 6)) > y > (YMARGIN + (CARD_HEIGHT * 5)):
       return 5


def main():
    '''
    Generates game board with shuffled cards placed face down,
    flips over cards associated with mouse clicks, and checks to make sure
    each click is a valid card choice.
    Calls a function at end to show when user has won the game
    '''

    win = create_board()
    cards = shuffle_cards()
    for i in range(6):
       for j in range(6):
           hide_card(win, i, j)
    matched_cards = [1]    # list to hold name of matched cards to letting the user choose a matched card
    while True:
       n = 1
       while n == 1:               # round 1
           point = win.getMouse()
           a = get_col(point.getX())
           b = get_row(point.getY())
           if a == -1 or b == -1:      # if point clicked is outside board it allows new click
               n = 1
           else:
               card_1 = cards[a][b]
               n = 2
               for c in range(len(matched_cards)):   # checks if point clicked is already a matched card
                   if card_1 == matched_cards[c]:
                       n = 1
       while n == 2:               # round 2
           show_card(win, cards[a][b], a, b)
           point = win.getMouse()
           i = get_col(point.getX())
           j = get_row(point.getY())
           if (i == -1 or j == -1) or (i == a and j == b):
               n = 2
           else:
               card_2 = cards[i][j]
               n = 3
               for d in range(len(matched_cards)):   # checks if point clicked is already a matched card
                   if card_2 == matched_cards[d]:
                       n = 2
       while n == 3:               # once two legitimate clicks have been made
           show_card(win, cards[i][j], i, j)
           game_delay(1)
           if card_1 == card_2:            # if cards are a matching pair they are marked and stay up
               mark_card(win, a, b)
               mark_card(win, i, j)
               matched_cards.append(card_1)        # adds name of matched card to list
           else:                           # if they do not match they are hidden
               hide_card(win, a, b)
               hide_card(win, i, j)
           n = 4                           # variable to stop while n==3 loop
       if len(matched_cards) == 19:        # number of different cards with a pair + 1
           break                   # ends all current loops, if reached then game has been won
       else:
           continue
    you_won(win)

    win.getMouse()



main()
