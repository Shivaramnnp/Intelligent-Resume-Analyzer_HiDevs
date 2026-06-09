import json


def save_results(candidate, score, filename):

    data = {
        "name": candidate.name,
        "email": candidate.email,
        "skills": candidate.skills,
        "experience": candidate.experience,
        "education": candidate.education,
        "score": score
    }

    with open(filename, "w") as file:
        json.dump(
            data,
            file,
            indent=4
        )


def load_job_requirements(filename):

    with open(filename, "r") as file:
        return json.load(file)