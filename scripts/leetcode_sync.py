import os
import re
import sys
import time
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import requests


LEETCODE_GRAPHQL = "https://leetcode.com/graphql/"

SESSION = os.environ.get("LEETCODE_SESSION")
CSRF_TOKEN = os.environ.get("LEETCODE_CSRF_TOKEN")

if not SESSION:
    print("ERROR: LEETCODE_SESSION is not configured.")
    sys.exit(1)

if not CSRF_TOKEN:
    print("ERROR: LEETCODE_CSRF_TOKEN is not configured.")
    sys.exit(1)


HEADERS = {
    "Content-Type": "application/json",
    "Origin": "https://leetcode.com",
    "Referer": "https://leetcode.com/",
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/140.0 Safari/537.36"
    ),
    "X-CSRFToken": CSRF_TOKEN,
}

COOKIES = {
    "LEETCODE_SESSION": SESSION,
    "csrftoken": CSRF_TOKEN,
}


def graphql(query, variables=None, retries=3):
    payload = {
        "query": query,
        "variables": variables or {},
    }

    for attempt in range(retries):
        try:
            response = requests.post(
                LEETCODE_GRAPHQL,
                json=payload,
                headers=HEADERS,
                cookies=COOKIES,
                timeout=30,
            )

            response.raise_for_status()

            data = response.json()

            if "errors" in data and data["errors"]:
                print("LeetCode GraphQL error:")
                print(data["errors"])

                if attempt < retries - 1:
                    time.sleep(3 * (attempt + 1))
                    continue

                return None

            return data.get("data")

        except Exception as exc:
            print(
                f"Request failed "
                f"(attempt {attempt + 1}/{retries}): {exc}"
            )

            if attempt < retries - 1:
                time.sleep(3 * (attempt + 1))
            else:
                return None

    return None


def check_login():
    query = """
    query {
        userStatus {
            isSignedIn
            username
        }
    }
    """

    data = graphql(query)

    if not data:
        print("ERROR: Could not contact LeetCode.")
        sys.exit(1)

    status = data.get("userStatus") or {}

    if not status.get("isSignedIn"):
        print("ERROR: LeetCode session is not authenticated.")
        print("Refresh LEETCODE_SESSION and try again.")
        sys.exit(1)

    username = status.get("username", "unknown")

    print(f"Authenticated as LeetCode user: {username}")

    return username


