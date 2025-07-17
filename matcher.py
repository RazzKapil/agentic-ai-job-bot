# matcher.py

from user_profile import UserProfile


class Matcher:
    def score_job(self, job, user_profile):
        # Compute match score (skills, experience, location, pay)
        pass

    def rank_jobs(self, jobs, user_profile):
        # Return jobs sorted by score
        pass

# test_matcher.py

def test_score_job():
    job = {...}
    user = UserProfile(...)
    score = Matcher().score_job(job, user)
    assert 0 <= score <= 1
