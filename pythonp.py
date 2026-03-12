# Function in Python

def greet():  # defining a function
    print("Hello, abc")  # function body

# greet()  # calling the function


def test(name):  # function with parameter
    print("Hello, " + name)

test("abc")  # calling the function with argument


def add(a, b):  # function with parameters
    return a + b  # returning the sum

result = add(5, 3)  # calling function
print("The sum is:", result)


# File Handling in Python

# file = open("example.txt", "w")  # opening a file in write mode
# file.write("Hello, this is an example of file handling in Python.")
# file.close()


'''
w - write mode: creates file or overwrites existing file
r - read mode: error if file does not exist
a - append mode: adds data at the end of the file
'''


# Save data to a file
def saveDataToFile():
    file = open("userdata.txt", "a")  # opening file in append mode

    for i in range(3):  # loop for 3 users
        name = input("Enter your name: ")
        age = input("Enter your age: ")

        file.write(f"Name: {name}, Age: {age}\n")  # writing data to file

    file.close()  # closing the file


saveDataToFile()  # calling function


# Read data from file
def readDataFromFile():
    file = open("userdata.txt", "r")  # opening file in read mode
    data = file.read()  # reading file content
    print("User Data:\n", data)
    file.close()  # closing the file


readDataFromFile()  # calling function