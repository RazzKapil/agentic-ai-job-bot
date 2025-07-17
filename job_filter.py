# job_filter.py

class JobFilter:
    def filter_by_criteria(self, jobs, user_profile):
        # Filter jobs by location, pay, type, etc.
        pass

# test_job_filter.py

def test_filter_by_criteria():
    jobs = [{...}, {...}]
    user = UserProfile(...)
    filtered = JobFilter().filter_by_criteria(jobs, user)
    assert all(job['pay'] >= user.desired_pay for job in filtered)
