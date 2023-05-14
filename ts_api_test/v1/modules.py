import requests
import sys
import argparse

from typing import Sequence

from ts_api_test.v1 import BASE_URL

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("api_key_file", nargs=1, type=str, help="File containing the API Key (v1)")
    args = parser.parse_args(argv)

    with open(args.api_key_file[0]) as f:
        api_key = f.read()

    print(api_key)

    return 1

if __name__ == "__main__":
    sys.exit(main())