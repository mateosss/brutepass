# Brutepass
Easy script to generate passwords lists from combining specified words in various ways.

Passwords usually are made of combinations of words/numbers/whatever that have some kind of meaning for the user. This script supposes you already have those possible striings from which a password could be made, and combines and modifies them in different ways.

It was inspired from the first episode of Mr Robot, in which Elliot hacks his therapist, using a script similar to this.

Brutepass creates a password list, which should be a lot smaller than trying with bruteforce, at least of course you use thousand of strings.

The script is pretty fast, for common use, it usually takes less than seconds in a low profile i3 notebook, for a general picture, with 450 input words, it takes about 80 seconds. It could however be improved, currently it is single threaded. For some reason running it in python2.7 is about 20% faster than in python3.

    Usage Example:
    python brutepass.py -t 3600 -d -s 100 -o pass.txt -w tag1 tag2 tag3 tag4

    Commands:
    -h: Show this help.
    -t: Specifies the max time (in seconds) to spend in generating passwords.
    -s: Specifies the max size (in kilobytes) of the file of passwords.
    -w: List of tags to make passwords from.
    -o: Specifies the output file in which the passwords will be stored (default: passwords.txt).
    -d: Tells the program to use the defaults tags (F.e. "1234", "admin", "", "root").
    -i: Specifies an input file with tags to prove.
    
#Things to do

- Make -t parameter functional
- Make -s parameter functional
- Make pausable and resumable password generation
- Make multithreaded password generation
- Continue proposing new combinations to add more combination types (make polls, and test with people the script)
    - Insert one word in the middle of other [perro, pato] = pepatorro, paperroto
    - Change vocals to numbers Microfono = M1cr0f0n0
    - Add l33t combinations
    - Invert words
