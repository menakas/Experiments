from typing import List
import itertools

def solveProblem(R: int, C: int, G: List[List[str]]) -> int:

   print(G,"\n")
   mtrx = list(itertools.chain(*G))
   
   for s in G:
     print(*s)
 
   for i in range(len(mtrx)):
     print('Neighbours of',mtrx[i],'at position ', i, ':', [(x,mtrx[x]) for x in getneighbours(i,R,C)])
     print("\n")

def getneighbours(a,R,C):
    (x,y) = (int(a/C),a%C)
 
    for (i,j) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        if 0 <= i < R and 0 <=j < C:
            yield (i*C)+j


solveProblem(3,4,[['.','E','.','.'],['.','#','.','E'],['.','S','#','#']])
