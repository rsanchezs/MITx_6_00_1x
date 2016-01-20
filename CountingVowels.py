from getpass import _raw_input

s = _raw_input("Enter a string:")
count = 0
for letter in s:

    # Applied the Morgan´s Law
    if not (not (letter == "a") and not ("e" == letter) and not (letter == "i")) or letter == "o" or letter == "u":
        count = count + 1
print(count)
