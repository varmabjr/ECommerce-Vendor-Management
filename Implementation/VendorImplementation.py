from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel


class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()

    def login(self, username, password):
        # Add you code here after verifying the vendor data exists in the dictionary

        if (self.vendor_model.is_correct_vendor(username,password))==True:
            self.vendor_session.login(username)
            return True
        else:
            return False


    def logout(self, username):
        # Add your code here to log out the current vendor

        if(self.vendor_session.logout(username)==True):
            print("Vendor "+username+" has logged out successfully")
        else:
            print("Error in logging out Vendor "+username)

