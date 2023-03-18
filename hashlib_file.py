import hashlib

emp = []
paswrd = input("Enter your pass: ")
key_hash = hashlib.sha256(paswrd.encode("utf-8")).hexdigest()

emp.append(key_hash)
cond = False
while True:
    x = input("PLease enter your pass:")
    input_hash = hashlib.sha256(x.encode("utf-8")).hexdigest()

    for i in emp:
        if input_hash == i:
            print("Your pass is correct")
            cond = True
            break
        else:
            print("Try again!")
    if cond:
        break
