melon_cost = 1  # set melon_cost


def check_underpaid_customer(customer_order_data):
    """ Check underpay or overpay customer

        Open customer order data. Break each line into a list of words. 
        Assign the words to different variables (Customer's name, the amount of melon bought, 
        the amout paid). Calculate the expected pay and Compare it to actual pay.
        If actual pay > expected pay, print out overpay warning.
        If expected pay > actual pay, print out underpay warning. 
        """
    customer_order = open(customer_order_data)   # oepn a file
    for line in customer_order:
        line.rstrip()   # take out white spaces at the right
        word = line.split("|")   # split the line by "|"
        
        customer_name = word[1]  # set customer_name
        customer_bought = float(word[2])  # set customer_melon
        customer_paid = float(word[3])  # set customer_paid  
        customer_expected_paid = melon_cost * customer_bought  # set customer_expected
        
        if customer_paid > customer_expected_paid:
            print "%s overpaid. Paid: %.2f, Expected: %.2f." %(customer_name, customer_paid, customer_expected_paid) 
        
        elif customer_paid < customer_expected_paid:
            print "%s underpaid. Paid: %.2f, Expected: %.2f." %(customer_name, customer_paid, customer_expected_paid)
    customer_order.close
check_underpaid_customer("customer-orders.txt")
