print("=================================")
print("    Welcome to the SMART ATM     ")
print("=================================")

data = {
    "name": "haziqa",
    "pin": 1234,
    "balance": 10000
}

name = input("Please enter your name: ")
pin = int(input("To check your balance, please enter your PIN: "))

if name == data["name"] and pin == data["pin"]:

 print("=================================")
 print("       Balance Information       ")
 print("=================================")

 print("1. Check Balance")
 print("2. Deposit")
 print("3. Withdraw")
 print("4. Exit")
 
 balance = "1"
 deposite = "2"
 withdraw = "3"
 exit = "4"
 option = input("Please select an option (1-4): ")
else:
   print("ERROR: Invalid name or PIN.")
exit()
  
if option == balance:
   print("Your balance is:", data["balance"])
   
elif option == deposite:
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
     data["balance"] += amount
     print("Deposit successful. Your new balance is:", data["balance"])
    else:
     print("Invalid deposit amount.")   
elif option == withdraw: 
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= data["balance"] and amount > 0:
        data["balance"] -= amount
        print("Withdrawal successful. Your new balance is:", data["balance"])
    else:
        print("Insufficient funds.")
        
if option == exit:
    print("=================================")
    print("Thank you for using Smart ATM.")
    print("Have a great day!")
    print("=================================")
