import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if 'iframe' not in s:
        return(None)
    else:
        if url := re.search(r'(http)s?(://)(?:www\.)?(youtu)(be).com/embed(/[\w]{11})', s):
            return(url.group(1) + 's' + url.group(2) + url.group(3) +'.' + url.group(4) + url.group(5))


if __name__ == "__main__":
    main()