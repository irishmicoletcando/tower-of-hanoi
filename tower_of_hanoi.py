def TowerOfHanoi(disk, from_rod, to_rod, aux_rod):
    if disk == 0:
        return
    TowerOfHanoi(disk-1, from_rod, aux_rod, to_rod)
    print("Move disk", disk, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(disk-1, aux_rod, to_rod, from_rod)
 
 
# Driver code
N = 3
 
# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')

# References used:
# Tower of Hanoi Recursion: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/