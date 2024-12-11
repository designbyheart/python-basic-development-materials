file1 = open("Employees.txt", "a")

lst = []
for i in range(2):
    name = input("Enter the name of the employee: ")
    lst.append(name)  # + "\n")

file1.writelines(lst)
file1.close()
print("Data is written into the file.")
