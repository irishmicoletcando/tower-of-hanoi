from tkinter import * # sets up the GUI window
from PIL import ImageTk,Image # for displaying and positioning images
import time # used for delaying function for a specified number of seconds

# displays window and components
towerOfHanoiWindow = Tk()
# sets the title of window
towerOfHanoiWindow.title( "Tower of Hanoi Solver" )
# sets size of window with a width of 800 and height of 500
towerOfHanoiWindow.geometry( "800x500")
# sets opacity of window; 1 - no opacity 
towerOfHanoiWindow.attributes( "-alpha", 1 )
# sets background color of window 
towerOfHanoiWindow.configure( background="#1E2665" )

# creates a label widget for tower of hanoi title
towerOfHanoiTitle = Label( towerOfHanoiWindow, text="Tower of Hanoi", fg="#FFFFFF", font=("Arial 30"), bg="#1E2665" ).pack()

# creates a label widget for objective
towerOfHanoiTitle = Label( towerOfHanoiWindow, text="Objective: Helps user to visualize how a 4-disk Tower of Hanoi can be solved", fg="#FFFFFF", font=("Arial 15"), bg="#1E2665" ).pack()

# declares the initial move count
movescount = 0

# sets up the initial state of the game
def towerOfHanoi_start():
  # declares global variable to be used anywhere in the program
  global allPositionX, allPositionY, canvas, pole, disk1, disk2, disk3, disk4, moves, movescount
  # sets the x - position of disk
  allPositionX=[]
  # sets the y - position of disk
  allPositionY=[]

  # creates a label widget for number of moves
  moves = Label( towerOfHanoiWindow, text=f"{movescount} Moves", fg="#FFFFFF", font=("Arial 20"), bg="#1E2665" )
  # sets label widget's position and centered alignment
  moves.place( relx=0.5, rely=0.22, anchor=CENTER )

  # sets the canvas width and height which contains the poles png and disks' images
  canvas = Canvas( towerOfHanoiWindow, width=550, height=350, background="#1E2665", bd=0, highlightthickness=0 )  
  # sets the position of canvas and centered alignment
  canvas.place( relx=0.5, rely=0.6, anchor=CENTER )

  # creates the poles object of the image in the path
  pole = ImageTk.PhotoImage( Image.open("poles.png") )
  # displays the image on the specific position
  canvas.create_image( -20, -20, anchor=NW, image=pole )

  # --------------------- BUTTONS ------------------------
  # creates a start button that pass the function of TowerOfHanoi
  startGame = Button( towerOfHanoiWindow, text ="START", fg="#FFFFFF", font=("Arial 30 bold"), bg="#FFFFFF", activebackground="#FFFFFF", highlightbackground="#71CAD3", justify=CENTER, command=lambda:TowerOfHanoi(4 , 0, 360, 180), width=12, bd=0 )
  # sets the background color of start button
  startGame.configure( bg="#555B91" )
  # sets the position of start button
  startGame.place( relx=0.5, rely=0.95, anchor=SE )

  # creates a play again button that pass the function of playAgainTowerOfHanoi
  playAgainGame = Button( towerOfHanoiWindow, text="PLAY AGAIN", fg="#FFFFFF", font=("Arial 30 bold"), bg="#FFFFFF", activebackground="#FFFFFF", highlightbackground="#71CAD3", justify=CENTER, command=lambda:playAgainTowerOfHanoi(), width=12, bd=0 )
  # sets the background color of play again button
  playAgainGame.configure( bg="#555B91" )
  # sets the position of play again button
  playAgainGame.place( relx=0.52, rely=0.95, anchor=SW )

  # ---------------------- DISKS ---------------------------
  # creates the smallest disk object of the image in the path
  disk1 = ImageTk.PhotoImage( Image.open("1.png") )
  # sets the x and y-positions of smallest disk
  allPositionX.append(10)
  allPositionY.append(0)
  # displays the smallest disk png on the specific position
  canvas.create_image( allPositionY[0], allPositionX[0], anchor=NW, image=disk1 )

  # creates the second smallest disk object of the image in the path
  disk2 = ImageTk.PhotoImage( Image.open("2.png") )
  # sets the x and y-positions of second smallest disk
  allPositionX.append(55)
  allPositionY.append(0)
  # displays the second smallest disk png on the specific position
  canvas.create_image( allPositionY[1], allPositionX[1], anchor=NW, image=disk2 )

  # creates the second largest disk object of the image in the path
  disk3 = ImageTk.PhotoImage( Image.open("3.png") )
  # sets the x and y-positions of second largest disk
  allPositionX.append(100)
  allPositionY.append(0)
  # displays the second largest disk png on the specific position
  canvas.create_image( allPositionY[2], allPositionX[2], anchor=NW, image=disk3 )

  # creates the largest disk object of the image in the path
  disk4 = ImageTk.PhotoImage( Image.open("4.png") )
  # sets the x and y-positions of largest disk
  allPositionX.append(145)
  allPositionY.append(0)
  # displays the largest disk png on the specific position
  canvas.create_image( allPositionY[3], allPositionX[3], anchor=NW, image=disk4 )


