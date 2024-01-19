import hashlib
import time


# hashing password
with open('passes_real.txt', 'r') as passwdfile:
    passwdlist = passwdfile.readlines()

# store hashes in th pass_dict
pass_dict = {}
for passwd in passwdlist:
    passwd = passwd.strip()
    try:
        # Attempt to decode with UTF-8, then encode to UTF-8
        hashed_passwd = hashlib.sha256(passwd.decode('utf-8').encode('utf-8')).hexdigest()
    except UnicodeDecodeError:
        # If UTF-8 fails, you might need to try a different encoding, or skip the password
        continue
    
    pass_dict[hashed_passwd] = passwd


# create [username, hash(password)] list
breachlist = []
with open('breached_data.txt', 'r') as breachedfile:
    breachlist = breachedfile.readlines()
    breachlist = [item.split() for item in breachlist]

# for each hash(password), chech it in the dictionary
count = 0
start_time = time.time()
with open('cracked_passwords.txt', 'w') as crackfile:
    for item in breachlist:
        if item[1] in pass_dict:
            crackfile.write("{}: {}\n".format(item[0], pass_dict[item[1]]))
            count += 1

end_time = time.time()
print("Time used: {}".format(end_time - start_time))
print("number of password cracked: {}".format(count))