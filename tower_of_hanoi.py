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

def TowerOfHanoi(disk, from_rod, to_rod, aux_rod):
    if disk == 0:
        return
    TowerOfHanoi(disk-1, from_rod, aux_rod, to_rod)
    print("Move disk", disk, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(disk-1, aux_rod, to_rod, from_rod)


# def playAgainTowerOfHanoi():


# starts the main event loop of the GUI window
towerOfHanoiWindow.mainloop()

# References used:
# Tower of Hanoi Recursion: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/