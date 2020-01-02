import random
from typing import Any, Union


def primary():
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    last = 13
    rnd: Union[int, Any] = random.randint(0, last)
    print(quotes[rnd])


if __name__ == "__main__":
    primary()
