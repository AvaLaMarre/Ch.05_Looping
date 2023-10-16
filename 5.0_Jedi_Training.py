# 5.0 Jedi Training (50pts)  Name:________________

'''
 1. Make the following program work. LIST THE 3 MISTAKES (5pts)
   '''
import random

print("This program takes three integers and returns the sum.")
total = 0
for i in range(3):
    x = int(input("Enter a number: "))
    total += x
print("The total is:", total)
print()
#1 Nothing is being added to the total, change i to x
#2 put int() in front of the input
#3 make it print total not x


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive. (5pts)
'''
print("Question 2")
for i in range(2 , 102, 2):
    print(i)
print()
'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop. (5pts)
'''
print("Question 3")
i = 10
while i > -1:
    print(i)
    i -= 1
print()

'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive). (5pts)
'''
print("Question 4")
myNumber = random.randrange(1, 11)
print(myNumber)



'''
  5. 7 NUMBER ANALYSIS (5pts)
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''






'''
6. COIN TOSS PROGRAM (10pts)
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
print("Question 6")
heads = 0
tails = 0
for i in range(50):
    coinToss = random.randrange(0, 2)
    if coinToss == 0:
        print("Heads")
        heads += 1
    else:
        print("Tails")
        tails += 1
print("Total Count For Heads = ", heads)
print("Total Count For Tails = ", tails)
print()

'''
ROSHAMBO PROGRAM (15pts)
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round, tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits, print an end game message and their win/loss/tie record

'''





