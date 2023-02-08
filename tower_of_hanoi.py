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




def TowerOfHanoi(disk, from_rod, to_rod, aux_rod):
    if disk == 0:
        return
    TowerOfHanoi(disk-1, from_rod, aux_rod, to_rod)
    print("Move disk", disk, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(disk-1, aux_rod, to_rod, from_rod)


# starts the main event loop of the GUI window
towerOfHanoiWindow.mainloop()

# References used:
# Tower of Hanoi Recursion: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/