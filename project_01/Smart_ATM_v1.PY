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
print("balance", data["balance"])