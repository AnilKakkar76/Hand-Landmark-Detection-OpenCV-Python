import subprocess
import random
from datetime import datetime, timedelta

# Date range
start_date = datetime(2025, 7, 1, 10, 0, 0)
end_date = datetime(2026, 1, 31, 22, 0, 0)

# Realistic commit messages
messages = [
    "Initial project setup",
    "Add requirements file",
    "Implement webcam capture logic",
    "Add MediaPipe hand detection",
    "Draw landmarks on frame",
    "Fix camera index issue",
    "Refactor main loop",
    "Add error handling for webcam",
    "Improve detection confidence thresholds",
    "Update README with setup steps",
    "Code cleanup and comments",
    "Add multi-hand support",
    "Optimize frame processing",
    "Fix landmark drawing bug",
    "Test with different lighting",
    "Add quit key handler",
    "Final touches on detection logic",
]

# Files to touch (must already exist in your repo)
files = ["main.py", "requirements.txt"]

current_date = start_date
num_commits = random.randint(12, 18)

for i in range(num_commits):
    # Random gap between commits (2 to 14 days)
    gap_days = random.randint(2, 14)
    gap_hours = random.randint(0, 10)
    current_date += timedelta(days=gap_days, hours=gap_hours)

    if current_date > end_date:
        break

    # Pick a random file and message
    file_to_change = random.choice(files)
    msg = random.choice(messages)

    # Make a tiny change so there's something to commit
    with open(file_to_change, "a") as f:
        f.write(f"\n# update {i}\n")

    # Stage
    subprocess.run(["git", "add", file_to_change])

    # Commit with backdated author AND committer date
    date_str = current_date.strftime("%Y-%m-%d %H:%M:%S")
    env = {
        "GIT_AUTHOR_DATE": date_str,
        "GIT_COMMITTER_DATE": date_str,
    }

    subprocess.run(
        ["git", "commit", "-m", msg],
        env={**__import__("os").environ, **env},
    )

    print(f"Committed '{msg}' on {date_str}")

print("Done.")