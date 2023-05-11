def get_grade(score):
    """
    Function to calculate grade based on score
    """
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def test_boundary_values():
    """
    Function to test boundary values using boundary value analysis
    """
    boundary_test_cases = [(0, "F"), (59, "F"), (60, "D"), (69, "D"), (70, "C"), (79, "C"), (80, "B"), (89, "B"), (90, "A"), (100, "A")]
    for test_case in boundary_test_cases:
        assert get_grade(test_case[0]) == test_case[1], f"Expected {test_case[1]} but got {get_grade(test_case[0])}"

if __name__ == "__main__":
    test_boundary_values()

    print("All tests passed!")
