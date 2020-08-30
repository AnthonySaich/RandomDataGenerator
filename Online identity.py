#All thre libeares used
import random
from random import randint
from datetime import datetime

#theses list varbles are used for the name password and email address
fristname = ("Liam","Noah","William","James","Oliver","Benjamin","Elijah","Lucas","Mason","Logan","Dave","James","Martin")
lastname = ("Smith","Miller","Jones","Williams","Anderson","Murphy","Jacobs","Taylor","Williams","Wright")
email = ("@gmail.com", "@Outlook.com","@mail.com","@aol.com")
letters = 'abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@£$%^&*()?|'
passwordlen = 8
cardtypee =("Visa" ,"MasterCard")
cardtype = random.choice(cardtypee)


#This selcts a random frist and last name then conbines them
firsttname = random.choice(fristname)
lastnname = random.choice(lastname)
name = (firsttname + " " + lastnname)


emaill = random.choice(email)

#This makes a random password from the password length and the letters 
password = "".join(random.sample(letters,passwordlen))

#this generates a random number between 0 and 999
ccv = random.randint(0,999)



def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

number = (random_with_N_digits(9))

##This adds the name and email list together to create a email
emaill = (name + emaill)




#This prints all of the vales to the screen

print("****************Test Data ***************")
print ("Your full name is " + name)
print (emaill)
print ("Your password is " + password)
print ("Your card type is " + cardtype)
print ("Your CCV is " + str(ccv))
print("Your phone number is  07" + str(number))
