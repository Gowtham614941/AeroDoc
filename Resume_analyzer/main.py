from parser import parse_resume_text, parse_resume_file
from matcher import rank_candidates
from reporter import generate_detailed_report
from file_manager import save_results
from utils import load_job_from_input


def main():
    try:
        print("=== AI Resume Matcher ===\n")

        # Load Job Description
        job = load_job_from_input()

        # Choose input type
        print("\nChoose Resume Input Method:")
        print("1 → Paste Resume Text")
        print("2 → Upload Resume File (PDF/DOCX/TXT/JSON)")

        choice = input("Enter choice: ")

        n = int(input("\nEnter number of resumes: "))
        candidates = []

        for i in range(n):
            print(f"\n--- Resume {i+1} ---")

            if choice == "1":
                print("Paste resume text (Press ENTER twice to finish):")
                lines = []
                while True:
                    line = input()
                    if line == "":
                        break
                    lines.append(line)

                resume_text = "\n".join(lines)
                candidate = parse_resume_text(resume_text)

                if not candidate.email:
                    candidate.email = input("Enter Email: ")

                if not candidate.degree:
                    candidate.degree = input("Enter Degree: ")

            else:
                path = input("Enter file path: ")
                candidate = parse_resume_file(path)

            candidates.append(candidate)

        ranked = rank_candidates(candidates, job)

        report = generate_detailed_report(ranked, job)
        print("\n" + report)

        save_results(ranked, job)

        print("\nResults saved to results.json")

    except Exception as e:
        print(f"System Error: {e}")


if __name__ == "__main__":
    main()