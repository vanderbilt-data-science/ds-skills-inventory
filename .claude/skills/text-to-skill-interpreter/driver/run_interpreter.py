#!/usr/bin/env python3
"""Interactive demo driver for the text-to-skill-interpreter skill (issue #17).

For people who don't want to touch Claude Code directly: this is the
"press one button" way to see the skill work end to end. It takes one
narrative paragraph, sends it to Claude with the skill's own instructions,
and writes what comes back to a plain .txt file next to this script.

TWO WAYS TO GIVE IT YOUR TEXT (either works, no coding required):

  1. Open input.txt in this same folder, replace the paragraph in it with
     your own, save, and run this script.
  2. Or paste your paragraph into the NARRATIVE variable directly below,
     between the triple quotes, and run this script -- this always wins
     over input.txt if it's filled in.

HOW TO RUN IT:

    python3 run_interpreter.py

Requires the Claude Code CLI ("claude") to be installed and logged in --
that's the same tool this demo was built with. Nothing else to install.
"""
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# EDIT ME: paste a narrative paragraph here to use it instead of input.txt.
# Leave it as "" to read from input.txt in this folder instead.
NARRATIVE = ""
# ---------------------------------------------------------------------------

DRIVER_DIR = Path(__file__).resolve().parent
SKILL_DIR = DRIVER_DIR.parent
REPO_ROOT = SKILL_DIR.parent.parent.parent
INPUT_FILE = DRIVER_DIR / "input.txt"
OUTPUT_FILE = DRIVER_DIR / "output.txt"
SKILL_FILE = SKILL_DIR / "SKILL.md"
RUBRIC_FILE = REPO_ROOT / "skill-level-rubric.md"
TIMEOUT_SECONDS = 300


def get_narrative():
    if NARRATIVE.strip():
        print("Using the paragraph pasted into the NARRATIVE variable.")
        return NARRATIVE.strip()
    if INPUT_FILE.exists() and INPUT_FILE.read_text().strip():
        print(f"Using the text in {INPUT_FILE.name}.")
        return INPUT_FILE.read_text().strip()
    sys.exit(
        "No narrative text found. Either paste a paragraph into the "
        "NARRATIVE variable at the top of this script, or put one in "
        f"{INPUT_FILE.name}."
    )


def build_prompt(narrative):
    skill_instructions = SKILL_FILE.read_text()
    rubric = RUBRIC_FILE.read_text()
    return f"""You are running the text-to-skill-interpreter skill as a one-shot,
non-interactive demo. Follow the skill's procedure exactly and rely only on
the material below -- do not read or write any files, you have been given
everything you need as text.

===== SKILL.md =====
{skill_instructions}

===== skill-level-rubric.md =====
{rubric}

===== NARRATIVE TO INTERPRET =====
{narrative}
===== END NARRATIVE =====

Produce, as your entire reply:
1. The JSON observation log described in the skill (matching its schema).
2. Then the short plain-text summary described in the skill's step 8.
Nothing else -- no preamble, no offer to do more.
"""


def run_claude(prompt):
    if shutil.which("claude") is None:
        sys.exit(
            "Can't find the 'claude' command on this machine. Install the "
            "Claude Code CLI and make sure you're logged in, then try again."
        )
    print("Asking Claude to score the narrative against the rubric... "
          "(this can take a minute)")
    result = subprocess.run(
        ["claude", "-p"],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=TIMEOUT_SECONDS,
        cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        sys.exit(f"claude exited with an error:\n{result.stderr}")
    return result.stdout.strip()


def main():
    narrative = get_narrative()
    prompt = build_prompt(narrative)
    response = run_claude(prompt)

    header = (
        f"text-to-skill-interpreter demo run\n"
        f"generated: {datetime.now().isoformat(timespec='seconds')}\n"
        f"{'-' * 60}\n\n"
    )
    OUTPUT_FILE.write_text(header + response + "\n")
    print(f"Done. Results written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
