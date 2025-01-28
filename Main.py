#This is a very old and dated programming question in order to test a programmers coding skills
#We will be using this as practice and as a warm up

#Write a program that prints the numbers from 1 to 100. But for multiples of certain numbers:

    #Print "Fizz" for numbers that are multiples of 3.
    #Print "Buzz" for numbers that are multiples of 5.
    #Print "FizzBuzz" for numbers that are multiples of both 3 and 5.

#If the number is not a multiple of 3 or 5, simply print the number.



#While this may seem daunting upon first sight, like many other problems, if we just break up the
#question into its seperate parts, we can see that it is pretty easy to translate into code

#So in order to print numbers from 1 to 100, we can see that we would need a for loop in Python to go from 1 to 100
#Please note that in Python the "range" convention is used where in most other languages an iterator would be manually declared and initialized, and then manually incremented within the for loop
#Range handles a lot of that manually coding/typing for us, but it is necessary to note that in it's arguments list/parameters that range has (A starting point, an ending point that is exclused/does not include the ending point itself, a pattern to increment by)
#Thus range would be Range(start point/number, stop point(non-inclusive), skip/steps to take)
#The default start point for range is 0, and the default skip/step is to increment by 1, thus if we wrote out range like this: range(5) it is assumed we start from 0, and stop when we reach 5, thus numbers 0, 1, 2, 3, 4 will be iterated through
#In our example below, we write range (1,101) because we do not want range to start at the number 0, it's default, and we want the for loop to stop when it reaches 101. When a step/skip/pattern
#parameter isn't provided, we can assume that 101-1 = 100, so a total of 100 numbers will be provided, and that will be in the range of 1-100
for iteration in range(1, 101):
    #Now that we know we will be iterating 100 times, we now need to figure the logic of the problem out.
    #We know we will be printing each number out, but at certain multiples we are to print different words out. Lets go through them case by case, as the problem does
    #We know if the number we iterate through is a multiple of 3, we print "Fizz"
    #We will be using the modulo operation and setting it equal to 0 so we know that we have an exact multiple instead of a rounded division (which would occur if we used the standard
    #Python "/" symbol)
    if (iteration % 3 == 0):
        print("Fizz")
    #We know if the number we iterate through is a multiple of 5, we print "Buzz"
    if (iteration % 5 == 0):
        print("Buzz")
    #If the number is both divisible by 5 and 3 cleanly, then we must account for that when we print "FizzBuzz"
    if (iteration % 5 == 0 and iteration % 3 == 0):
        print("FizzBuzz")
    else:
        print(iteration)


#PLEASE WORK ON THIS PROBLEM FURTHER TO CORRECT THE IF STATEMENTS PRINTING DUPLICATE FIZZ and BUZZ's WHEN THE CONDITIONALS ARE MET, for example when the condition "FizzBuzz" is met,
#with this code so is the individual conditional "Fizz" and individual conditional "Buzz", which both print out on seperate lines before "FizzBuzz" itself is printed