"""
Filename:    group1FinalProject.py
Description: A quick and simple Python program to make airline reservations
Author:      Camden Amy, Johnny Romero, Diego Mendoza
Class:       ITIS-30-46475 Intro to Computer Programming
Date:        07/21/2026
"""

# Price constants
FIRST_PRICE = 500       
COACH_PRICE = 199       
TAX_RATE = 0.0775       

# Seating layout constants
FIRST_ROWS = 2      
FIRST_SEATS_PER_ROW = 4   
COACH_ROWS = 10        
COACH_SEATS_PER_ROW = 4

# Names are shortened to this length on the chart only
NAME_DISPLAY_LENGTH = 12    

# Change denominations, largest to smallest, stored in whole cents.
# Each entry is (value in cents, singular name, plural name).
DENOMINATIONS = [
    (10000, "$100 bill", "$100 bills"),
    (2000, "$20 bill", "$20 bills"),
    (500, "$5 bill", "$5 bills"),
    (100, "$1 bill", "$1 bills"),
    (25, "quarter", "quarters"),
    (10, "dime", "dimes"),
    (5, "nickel", "nickels"),
    (1, "penny", "pennies"),
]

def seat_label(row_index, seat_index):
    # Turn list indices into a seat name such as '2C'.
    # Rows are numbered from 1 for the passenger, so add 1 to the index.
    # Seats are lettered, so convert the column index into a letter.
    return f"{row_index + 1}{chr(ord('A') + seat_index)}"

def parse_seat(location, seats):
    # Turn a seat name such as '2C' into (row_index, seat_index).
    # Returns None if the entry is malformed or outside this compartment.
    # Clean up the entry so '  2c ' is treated the same as '2C'.
    location = location.strip().upper()
    
    # A valid entry needs at least one row digit and one seat letter.
    if len(location) < 2:
        return None
    
    # Everything except the last character is the row number.
    # Subtract 1 because list indices start at 0 but rows are numbered from 1.
    try:
        row = int(location[:-1]) - 1
    except ValueError:
        # The row part was not a number
        return None     
    
    # The last character is the seat letter. 'A' becomes 0, 'B' becomes 1, etc.
    seat = ord(location[-1]) - ord("A")

    # Confirm the seat actually exists before handing back the indices,
    # otherwise the caller would crash with an IndexError.
    if 0 <= row < len(seats) and 0 <= seat < len(seats[row]):
        return row, seat
    return None

def is_full(seats):
    # True when every seat in the compartment is reserved.
    # Walk every seat in every row. An empty string means the seat is open.
    return all(seat != "" for row in seats for seat in row)

def calculate_fare(age, base_price):
    # Fare after any age discount, with sales tax added.
    fare = base_price

    # Children under 7 and seniors 65 and older receive a 20 % discount.
    if age < 7 or age >= 65:
        fare = fare * 0.80             

    # Add sales tax to the discounted fare and return the amount owed.
    return fare + (fare * TAX_RATE)

def compute_change(change_amount):
    # Display the change owed broken down into bills and coins.
    # Convert to whole cents first. Floating point cannot store amounts like
    # 0.10 exactly, so dividing dollars directly would hand back wrong coins.
    cents = round(change_amount * 100)

    print(f"\nYour change is ${change_amount:.2f}:")

    # Work from the largest denomination down, taking as many of each as
    # possible and carrying the remainder to the next denomination.
    for denomination, singular, plural in DENOMINATIONS:
        count, cents = divmod(cents, denomination)

        # Skip denominations that are not needed for this amount.
        if count > 0:
            name = singular if count == 1 else plural
            print(f"    {count} {name}")

def process_payment(total):
    # Collect payment. Returns True if the passenger paid enough.
    # Read the amount handed over. A non-numeric entry counts as a failed sale.
    try:
        amount = float(input("Amount tendered: $"))
    except ValueError:
        return False

    # Compare in whole cents so tiny floating point differences do not
    # reject a passenger who paid the exact amount.
    if round(amount * 100) < round(total * 100):
        return False

    if round(amount * 100) > round(total * 100):
        compute_change(amount - total)


    return True

def make_reservation(seats, base_price, class_name):
    # Book one passenger into the given compartment.
    # Nothing can be sold if the compartment is already sold out.
    if is_full(seats):
        print(f"\nNo new reservations can be made in {class_name}.")
        return

    # Ask which seat the passenger wants and translate it into list indices.
    print(f"\n--- New {class_name} Reservation ---")
    location = parse_seat(input("Enter desired seat (example 1A): "), seats)
    if location is None:
        print("That is not a valid seat in this compartment.")
        return
    row, seat = location

    # A seat holding a name is already sold, so the request is refused.
    if seats[row][seat] != "":
        print(f"Seat {seat_label(row, seat)} is taken. Reservation refused.")
        return

    # Collect the passenger details needed to price the ticket.
    name = input("Passenger name: ").strip()
    if name == "":
        print("A name is required. Reservation refused.")
        return

    try:
        age = int(input("Passenger age: "))
    except ValueError:
        print("That is not a valid age. Reservation refused.")
        return

    # Price the ticket and show the passenger what is owed.
    total = calculate_fare(age, base_price)
    if age < 7 or age >= 65:
        print("A 20% age discount has been applied.")
    print(f"Total due (fare plus {TAX_RATE * 100:.2f}% tax): ${total:.2f}")

    # Take payment. The seat stays open if the passenger cannot cover the fare.
    if not process_payment(total):
        print("\nInsufficient funds. Seat not booked.")
        return

    # Payment succeeded, so record the passenger in the seating list.
    seats[row][seat] = name
    print(f"\nReservation confirmed for {name} in seat {seat_label(row, seat)}.")

