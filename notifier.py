# notifier.py

class Notifier:
    def send_email(self, user, subject, message):
        # Send email notification
        pass

    def send_push(self, user, message):
        # Send push notification
        pass

# test_notifier.py

def test_send_email():
    user = UserProfile(...)
    result = Notifier().send_email(user, "Job Alert", "You have a new match!")
    assert result == True
