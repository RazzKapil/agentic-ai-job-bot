class Recommender:
    def recommend(self, user_profile, jobs, top_n):
        return jobs[:top_n]
