
def convertNumber(num):
    #  Verify it's an integer (assume performance not a problem)
    if not isinstance(num, int):
        raise Exception("Integer number expected")
    if (num % 3) == 0 and (num % 5) == 0:
        return "ThreeFive"
    elif (num % 3 ) == 0:
        return "Three"
    elif (num % 5) == 0:
        return "Five"
    else:
        return num

assert convertNumber(3) == "Three", "Coversion of 3 fails"
assert convertNumber(5) == "Five", "Conversion of 5 fails"
assert convertNumber(30) == "ThreeFive", "Conversion of 30 fails"
assert convertNumber(11) == 11, "No coversion for 11"
# Could add a unit test to verify this but seems like overkill
# assertRaises(convertNumber('g'))

for i in range(1,101):
    print(convertNumber(i))

