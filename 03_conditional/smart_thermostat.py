# nested if
device_status = "active"
temperature = 38

if device_status == "active":
    # pass # The keyword pass help to write the else part first without giving any warning..
    if temperature > 35:
        print("High Temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")