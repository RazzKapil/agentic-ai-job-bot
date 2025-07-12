# application_assist.py

class ApplicationAssistant:
    def autofill_form(self, job, user_profile):
        # Fill application form fields
        pass

    def generate_cover_letter(self, job, user_profile):
        # Use LLM to generate cover letter
        pass

# test_application_assist.py

def test_generate_cover_letter():
    job = {...}
    user = UserProfile(...)
    letter = ApplicationAssistant().generate_cover_letter(job, user)
    assert "Dear" in letter
