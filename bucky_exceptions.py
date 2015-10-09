while True:
    try:
        x = int(input("What is your age?\n"))
        print(100/x)
        break
    except ValueError:
        print("Try again, and enter a number!")
    except ZeroDivisionError:
        print("Don't pick Zero!")
    except:
        break
    finally:
        print("Loop complete")
