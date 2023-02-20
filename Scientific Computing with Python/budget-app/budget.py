class Category:
    def __init__(self, category_name):
        # initialize instance variable with category name
        self.category_name = category_name  
        # initialize empty list to store transactions
        self.ledger = []   

    def __str__(self):
        # create a title string with centered category name
        title = self.category_name.center(30, "*")  
        # iterate through transactions list and format each item with specified width and precision
        items = [f"{item['description'][0:23]:23}{item['amount']:>7.2f}" for item in self.ledger] 
        # create a total string with balance to 2 decimal places
        total = f"Total: {self.get_balance():.2f}"  
        # return string with joined title, transactions, and total strings with newline in between
        return "\n".join([title] + items + [total]) 

    def deposit(self, amount, description=""):
        # add a dictionary with transaction details (amount and description) to the transactions list
        self.ledger.append({"amount": amount, "description": description})  

    def withdraw(self, amount, description=""):
        # if enough funds are available for withdrawal
        if self.check_funds(amount):  
            # add a dictionary with transaction details (negative amount and description) to the transactions list
            self.ledger.append({"amount": -amount, "description": description})  
            # return True to indicate successful withdrawal
            return True  
        # otherwise, return False
        return False  

    def get_balance(self):
        # return the sum of all amounts in the transactions list
        return sum([item["amount"] for item in self.ledger])  

    def transfer(self, amount, budget_category):
        # if enough funds are available for transfer
        if self.check_funds(amount):  
            # withdraw specified amount with description of transfer to the target budget category
            self.withdraw(amount, f"Transfer to {budget_category.category_name}")  
            # deposit the same amount with description of transfer from the current budget category to the target budget category
            budget_category.deposit(amount, f"Transfer from {self.category_name}")  
            # return True to indicate successful transfer
            return True  
        # otherwise, return False
        return False  

    def check_funds(self, amount):
        # return True if the current balance is greater than or equal to the specified amount, otherwise return False
        return self.get_balance() >= amount  


def create_spend_chart(categories):
    category_names = []
    spent = []
    
    # Iterate through each budget category and calculate the total amount spent and append it to spent list
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total -= item["amount"]
        spent.append(round(total, 2))
        category_names.append(category.category_name)

    # Calculate the percentage of money spent for each budget category and append it to spent_percentage list
    spent_percentage = [round((category / sum(spent)) * 100, 2) for category in spent]

    # Create the bar chart graph
    graph = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        graph += str(i).rjust(3) + "| "
        for percentage in spent_percentage:
            if percentage >= i:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    # Add the x-axis line to the graph
    graph += " " * 4 + "-" * (len(categories) * 3 + 1) + "\n"

    # Find the length of the longest category name
    longest_name_length = max([len(name) for name in category_names])
    
    # Iterate through the length of the longest category name and add each character to the graph
    for i in range(longest_name_length):
        graph += " " * 5
        for name in category_names:
            if i >= len(name):
                graph += "   "
            else:
                graph += name[i] + "  "
        graph += "\n"

    # Remove the trailing newline and return the graph
    return graph[:-1]
