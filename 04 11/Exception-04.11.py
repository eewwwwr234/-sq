print("Prev code")
try:
    input()
    print(10 / 0)
    print(velue)
except KeyboardInterrupt:
    print("Помилка роботи з клвіатурою")
except ZeroDivisionError:
    print("Не можна ділити на нуль")
except (NameError, KeyError) as error:
    print(error)


print("Next code")
