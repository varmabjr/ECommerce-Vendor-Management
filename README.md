# ECommerce Vendor Management system

The system supports various features such as storing the
product data for different vendors.

Here each vendor can save various products and fetch that information whenever required. The
focus of the project is to design and implement various functionalities based on that.
Each vendor will have their user_name and password, based on that they can login and retrieve
the saved product information.

This product will leverage the core OOPs concepts covered such as class, object, methods,
inheritance, abstraction etc. 

Program Organization
The simple program is structured in various layers.
1. Abstractions:
a. Products.py: This file will have the implementation abstract class and methods
that are going to be implemented in the Implementation package for product
related tasks. The abstract method in Product.py will be there to do
add_product(), search_product(), all_products().
b. Vendor.py: This file will have the implementation abstract class and methods that
are going to be implemented in the Implementation package for vendor related
operations. The abstract method in Vendor.py will be there to do login(), logout().

2. Implementation:
a. ProductsImplementation.py: In this file learners should implement the actual
functionalities that are mentioned in driver.py for product implementation. The
methods in the created class will be the extension of the methods created as
abstract methods in the abstraction package.
b. VendorImplementation.py: In this file learners should implement the actual
functionalities that are mentioned in driver.py for vendor implementation. The
methods in the created class will be the extension of the methods created as
abstract methods in the abstraction package.

3. Models:
a. ProductModel.py: Implementation of the class and methods that are performing
Create and Read operation on the product database.
b. VendorModel.py: Implementation of class and methods that implements the
functionality of loading existing vendors. In this model we are also checking if the
correct vendor is passed for VendorSessionModel.
c. VendorSessionModel.py: Before performing several operations such as adding
the product information, reading the product data, functionality such as login,
logout of the vendors are implemented in this file.

4. driver.py: This file imports the implementation package for product and vendor that has
all the methods already implemented and available for use. Take a close look at the
method names that are being used to perform the functionality
 
