# ProblemSolvingAssignment
Problem Solving Module Coursework Assignment using Python

## Task Instructions:

Consider  a  Toy  world,  containing  a  finite  number  n  of  objects.  Each  object  is  specified  by  a  unique name (a string, such as “A”, or “B”, or “d1”, or “table2”). The current state of the world  is described using a (finite) set of properties (propositions) which specify the state the objects  are  in.  In  the  simple  scenario  considered  here,  only  3  possibly  propositions  are  used  to  describe the state of the world: 

ON(x, y):       in the current state, object x is on top of object y;
CLEAR(x):       object x is clear, i.e. it has nothing (no other object) on top of it;
HEAVIER(x, y):  object x is heavier than object y.

The current state of the world is specified by a finite set of “ground instances” of the above  propositions, i.e., instances obtained by replacing all the variables (x and y) with specific 
object names. For example, the following state

s1 = { ON(A, table1), HEAVIER(table1, A), HEAVIER(table2, A), CLEAR(A), CLEAR(table2) }   

contains 5 propositions involving 3 objects (named “A”, “table1”, “table2”). Here s1 describes  a state in which object A is clear and is on top of table1, table2 is clear, and table1 and table2  are both heavier than A. Note that the order of the propositions is irrelevant (i.e., a state is  a set, and not a sequence, of propositions).

In this Toy world only 1 action is possible, namely, moving an object from its current location  to a different one. This action is described by the “Move” schema (or operator) below: 
 
Move(x, y, z): 
Preconditions:  
Add: 
Delete:   
ON(x, y), CLEAR(z), CLEAR(x), HEAVIER(z, x)  ON(x, z), CLEAR(y) 
ON(x, y), CLEAR(z) 

This  operator  moves  object  x  (lying  on  top  of  y)  onto  object  z,  leaving  y  clear.  The  Move  operator, however, can only be applied if all of its preconditions are true in the current state.

When the operator Move is applied, the current world state is changed in the following way:  
•  all the propositions in the “Add” list are added to the state (i.e., they become true); 
•  all propositions in the “Delete” list are removed from the state (i.e., are no longer true).  In the above example, executing Move(A, table1, table2) in s1 produces a new state, s2, where 

s2 = { ON(A,table2), HEAVIER(table1, A), HEAVIER(table2, A), CLEAR(A), CLEAR(table2) } 

In  short,  executing  a  Move  action  removes  two  propositions  from  the  state,  adds  two  new 
propositions, and leaves the rest of the state unchanged. 

Given the previous Introduction, write a Python program that executes the following steps:   
1.  Asks the user to enter a list Obj of object names (as strings);  
2.  Asks the user to enter an initial state, S0 (see below for the format);  
3.  Asks the user to enter a goal, G (see below for the format); 
4.  Prints  a  finite  sequence  of  Move  action  instances  (having  all  variables  replaced  by  object 
names  taken  from  Obj)  such  that,  if  applied  in  the  specified  order,  they  change  the  initial 
state S1 into a final one, Sn, such that Sn contains all of the propositions listed in G.  
5.  Terminates. 





