from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("current date:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    days = int(input("Enter the number of days to add to the current date: "))
    today = datetime.now()
    future_date = today + timedelta(days=days)
    formatted_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Future date: ", {formatted_date})
calculate_future_date('days')


