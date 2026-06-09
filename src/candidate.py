# candidate.py

class Candidate:
    def __init__(self, name, email, skills,
                 experience, education):

        self.name = name
        self.email = email
        self.skills = skills
        self.experience = experience
        self.education = education

    def __str__(self):
        return f"{self.name} ({self.email})"