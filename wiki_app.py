#!/usr/bin/env python3
import wikipedia as wiki
import re
import sys
import argparse


def get_random_title():
    title = wiki.random()
    print("Random article's title:")
    print(title)

    ans = input(
        "Do you want to read it?\n (Press any key if yes or \"n\" if you want to see next suggestion)\n\
            Press \"q\" to quit")

    if ans in ("n", "next"):
        return get_random_title()
    elif ans == "q":
        print("sorry for that")
        sys.exit(0)
    else:
        return title


def search_title(search):

    titles = wiki.search(search)
    print("We found such articles:\n")
    print(*[f"\"{t}\","for t in titles[:5]], "\n")

    for title in titles:
        print("Did you mean \"{}\"?\n Press any key if yes or \"n\"".format(title),
              "if you want to see next suggestion")
        ans = input("Press \"q\" to quit")
        if ans in ("n", "next"):
            continue
        elif ans == "q":
            print("sorry for that")
            sys.exit(0)
        else:
            return title


def split_paragraphs(text):

    text = re.sub(r"\s{2,}", " ", text)


    pat = re.compile(
        r"(?:(?:(?:\n+)?)(?:\s?)(?:={2,})(?:\s*?)(?:.+)(?:\s*?)(?:={2,})(?:(?:\n+)?))+")

    paragraphs = pat.split(text)

    pat2 = re.compile(
        r"(?:(?:(?:\n+)?)(?:\s?)(?:={2,})(?:\s?)(.+)(?:\s?)(?:={2,})(?:(?:\n+)?))")

    titles = list(map(lambda x: x.strip(), ["Summary"] + pat2.findall(text)))

    result = dict(zip(titles, paragraphs))
    if "References" in result:
        del result["References"]
    return result


if __name__ == "__main__":
    global keyPressed
    keyPressed = None

    parser = argparse.ArgumentParser()
    parser.add_argument("search", type=str, nargs='?',
                        help="search wiki article by title")
    args = parser.parse_args()

    if args.search:
        name = search_title(args.search)
    else:
        name = get_random_title()

    print("Article is loading. Please, wait...")
    page = wiki.page(name)

    paragraphs = split_paragraphs(page.content)

    for title in paragraphs:
        print("\n")
        print("=== ", title, " ===")
        print(paragraphs[title])
        ans = input(
            "Press any key to proceed, \"q\" to quit")
        if ans == "q":
            sys.exit(0)
