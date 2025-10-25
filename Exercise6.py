#("exercise_6\n")

correct_password = "12345"

max_attempts = 5# Set attempt counter and maximum attempts
attempts = 0

while attempts < max_attempts:# will Loop until it reach maximum attempts
    user_input = input("Enter the password: ") # Gets the password from user
    
    if user_input == correct_password:# these lines Check if password is correct
        print("Access granted, Welcome.")# Success message if the password
        break  # Exit the loop immediately
    else:
        attempts += 1 # Increases the attempt counter by 1
        remaining_attempts = max_attempts - attempts # Calculates the remaining tries
        
        if remaining_attempts > 0:# Check if user has attempts left and prints out the outcome of the attempts tried
            print(f"Wrong password {remaining_attempts} attempts remaining.")
        else:
            print("Maximum attempts reached, Authorities have been alerted")