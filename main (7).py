serving_cost = 1.00
labor_rate = 7.50
shop_rental = 800
utilities = 150
advertising = 100
servings_per_month = 1000
selling_price = 4.00

def profit_loss(serving_cost, labor_rate, shop_rental, utilities, advertising, selling_price, servings_per_month):
    expenses = serving_cost + labor_rate * 8 * 6 + shop_rental + utilities + advertising
    income = selling_price * servings_per_month
    return income - expenses

def what_if_analysis_expense(serving_cost, labor_rate, shop_rental, utilities, advertising, selling_price, servings_per_month):
    for i in range(-10, 11, 2):
        percent = i
        expenses = (serving_cost + labor_rate * 8 * 6 + shop_rental + utilities + advertising) * (1 + percent / 100)
        profit_loss = (selling_price * servings_per_month) - expenses
        print("Percent: {} Expenses: {:.1f} Profit/Loss: {:.1f}".format(percent, expenses, profit_loss))

def what_if_analysis_income(serving_cost, labor_rate, shop_rental, utilities, advertising, selling_price, servings_per_month):
    for i in range(-10, 11, 2):
        percent = i
        income = selling_price * servings_per_month * (1 + percent / 100)
        profit_loss = income - (serving_cost + labor_rate * 8 * 6 + shop_rental + utilities + advertising)
        print("Percent: {} Income: {:.1f} Profit/Loss: {:.1f}".format(percent, income, profit_loss))

while True:
    print("\nExpenses:")
    print("1. Cost per serving: {:.2f}".format(serving_cost))
    print("2. Labor rate per hour: {:.2f}".format(labor_rate))
    print("3. Shop rental per month: {:.2f}".format(shop_rental))
    print("4. Utilities per month: {:.2f}".format(utilities))
    print("5. Advertising budget per month: {:.2f}".format(advertising))
    print("\nIncome:")
    print("6. Selling price (each): {:.2f}".format(selling_price))
    print("7. Servings sold per month: {:.2f}".format(servings_per_month))
    print("\nAnalysis:")
    print("8. Profit/Loss Calculation")
    print("9. What If analysis with 10% variance")
    print("0. Exit")

  
    selection = int(input("\nEnter Selection (0 to Exit): "))

    if selection == 0:
        break
    elif selection == 1:
        serving_cost = float(input("Enter cost per serving: "))
    elif selection == 2:
        labor_rate = float(input("Enter labor rate per hour: "))
    elif selection == 3:
        shop_rental = float(input("Enter shop rental per month: "))
    elif selection == 4:
        utilities = float(input("Enter utilities per month: "))
    elif selection == 5:
        advertising = float(input("Enter advertising budget per month: "))
    elif selection == 6:
        selling_price = float(input("Enter selling price (each): "))
    elif selection == 7:
        servings_per_month = float(input("Enter servings sold per month: "))
    elif selection == 8:
        profit_loss_result = profit_loss(serving_cost, labor_rate, shop_rental, utilities, advertising, selling_price, servings_per_month)
        print("\nProfit/Loss: {:.1f}".format(profit_loss_result))
    elif selection == 9:
        print("\nExpenses:")
        what_if_analysis_expense(serving_cost, labor_rate, shop_rental, utilities, advertising, selling_price, servings_per_month)
        print("\nIncome:")
        what_if_analysis_income(serving_cost, labor_rate, shop_rental, utilities, advertising, selling_price, servings_per_month)
    else:
        print("\nInvalid selection. Please try again.")
