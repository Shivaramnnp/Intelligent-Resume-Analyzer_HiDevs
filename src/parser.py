import re
from candidate import Candidate


def parse_resume(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()

        name_match = re.search(r"Name:\s*(.*)", text)
        email_match = re.search(r"Email:\s*(.*)", text)
        exp_match = re.search(r"Experience:\s*(\d+)", text)
        edu_match = re.search(r"Education:\s*(.*)", text)

        skills_match = re.search(
            r"Skills:\s*(.*)",
            text
        )

        name = name_match.group(1) if name_match else "Unknown"
        email = email_match.group(1) if email_match else "Not Available"

        experience = (
            int(exp_match.group(1))
            if exp_match
            else 0
        )

        education = (
            edu_match.group(1)
            if edu_match
            else "Unknown"
        )

        skills = []

        if skills_match:
            skills = [
                skill.strip()
                for skill in skills_match.group(1).split(",")
            ]

        return Candidate(
            name,
            email,
            skills,
            experience,
            education
        )

    except FileNotFoundError:
        print("Resume file not found")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None