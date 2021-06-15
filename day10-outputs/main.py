#function with outputs

def my_function():
  return 3 * 2

output = my_function()

#using docstrings
def format_name(f_name, l_name):
  """
    Take a first and last name and format it to return the title case version of the name.
  """
  if f_name == "" or l_name == "":
    return "You didn't provide a valid name"

  return f"{f_name.title()} {l_name.title()}"

name = format_name("alex", "lee")
print(name)

#leap year
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  if month > 12 or month < 1:
    return "Invalid month"

  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return 29
  return month_days[month - 1]

#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

