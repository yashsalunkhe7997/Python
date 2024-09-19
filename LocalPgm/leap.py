
# def leap(year):
#     leap_year=year%4==0
#     return leap_year
# year=1800
# result=leap(year)
# print(f"{year } :{result} This is leap year ")

year=2000

if year%4==0 and year%100 != 0 or  year %400 == 0  :
    print(f" {year} is leap year  ")

else:
    print(f" {year} is not leap year ")


# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# # Input from the user
# year = int(input("Enter a year: "))

# # Output whether the year is a leap year or not
# if is_leap_year(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")