def change_reservation(first_class, coach):
    # Release an existing seat, then rebook the passenger elsewhere.
    # Menu choice mapped to the seating list, fare, and display name
    # so either compartment can be selected the same way.
    compartments = {
        "1": (first_class, FIRST_PRICE, "First Class"),
        "2": (coach, COACH_PRICE, "Coach"),
    }

    # Find out which compartment currently holds the reservation.
    print("\n--- Change a Reservation ---")
    old = input("Which compartment holds the reservation? (1 first class, 2 coach): ").strip()
    if old not in compartments:
        print("That is not a valid compartment.")
        return
    seats = compartments[old][0]

    # Find out which seat is being given up.
    location = parse_seat(input("Which seat is being changed? (example 1A): "), seats)
    if location is None:
        print("That is not a valid seat in this compartment.")
        return
    row, seat = location

    # There is nothing to change if that seat was never sold.
    if seats[row][seat] == "":
        print("No reservation there.")
        return

    # Open the seat back up. Chaffey Airlines gives no refunds, so no money
    # is returned to the passenger here.
    passenger = seats[row][seat]
    seats[row][seat] = ""
    print(f"Seat {seat_label(row, seat)} released for {passenger}. No refunds are given.")

    # Ask where the passenger would like to sit now.
    new = input("Rebook into which compartment? (1 first class, 2 coach): ").strip()
    if new not in compartments:
        print("That is not a valid compartment. Nothing was rebooked.")
        return

    # Hand the new compartment to the booking function, which charges the
    # passenger again at that compartment's fare.
    new_seats, new_price, class_name = compartments[new]
    make_reservation(new_seats, new_price, class_name)

def print_seating(seats, class_name):
    # Display one compartment's seating chart.
    # Take the seat count from the compartment itself so first class (2 seats
    # per row) and coach (4 seats per row) both print the correct headers.
    seats_per_row = len(seats[0])
    
    print(f"\n{class_name}")
    print("       " + "".join(f"{chr(ord('A') + s):<14}" for s in range(seats_per_row)))

    # Build and print one line per row of seats.
    for row_index, row in enumerate(seats):
        # Start the line with the row number, numbered from 1 for the attendant.
        line = f"Row {row_index + 1:<3}"

        # Append each seat in the row to the same line so the columns align.
        for passenger in row:
            if passenger == "":
                line += f"{'OPEN':<14}"
            else:
                # Shorten long names for neatness. The full name stays in the
                # list, only the printed copy is trimmed.
                line += f"{passenger[:NAME_DISPLAY_LENGTH]:<14}"

        # The row is complete, so write the whole line out at once.
        print(line)

    # Warn the attendant when this compartment has nothing left to sell.
    if is_full(seats):
        print(f"No new reservations can be made in {class_name}.")

def main():
    """Run the reservation system menu until the attendant quits."""
    # Build both compartments as 2D lists. An empty string marks an open seat.
    first_class = [["" for _ in range(FIRST_SEATS_PER_ROW)] for _ in range(FIRST_ROWS)]
    coach = [["" for _ in range(COACH_SEATS_PER_ROW)] for _ in range(COACH_ROWS)]

    print("Welcome to Chaffey College Airlines")

    # Keep serving the attendant until option 5 is chosen.
    while True:
        # Display the menu of available actions.
        print("\n========== MAIN MENU ==========")
        print("1. Make a first class reservation")
        print("2. Make a coach reservation")
        print("3. Change a reservation")
        print("4. Print the seating chart")
        print("5. Quit")
        choice = input("Enter your choice: ").strip()

        # Send the attendant to the function matching the chosen option.
        if choice == "1":
            make_reservation(first_class, FIRST_PRICE, "First Class")
        elif choice == "2":
            make_reservation(coach, COACH_PRICE, "Coach")
        elif choice == "3":
            change_reservation(first_class, coach)
        elif choice == "4":
            # Both compartments are printed together for a full picture.
            print_seating(first_class, "FIRST CLASS")
            print_seating(coach, "COACH")
        elif choice == "5":
            print("\nThank you for flying Chaffey College Airlines.")
            break
        else:
            # Anything outside 1 through 5 returns to the menu.
            print("Invalid choice. Please enter 1 through 5.")


# Only start the program when this file is run directly.
if __name__ == "__main__":
    main()