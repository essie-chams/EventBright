
class User:
    
    user = dict()
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.uname = ""
        self.email = ""
        self.pword = ""
        self.cpword = ""
        #initializing the user dictionary 
        self.user = {self.uname:
        {'fname': self.fname,'lname': self.lname, 'email': self.email, 'password': self.pword, 'c_password': self.cpword}
        }
            
    #method to create user account 
    def create_user(self, fname, lname,email, uname, pword, cpword):
        if fname != '' and lname != '' and uname != '' and pword != '' and cpword != '':
            if pword == cpword:
                self.user = {uname:{'fname': fname,'lname': lname, 'email': email, 'password': pword, 'c_password': cpword}}
            else:
            	return "Password and confirm password do not match"
        else:
        	return "please input all the fields"
    #method to delete user account
    def user_delete(self, uname):
    	if uname in self.user.keys():
    		self.user.pop(uname)

    	else:
    		return "User does not exists. Please create account"

    #method to view user datails 
    def view_user_details(self):
    	return self.user.items()


    #method to modify user details
    def modify_user(self, fname, lname,email, uname, pword, cpword):
    	if fname != '' and lname != '' and uname != '' and pword != '' and cpword != '':
            if pword == cpword:
            	if uname in self.user.keys():
            		   self.user = {uname:{'fname': fname,'lname': lname, 'email': email, 'password': pword, 'c_password': cpword}}
               
'''
Trying the functionality of the class'''
