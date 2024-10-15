import csv
import os

valid_transaction_types = ['deposit', 'withdraw']
customer_data = {}
rejected_records = []
transaction_count = 0
transaction_counter = 0
total_transaction_amount = 0
valid_record = True
error_message = ''

# Clear the console for better readability
os.system('cls' if os.name == 'nt' else 'clear')

try:
    # Open the CSV file containing bank transaction data
    with open('bank_data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        # Skip the header row
        next(reader)

        for row in reader:
            # Reset valid record flag and error message for each iteration
            valid_record = True
            error_message = ''

            # Extract the customer ID from the first column
            customer_id = row[0]

            # Extract the transaction type from the second column
            transaction_type = row[1].strip().lower()  # Normalize transaction type

            # Initialize transaction amount
            transaction_amount = 0.0
            
            # Try to convert the transaction amount to a float
            try:
                transaction_amount = float(row[2])
            except ValueError:
                valid_record = False
                error_message = "Non-numeric transaction amount."

            # VALIDATION: Check for valid transaction type
            if transaction_type not in valid_transaction_types:
                valid_record = False
                error_message = "Not a valid transaction type."

            # If valid, update customer data
            if valid_record:
                # Initialize the customer's account balance if it doesn't already exist
                if customer_id not in customer_data:
                    customer_data[customer_id] = {'balance': 0.0, 'transactions': []}

                # Update the account balance based on the transaction type
                if transaction_type == 'deposit':
                    customer_data[customer_id]['balance'] += transaction_amount
                elif transaction_type == 'withdraw':
                    customer_data[customer_id]['balance'] -= transaction_amount

                # Record the transaction in the customer's transaction history
                customer_data[customer_id]['transactions'].append((transaction_amount, transaction_type))
                # Increase the counters for valid transactions
                transaction_count += 1
                total_transaction_amount += transaction_amount
                transaction_counter += 1
            else:
                # Collect invalid records with error messages
                rejected_records.append((row, error_message))

except FileNotFoundError as e:
    print(f"ERROR: File not found. {e}")
except Exception as e:
    print(f"ERROR: {e}")

# Output the transaction report
print("PiXELL River Transaction Report\n===============================\n")
# Print the final account balances for each customer
for customer_id, data in customer_data.items():
    balance = data['balance']
    print(f"\nCustomer {customer_id} has a balance of ${balance:,.2f}.")
    print("Transaction History:")
    for transaction in data['transactions']:
        amount, type = transaction
        print(f"\t{type.capitalize()}: ${amount:,.2f}")

# Calculate and print the average transaction amount
if transaction_counter > 0:
    print(f"\nAVERAGE TRANSACTION AMOUNT: ${total_transaction_amount / transaction_counter:,.2f}")
else:
    print("\nNo valid transactions were processed.")

# Print the rejected records
print("\nREJECTED RECORDS\n================")
if rejected_records:
    for record in rejected_records:
        print("REJECTED:", record)
else:
    print("No records were rejected.")
