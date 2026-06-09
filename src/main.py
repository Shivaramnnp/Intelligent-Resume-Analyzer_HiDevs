import logging

from parser import parse_resume
from matcher import match_candidate
from reporter import generate_report
from file_manager import (
    save_results,
    load_job_requirements
)

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="reports/app.log",
    filemode="a"
)


def main():
    logging.info("Application Started")

    print("=" * 40)
    print("INTELLIGENT RESUME ANALYZER")
    print("=" * 40)

    try:
        logging.info("Loading Resume")

        candidate = parse_resume(
            "data/sample_resume.txt"
        )

        if candidate is None:
            logging.error("Resume Parsing Failed")
            print("Failed to load candidate resume.")
            return

        logging.info(
            f"Resume Parsed Successfully: {candidate.name}"
        )

        logging.info("Loading Job Requirements")

        job = load_job_requirements(
            "data/job_requirements.json"
        )

        logging.info("Job Requirements Loaded")

        score, matched_skills = match_candidate(
            candidate,
            job
        )

        logging.info(
            f"Candidate Matched with Score: {score}"
        )

        report = generate_report(
            candidate,
            job,
            score,
            matched_skills
        )

        print(report)

        save_results(
            candidate,
            score,
            "reports/result.json"
        )

        logging.info("Results Saved Successfully")

        print("\nResults saved successfully!")
        print("JSON File: reports/result.json")
        print("Log File: reports/app.log")

    except Exception as e:
        logging.error(
            f"Unexpected Error: {e}",
            exc_info=True
        )
        print(f"Error: {e}")


if __name__ == "__main__":
    main()