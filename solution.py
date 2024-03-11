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
    transactions = {}

    #Iterating through our list to know if it was income received or a card payment
    for i in range(len(A)):
        # Checking whether it's income received or a card payment
        # income received
        if A[i] > 0:
            income += A[i]

        # card payment
        elif A[i] < 0:
            card_payment -= A[i] 

       # Extracting year, month, and day from the transaction date
        trans_year, trans_month, trans_day = map(int, D[i].split('-'))
        trans_date = (trans_year, trans_month)

        # Count the number of transactions for each month
        transactions[trans_date] = transactions.get(trans_date, 0) + 1


    # Deduct card payment only if there are less than 3 transactions of 100 or more in a month
    for trans_date, count in transactions.items():
        if count < 3:
            card_payment -= 5

    # total at the end of the year
    result = income - card_payment
    return result
        
# Example usage:
A = [100, 100, 100, -10]
D = ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]
final_result = solution(A, D)
print(final_result)