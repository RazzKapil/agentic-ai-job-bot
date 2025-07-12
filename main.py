from user_profile import UserProfile
from nlp_preprocessor import NLPPreprocessor
from job_filter import JobFilter
from matcher import Matcher
from recommender import Recommender
from application_assist import ApplicationAssistant
from notifier import Notifier
from feedback import FeedbackManager
from job_aggregator import JobAggregator

def main():
    # 1. Create user
    user = UserProfile(
        user_id="u1",
        name="Alice",
        skills=["Python", "SQL", "Django"],
        experience=3,
        location="Remote",
        desired_pay=35
    )

    # 2. Aggregate jobs
    jobs = JobAggregator().fetch_jobs()

    # 3. NLP Preprocessing (mocked here)
    nlp = NLPPreprocessor()
    for job in jobs:
        job["skills"] = nlp.extract_skills(job)
        job["pay"] = nlp.extract_pay(job)
        job["location"] = nlp.extract_location(job)

    # 4. Filter jobs
    filtered_jobs = JobFilter().filter_by_criteria(jobs, user)

    # 5. Match and rank
    matcher = Matcher()
    ranked_jobs = matcher.rank_jobs(filtered_jobs, user)

    # 6. Recommend
    recs = Recommender().recommend(user, ranked_jobs, top_n=2)

    # 7. Application assistance
    app_assist = ApplicationAssistant()
    notifier = Notifier()
    for job in recs:
        app_assist.autofill_form(job, user)
        cover_letter = app_assist.generate_cover_letter(job, user)
        notifier.send_email(user, f"Recommended Job: {job['title']}", cover_letter)

    # 8. Feedback
    feedback_mgr = FeedbackManager()
    for job in recs:
        feedback_mgr.record_feedback(user, job, "applied")

if __name__ == "__main__":
    main()
