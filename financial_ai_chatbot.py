# Financial AI Chatbot (Rule-Based Version)
def get_financial_advice(expenses):
    total = sum(expenses.values())
    savings = expenses.get('savings', 0)
    ratio = savings / total if total > 0 else 0

    if ratio >= 0.3:
        return "You're doing great! Keep saving."
    elif 0.1 <= ratio < 0.3:
        return "You're saving moderately. Try to cut some costs."
    else:
        return "Your savings are too low. Consider revising your budget."

print("Enter your monthly expenses below:")
rent = float(input("Rent: "))
food = float(input("Food: "))
transport = float(input("Transport: "))
shopping = float(input("Shopping: "))
savings = float(input("Savings: "))

user_expenses = {
    'rent': rent,
    'food': food,
    'transport': transport,
    'shopping': shopping,
    'savings': savings
}

advice = get_financial_advice(user_expenses)
print("\nFinancial Advice:", advice)

import matplotlib.pyplot as plt
labels = user_expenses.keys()
sizes = user_expenses.values()
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Your Monthly Spending Breakdown")
plt.show()
