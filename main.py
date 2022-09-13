import calendar 
#Access to other modules
print("Hello welcome to py calendar")
print("")
print("What is your name?")
name = input()
print(f"nice to meet you {name}, My name is harry")
print("")
print("which year you wanna get in? for example 2022")
example = calendar.TextCalendar(firstweekday =0) 
#data stored in example, 
#firstweekday value: -1 Sunday, 0 monday, 1 Tuesday  
year = int(input())
# Year access
print("")
print("Enter width size? for example 1, 2, 3 ,4,...,5")
width = int(input())   
# Size 3
data = (example.formatyear(year, width)) 
print("")
print(f"Your have entered {year}, with width size of {width}, your data is given below.")
print("")
print(data)
#Print command 