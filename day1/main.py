f = open("input.txt", "r")

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sum = 0

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
  sum += int(calibration) 
      

print(sum)