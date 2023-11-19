import datetime

#Get the current date
current_date = datetime.date.today()

#Get user input
payer_name = input("Enter payer's name: ")
amount_paid = float(input("Enter the amount paid: "))
receipt_number = input("Enter receipt number: ")

#Generate and print the receipt
receipt = f"""
------------------------ Payment Receipt ------------------------
Date: {current_date}

Payer: {payer_name}
Amount Paid: ${amount_paid:.2f}
Receipt Number: {receipt_number}

Thank you for your payment!
-----------------------------------------------------------------
"""

print(receipt)

#Optionally, save the receipt to a file
file_name = "payment_receipt.txt"
with open(file_name, "w") as file:
    file.write(receipt)

print(f"Receipt saved as {file_name}.")
