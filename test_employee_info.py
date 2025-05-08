import employee_info as empinfo
def test_get_employees_by_age_range():
    result = empinfo.get_employees_by_age_range(24, 36)
    names = [emp["name"] for emp in result]
    assert "John" in names
    assert "Jane" in names
    assert "Chloe" in names
    assert "Mike" in names
    assert "Mary" not in names
    assert "Peter" not in names

def test_calculate_average_salary():
    avg = empinfo.calculate_average_salary()
    expected_avg = (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6
    assert avg == expected_avg

def test_get_employees_by_dept():
    result = empinfo.get_employees_by_dept("Marketing")
    names = [emp["name"] for emp in result]
    assert "Jane" in names
    assert "Mary" in names
    assert len(names) == 2

    result = empinfo.get_employees_by_dept("Sales")
    names = [emp["name"] for emp in result]
    assert "John" in names
    assert "Peter" in names
    assert len(names) == 2

    result = empinfo.get_employees_by_dept("NonExistent")
    assert result == []