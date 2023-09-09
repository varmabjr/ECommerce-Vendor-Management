from Abstractions.Products import Products
from Models.ProductModel import ProductModel
from Models.VendorSessionModel import VendorSessionModel


class ProductsImplementation(Products):

    def __init__(self, username):
        self.product_model = ProductModel()
        self.vendor_session = VendorSessionModel()
        self._username = username

    def add_product(self, product_name, product_type, available_quantity, unit_price):
    # check if the vendor is logged in, then add the product and return True else Return False
        if self.vendor_session.check_login(self._username):
           if self.product_model.add_product(product_name, product_type, available_quantity, unit_price):
                #print("product "+product_name+" added successfully")
                return True
           else:
               print("error in adding product " + product_name + " to the product db")
               return False
        else:
            print("vendor not logged in..could not add product")
            return False

    def search_product_by_name(self, product_name):
    # Search if the product is available in the dictionary if the vendor is authorized to access else return False
    # If product is available then return product
        if self.vendor_session.check_login(self._username):
            return( self.product_model.search_product(product_name))
        else:
            print("Vendor not logged in")
            return False

    def get_all_products(self):
        # Check if the vendor can retrieve all the product if not return False
        # otherwise return all the products

        if self.vendor_session.check_login(self._username):
                dict_all_products = self.product_model.all_products()
                return dict_all_products
        else:
            print("Vendor not logged in")
            return False
