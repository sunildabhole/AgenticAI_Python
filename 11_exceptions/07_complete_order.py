class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"Masala": 20, "Ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")

    except Exception as e:
        print("Error: ", e)

    finally:
        print("Thanks you for visiting...")

bill("Mint", 2)
bill("Masala", "three")
bill("Ginger", 3)