n = 2  
while True:  
    i = 1  
    while i <= 10:  
        print("%d X %d = %d\n" % (n, i, n * i))  
        i += 1  
    choice = int(input("Do you want to continue printing the table? Press 0 for no: "))  
    if choice == 0:  
        print("Exiting the program...")  
        break  
    n += 1  
print("Program finished successfully.")  