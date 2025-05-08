import Lab2.Python as bmi

def test_bmi_normal_weight() :
    result = 0
    height = 1.73
    weight = 57
    expected_result = 0

    result = bmi.calculate_bmi(height, weight)
    print(result)
    assert (result == expected_result)
def test_bmi_over_weight() :
    result = 0
    height = 1.76
    weight = 90
    expected_result = 1

    result = bmi.calculate_bmi(height, weight)
    print(result)
    assert (result == expected_result)
def test_bmi_under_weight() :
    result = 0
    height = 1.76
    weight = 10
    expected_result = -1

    result = bmi.calculate_bmi(height, weight)
    print(result)
    assert (result == expected_result)
