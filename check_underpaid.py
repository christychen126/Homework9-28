melon_cost = 1  # set melon_cost


def check_underpaid_customer(customer_order_data):
    customer_order = open(customer_order_data)   # oepn a file
    for line in customer_order:
        line.rstrip()   # take out white spaces at the right
        word = line.split("|")   # split the line by "|"
        customer_name = word[1]  # set customer_name
        customer_bought = float(word[2])  # set customer_melon
        customer_paid = float(word[3])  # set customer_paid  
        customer_expected_paid = melon_cost * customer_bought  # set customer_expected
        if customer_paid != customer_expected_paid:
            print customer_name, "paid %.2f, expected %.2f" %(customer_paid, customer_expected_paid) 
            #if customer_paid != customer_expected print warning
    customer_order.close
check_underpaid_customer("customer-orders.txt")