# implements the logic of the Tower of Hanoi game
# takes four arguments, the number of disks (disk), the source (from_rod), destination (to_rod), and auxiliary poles (aux_rod)
def TowerOfHanoi(disk, from_rod, to_rod, aux_rod):
    global movescount, moves
    if disk == 0:
      movescount+=1
      # displays the number of moves made during the game
      moves.configure( text=str(movescount) + " Moves" )
      # delays in moving disk
      time.sleep(0.3)
      move(0, to_rod)
      time.sleep(0.3)
      return
    # uses a recursive approach to solve the game by moving the (disk-1) disks to the auxiliary pole, then moving the nth disk to the destination pole, and finally moving the (disk-1) disks to the destination pole.
    TowerOfHanoi(disk-1, from_rod, aux_rod, to_rod)
    movescount+=1
    # displays the updated number of moves made during the game
    moves.configure( text=str(movescount) + " Moves" )
    # delays in moving disk
    time.sleep(0.3)
    move( disk-1, to_rod )
    time.sleep(0.3)
    TowerOfHanoi(disk-1, aux_rod, to_rod, from_rod)


# updates the position of the disks on the canvas as they are moved during the game
# takes two arguments, the item (disk) to be moved and its destination (to_rod)
def move( item, to_rod ):
  global disk1, disk2, disk3, disk4
  # moves disk 1 on the tower of hanoi game window
  if item == 0:
    # checks if disk 1 is not already on the target rod (specified by the "to_rod" variable) before moving it
    if( allPositionY[0]!=to_rod ):
      # loads an image of disk 1 and displays it on the canvas widget
      disk1 = ImageTk.PhotoImage( Image.open("1.png") )
      # displays disk 1 on the canvas widget at the target rod's y-position and a calculated x-position
      canvas.create_image( to_rod, 145 - (45 * allPositionY.count(to_rod)), anchor=NW, image=disk1 ) # position disk exactly above the larger disk with only a small gap
      # stores the updated rod position of disk 1
      allPositionY[0] = to_rod
      allPositionX[0] = 145 - (45 * allPositionY.count(to_rod))
      # updates the window
      Tk.update(towerOfHanoiWindow) 
      return

  # moves disk 2 on the tower of hanoi game window
  elif item == 1 :
    # checks if disk 2 is not already on the target rod (specified by the "to_rod" variable) before moving it
    if( allPositionY[1]!=to_rod ):
      # loads an image of disk 2
      disk2 = ImageTk.PhotoImage( Image.open("2.png") )
      # displays disk 2 on the canvas widget at the target rod's y-position and a calculated x-position
      canvas.create_image(to_rod, 145 - (45 * allPositionY.count(to_rod)), anchor=NW, image=disk2 )
      # stores the updated rod position of disk 2
      allPositionY[1] = to_rod
      allPositionX[1] = 145 - (45 * allPositionY.count(to_rod))
      # updates the window
      Tk.update(towerOfHanoiWindow) 
      return

  # moves disk 3 on the tower of hanoi game window
  elif item == 2 :
    # checks if disk 3 is not already on the target rod (specified by the "to_rod" variable) before moving it
    if( allPositionY[2]!= to_rod ):
      # loads an image of disk 3 and displays it on the canvas widget
      disk3 = ImageTk.PhotoImage( Image.open("3.png") )
      # displays disk 3 on the canvas widget at the target rod's y-position and a calculated x-position
      canvas.create_image( to_rod, 145 - (45*allPositionY.count(to_rod)), anchor=NW, image=disk3 )
      # stores the updated rod position of disk 3
      allPositionY[2] = to_rod
      allPositionX[2] = 145 - (45 * allPositionY.count(to_rod))
      # updates the window
      Tk.update(towerOfHanoiWindow) 
      return

  # moves disk 4 on the tower of hanoi game window
  else:
    # checks if disk 4 is not already on the target rod (specified by the "to_rod" variable) before moving it
    if( allPositionY[3]!= to_rod ):
      # loads an image of disk 4 and displays it on the canvas widget
      disk4 = ImageTk.PhotoImage( Image.open("4.png") )
      print( allPositionX.count(to_rod) )
      # displays disk 4 on the canvas widget at the target rod's y-position and a calculated x-position
      canvas.create_image(to_rod, 145 - (45 * allPositionY.count(to_rod)), anchor=NW, image=disk4 )
      # stores the updated rod position of disk 4
      allPositionY[3] = to_rod
      allPositionX[3] = 145 - (45 * allPositionY.count(to_rod))
      # updates the window
      Tk.update(towerOfHanoiWindow) 
      return


# user clicks play again button
def playAgainTowerOfHanoi():
  # resets the number of moves
  movescount = 0
  Label.destroy(moves)


  
# starts the game
towerOfHanoi_start()
# starts the main event loop of the GUI window
towerOfHanoiWindow.mainloop()

# References used:
# Tower of Hanoi Recursion: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
# For aligning in center: https://www.tutorialspoint.com/python/tk_anchors.htm
# For creating GUI window: https://www.youtube.com/watch?v=ibf5cx221hk
# For buttons with functions: https://www.tutorialspoint.com/tkinter-button-commands-with-lambda-in-python