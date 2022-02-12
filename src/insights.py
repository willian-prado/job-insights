from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)

    unique_job_types = []
    for job in jobs_list:
        if not job["job_type"] in unique_job_types:
            unique_job_types.append(job["job_type"])

    return unique_job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [job for job in jobs if job["job_type"] == job_type]
    return filtered_jobs


def get_unique_industries(path):
    jobs = read(path)
    indrustries = list(
        {job["industry"] for job in jobs if job["industry"] != ""}
    )
    return indrustries


def filter_by_industry(jobs, industry):
    filtered_jobs = [job for job in jobs if job["industry"] == industry]
    return filtered_jobs


def get_max_salary(path):
    jobs = read(path)
    salaries = [
        int(job["max_salary"])
        for job in jobs
        if job["max_salary"] not in ["", "invalid"]
    ]
    highest_salary = max(salaries)
    return highest_salary


def get_min_salary(path):
    jobs = read(path)
    salaries = [
        int(job["min_salary"])
        for job in jobs
        if job["min_salary"] not in ["", "invalid"]
    ]
    lowest_salary = min(salaries)
    return lowest_salary


def matches_salary_range(job, salary):
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        my_salary = int(salary)

        if min_salary > max_salary:
            raise ValueError

        if min_salary <= my_salary and my_salary <= max_salary:
            return True
    except (ValueError, TypeError, KeyError):
        raise ValueError
    else:
        return False


def filter_by_salary_range(jobs, salary):
    filtered_jobs = [
        job
        for job in jobs
        if (type(salary) == int)
        if (int(job["min_salary"]) <= salary <= int(job["max_salary"]))
    ]
    return filtered_jobs
