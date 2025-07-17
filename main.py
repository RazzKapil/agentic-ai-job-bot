
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
=======
import requests

# --- User Profile ---
class UserProfile:
    def __init__(self, user_id, name, skills, experience, location, desired_pay):
        self.user_id = user_id
        self.name = name
        self.skills = skills
        self.experience = experience
        self.location = location
        self.desired_pay = desired_pay

# --- Real-Time Job Fetcher using Adzuna API ---
class RealTimeJobFetcher:
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def fetch_jobs(self, search_term="python", location="remote", results_per_page=10):
        url = f"https://api.adzuna.com/v1/api/jobs/us/search/1"
        params = {
            "app_id": self.app_id,
            "app_key": self.app_key,
            "results_per_page": results_per_page,
            "what": search_term,
            "where": location,
            "content-type": "application/json"
        }
        response = requests.get(url, params=params)
        jobs = []
        if response.status_code == 200:
            data = response.json()
            for result in data.get("results", []):
                jobs.append({
                    "job_id": result.get("id"),
                    "title": result.get("title"),
                    "skills": self.extract_skills(result.get("description", "")),
                    "experience": 1,  # Placeholder, as most APIs don't provide this directly
                    "location": result.get("location", {}).get("display_name", "Remote"),
                    "pay": self.extract_pay(result)
                })
        else:
            print("API Error:", response.status_code, response.text)
        return jobs

    def extract_skills(self, description):
        # Simple keyword-based skill extraction (replace with NLP for production)
        skills = []
        for skill in ["Python", "SQL", "Django", "AWS", "Excel", "JavaScript", "HTML", "CSS"]:
            if skill.lower() in description.lower():
                skills.append(skill)
        return skills

    def extract_pay(self, result):
        # Use salary_min or salary_max if available, else default
        pay = result.get("salary_min") or result.get("salary_max") or 0
        # Adzuna salaries are annual; convert to hourly (divide by 2080 work hours/year)
        if pay > 1000:
            pay = round(pay / 2080, 2)
        return pay

# --- Job Filter ---
class JobFilter:
    def filter_by_criteria(self, jobs, user_profile):
        return [
            job for job in jobs
            if job["pay"] >= user_profile.desired_pay and
               (user_profile.location.lower() in job["location"].lower() or "remote" in job["location"].lower())
        ]

# --- Matcher ---
class Matcher:
    def score_job(self, job, user_profile):
        score = 0
        score += len(set(job["skills"]) & set(user_profile.skills))
        if user_profile.experience >= job["experience"]:
            score += 1
        return score

    def rank_jobs(self, jobs, user_profile):
        scored = [(job, self.score_job(job, user_profile)) for job in jobs]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [job for job, score in scored if score > 0]

# --- Recommender ---
class Recommender:
    def recommend(self, jobs, top_n=2):
        return jobs[:top_n]

# --- Application Assistant ---
class ApplicationAssistant:
    def autofill_form(self, job, user_profile):
        print(f"Auto-filling application for {user_profile.name} to {job['title']}")

    def generate_cover_letter(self, job, user_profile):
        return f"Dear Hiring Manager,\nI am excited to apply for {job['title']} as I have experience in {', '.join(user_profile.skills)}.\nBest,\n{user_profile.name}"

# --- Notifier ---
class Notifier:
    def send_email(self, user, subject, message):
        print(f"Email to {user.name}: {subject}\n{message}\n")

# --- Feedback Manager ---
class FeedbackManager:
    def record_feedback(self, user, job, feedback):
        print(f"Feedback from {user.name} on {job['title']}: {feedback}")

# --- Main Real-Time Pipeline ---
def main():
    # 1. User input (simulate)
    user = UserProfile(
        user_id="u1",
        name="Alice",
        skills=["Python", "SQL", "Django"],
        experience=3,
        location="Remote",
        desired_pay=35
    )

    # 2. Real-time job fetch from Adzuna API
    app_id = "YOUR_ADZUNA_APP_ID"   # <-- Replace with your Adzuna APP ID
    app_key = "YOUR_ADZUNA_APP_KEY" # <-- Replace with your Adzuna APP KEY
    jobs = RealTimeJobFetcher(app_id, app_key).fetch_jobs(
        search_term="python",
        location="remote",
        results_per_page=20
    )

    if not jobs:
        print("No jobs found or API error.")
        return

    # 3. Filter jobs
    filtered_jobs = JobFilter().filter_by_criteria(jobs, user)

    # 4. Match and rank
    matcher = Matcher()
    ranked_jobs = matcher.rank_jobs(filtered_jobs, user)

    # 5. Recommend
    recs = Recommender().recommend(ranked_jobs, top_n=2)

    if not recs:
        print("No suitable jobs found for your profile.")
        return

    # 6. Application assistance and notification
    app_assist = ApplicationAssistant()
    notifier = Notifier()
    for job in recs:
        app_assist.autofill_form(job, user)
        cover_letter = app_assist.generate_cover_letter(job, user)
        notifier.send_email(user, f"Recommended Job: {job['title']}", cover_letter)

    # 7. Feedback
    feedback_mgr = FeedbackManager()
    for job in recs:
        feedback_mgr.record_feedback(user, job, "applied")

if __name__ == "__main__":
    main()

