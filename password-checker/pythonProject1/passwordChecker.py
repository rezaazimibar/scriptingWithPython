import hashlib
import sys

import requests


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"error fetching: {res.status_code}, check the api and try again")
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, c in hashes:
        if hash_to_check == h:
            return c
    return 0


def pwned_api_check(password):
    sha1_pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1_pass[:5], sha1_pass[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main_func(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{count} was found try another password")
        else:
            print(f"{password} is good choice carry on")
    return "done!"


if __name__ == "__main__":
    sys.exit(main_func(sys.argv[1:]))
