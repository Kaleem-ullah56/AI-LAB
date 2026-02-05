# i used no as short form of number
last_no = 0

while True:
    num = int(input("Enter a number (0 to quit): "))

    if num == 0:
        print("Game ended.")
        break

    # add ONLY the last number
    current_no = last_no + num

    # FizzBuzz check
    if current_no % 3 == 0 and current_no % 5 == 0:
        print(f"{current_no} → FizzBuzz")
    elif current_no % 3 == 0:
        print(f"{current_no} → Fizz")
    elif current_no % 5 == 0:
        print(f"{current_no} → Buzz")
    else:
        print(current_no)

    last_no = current_no