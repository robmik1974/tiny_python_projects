#! /usr/bin/env python3
"""
Author: Robert Mikolajczyk
email: ronert1674@gmail.com
Purpose: Say hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    print("Hello, " + args.name + "!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
