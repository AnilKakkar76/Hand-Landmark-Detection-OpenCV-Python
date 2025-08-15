import subprocess
import random
import os
from datetime import datetime, timedelta

# ---------------- CONFIG ----------------
START_DATE = datetime(2025, 12, 1, 9, 0, 0)
END_DATE   = datetime(2026, 2, 23, 22, 0, 0)

# Files that will receive the commits (must already exist in your repo)
FILES = ["main.py", "requirements.txt"]

# Realistic commit messages grouped by type of work
MESSAGES = [
    "Update detection confidence threshold",
    "Fix landmark drawing offset",
    "Improve webcam error handling",
    "Add multi-hand tracking support",
    "Clean up unused imports",
    "Refactor hand detection loop",
    "Add frame rate logging",
    "Fix color space conversion bug",
    "Update requirements.txt",
    "Add comments to main loop",
    "Test with different lighting",
    "Handle empty frame gracefully",
    "Add quit key handler",
    "Optimize landmark rendering",
    "Fix camera release on exit",
    "Minor syntax cleanup",
    "Add docstring to functions",
    "Improve variable naming",
    "Adjust min_tracking_confidence",
    "Test 2-hand detection",
    "Add FPS counter to display",
    "Fix landmark circle size",
    "Cleanup drawing utils call",
    "Add error message when no camera",
    "Update README instructions",
    "Format code with black",
    "Remove debug print statements",
    "Tweak hand connection style",
    "Handle cv2.waitKey edge case",
    "Small performance improvement",
]
# ----------------------------------------

def random_commit_time():
    """Pick a random moment within working hours weighted toward evenings."""
    # Some commits in the day, more in the evening
    hour = random.choices(
        population=[9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        weights=[1, 1, 2, 1, 2, 2, 3, 4, 5, 6, 7, 5, 2],
        k=1
    )[0]
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return hour, minute, second

def make_commit(date, msg, counter):
    # Append a tiny realistic-looking change
    file_to_touch = random.choice(FILES)
    with open(file_to_touch, "a", encoding="utf-8") as f:
        f.write(f"\n# refactor {counter}\n")

    subprocess.run(["git", "add", file_to_touch], check=True)

    date_str = date.strftime("%Y-%m-%d %H:%M:%S")
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"]    = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    subprocess.run(
        ["git", "commit", "-m", msg, "--allow-empty"],
        env=env,
        check=True,
    )
    print(f"[{date_str}] {msg}")

def main():
    random.seed()  # true randomness
    current = START_DATE
    counter = 0

    while current <= END_DATE:
        # Decide how many commits this day gets
        # Distribution:
        #   45% -> 0 commits (rest day)
        #   35% -> 1 commit
        #   12% -> 2 commits
        #    6% -> 3 commits
        #    2% -> 4 commits
        roll = random.random()
        if roll < 0.45:
            num_commits = 0
        elif roll < 0.80:
            num_commits = 1
        elif roll < 0.92:
            num_commits = 2
        elif roll < 0.98:
            num_commits = 3
        else:
            num_commits = 4

        if num_commits > 0:
            # Sort times within the day so they're chronological
            times = sorted(random_commit_time() for _ in range(num_commits))
            for h, m, s in times:
                commit_dt = current.replace(hour=h, minute=m, second=s)
                msg = random.choice(MESSAGES)
                counter += 1
                make_commit(commit_dt, msg, counter)

        current += timedelta(days=1)

    print(f"\n✅ Done. Created {counter} backdated commits.")

if __name__ == "__main__":
    main()