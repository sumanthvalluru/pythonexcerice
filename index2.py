from datetime import datetime
import pytz  # Import the pytz module for time zone information

# Get the current date and time
current_datetime = datetime.now()

# Set the time zone to IST (Indian Standard Time)
ist = pytz.timezone('Asia/Kolkata')
current_datetime_ist = current_datetime.astimezone(ist)

# Format the date in the specified format
formatted_date = current_datetime_ist.strftime("%a %b %d %H:%M:%S %Z %Y")

# Print the formatted date
print("Current Date:", formatted_date)
