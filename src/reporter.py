def generate_report(
    candidate,
    job,
    score,
    matched_skills
):

    missing_skills = [
        skill
        for skill in job["required_skills"]
        if skill not in matched_skills
    ]

    if score >= 80:
        recommendation = "Strong Hire"

    elif score >= 60:
        recommendation = "Recommend"

    else:
        recommendation = "Not Recommended"

    report = f"""
=============================
CANDIDATE ANALYSIS REPORT
=============================

Name: {candidate.name}

Email: {candidate.email}

Education: {candidate.education}

Experience: {candidate.experience} Years

Skills:
{", ".join(candidate.skills)}

Matched Skills:
{", ".join(matched_skills)}

Missing Skills:
{", ".join(missing_skills)}

Match Score:
{score}/100

Recommendation:
{recommendation}
"""

    return report