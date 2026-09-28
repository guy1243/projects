def shutdown():
    y_or_no = input("are you sure you wanna shutdow?")
    if y_or_no == "yes":
        print("="*10, "SHUTTING DOWN", "="*10)
    elif y_or_no == "no":
        print("="*10, "canceld shutting down", "="*10)
    else:
        print("sorry")

shutdown()