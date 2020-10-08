# Python-Fundamental
My tasks which I solve from the SoftUni and Codewars

08.Data-Types-and-Variables-Exercises

  01.Integer Operations
Read four integer numbers. Add first to the second, divide (integer) the sum by the third number and multiply the result by the fourth number. Print the result.

  02.Chars to String
Write a function that receives 3 characters. Combine all the characters into one string and print it on the console.

  03.Elevator
Calculate how many courses will be needed to elevate n persons by using an elevator with capacity of p persons. The input holds two lines: the number of people n and the capacity p of the elevator.

  04.Sum of Chars
Write a program, which sums the ASCII codes of n characters and prints the sum on the console.
Input
    • On the first line, you will receive n – the number of lines, which will follow
    • On the next n lines – you will receive letters from the Latin alphabet
Output
Print the total sum in the following format:
The sum equals: {total_sum}
Constraints
    • n will be in the interval [1…20].
    • The characters will always be either upper or lower-case letters from the English alphabet
    • You will always receive one letter per line

  05.Print Part of the ASCII Table
Find online more information about ASCII (American Standard Code for Information Interchange) and write a program that prints part of the ASCII table of characters on the console.  On the first line of input you will receive the char index you should start with and on the second line - the index of the last character you should print.

  06.Triples of Latin Letters
Write a program to read an integer n and print all triples of the first n small Latin letters, ordered alphabetically:

  07.Water Overflow
You have a water tank with capacity of 255 liters. On the next n lines, you will receive liters of water, which you have to pour in your tank. If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last line, print the liters in the tank.
Input
The input will be on two lines:
    • On the first line, you will receive n – the number of lines, which will follow
    • On the next n lines – you receive quantities of water, which you have to pour in the tank
Output
Every time you do not have enough capacity in the tank to pour the given liters, print:
Insufficient capacity!
On the last line, print only the liters in the tank.
Constraints
    • n will be in the interval [1…20]
    • liters will be in the interval [1…1000]
    
  08.Party Profit
As a young adventurer, you travel with your party around the world, seeking for gold and glory. But you need to split the profit among your companions.
You will receive a party size. After that you receive the days of the adventure. 
Every day, you are earning 50 coins, but you also spent 2 coins per companion for food. 
Every 3rd (third) day, you have a motivational party, spending 3 coins per companion for drinking water. 
Every 5th (fifth) day you slay a boss monster and you gain 20 coins per companion. But if you have a motivational party the same day, you spent additional 2 coins per companion. 
Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave, but every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.
You have to calculate how much coins gets each companion at the end of the adventure.
Input / Constraints
The input will consist of exactly 2 lines:
    • party size – integer in range [1…100]
    • days – integer in range [1…100]
Output
Print the following message: "{companions_count} companions received {coins} coins each."
You cannot split a coin, so take the integral part (round down the coins to integer number). 

  09.Snowballs
Tony and Andi love playing in the snow and having snowball fights, but they always argue which makes the best snowballs. They have decided to involve you in their fray, by making you write a program, which calculates snowball data, and outputs the best snowball value.
You will receive N – an integer, the number of snowballs being made by Tony and Andi.
For each snowball you will receive 3 input lines:
    • On the first line you will get the snowball_snow – an integer.
    • On the second line you will get the snowball_time – an integer.
    • On the third line you will get the snowball_quality – an integer.
For each snowball you must calculate its snowball_value by the following formula:
(snowball_snow / snowball_time) ^ snowball_quality
At the end you must print the highest calculated snowball_value.
Input
    • On the first input line you will receive N – the number of snowballs.
    • On the next N * 3 input lines you will be receiving data about snowballs. 
Output
    • As output you must print the highest calculated snowball_value, by the formula, specified above. 
    • The output format is: 
{snowball_snow} : {snowball_time} = {snowball_value} ({snowball_quality})
Constraints
    • The number of snowballs (N) will be an integer in range [0, 100].
    • The snowball_snow is an integer in range [0, 1000].
    • The snowball_time is an integer in range [1, 500].
    • The snowball_quality is an integer in range [0, 100].
    
  10.Gladiator Expenses
As a gladiator, Peter has to repair his broken equipment when he loses a fight. His equipment consists of helmet, sword, shield and armor. You will receive the Peter\`s lost fights count. 
Every second lost game, his helmet is broken.
Every third lost game, his sword is broken.
When both his sword and helmet are broken in the same lost fight, his shield also brakes.
Every second time, when his shield brakes, his armor also needs to be repaired. 
You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment. 
Input / Constraints
The input will consist of 5 lines:
    • On the first line you will receive the lost fights count – integer in the range [0, 1000].
    • On the second line you will receive the helmet price - floating point number in range [0, 1000]. 
    • On the third line you will receive the sword price - floating point number in range [0, 1000]. 
    • On the fourth line you will receive the shield price - floating point number in range [0, 1000]. 
    • On the fifth line you will receive the armor price - floating point number in range [0, 1000]. 
Output
    • As output you must print Peter\`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"
    
08.Data-Types-and-Variables-More-Exercises

  01.Biggest of 3 Numbers
Write a program that finds the biggest of 3 numbers.
The input comes as 3 integers.
The output is the biggest from the input numbers.

  02.Exchange Integers
Read two integer numbers and after that exchange their values by using some programming logic. Print the variable values before and after the exchange.

  03.Prime Number Checker
Write a program to check if a number is prime (only wholly divisible by itself and one).
The input comes as an integer number.
The output should be true for prime number and false otherwise.

  04.Decrypting Messages
You will receive a key (integer) and n characters afterward. Add the key to each of the characters and append them to a message. At the end print the message, which you decrypted. 
Input
    • On the first line, you will receive the key
    • On the second line, you will receive n – the number of lines, which will follow
    • On the next n lines – you will receive lower and uppercase characters from the Latin alphabet
Output
Print the decrypted message.
Constraints
    • The key will be in the interval [0…20]
    • n will be in the interval [1…20]
    • The characters will always be upper or lower-case letters from the English alphabet
    • You will receive one letter per line
    
  05.Balanced Brackets
You will receive n lines. On those lines, you will receive one of the following:
    • Opening bracket – “(“,
    • Closing bracket – “)” or
    • Random string
Your task is to find out if the brackets are balanced. That means after every closing bracket should follow an opening one. Nested parentheses are not valid, and if two consecutive opening brackets exist, the expression should be marked as unbalanced. 
Input
    • On the first line, you will receive n – the number of lines, which will follow
    • On the next n lines, you will receive “(”, “)” or another string
Output
You have to print “BALANCED”, if the parentheses are balanced and “UNBALANCED” otherwise.
Constraints
    • n will be in the interval [1…20]
    • The length of the stings will be between [1…100] characters
