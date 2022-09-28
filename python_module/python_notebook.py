"""
This is your python assignment. Please submit this assignment to canvas after it is complete.

one # is meant to be un-commented and run as code
two ## indicates instructions for coding exercise
three ### are individual/group exercises to be done on day 2

"""


## Create a message and assign it to the variable, message.
message = ""

## What year were you born?
birth_year = ''

## What is the value of pi?
pi = ''


## What is the data type of message? Print the output of the type() function.
type_ms = ...
print(type_ms)

## What is the data types of birth_year? Print the output of the type() function.


### IND -- What is the data type for pi? Print the output of the type() function


## Print your message. Use the message variable you created as an argument in the print function.


## Print your age using the following code:
#print("I was born in", birth_year)

### IND  Print " the value of pi is:" and the variable pi in the same print statement.


## Import the math package. Don't worry, this does not require an installation. The math package comes with base python!


## Practice using functions from packages.
## Use the math module to find the square root of 100 (function is sqrt() and argument is 100). Assign the output to a variable, answer.
answer = ''
#print("The square roof of 100 is", answer)

## Use the math module to find the log2 of 4 (function is log2() and argument is 4). Assign the output to a variable and print.


### IND  Import the base python os module. From this module, use the function getcwd() and assign it to cwd.
  ## Print the output of getcwd. What does this function do? what does cwd stand for?

#import ...
#cwd = ...
#print(cwd)

## install the pandas package using the error prompted by pycharm. Import pandas as pd.


## Install the numpy package using pip in the terminal. IND -- Import package as np.
    # when you are on a server without administrative privilege, use --user flag.


# Populate the list, animal_ls, with the names of 4 animals
animal_ls = []

## Using the indexing method, print out the 1st element in the list. Was the output what you were expecting?

## Using the indexing method, print out the 4th element in the list. Why do you get an error?
#print("the fourth animal is:", animal_ls[4])

## Initialize a list, and populate this list with 5 numbers. Assign the list to the variable name, num_ls (for number list)


### IND  pass the num_ls variable into the functions min(), max(), len(), and mean().
    # The mean function is from the numpy package.
    # The len() function calculates the length of the variable.


### IND  Use the len() function on the message variable from earlier.
    # What is the difference between the using len() on a list variable vs a string variable?


## Make a function called squared() that takes in one argument, x, and outputs x to the power of 2
def squared(x):
    """write instructions here"""

x_squared = squared(x=5)

#print(x_squared)

## Now use the pow() function from the math module to calculate 2^5.


## Make a function called power() that takes in two arguments, x and y, and outputs the value of x^y
    # use your function to determine 2^5


### IND  Use the comparative operator == to see if power() and pow() produce the same output.
    ## What data type is returned using comparative operators? (hint: it starts with a B and ends with oolean)


# Lets practice for-loops on a string. Previously, you created an variable called message.
# write a for loop that iterates over every character in your message and prints out that character.

for character in message:
    "write instructions here"


### IND  Previously, you created a list of animals, called animal_ls.
    # Write a for loop to parse through animal_ls that prints out the length of each list item

for animal in animal_ls:
    'do something here'



#######################################################################################################################
# Project: design primers for gene1, gene2, and gene3.
    # There are a lot of different ways to do this!
    # If you want a challenge, consider writing a function (def) to design primers
    # If you want even more of a challenge, use a for-loop to iterate over each gene.

gene1 = "gtgggagacatagtggtcaaggtccccccgagtgtggacgaaaagctggccgatttgatagcaaagactatcgcggagagactgaaaaccctcgcaaggctcaatgagatgctcaagaactccgaactctcagaagaggatgcaatagaactcggacggaaggcgaaaatgggaaggggcgagtaccttgagagaagatattcttctcgtagttaa"
gene2 = "atgagagaagatattcttctcgtagttaacacaaacgtgctattctctttcttcgggaaatcaacagtaaccagagagctcgtgttcttggtatcagggagacttataagtcccgagtttgcactggaagagcttcacgagcacagggacgaagtcctgaaaaaagcaaagatcggagagaaagagttcgaggaaatactgtccgttcttaaagagcatgtcatattcgtaaacgaggggttctacgccgagttcatacctctagcactcgaataa"
gene3 = "atggaagttatccgtctgctgaagagaaagtcccaagacaaggttgagttcgtgcgcgatctggtagttttcatggcttctcccgacgttgatttttccaacgaggttctgtttaaggacgccgttgatgagatatactcaatcctgagggaggaagtcattgaaaatgggaacaaagagctagccagcgcgtatgaaaaagccgttctccttagagctgcggtttttggagaggaaatggatccgaaaaagctccttaagggtattctcgaggagctgaggtga"

## Other considerations:
    # Generally, it is good practice for your primers to have a 3' end that ends with "c" or "g", but this is not necessary and might require more advanced skills (if-else statements).
    # Primer sequences are usually between 18 and 21 bp long.
    # If you want to be fancy, consider calculating the melting temperature of each primer. (crudly, the Tm increases ~2 C for each base.)

## Here is a function to reverse compliment a sequence. The function is called rev_comp() and takes a string as an argument.
def rev_comp(sequenec):
    complement_dictionary = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
    rev_complement = "".join(complement_dictionary.get(base, base) for base in reversed(sequenec))
    return rev_complement

## write a script to print the sequence of the forward and reverse primers in fasta format.
    ## '\n' will print a new line. You could also stack two print statements on separate lines to separate the fasta header from the sequence.


