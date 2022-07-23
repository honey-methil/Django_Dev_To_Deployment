# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create a function
def sayHello(name = 'Sam'):
    print("Hello " + name)

sayHello()

# Function which returns value
def getSum(num1, num2):
    total = num1 + num2
    return total

numSum = getSum(4, 5)
print(numSum)

def addOnetoNum(num):
    num = num +1 
    return num

num = 5
newNum = addOnetoNum(num)
print(newNum)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSumLambda = lambda num1, num2 : num1 + num2
print(getSumLambda(9,10))

addOneLambda = lambda num: num+1
print(addOneLambda(99))