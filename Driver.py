from Implementation.ProductsImplementation import ProductsImplementation
from Implementation.VendorImplementation import VendorImplementation

# Student name: Jophy Joseph
# IIIT Hyderabad: Post Graduate Certificate in Software Engineering for Data Science . IIITH-SEDS-Part A_July 21
# OOP Assignment Submission
# Submission Date : Aug 22,2021

if __name__ == '__main__':

    vendor = VendorImplementation()

    login_res = vendor.login('Rossum', 'rossum_pw')

    #login_res = vendor.login('Jophy', 'rossum_pw')              #TestCase 1 : Invalid User


    if login_res == False:
        print("Not Authorized Vendor")
    else:
        products = ProductsImplementation('Rossum')
        products.add_product("Lenovo Thinkpad", "Laptop", 40, 20000)
        products.add_product("Dell Inspiron", "Laptop", 40, 30000)
        products.add_product("Acer razor", "Laptop", 40, 25000)        
        products.add_product("Asus Tinker", "Laptop", 40, 20000)
        products.add_product("Lenovo Gaming", "Laptop", 40, 20000)



        search_product = products.search_product_by_name("Lenovo Gaming")

        #search_product = products.search_product_by_name("Apple Macbook")       #TestCase 2 : Non existent product

        if (search_product):
            print("Searched product: "+ str(search_product))
        else:
            print("No product exists by the name")

        print()
        all_products = products.get_all_products()

        #all_products = ''                                      #TestCase 3 : No products

        if (all_products):
            print("**** List of All Products ****")
            for p_id, p_info in all_products.items():
                print("\nProduct Name:", p_id)
                for key in p_info:
                    print("\t"+key + ':', p_info[key],end='')
        else:
            print("No product is available to fetch.")
            
        print()
        print()
        vendor.logout("Rossum")