def email_slicer(email):
    username = email.split('@')[0]
    domain = email.split('@')[1]
    if domain == "gmail.com":
        domain =''
    print(f"username: {username}")
    if domain:
        print(f"Domain: {domain}")
    else:
        print("Domain: Remove 'gmail.com'")
    # print(last.pop)2

email = input("Enter your Email: ")
email_slicer(email)