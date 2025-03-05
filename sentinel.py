def sentinel_search():
    # Define the sentinel value
    sentinel_value = "exit"  # You can change this to any value you want to use as a sentinel

    # List to store user inputs
    user_inputs = []

    while True:
        # Get input from the user
        user_input = input("Enter a value (type 'exit' to stop): ")

        # Check if the user entered the sentinel value
        if user_input.lower() == sentinel_value:
            break  # Exit the loop if the sentinel value is entered

        # Store the input in the list
        user_inputs.append(user_input)

    # Perform any desired action with the collected inputs
    print("\nYou entered the following values:")
    for value in user_inputs:
        print(value)

# Call the function to run the program
sentinel_search()
