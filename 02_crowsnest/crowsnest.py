#!/usr/bin/env python3
"""
Author : robertmikolajczyk <ronert1674@gmail.com>
Date   : 2025-05-12
Purpose: Crow's Nest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word",
                        metavar="word",
                        help="A word")

    parser.add_argument('--starboard',
                        help='A right side of the board',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    side = args.starboard

    sideboard = "starboard" if side else "larboard"
    article = "an" if word[0].lower() in "aeiou" else "a"
    print(f"Ahoy, Captain, {article} {word} off the {sideboard} bow!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
