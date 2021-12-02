'''
@Date:  2021-11-28	
@Author:Srividya
@Title : User_login

'''
import re
    
def firstname(self):
    """"
        Description: this function will take the input from user as firstname
        Parameter: self
        Return: firstname
    """
    firstname= 'Srividya'
    pattern="^[A-Z]{1}|[a-z][.]+\s[A-Z][a-z]+$"
    result=re.match(pattern,firstname)
    if result:
        if type(firstname) in [str] :
            return firstname
    else:
        raise TypeError("name must be in string format")

def lastname(self):
    """"
        Description: this function will take the input from user as lasstname
        Parameter: self
        Return: lastname
    """
    lastname= 'Vangapelli'
    pattern="^[A-Z]{1}|[a-z][.]+\s[A-Z][a-z]+$"
    result=re.match(pattern,lastname)
    if result:
        return lastname
    else:
        raise TypeError("name must be in string format")

def email(self):
    """"
        Description: this function will take the input from user as email
        Parameter: self
        Return: emai
    """
    email= 'vangapellisreevidya@gmail.com'
    pattern="^[a-zA-Z0-9]+([.#_$+-][a-zA-Z0-9]+)*[@][a-zA-Z0-9]+[.][a-zA-Z]{2,3}([.][a-zA-Z]{2})?$"
    result=re.match(pattern,email)
    if result:
        return email
    else:
        raise ValueError("email must be in given format")

def phonenumber(self):
    """"
        Description: this function will take the input from user as email
        Parameter: self
        Return: emai
    """
    phonenumber=  '7036653770'
    pattern="^[789]\d{9}$"
    result=re.match(pattern,phonenumber)
    if result:
        return phonenumber
    else:
        raise ValueError("PhoneNumber must be in given format")

def password(self):
    """"
        Description: this function will take the input from user as password
        Parameter: self
        Return: password
    """
    password= 'Sri@123'
    #pattern= "^[A-Z]+[a-zA-Z](\s)*$"
    pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,8}$"
    result=re.match(pattern,password)
    if result:
        return password
    else:
        raise ValueError("password must be in given format includes A,a,0-9,and special characters ")
    
    def test_values1(self):
        """"
        Description: this function will test the firstname
        Parameter: self
        Return: None
        """
        self.assertRaises(TypeError,firstname(123),123)
    def test_values2(self):
        """"
        Description: this function will test the lasstname
        Parameter: self
        Return: None
        """
        self.assertRaises(TypeError,lastname(123),123)
        
    def test_values3(self):
        """"
        Description: this function will test the email
        Parameter: self
        Return: None
        """
        self.assertRaises(TypeError,email('vidygmail.com'),'vidygmail.com')
            
    def test_values4(self):
        """"
        Description: this function will test the phonenumber
        Parameter: self
        Return: None
        """
        self.assertRaises(TypeError,phonenumber('helo'),'helo')
    def test_values5(self):
        """"
        Description: this function will test the password
        Parameter: self
        Return: None
        """
        self.assertRaises(TypeError ,password('vidya123'),'vidya123')
    

if __name__=='__main__':
    firstname(self="")
    lastname(self="")
    email(self="")
    password(self="")
    phonenumber(self="")