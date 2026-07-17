# A guided program that walks a person through folding a paper airplane.


def wait_for_step(instruction):
    """Print one instruction and pause until the user confirms it's done."""
    print(instruction)
    input("   Press Enter when you've finished this step... ")
    print()


def fold_wings():
    """Fold both wings using a loop, just like the WHILE in the pseudocode."""
    wing_count = 0
    while wing_count < 2:
        side = "first" if wing_count == 0 else "second"
        wait_for_step(
            f"Fold the {side} wing down so its top edge lines up "
            "with the bottom edge of the body, then press the crease."
        )
        wing_count = wing_count + 1


def test_flight():
    """
    Test the airplane and adjust until it flies.
    This is the IF / ELSE IF / ELSE decision from the pseudocode,
    wrapped in a loop so the user can keep trying.
    """
    while True:
        print("Give the airplane a gentle throw forward.")
        result = input(
            "How did it fly? Type 'nosedive', 'veers', or 'good': "
        ).strip().lower()
        print()

        if result == "nosedive":
            wait_for_step("Bend the back edges of both wings up slightly.")
        elif result == "veers":
            wait_for_step("Even out the wings so they match, then try again.")
        elif result == "good":
            print("Success! Your paper airplane flies. Nice work!")
            break
        else:
            print("Please type 'nosedive', 'veers', or 'good'.\n")


def make_paper_airplane():
    """Main routine: runs the whole build from start to finish."""
    print("=== How to Make a Paper Airplane ===\n")

    wait_for_step("Get a rectangular sheet of paper.")
    wait_for_step("Place it flat on the table in portrait orientation (tall).")

    wait_for_step("Fold the paper in half lengthwise, press the crease, "
                  "then unfold it. This leaves a center line.")

    wait_for_step("Fold the top-left corner in to meet the center line.")
    wait_for_step("Fold the top-right corner in to meet the center line. "
                  "The top now forms a point (the nose).")

    wait_for_step("Fold the angled left edge in to the center line again.")
    wait_for_step("Fold the angled right edge in to the center line again. "
                  "This sharpens the nose.")

    wait_for_step("Fold the whole plane in half along the original "
                  "center crease, flaps on the outside.")

    fold_wings()

    wait_for_step("Open the two wings out flat so they stick straight out.")

    test_flight()
    print("\n=== Done. Enjoy your flight! ===")


# This line starts the program when you run the file.
if __name__ == "__main__":
    make_paper_airplane()