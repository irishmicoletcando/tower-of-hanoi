from tkinter import * # sets up the GUI window
from PIL import ImageTk,Image # for displaying and positioning images
import time # used for delaying function for a specified number of seconds

# displays window and components
towerOfHanoiWindow = Tk()
# sets the title of window
towerOfHanoiWindow.title( "Tower of Hanoi Solver" )
# sets size of window with a width of 800 and height of 500
towerOfHanoiWindow.geometry( "800x500")


def TowerOfHanoi(disk, from_rod, to_rod, aux_rod):
    if disk == 0:
        return
    TowerOfHanoi(disk-1, from_rod, aux_rod, to_rod)
    print("Move disk", disk, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(disk-1, aux_rod, to_rod, from_rod)


# References used:
# Tower of Hanoi Recursion: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/