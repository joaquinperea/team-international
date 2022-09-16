import pytest
from data_capture import DataCapture


@pytest.mark.parametrize(
    "values_added, input_value, expected",
    [
        ([3, 9, 3, 4, 6], 4, 2),  # Positive case
        ([2, 10, 15, 20, 20, 5, 6, 7], 15, 5),  # Positive case.
        ([2, 10, 15, 20, 20, 'somestring', 6, 7], 15, ValueError),  # Validating string input.
        ([2, 10, 15, 20, 20.5, 5, 6, 7], 15, ValueError),  # Validating float input.
        ([2, 10, 15, 20, 1000, 5, 6, 7], 15, ValueError),  # Validating input equal to 1000.
        ([2, 10, 15, 20, 1020, 5, 6, 7], 15, ValueError),  # Validating input up than 1000.
        ([2, 10, 15, 20, -1, 5, 6, 7], 15, ValueError),  # Validating input less than 0.
        ([2, 10, 15, 20, 0, 5, 6, 7], 15, 6)  # Validating input equal to 0.
    ]
)
def test_less(values_added, input_value, expected):
    try:
        capture = DataCapture()
        for i in values_added:
            capture.add(i)
        stats = capture.build_stats()
        assert stats.less(input_value) == expected
    except ValueError:
        assert expected == ValueError


@pytest.mark.parametrize(
    "values_added, input_value, expected",
    [
        ([3, 9, 3, 4, 6], 4, 2),  # Positive case.
        ([2, 10, 15, 20, 20, 5, 6, 7], 15, 2),  # Positive case.
        ([2, 10, 15, 20, 'somestring', 5, 6, 7], 15, ValueError),  # Validating string input.
        ([2, 10, 15, 20, 20.5, 5, 6, 7], 15, ValueError),  # Validating float input.
        ([2, 10, 15, 20, 1000, 5, 6, 7], 15, ValueError),  # Validating input equal to 1000.
        ([2, 10, 15, 20, 1020, 5, 6, 7], 15, ValueError),  # Validating input up than 1000.
        ([2, 10, 15, 20, -1, 5, 6, 7], 15, ValueError),  # Validating input less than 0.
        ([2, 10, 15, 20, 0, 5, 6, 7], 15, 1)  # Validating input equal to 0.
    ]
)
def test_greater(values_added, input_value, expected):
    try:
        capture = DataCapture()
        for i in values_added:
            capture.add(i)
        stats = capture.build_stats()
        assert stats.greater(input_value) == expected
    except ValueError:
        assert expected == ValueError


@pytest.mark.parametrize(
    "values_added, input_min_value, input_max_value, expected",
    [
        ([3, 9, 3, 4, 6], 3, 6, 4),  # Positive case.
        ([2, 10, 15, 20, 20, 5, 6, 7], 6, 15, 4),  # Positive case.
        ([2, 10, 15, 20, 20, 5, 6, 'somestring'], 6, 15, ValueError),  # Validating string input.
        ([2, 10, 15, 20, 20.5, 5, 6, 7], 6, 15, ValueError),  # Validating float input.
        ([2, 10, 15, 20, 1000, 5, 6, 7], 6, 15, ValueError),  # Validating input equal to 1000.
        ([2, 10, 15, 20, 1020, 5, 6, 7], 6, 15, ValueError),  # Validating input up than 1000.
        ([2, 10, 15, 20, -1, 5, 6, 7], 6, 15, ValueError),  # Validating input less than 0.
        ([2, 10, 15, 20, 0, 5, 6, 7], 6, 15, 4)  # Validating input equal to 0.
    ]
)
def test_between(values_added, input_min_value, input_max_value, expected):
    try:
        capture = DataCapture()
        for i in values_added:
            capture.add(i)
        stats = capture.build_stats()
        assert stats.between(input_min_value, input_max_value) == expected
    except ValueError:
        assert expected == ValueError
