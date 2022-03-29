# Question 1
print("Hello Glasgow!")

# Question 2
x = int(input("Input number for x: "))
y = int(input("Input number for y: "))

print("Average of x and y is", (x+y)/2, "\n")

# Question 3a
module_code = input("Enter module code eg.(CSC1006):\n")

if module_code == "CSC1006":
    print("Mathematics II")
elif module_code == "CSC1007":
    print("Operating Systems")
elif module_code == "CSC1008":
    print("Data Structures & Algorithms")
elif module_code == "CSC1009":
    print("Object-Oriented Programming")
elif module_code == "CSC1010":
    print("Computer Networks")

print()
# Question 3b
for i in range(102, 65, -1):
    if i % 2 != 0:
        print(i)
