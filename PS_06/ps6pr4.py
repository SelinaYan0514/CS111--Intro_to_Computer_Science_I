# ps6pr4.py (Problem Set 6, Problem 4)
#
# TT Securities    
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the max price and its day')
    print('(5) Find the min single-day change and its day')
    print('(6) Test a threshold')
    print('(7) Your invetsment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.

#option 3
def avg_price(a):
    """takes a list of 1 or more prices and computes and returns the average price
    """
    sum = 0
    for x in a:
        sum += x
        
    return sum/len(a)


#option 4
def max_day(b):
    """takes a list of 1 or more prices and computes and returns the day 
    (i.e., the index) of the maximum price
    """ 
    maximum_index = 0
    
    for i in range(len(b)):
        if b[i] > b[maximum_index]:
          maximum_index = i
          
    return maximum_index


#option 5
def min_change_day(c):
    """takes a list of 2 or more prices and computes and returns the day 
    (i.e., the index) of the minimum single-day absolute change in price
    """
    min_change = abs(c[1] - c[0])  # Initialize minimum change
    min_index = 1  # Initialize index of minimum change
    for i in range(2, len(c)):
        change = abs(c[i] - c[i-1])
        if change < min_change:
            min_change = change
            min_index = i
    return min_index


#option 6
def any_above(d, threshold):
    """
    The function should return True if there are any prices above the 
    threshold, and False otherwise
    """
    for x in d:
        if x > threshold:
            return True
    else:
        return False
    
     
#option 7
def find_tts(e):
    """
    find the best days on which to buy and sell the stock whose prices are given 
in the list of prices. The buy and sell days that you determine should maximize 
the profit earned, but the sell day must be greater than the buy day. The function 
should return a list containing three integers:the buy day, the sell day, and 
the resulting profit. 
    """
    buy_day = 0
    sell_day = 0
    max_profit = 0
    for i in range(len(e)):
        for j in range(i+1, len(e)):
            profit = e[j] - e[i]
            if profit > max_profit:
                max_profit = profit
                buy_day = i
                sell_day = j
    return [buy_day, sell_day, max_profit]

        



    
    
    
def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            print('The average price is', avg_price(prices))
            
        elif choice == 4:
            max_price = prices[max_day(prices)]
            print("The max price is", max_price, "on day", max_day(prices))
            
        elif choice == 5:
             price1 = prices[min_change_day(prices) - 1]
             price2 = prices[min_change_day(prices)]
             print("The min single-day change occurs on day", min_change_day(prices))
             print("when the price goes from", price1, "to", price2)
            
        elif choice == 6:
            threshold = int(input("Enter the threshold:"))
            if any_above(prices, threshold) == True:
                print("There is at least one price above", threshold)
            else:
                print("There are no prices above", threshold)
                
        elif choice == 7:
            result = find_tts(prices)
            buy_day = result[0]
            sell_day = result[1]
            max_profit = result[2]
            
            print("Buy on day", buy_day, "at price", prices[buy_day])
            print("Sell on day", sell_day, "at price", prices[sell_day])
            print("Total profit:", max_profit)
            
      
    print('See you yesterday!')
