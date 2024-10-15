import csv
import os

valid_transaction_types = ['deposit', 'withdraw']
customer_data = {}
rejected_records = []
transaction_count = 0
total_transaction_amount = 0

os.system('cls' if os.name == 'nt' else 'clear')

# Open the CSV file
with open('bank_data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip the header row
    for row in reader:
        # Reset valid record and error message for each iteration
        valid_record = True
        error_message = ''

        # Check if the row has exactly 3 elements
        if len(row) != 3:
            valid_record = False
            error_message += 'Record does not contain exactly 3 items. '
            rejected_records.append((row, error_message.strip()))
            continue  # Skip to the next record

        # Extract the customer ID
        customer_id = row[0].strip()
        
        # Extract the transaction type
        transaction_type = row[1].strip()
        
        ### VALIDATION 1 ###
        # Validate transaction type
        if transaction_type not in valid_transaction_types:
            valid_record = False
            error_message += 'Not a valid transaction type. '

        # Extract and validate the transaction amount
        ### VALIDATION 2 ###
        try:
            transaction_amount = float(row[2].strip())
        except ValueError:
            valid_record = False
            error_message += 'Non-numeric transaction amount. '

        if valid_record:
            # Initialize the customer's account balance if it doesn't already exist
            if customer_id not in customer_data:
                customer_data[customer_id] = {'balance': 0, 'transactions': []}

            # Update the customer's account balance based on the transaction type
            if transaction_type == 'deposit':
                customer_data[customer_id]['balance'] += transaction_amount
                transaction_count += 1
                total_transaction_amount += transaction_amount
            elif transaction_type == 'withdraw':
                customer_data[customer_id]['balance'] -= transaction_amount
            
            # Record transactions in the customer's transaction history
            customer_data[customer_id]['transactions'].append((transaction_amount, transaction_type))
        
        ### COLLECT INVALID RECORDS ###
        if not valid_record:
            rejected_records.append((row, error_message.strip()))

print("PiXELL River Transaction Report\n===============================\n")
# Print the final account balances for each customer
for customer_id, data in customer_data.items():
    balance = data['balance']

    print(f"\nCustomer {customer_id} has a balance of ${balance:.2f}.")
    # Print the transaction history for the customer
    print("Transaction History:")
    for transaction in data['transactions']:
        amount, type = transaction
        print(f"\t{type.capitalize()}: ${amount:.2f}")

# Calculate and print average transaction amount
if transaction_count > 0:
    print(f"\nAVERAGE TRANSACTION AMOUNT: ${total_transaction_amount / transaction_count:.2f}")
else:
    print("\nAVERAGE TRANSACTION AMOUNT: $0.00")

print("\nREJECTED RECORDS\n================")
for record in rejected_records:
    print("REJECTED:", record)
