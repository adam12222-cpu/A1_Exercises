#("exercise5") title at the beginning of the output in the console

dim={1:31,
     2:28,
     3:31,
     4:30,
     5:31,
     6:30,
     7:31,
     8:31,
     9:30,
     10:31,
     11:30,
     12:31
     }#(dim)days in a month, states the month and the number of days

month=int(input("Enter the Chosen Month Number:"))#user input is needed

if month in dim:#gathers all the days from the dictionary, this is where the 
    if month == 2:
        leap=input("Is it a Leap Year? (yes/no):")
        if leap =="yes":
            print("29_days")
        else:
            print("28_days")#unless it isnt  
            
    else: 
        days=dim[month]
        print(f"{days} days")#outputs the number of days
        