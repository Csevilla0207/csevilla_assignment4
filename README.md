# Assignment 4

## Description

The pixel transaction report program is designed to process banking transaction data. It calculates account balances for customers based on their deposit and withdrawal transactions. 

## Author

Kimi Sevilla

## Assignment

Module 4 assignment 4

## PiXELL Transaction Report

Input Validation: The program validates transaction types and amounts to ensure data is processed. This reduces the chance of errors and ensures accuracy.

Exception Handling: Comprehensive exception handling is implemented throughout the program.

Catching FileNotFoundError to inform users if the CSV file is missing.

Handling ValueError during the conversion of transaction amounts to manage invalid inputs.

Using a generic Exception block to catch any errors.

By implementing these tools and techniques, the PiXELL Transaction Report program ensures reliable software that meets the needs of users.

## Code Modification:

Added exception handling throughout the pixell_transaction_report.py program.

Wrapped the file reading and data processing logic in a try-except block to catch and handle FileNotFoundErro` and other potential exceptions.

Added validation checks for transaction types and amounts to ensure data integrity and prevent runtime errors.

Collected and reported rejected records with appropriate error messages for better debugging and user feedback.



 