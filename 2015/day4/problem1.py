import hashlib


def main(start):
    i = 0
    while True:
        text = f"{start}{i}"
        hash_ = hashlib.md5(bytes(text, "ascii"))
        hash_ = hash_.hexdigest()
        if hash_.startswith("00000"):
            break
        i += 1
    print(i)


if __name__ == "__main__":
    main("yzbqklnj")
