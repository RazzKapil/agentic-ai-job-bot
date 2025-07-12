class UserProfile:
    def __init__(self, user_id, name, skills, experience, location, desired_pay):
        self.user_id = user_id
        self.name = name
        self.skills = skills  # list of strings
        self.experience = experience  # years
        self.location = location
        self.desired_pay = desired_pay  # hourly

    def __repr__(self):
        return f"<UserProfile {self.name}>"
