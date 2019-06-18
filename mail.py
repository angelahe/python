#make a function called email
#received 2 parameters: first name and last name
#e.g. Larry Shumlich => larry.shumlich@evolveu.ca
#e.g. Heiko Peters => heiko.peters@evolveu.ca

#write an automated test that will check the results are what you expect
#email the test to Larry before you write the code

def make_email(first="", last=""):
    #first.last@evolveu.ca
    email = None

    lastname = last.lower()
    firstname = first.lower()

    #if first.len() == 0 and last.len() == 0
    if len(first) > 0:
        if len(last) > 0:
             email = firstname+'.'+lastname+'@evolveu.ca'
        else:
            email = firstname+'@evolveu.ca'
    else:
        if len(last) > 0:
            email = lastname+'@evolveu.ca'
    
    return email

