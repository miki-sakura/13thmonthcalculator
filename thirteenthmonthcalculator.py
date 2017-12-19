hours_in_days = 8.0
days_in_month = 22
month_in_hours = hours_in_days * days_in_month
base_salary = 10000

# put the total number of lates / absences you have (in hours)..
# ..per month / index
# meaning, each index corresponds to a month of the year
# NOTE: the last index's (December's) value is composed of the 1st half of the current year..
# .. and the last half of the previous year (in relation to the salary period)
attendance = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def compute_13th_month_pay():
    for idx, val in enumerate(attendance):
        attendance[idx] = (month_in_hours - val) / month_in_hours
        
compute_13th_month_pay()
total = 0.0
for val in attendance:
    total += val
    
month_13_salary = (total / 12) * base_salary
print month_13_salary
