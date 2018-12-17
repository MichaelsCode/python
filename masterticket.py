SERVICE_CHARGE = 2

TICKET_PRICE = 10

tickets_remaining = 100


def calculate_price(number_of_tickets):
    return (TICKET_PRICE * number_of_tickets) + SERVICE_CHARGE


while tickets_remaining >= 1:
    print("These are the remaining gig tickets: {}".format(tickets_remaining))
    customer_name = input("What is your name?  ")
    number_of_tickets = input("How many tickets would like, {}?  ".format(customer_name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("On no, We ran into an issue. {}. Please try again".format(err))
    else:
        amount_due = calculate_price(number_of_tickets)
        print("Total due is: {}  ".format(amount_due))
        should_proceed = input("Do you want to proceed?  Y/N  ")
        if should_proceed.lower() == 'y':
            print("SOLD!")
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you anyways, {}".format(customer_name))
print("Sorry the tickets are all sold out!!! :(")
# test for git
