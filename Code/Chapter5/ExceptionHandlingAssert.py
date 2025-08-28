# Assertion Error :

"""An assertion is a statement used to check whether a condition is True during the execution of a program. 
It is mainly used for debugging purposes to catch bugs early in the development process.
The assert keyword helps the programmer test assumptions made in the code. 
If the condition is false, an AssertionError is raised.

Syntax: 
assert condition, "optional error message"""


try:
    password = "123"
    assert len(password) >= 6, "Password must be at least 6 characters"
except AssertionError as e:
    print("Error:", e)



try:
    temperature = -100
    assert -50 <= temperature <= 50, "Temperature out of realistic range"
except AssertionError as e:
    print("Error:", e)


try:
    x = 10
    y = 0
    assert y != 0, "Denominator should not be zero"
    result = x / y
except AssertionError as e:
    print("Error:", e)
