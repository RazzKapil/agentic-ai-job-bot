class NLPPreprocessor:
    def extract_skills(self, job):
        # In real use, parse job description text
        return job["skills"]

    def extract_pay(self, job):
        return job["pay"]

    def extract_location(self, job):
        return job["location"]
