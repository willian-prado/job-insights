from src.sorting import sort_by
import pytest


jobs = [
        {
            "min_salary": 500, "max_salary": 1500, "date_posted": "2020-01-23"
        },
        {
            "min_salary": 1000, "max_salary": 4500, "date_posted": "2020-01-15"
        },
        {
            "min_salary": 100, "max_salary": 2500, "date_posted": "2020-01-18"
        },
    ]


def test_sort_by_criteria():
    expected_sort_by_max_salary = [jobs[1], jobs[2], jobs[0]]
    expected_sort_by_min_salary = [jobs[2], jobs[0], jobs[1]]
    expected_sort_by_date_posted = [jobs[0], jobs[2], jobs[1]]

    invalid_criteria = ["industry", "salary", None, "", 4444]

    sort_by(jobs, "max_salary")
    assert jobs == expected_sort_by_max_salary
    sort_by(jobs, "min_salary")
    assert jobs == expected_sort_by_min_salary
    sort_by(jobs, "date_posted")
    assert jobs == expected_sort_by_date_posted

    for invalid in invalid_criteria:
        with pytest.raises(ValueError):
            sort_by(jobs, invalid)
