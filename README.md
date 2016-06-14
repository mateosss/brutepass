# Brutepass
Easy script to generate passwords from specified words

Trying to figuring out how someone tries to determine a password of another person, I am writting a script to automate password generation by give to it words that can be in the password in some way or another, and making lots of possible human combinations of that words.

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
- Make multithreaded, multicore, cluster ready, password generation
- Investigate to add more combination types (make polls, and test with people the script)
- Insert one word in the middle of other [perro, pato] = pepatorro, paperroto
- Change vocals to numbers Microfono = M1cr0f0n0
