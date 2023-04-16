def read_input():
    num = None
    while not num:
        mode = input("Enter input mode (F/I): ")
        
        if mode == "F":
            with open("tests/06", "r") as f:
                pat = f.readline()
                txt = f.readline()
            return (pat, txt)
        
        if mode == "I":
            return (input().rstrip(), input().rstrip())

        else:
            print("Wrong mode")

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    d = 256
    plen = len(pattern)
    tlen = len(text)
    phash = 0
    thash = 0
    h = 1
    q = 101
    result = []

    # calculate h that'll be used in calculating next hash
    # same as pow(d, plen - 1) % q
    # modulo each iteration to avoid integer overflow
    for i in range(plen - 1):
        h = (h * d) % q
    
    # calculate initial hash values
    for i in range(plen):
        phash = (d * phash + ord(pattern[i])) % q
        thash = (d * thash + ord(text[i])) % q

    # each loop iteration moves the window by one char
    for i in range(tlen - plen + 1):
        if phash == thash:
            # double check in case hashes are the same but the strings aren't
            if text[i : i + plen] == pattern:
                #print("Found at index " + str(i))
                result.append(i)

        # compute a new hash using the O(1) formula for computing a new hash
        if i < tlen - plen:
            thash  = (d * (thash - ord(text[i]) * h) + ord(text[i + plen])) % q

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))