def get_last_sync_timestamp():
    """
    Find the timestamp of our latest sync commit.

    If there is no previous sync commit, return 0 so that
    the script considers all solved problems.
    """

    try:
        result = subprocess.run(
            [
                "git",
                "log",
                "-1",
                "--format=%ct",
                "--grep=Sync LeetCode submission",
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        value = result.stdout.strip()

        if value:
            timestamp = int(value)
            print(
                "Last sync commit:",
                datetime.fromtimestamp(
                    timestamp,
                    tz=timezone.utc,
                ).isoformat(),
            )
            return timestamp

    except Exception as exc:
        print(f"Could not determine last sync timestamp: {exc}")

    print("No previous sync commit found.")
    print("Checking all solved problems.")

    return 0


def get_solved_questions():
    query = """
    query userProgressQuestionList(
        $filters: UserProgressQuestionListInput
    ) {
        userProgressQuestionList(filters: $filters) {
            totalNum
            questions {
                frontendId
                title
                titleSlug
                difficulty
                lastSubmittedAt
            }
        }
    }
    """

    all_questions = []
    skip = 0
    limit = 1000

    while True:
        variables = {
            "filters": {
                "questionStatus": "SOLVED",
                "skip": skip,
                "limit": limit,
            }
        }

        data = graphql(query, variables)

        if not data:
            return all_questions

        result = data.get("userProgressQuestionList") or {}

        questions = result.get("questions") or []
        total = result.get("totalNum") or 0

        all_questions.extend(questions)

        print(
            f"Fetched {len(all_questions)}/{total} solved problems."
        )

        if not questions or len(all_questions) >= total:
            break

        skip += limit
        time.sleep(1)

    return all_questions


def parse_timestamp(value):
    if not value:
        return 0

    try:
        normalized = value.replace("Z", "+00:00")

        dt = datetime.fromisoformat(normalized)

        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)

        return int(dt.timestamp())

    except Exception:
        return 0


def get_changed_questions(questions, last_sync):
    changed = []

    for question in questions:
        submitted_at = parse_timestamp(
            question.get("lastSubmittedAt")
        )

        if submitted_at > last_sync:
            changed.append(question)

    changed.sort(
        key=lambda q: parse_timestamp(
            q.get("lastSubmittedAt")
        )
    )

    print(
        f"Problems changed since last sync: {len(changed)}"
    )

    return changed


def get_latest_accepted_submission(slug):
    query = """
    query questionSubmissionList(
        $offset: Int!
        $limit: Int!
        $questionSlug: String!
    ) {
        questionSubmissionList(
            offset: $offset
            limit: $limit
            questionSlug: $questionSlug
        ) {
            submissions {
                id
                statusDisplay
                lang
                timestamp
                runtime
                memory
            }
        }
    }
    """

    data = graphql(
        query,
        {
            "offset": 0,
            "limit": 20,
            "questionSlug": slug,
        },
    )

    if not data:
        return None

    result = data.get("questionSubmissionList") or {}

    submissions = result.get("submissions") or []

    accepted = [
        submission
        for submission in submissions
        if submission.get("statusDisplay") == "Accepted"
    ]

    if not accepted:
        return None

    accepted.sort(
        key=lambda x: int(x.get("timestamp", 0)),
        reverse=True,
    )

    return accepted[0]


def get_submission_code(submission_id):
    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(
            submissionId: $submissionId
        ) {
            code
            lang {
                name
            }
            runtime
            memory
            statusDisplay
            runtimePercentile
            memoryPercentile
        }
    }
    """

    data = graphql(
        query,
        {
            "submissionId": int(submission_id),
        },
    )

    if not data:
        return None

    return data.get("submissionDetails")


def get_question_content(slug):
    query = """
    query question($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            content
        }
    }
    """

    data = graphql(
        query,
        {
            "titleSlug": slug,
        },
    )

    if not data:
        return None

    question = data.get("question") or {}

    return question.get("content")


def pad_problem_number(frontend_id):
    value = str(frontend_id)

    if value.isdigit() and len(value) < 4:
        return value.zfill(4)

    return value


def normalize_slug(title):
    value = title.lower()

    value = re.sub(r"\s+", "-", value)

    value = re.sub(
        r"[^a-zA-Z0-9_-]",
        "",
        value,
    )

    return value


LANGUAGE_EXTENSIONS = {
    "python": "py",
    "python3": "py",
    "pythondata": "py",
    "javascript": "js",
    "typescript": "ts",
    "java": "java",
    "cpp": "cpp",
    "c": "c",
    "csharp": "cs",
    "golang": "go",
    "go": "go",
    "kotlin": "kt",
    "swift": "swift",
    "rust": "rs",
    "ruby": "rb",
    "php": "php",
    "scala": "scala",
    "dart": "dart",
    "bash": "sh",
    "mysql": "sql",
    "mssql": "sql",
    "postgresql": "sql",
    "oraclesql": "sql",
}


def find_existing_folder(problem_number, title):
    slug = normalize_slug(title)

    expected = (
        f"{pad_problem_number(problem_number)}-{slug}"
    )

    expected_path = Path(expected)

    if expected_path.exists():
        return expected_path

    prefix = f"{pad_problem_number(problem_number)}-"

    for path in Path(".").iterdir():
        if path.is_dir() and path.name.startswith(prefix):
            return path

    return None


def write_solution(
    question,
    submission,
    details,
    question_content,
):
    problem_number = question.get("frontendId")
    title = question.get("title")
    slug = question.get("titleSlug")

    folder_name = (
        f"{pad_problem_number(problem_number)}-"
        f"{normalize_slug(title)}"
    )

    folder = Path(folder_name)

    existing_folder = find_existing_folder(
        problem_number,
        title,
    )

    if existing_folder:
        folder = existing_folder

    folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    language = (
        submission.get("lang")
        or details.get("lang", {}).get("name", "")
    )

    language = language.lower()

    extension = LANGUAGE_EXTENSIONS.get(language)

    if not extension:
        print(
            f"Unsupported language '{language}' "
            f"for {title}. Skipping."
        )
        return False

    code = details.get("code")

    if not code:
        print(
            f"No code returned for {title}. Skipping."
        )
        return False

    solution_file = folder / f"solution.{extension}"

    solution_file.write_text(
        code.rstrip() + "\n",
        encoding="utf-8",
    )

    readme = folder / "README.md"

    if not readme.exists():
        if question_content:
            readme.write_text(
                question_content,
                encoding="utf-8",
            )
        else:
            readme.write_text(
                f"# {problem_number}. {title}\n\n"
                f"LeetCode problem: "
                f"https://leetcode.com/problems/{slug}/\n",
                encoding="utf-8",
            )

    print(
        f"Synced: {folder}/{solution_file.name}"
    )

    return True


def main():
    print("=" * 60)
    print("Custom LeetCode → GitHub Sync")
    print("=" * 60)

    check_login()

    last_sync = get_last_sync_timestamp()

    questions = get_solved_questions()

    if not questions:
        print(
            "No solved questions were returned."
        )
        print(
            "This can happen if the LeetCode endpoint "
            "does not expose progress for the account."
        )
        sys.exit(0)

    changed_questions = get_changed_questions(
        questions,
        last_sync,
    )

    if not changed_questions:
        print("No new or updated LeetCode problems.")
        return

    synced_count = 0

    for index, question in enumerate(
        changed_questions,
        start=1,
    ):
        title = question.get("title")
        slug = question.get("titleSlug")

        print()
        print(
            f"[{index}/{len(changed_questions)}] "
            f"{title}"
        )

        submission = get_latest_accepted_submission(
            slug
        )

        if not submission:
            print(
                "No accepted submission found. "
                "Skipping."
            )
            continue

        submission_id = submission.get("id")

        print(
            f"Accepted submission: #{submission_id}"
        )

        details = get_submission_code(
            submission_id
        )

        if not details:
            print(
                "Could not retrieve submission details."
            )
            continue

        question_content = get_question_content(
            slug
        )

        success = write_solution(
            question,
            submission,
            details,
            question_content,
        )

        if success:
            synced_count += 1


        time.sleep(1)

    print()
    print("=" * 60)
    print(
        f"Sync complete. {synced_count} problem(s) processed."
    )
    print("=" * 60)


if __name__ == "__main__":
    main()
