#Write a function that does not take any arguments and prints Hello World
def please_print():
    print "Hello World"
please_print()

#Write a function that takes a name as a string and prints Hi followed by the name.
def my_name(name):
    print "Hi", name
my_name("Bas")

#Write a function that takes two integers and multiplies them together.
#Print the result inside of the function.

def multiples(integer_one, integer_two):
    print integer_one * integer_two
multiples(1, 5)

#Write a function that takes a string and an integer and prints that
#string that many times.

def many(string, integer):
    print string * integer
multiples("hallo", 5)

#Write a function that takes an integer and prints Higher than 0
#if higher than zero and Lower than 0 if lower than zero.
#If the integer is 0 print Zero.

def high_low(integer):
    if integer < 0:
        print "lower than 0"
        #had colon after elif
    elif integer > 0:
        print "higher than 0"
    else:
        #did not put zero in quotes
        print "Zero"
high_low(0)

#Write a function that takes an integer and returns a boolean
#(True or False), depending on whether the number is evenly divisible by 3.

def divide(integer):
    #had if integer % 3:
    if integer % 3 == 0:
        return True
    else:
        return False

print divide(6)

#Write a function that takes a sentence as one string and
#returns the number of spaces.

def spaces(string):
    count = 0
    for character in string:
        # if character == " " + 1
        if character == " ":
            count += 1
    return count
print spaces("how many spaces do I have?")


#Write a function that can be passed a meal price and a tip percentage.
#It should return the total amount paid (price + price * tip). However:
#passing in the tip percentage should be optional; if not given, it should default to 15%.

def tip(meal_price, tip_percentage=0.15):
    # didn't get default
    return meal_price * tip_percentage + meal_price
print tip(5)


#Write a function that takes an integer as an argument and returns two pieces
#of information as strings Positive or Negative and Even or Odd.
#Then, write code that shows the calling of this function on a number and unpack
#what is returned into two variables sign and parity (whether its odd or even).
#Print sign and parity.

def calling(integer):
    sign = "positive"
    #didn't have the positive/ negative
    if integer < 1:
        sign = "negative"
    parity = "odd"
    if integer % 2 == 0:
        parity = "even"
        #did return calling
    return [sign, parity]
print calling(7)
