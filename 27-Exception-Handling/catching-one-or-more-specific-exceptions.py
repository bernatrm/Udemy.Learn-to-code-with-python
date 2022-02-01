def devide_five_by_number(n):
    try:
        calculation = 5 / n
    except ZeroDivisionError:
        return "You can't divide by zero!"
    except TypeError as e:
        return f"No dividing by invalid objects! {e}"
    # except (ZeroDivisionError, TypeError) as e:
    #     return f"Something went wrong. The error was {e}"

    return calculation

print(devide_five_by_number(0))
print(devide_five_by_number(10))
print(devide_five_by_number("Nonsense"))