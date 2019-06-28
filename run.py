# Import needed libraries and such
import os
import random
import timeit

alphanumeric_ranges = [
    ( 0x0030, 0x0039 ), # Digits
    ( 0x0041, 0x005A ), # Upper-Case Alphabet
    ( 0x0061, 0x007A ), # Lower-Case Alphabet
]

# Random Unicode Generation
def get_random_file():
    
    files_each = 100
    sizes = [           # Should really make a way to randomize size too
        500,
        1000,
        10000,
        100000,
        1000000,
        100000000,
    ]

    if not os.path.isdir("output"):
        os.mkdir("output")
    
    # Would be a good idea to use iterator and generator here

    for x in range(0, files_each):
        for s in sizes:
            with open('output/' + get_random_filename(), 'ab') as fout:
                # Not exactly the most elegant code, but Windows didn't like
                # what I had before.
                if s < 1000000:
                    print(s)
                    fout.write(os.urandom(get_random_size(s*1024)))
                else:
                    for i in range(0, int(get_random_size(s)/100)):
                        print(i)
                        fout.write(os.urandom(100000))

def get_random_size(size):
    return size + random.randrange(0 - (size/10), (size / 10) +1 )

def get_random_filename():
    name_length = random.randint(1,13)
    extension_length = random.randint(2,3)
    file_name = [
        chr(code_point) for current_range in alphanumeric_ranges
            for code_point in range(current_range[0], current_range[1]+1 )
    ]
    filename = ''.join(random.choice(file_name) for i in range(name_length))
    extension = ''.join(random.choice(file_name) for i in range(extension_length))
    return filename + '.' + extension

if __name__ == "__main__":
    print(timeit.timeit("get_random_file()", setup="from __main__ import get_random_file"))
