#MINI PROJECT -ATM FULL SYSTEM

balance =10000

print("Welcome to ATM")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice ==1:
    print("your Balance is:", balance)

elif choice == 2:
    amount = float(input("Enter deposit amount: "))
    balance = balance + amount
    print("Updated Balance:", balance)
elif choice ==3:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successfull")
        print("Remaining Balance:", balance)
    else:
         print("Insufficient Balance")

elif choice == 4:
     print("Thank you for using ATM")

else:
     print("Invalid choice")















         
                   
             
