import requests
import sys
import argparse

from typing import Sequence

from ts_api_test.v1 import BASE_URL

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_key", nargs=1, type=str, help="API Key for the v1 API")
    args = parser.parse_args(argv)

    print(args.api_key)

    return 1

if __name__ == "__main__":
    sys.exit(main())