'''
@Date:  2021-12-01
@Author:Srividya
@Title : User_login

'''

import pytest
import user_register

class TestClass:
    def test_username1(self):
        """"
        Description: this function will test the firstname
        Parameter: self
        Return: None
        """
        user_register.firstname = 'Srividya'
        assert user_register.firstname=='Srividya'

    def test_username2(self):
        """"
        Description: this function will test the lastname
        Parameter: self
        Return: None
        """
        user_register.lastname = 'Vangapelli'
        assert user_register.lastname=='Vangapelli'

    def test_email(self):
        """"
        Description: this function will test the email
        Parameter: self
        Return: None
        """
        user_register.email = 'vangapellisreevidya@gmail.com'
        assert user_register.email=='vangapellisreevidya@gmail.com'
    
    def test_password(self):
        """"
        Description: this function will test the password
        Parameter: self
        Return: None
        """
        user_register.password = 'Sri@123'
        assert user_register.password=='Sri@123'

    def test_phonenumber(self):
        """"
        Description: this function will test the phonenumber
        Parameter: self
        Return: None
        """
        user_register.phonenumber = '917036653770'
        assert user_register.phonenumber=='917036653770'

    def test_values1(self):
        """"
        Description: this function will test the firstname
        Parameter: self
        Return: None
        """
        with pytest.raises(TypeError):
            assert user_register.firstname(self) == 123
    def test_values2(self):
        """"
        Description: this function will test the lasstname
        Parameter: self
        Return: None
        """
        with pytest.raises(TypeError):
            assert user_register.lastname(self) == 123
        
    def test_values3(self):
        """"
        Description: this function will test the email
        Parameter: self
        Return: None
        """
        with pytest.raises(TypeError):
            assert user_register.email(self) == 'vidygmail.com'
            
    def test_values4(self):
        """"
        Description: this function will test the phonenumber
        Parameter: self
        Return: None
        """
        with pytest.raises(TypeError):
            assert user_register.phonenumber(self) == 'helo'
    def test_values5(self):
        """"
        Description: this function will test the password
        Parameter: self
        Return: None
        """
        with pytest.raises(TypeError):
            assert user_register.password(self)=='vidya123'

