import hashlib

with open('passes_real.txt', 'r') as passwdfile:
    passwdlist = passwdfile.readlines()


with open('generate_unsalted_table.txt', 'w') as hashfile:

    for passwd in passwdlist:
        passwd = passwd.strip()
        hashed_passwd = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
        hashfile.write('{}: {}\n'.format(hashed_passwd, passwd))

        print(hashed_passwd, passwd)

