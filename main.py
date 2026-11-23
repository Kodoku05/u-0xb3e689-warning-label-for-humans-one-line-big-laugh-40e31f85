"""Write the competition's deterministic, one-line warning label."""

import os
from pathlib import Path
import sys


LABEL = "WARNING: This human read the instructions exactly once, understood none of them, and will now improvise with total confidence. Stand clear."


def main() -> int:
    # Fail loudly instead of shipping an empty or over-long entry.
    # The label is 139 code points: inside the 1-160 gate with room to spare,
    # and the length check below guards it if the text is ever edited.
    if not LABEL.strip() or len(LABEL) > 160:
        print("Label fails the entry gate (1-160 code points, not blank)",
              file=sys.stderr)
        return 1
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        # Write explicit UTF-8 bytes so the artifact is identical on every platform.
        (output_dir / "entry.txt").write_bytes(LABEL.encode("utf-8"))
    except OSError as exc:
        print(f"Could not write entry: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
