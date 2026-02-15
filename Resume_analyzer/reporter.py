def generate_detailed_report(candidates, job):
    report = []
    report.append("===== Resume Match Report =====\n")

    report.append(f"Job Required Skills: {', '.join(job['skills'])}")
    report.append(f"Required Degree: {job['degree']}\n")

    for i, c in enumerate(candidates, start=1):
        report.append(f"\nRank #{i}")
        report.append(f"Name: {c.name}")
        report.append(f"Email: {c.email}")
        report.append(f"Degree: {c.degree}")
        report.append(f"Skills: {', '.join(c.skills)}")
        report.append(f"Experience: {c.experience} years")
        report.append(f"Match Score: {c.score}")

    return "\n".join(report)