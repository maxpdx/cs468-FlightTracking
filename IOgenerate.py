from random import randint, SystemRandom, choice, normalvariate, expovariate
from datetime import date
import string


def get_contents(file_path="input.dat"):
    rows = []
    f = open(file_path, "r")
    with f as file:
        for line in file:
            if line.startswith("#"):
                continue
            rows.append(parse(line))
    f.close()
    return rows


def write_contents(lists=[], file_path="output.dat"):
    f = open(file_path, "w+")

    for line in lists:
        f.write(str(line) + "\n")

    f.close()


def parse(line):
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    line = line.split(",")
    return line


def random_(length=4, sample=string.ascii_uppercase + string.digits):
    """
    Returns a random string of given length and sample
    :param length: how log the string should be
    :param sample: See https://docs.python.org/2/library/string.html for
                    string vars. Some useful examples: ascii_letters,
                    ascii_lowercase, ascii_uppercase, digits, hexdigits
    :return: [str]
    """
    return ''.join(SystemRandom().choice(sample) for _ in range(length))


def random_week_days(days=2):
    result = ""
    sample = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    while len(result) < days * 2:
        r = choice(sample)
        sample.remove(r)
        result += r
    return result


def random_date():
    t = date.today()

    y = t.year - randint(-2, 20)
    m = randint(1, 12)
    d = abs(t.day - randint(0, 28)) + 1
    return str(t.replace(y, m, d))


def random_time():
    first = random_(1, "012")
    if first != "2":
        second = random_(1, string.digits)
    else:
        second = random_(1, "0123")

    third = random_(1, "012345")
    fourth = random_(1, string.digits)

    return first + second + ":" + third + fourth


def random_datetime():
    return random_date() + random_time()
