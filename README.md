# brutepass
Easy script to generate passwords from specified words

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
    
