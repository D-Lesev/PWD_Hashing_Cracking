import hashlib
import string
import pyautogui
import random
from datetime import datetime

#  We use MD5 method but we can replace it with SHA256

pswd_list = []
cond = False
result_time = 0
count = 0
while True:

    #  Asking user to enter his password
    password_input = pyautogui.password("Enter your password(exactly 5 symbols):")

    #  Checking if the password is with required length
    if len(password_input) == 5:

        #  Hashing the user password and adding it to the empty list
        hash = hashlib.md5(password_input.encode('utf-8')).hexdigest()
        pswd_list.append(hash)

        #  Starting time to calculate how much time it will take in order to find the password
        start_time = datetime.now()
        while True:

            #  Starting the script to search for the user's password
            #  Only use lower case letter with exactly 5 chars length
            guess_pass = random.choices(string.ascii_letters, k=5)

            #  Choice method give us separate symbols, so we need to concatenate them
            guess_concat = ''.join(guess_pass)

            #  We hash the concatenate password and compare it with the hash from the user's password
            #  Import thing is that we need to know what hash algorithm the system is using
            hashed_pwd = hashlib.md5(guess_concat.encode('utf-8')).hexdigest()

            #  Comparing the hashes
            if hashed_pwd == pswd_list[0]:
                print(f"Your password is correct !\nThe password is {guess_concat}")
                cond = True

                #  Ending time and checking the difference in order to find out the time it took to find the password
                end_time = datetime.now()
                result_time = end_time - start_time
                break
            else:
                #  Just implemented a normal count to show the user that the program is running and checking passwords
                count += 1
                if count % 100000 == 0:
                    print(f"Decrypting....\nTotal checked passwords {count}")
                continue

    else:
        print("Wrong length. Try again!")

    if cond:
        break

print(f"Total count {count}\nTotal time: {result_time}")