def match_candidate(candidate, job):
    score = 0

    matched_skills = []

    for skill in job["required_skills"]:
        if skill.lower() in [
            s.lower()
            for s in candidate.skills
        ]:
            matched_skills.append(skill)

    skill_score = (
        len(matched_skills)
        / len(job["required_skills"])
    ) * 70

    score += skill_score

    if candidate.experience >= job["min_experience"]:
        score += 20

    if job["education"].lower() in candidate.education.lower():
        score += 10

    return round(score, 2), matched_skills