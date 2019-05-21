def main():
    # Create a list to store days of the week.
    days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                 "Saturday", "Sunday"]
    sales_list = get_sales(days_list)
    total = calculate_total_sales(sales_list)
    min_sale_day = get_min_sale(sales_list, days_list)
    max_sale_day = get_max_sale(sales_list, days_list)

    print()
    input("Press the Enter key to terminate program...")

def get_sales(days_list):
    # Create an empty list to store sales.
    sales_list = []
     # Get the store's sales for each day of the week.
    for day in days_list:
        sales = float(input("Enter the sales for " + day + ": "))
        sales_list.append(sales)
    # Return the sales list.
    return sales_list

def calculate_total_sales(sales_list):
    # Set accumulator to 0.
    total = 0
    # Use for loop to calculate total.
    for sale in sales_list:
        total += sale
    print()
    print("Here is the weekly sales total: $", format(total, ',.2f'), sep='')

def get_min_sale(sales_list, days_list):
    # Use index to find lowest sale day.
    min_sale_day = sales_list.index(min(sales_list))
    day_of_week = days_list[min_sale_day]
    print("The lowest sale was on ", day_of_week, " with $", \
          format(min(sales_list), ',.2f'), ".", sep='')

def get_max_sale(sales_list, days_list):
    # Use index to find highest sale day.
    max_sale_day = sales_list.index(max(sales_list))
    day_of_week = days_list[max_sale_day]
    print("The highest sale was on ", day_of_week, " with $", \
          format(max(sales_list), ',.2f'), ".", sep='')
   

# Call main function.
main()


         
    
                 
