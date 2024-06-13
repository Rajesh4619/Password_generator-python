#importing random module
import random                      
def generate_password(pwlength):  
      # defining the list of characters that will be used to generate the password  
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"  
    passwords = [] 
    #pwlength=contains list of password lengths
    for i in pwlength:
        pass_str = "" 
        for j in range(i):
            pass_str = pass_str+ random.choice(list_of_chars)  
        passwords.append(pass_str) 
    
    return passwords
    
# main function  
def main():
    
    numPasswords = int(input("How many passwords would you like to generate? "))
    
    print("Generating " +str(numPasswords)+" passwords")
    
    passwordLengths = []

    print("The password should have a minimum length of 3 characters ")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length<3:
            length = 3
        #storing the all passwords lengths in a list
        passwordLengths.append(length)
  
    Password = generate_password(passwordLengths)

    
    # printing the final result for the users  
    for i in range(numPasswords):
        print ("Password #"+str(i+1)+" = " + Password[i])
#calling the main function
main()