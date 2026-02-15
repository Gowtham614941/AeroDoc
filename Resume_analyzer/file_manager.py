import json


def save_results(candidates, job):
    data = {
        "job": job,
        "candidates": [c.to_dict() for c in candidates]
    }

    with open("results.json", "w") as f:
        json.dump(data, f, indent=4)