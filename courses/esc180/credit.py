# You should modify initialize()
def initialize():
    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_update_day, last_update_month
    global last_country, last_country2
    global card_is_disabled
    global MONTHLY_INTEREST_RATE
    
    card_is_disabled = False
    
    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0
    
    last_update_day, last_update_month = -1, -1
    
    last_country = None
    last_country2 = None    
    
    MONTHLY_INTEREST_RATE = 0.05

    
def all_three_different(c1, c2, c3):
    if c1 != c2 and c1 != c3 and c2 != c3:
        return True
    return False


#what about the case when 2 are
#different but they are the first 2

def is_fraud(most_recent_country):
    global last_country2, last_country 
    if all_three_different(most_recent_country, last_country, last_country2) and not (last_country2 == None or last_country == None or last_country == None):
        return True
    
    last_country2 = last_country
    last_country = most_recent_country
    return False

#needs improvement
def date_same_or_later(day1, month1, day2, month2):
    #if month1 >= month2 and day1 >= day2:
    #    return True    
    #return False
    if month1 > month2:
        return True
    elif month1 == month2 and day1 >= day2:
        return True
    return False
        

#runs checks to ensure interest is not added mor than once per month 
#additionally it takes care of transfering each months balance into interest accuring account
def compute_interest_and_update_month(current_month, current_day):
    global last_update_month, last_update_day, cur_balance_owing_intst, cur_balance_owing_recent
    #if months since update > 0 move our recent balance to owing
    
    #if the user has a negative balance (overpaid) dont GIVE them interest lol
    if cur_balance_owing_recent < 0:
        return
    
    #hmmmmmmmmmm make sure to test this
    for i in range(last_update_month, current_month):
        cur_balance_owing_intst *= 1 + MONTHLY_INTEREST_RATE
        
        if i == last_update_month:
            cur_balance_owing_intst += cur_balance_owing_recent
            cur_balance_owing_recent = 0
    last_update_month = current_month
    last_update_day = current_day
    
    
def purchase(amount, day, month, country):    
    global cur_balance_owing_recent, card_is_disabled
    if card_is_disabled or is_fraud(country):
        card_is_disabled = True
        return "error"
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return "error"
    #always run, since it makes sure to not double count anything
    compute_interest_and_update_month(month, day)
    cur_balance_owing_recent += amount

def amount_owed(day, month):
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return "error"
    compute_interest_and_update_month(month, day)
    return cur_balance_owing_recent + cur_balance_owing_intst    

def pay_bill(amount, day, month):
    global cur_balance_owing_recent, cur_balance_owing_intst
    if card_is_disabled:
        return "error"
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return "error"
    
    compute_interest_and_update_month(month, day)
    
    
    if amount <= cur_balance_owing_intst:
        cur_balance_owing_intst -= amount
        return

    #elif amount > current owed interest balance
    amount -= cur_balance_owing_intst
    cur_balance_owing_intst = 0
    cur_balance_owing_recent -= amount
    
    return
