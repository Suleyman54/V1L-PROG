oldpassword = str(input("wat is je oude wachtwoord"))
newpassword = str(input("wat wil je als nieuw wachtwoord"))
def new_password(oldpassword, newpasword):
    if newpassword != str(oldpassword) and len(newpassword)>=6:
        return 'true'
    else:
        return 'false'
print(new_password(oldpassword, newpassword))





