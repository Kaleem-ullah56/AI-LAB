num = input("Enter card number: ")
# The Code was showing error with spaces so i replaced all spaces with no space
num = num.replace(" ", "")
tot = 0
num = num[::-1]
# Here i used for loop
for i in range(len(num)):
    digi = int(num[i])
    if i % 2 == 1:
        digi = digi * 2
        if digi > 9:
            digi = digi - 9
    tot = tot + digi
# If sum of final numbers in divisible by 10 its valid card
if tot % 10 == 0:
    print("Valid Card")
else:
    print("Invalid Card")