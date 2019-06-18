
## Qualification Round

### Problem -1 (LeapFrog Ch 1)

The problem states that if its possible for an **Alpha** frog to jump towards the right end from the left end of the pond, given that some of the
intermediate lilies are occupied by **Beta** Frogs.

The **Alpha** frog can only move towards right and it has to pass atleast one **Beta** frog to move towards the next unoccupied lily.
The **Beta** frog can move either left or right.

So possible cases are,

```
AB.
ABB.
ABB..
ABBB.
ABBB..

```
 
So we can tackle the problem as follows

AB. is the least possible case for the alpha frog to cross to right end. And in order for the frog to cross, it must have the subset `AB.`

Hence 

`A.B.B` => `AB..B` => `.BA.B` => `.BAB.` => `.B.BA` (Solution reached)

So given any random combination `A..B....B...B.B.BBBB.BB.BB..BB` we check to see if we can have a configuration `AB.` and thus solve the remaining
configuration like wise.

In other words, we see if we can arrange any given combination as follows `AB.AB.AB.AB.AB.`. Only in that case we have a possible solution.

As we can see for the above configuration to hold, we must have **no. of Bs**  == **no. of dots**. Only then the alpha frog is able to move forward
and in the end reach the right end.

[Solution](https://github.com/prateekiiest/Facebook-HackerCup-Archives/blob/master/2019/Qualification_Round/Leapfrog_Ch_1/prog.py)


-------------------

## Mr. X

[To be continued]
