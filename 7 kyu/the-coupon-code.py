from datetime import datetime 
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    date1 = datetime.strptime(current_date, "%B %d, %Y")
    date2 = datetime.strptime(expiration_date, "%B %d, %Y")
    if entered_code == correct_code and type(entered_code) == type(correct_code) and date1<= date2:
        return True
    else:
        return False
    