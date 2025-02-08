import argparse
from src.prefix import change_prefix
from src.constants import (
    COMPUTER_DATA_WIN_ROOT,
    PHONE_MUSIC_ROOT,
    COMPUTER_PLAYLIST_ROOT,
)
from pathlib import Path


def main():
    argp = argparse.ArgumentParser(description="Hello from music!")
    argp.add_argument("--input-dir", default=None)
    argp.add_argument("--output-dir", default=None)
    args = argp.parse_args()

    print("Hello from music!")

    if args.input_dir:
        input_dir = Path(args.input_dir)
        input_root = PHONE_MUSIC_ROOT
        output_dir = COMPUTER_PLAYLIST_ROOT
        output_root = COMPUTER_DATA_WIN_ROOT
    elif args.output_dir:
        input_dir = COMPUTER_PLAYLIST_ROOT
        input_root = COMPUTER_DATA_WIN_ROOT
        output_dir = Path(args.output_dir)
        output_root = PHONE_MUSIC_ROOT
    else:
        raise ValueError("Either input_dir or output_dir must be provided")

    change_prefix(input_dir, output_dir, input_root, output_root)


if __name__ == "__main__":
    main()
