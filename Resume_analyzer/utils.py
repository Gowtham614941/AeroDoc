def load_job_from_input():
    print("Enter Job Required Skills (comma separated): ")
    skills = input().split(",")

    degree = input("Enter Required Degree: ")

    return {
        "skills": [s.strip() for s in skills],
        "degree": degree
    }
