# Ask if user is already registered. If yes, inform user that no further action is needed. If not registered, move on to next check    
check_registered_voter = input("Are you already registered to vote?: ").lower()
if check_registered_voter in ('yes', 'y'):
    print("You are already registered. "
          "No further action is required."
        )
else:
    citizen_check = input("Are you a U.S. Citizen?: ").lower()
    if citizen_check in ('yes', 'y'):
        # Inform user they will need to have their DL number or ID number, the last 4 of their SSN, and their DOB. Once they have that info, they are ready to proceed.
        ready_to_register = input("You will need your CA Driver's License "
                                  "number or CA ID number, "
                                  "the last 4 of your Social Security Number," 
                                  "and you Date of Birth. Do you have these? "
                                  "Type y for yes or n for no: "
                                )
        if ready_to_register in ('yes', 'y'):
            # Ask user their age. Must be greater than or eqaul to 18
            age = int(input(("Enter your age: ")))
            # If 16 or 17 user may only pre-register to vote. Ask if user would like to pre-register
            if (age >= 16) and (age < 18):
                pre_register_check = input("You are only eligible to pre-register. "
                                           "Would you like to pre-register?: "
                                        ).lower()
                # If yes, prompt user for information
                if pre_register_check in ('yes', 'y'):
                    print("Follow instructions at the home page to "
                          "pre-register to vote."
                        )
                # If no thank you user and exit.    
                elif pre_register_check in ('no', 'n'):
                    print("Thank you for visitng.")
                else:
                    print("Invalid respone.")
            # If over 18 user can register
            elif age >= 18:
                print("You are eligible to vote!")
                # Ask if use is incarcerated for a felony
                background_check = input("Are you currently incarcerated "
                                         "for a felony offense?: "
                                        ).lower()
                # If yes, user cannot register
                if background_check in ('yes', 'y'):
                    print("You are currently not eligible to vote.")
                # If no, move to next check
                elif background_check in ('no', 'n'):
                    # Ask if user is enrolled in a confidential address program. 
                    address_check = input("Are you enrolled in a "
                                          "confidential address program?: "
                                        ).lower()
                    # If no, move to enrollment process
                    if address_check in ('no', 'n'):
                        print("Congratulations you are eligible to vote!")
                    # If yes, prompt user to contact Safe at Home
                    elif address_check in ('yes', 'y'):
                        print("Please contact Safe at Home")
                    else:
                        print("Invalid input.")
                else:
                    print("Invalid input.")
            else:
                print("Sorry, you are too young to register.")
        else:
            print("Please return when you have all necessary information.")
    elif not citizen_check.startswith('y'):
        print("You must be a U.S. Citizen to vote.")
    else:
        print("Invalid input")