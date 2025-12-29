def chai_serve(flavour):
    try:
        print(f"Praparing {flavour} chai...")
        if flavour == "unknown":
            raise ValueError("We don't know that flavour")
        
    except ValueError as e:
        print("Error:", e)

    else:
        print(f"{flavour} chai is served")

    finally:
        print("Next customer please")

chai_serve("Masala")
chai_serve("unknown")