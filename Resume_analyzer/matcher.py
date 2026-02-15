def calculate_score(candidate, job):
    score = 0

    skill_matches = len(set(candidate.skills) & set(job["skills"]))
    score += skill_matches * 10

    score += candidate.experience * 5

    if candidate.degree.lower() == job["degree"].lower():
        score += 15

    candidate.score = score
    return score


def rank_candidates(candidates, job):
    for c in candidates:
        calculate_score(c, job)

    return sorted(candidates, key=lambda x: x.score, reverse=True)