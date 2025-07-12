class JobAggregator:
    def fetch_jobs(self):
        # Mock job data
        return [
            {
                "job_id": "1",
                "title": "Python Developer",
                "skills": ["Python", "SQL"],
                "experience": 2,
                "location": "Remote",
                "pay": 40
            },
            {
                "job_id": "2",
                "title": "Data Analyst",
                "skills": ["SQL", "Excel"],
                "experience": 1,
                "location": "Remote",
                "pay": 25
            },
            {
                "job_id": "3",
                "title": "Senior Python Engineer",
                "skills": ["Python", "Django", "AWS"],
                "experience": 5,
                "location": "Remote",
                "pay": 60
            }
        ]
