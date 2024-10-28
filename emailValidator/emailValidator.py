email=input("Enter your email: ")
k, j, d=0,0, 0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1 #just a variable being increased, will use it later to tell that there is space
                    elif i.isalpha():
                        if i==i.upper():
                            j=1 #checks if there is upper case ...used for testing and showing result
                    elif i.isdigit():
                        continue #if there is digit then it's fine move to next step
                    elif i =="_" or i =="." or i=="@":
                        continue #if there is @, . or _ then it's fine move to next step
                    else:
                        d=1
                if k==1 or j ==1 or d==1:
                    print("email me spaxe, capital letters in dalte hai balak")
                else:
                    print("valid email")
            else:
                print("email me ek hi dot hoga domain me 4")
        else:
            print("email should have at most @ in it 3")
    else:
        print("email must start with a alphabet 2")
else:
    print("how come your email is less than 6 characters 1")