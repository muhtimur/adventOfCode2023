# part one

from sys import stdin
f = open("input.txt", "r")

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
summ = 0

for s in f:
    left = ""
    right = ""

    for i in range(len(s)):
        if s[i] in digits:
            left = s[i]
            break

    for i in range(len(s)-1, -1, -1):
        if s[i] in digits:
            right = s[i]
            break

    calibration = left + right
    summ += int(calibration)


print(summ)


# part two

f = open("input.txt", "r")
summ = 0

for s in f:
    left = ""
    right = ""

    s = (
        s.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )

    for i in range(len(s)):
        if s[i] in digits:
            left = s[i]
            break

    for i in range(len(s)-1, -1, -1):
        if s[i] in digits:
            right = s[i]
            break

    calibration = left + right
    summ += int(calibration)

print(summ)
