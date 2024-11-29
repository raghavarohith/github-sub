# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Test function to check the multiply function
def test_multiply():
    assert multiply(2, 3) == 6  # 2 * 3 should equal 6
    assert multiply(0, 5) == 0  # 0 * 5 should equal 0
    assert multiply(-2, 3) == -6  # -2 * 3 should equal -6
    assert multiply(-2, -3) == 6  # -2 * -3 should equal 6
