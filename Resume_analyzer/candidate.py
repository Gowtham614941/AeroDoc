class Candidate:
    def __init__(self, name="", email="", degree="", skills=None, experience=0):
        self.name = name
        self.email = email
        self.degree = degree
        self.skills = skills if skills else []
        self.experience = experience
        self.score = 0

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "degree": self.degree,
            "skills": self.skills,
            "experience": self.experience,
            "score": self.score
        }