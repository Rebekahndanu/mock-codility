#We have a list of transactions made using a bank account
# the balance at the beginning of the year is 0
# if the transaction was made when the account balance was below 0, it was a card payment
# if the transactio was done when the account balance was above 0 it was income received
# we also have a list of the date the transactions were made
# 5/= is deducted every month for card payment
# if more than 3 transactions of 100 are made there will be no card payment
# what is our final balance?



def solution(A, D):

    # Amount at the beginning of the year
    bal = 0

    # variables i will use to calculate my positive and negative numbers in the list
    income = 0
    card_payment = 0

    # Dictionary to store transaction counts for each month
    transaction_counts = {}

    # Extracting year and month from the current transaction date
    # current_transaction_year = D[i][0]
    # current_transaction_month = D[i][1]

    #Iterating through our list to know if it was income received or a card payment
    for i in range(len(A)):
        # Checking whether it's income received or a card payment
        if A[i] > 0:
            income += A[i]

        elif A[i] < 0:
            card_payment -= A[i] 

        # Count the number of transactions for each month
        month = (D[i][0], D[i][1])
        transaction_counts[month] = transaction_counts.get(month, 0) + 1

    # Deduct card payment only if there are less than 3 transactions of 100 or more in a month
    for month, count in transaction_counts.items():
        if count < 3:
            card_payment += 5

    # total at the end of the year
    result = income - card_payment
    return result
        
# Example usage:
A = [50, -5, 100, -200, 150]
D = [(2024, 1), (2024, 1), (2024, 2), (2024, 2), (2024, 2)]
final_result = solution(A, D)
print("Final result:", final_result)