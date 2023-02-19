def interest_formula(p, r, t):
    a = p * (1 + r / 100) ** t
    print("Compound Interest: " + str(round(a - p, 2)))

def collect_input():
    client_principal = float(input("Principle (amount): "))
    client_time = float(input("Time: "))
    client_rate = float(input("Rate: "))
    return client_principal, client_time, client_rate

def calculateCompoundInterest():
    line_break = "---"

    client_principal_1, client_time_1, client_rate_1 = collect_input()
    interest_formula(client_principal_1, client_rate_1, client_time_1)
    print(line_break)

    client_principal_2, client_time_2, client_rate_2 = collect_input()
    interest_formula(client_principal_2, client_rate_2, client_time_2)
    print(line_break)

    client_principal_3, client_time_3, client_rate_3 = collect_input()
    interest_formula(client_principal_3, client_rate_3, client_time_3)
    
    
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you


    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
