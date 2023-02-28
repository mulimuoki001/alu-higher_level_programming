#!/usr/bin/python3

import argparse

def main(args):
    if len(args) == 0:
        print("0 arguments.")
    elif len(args) == 1:
        print("1 argument:")
        print(f"1: {args[0]}")
    else:
        print(f"{len(args)} arguments:")
        for i, arg in enumerate(args):
            print(f"{i+1}: {arg}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command-line argument parser")
    parser.add_argument("args", nargs="*", help="arguments to parse")
    try:
        args = parser.parse_args()
        main(args.args)
    except Exception as e:
        print(f"Error: {e}")
