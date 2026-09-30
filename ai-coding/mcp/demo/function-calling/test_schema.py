import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from agent import QueryArgs
from pydantic import ValidationError


def test_extra_argument_is_rejected():
    try:
        QueryArgs(sql="SELECT 1", limit=10)
    except ValidationError:
        return
    raise AssertionError("extra tool arguments must be rejected")


if __name__ == "__main__":
    test_extra_argument_is_rejected()
    print("ok")
