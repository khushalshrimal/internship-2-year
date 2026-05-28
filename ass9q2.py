#2) Explore more datetime function and uses in pandas 
 
import pandas as pd


current = pd.Timestamp.now()

print("Current DateTime:", current)

print("Current Date:", current.date())

print("Current Time:", current.time())

print("Year:", current.year)

print("Month:", current.month)

print("Day:", current.day)

print("Weekday:", current.day_name())

dates = pd.date_range(start="2026-01-01", periods=5)

print("\nDate Range:")
print(dates)

# Str -> Date time
date = pd.to_datetime("2026-05-23")

print("\nConverted Date:", date)

#diff btw 2 dates
date1 = pd.to_datetime("2026-05-01")
date2 = pd.to_datetime("2026-05-23")

difference = date2 - date1

print("\nDifference:", difference)

# Add Days
date3 = date1 + pd.Timedelta(days=10)

print("\nNew Date:", date3)