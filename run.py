#! /usr/bin/python3
def board_print(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
# make board layout

def checkwin(check):

  sol_win = [
    [1,2,3], [4,5,6], [7,8,9], [1,4,7], 
    [2,5,8], [3,6,9], [1,5,9], [3,5,7],
  ]

  for i in sol_win:
    if all(y in check for y in i):
      return True
  return False    

def retake():
    usrtake = input("Do you want to Play Again? ").lower()

    if usrtake == "y":
        game_play()
    elif usrtake == "n"
        print("Thank you for playing\nBye Bye")
    else:
        print("Did catch what you wrote:)")


# game play
def game_play():

  # this is an array of empty squares
  values = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

  # board_print(values)
  gameon = True
  count = 0
  curr_user = 'X'

  user_x = []
  user_o = []

  board_print(values)


  while gameon:

    try:
      userplay = int(input(f"It is {curr_user} turns: "))
    except ValueError:
      print('Invalid character should be 1 to 9')
      continue

    if userplay < 1 or userplay > 9:
      print('Choose a number btwn 1 to 9')
      continue

    if values[userplay-1] != " ":
      print('Choose another box already taken')
      continue

    if curr_user == "X":
      values[userplay-1] = "X"
      user_x.append(userplay) 
      curr_user = "O" 

    else:
      values[userplay-1] = "O"
      user_o.append(userplay) 
      curr_user = "X"

    board_print(values)
    print('\n')
    # print(values)
    # print(user_x)
    # print(user_o)

    if len(user_x) >= 3:
      if checkwin(user_x):
        print('-'*10)
        print('\n')
        print('winner is X')
        print('\n')
        print('-'*10)
        continue

    if len(user_o) >= 3:
      if checkwin(user_o):
        print('-'*10)
        print('\n')
        print('winner is Y')
        print('\n')
        print('-'*10)
        continue

    if count == 8:
        print('-'*10)
        print('\n')
        print('Game Over')
        print('Its a Draw')
        print('\n')
        print('-'*10)
        continue

    count += 1
  retake()

if __name__ == '__main__':
  game_play()

