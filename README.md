# Cash-Register

Cash Register System
Overview:
    This project is a Python-based cash register system designed to manage sales, inventory, and payments in a retail environment. The system is modular, with separate components handling different aspects of the business, such as inventory management, packaging, and payment processing.

Project Structure:
    The project is organized into the following modules:

        cash_register.py - This module handles the main cash register operations, including the processing of sales transactions and interaction with other modules.

        inventory.py - This module manages the inventory of products, including stock levels, product details, and inventory updates.

        packaging.py - This module handles the packaging process, ensuring products are appropriately packed before being handed over to the customer.

        payment.py - This module deals with payment processing, supporting various payment methods and ensuring secure transactions.

        test_inventory.py - This module contains unit tests for the inventory.py module to ensure that inventory operations are functioning correctly.

Features:
        Inventory Management: Tracks product stock levels, updates inventory after sales, and ensures that the correct items are available for purchase.
        
        Packaging: Manages the packaging of products, ensuring they are ready for delivery or pick-up.
        
        Payment Processing: Supports multiple payment methods, ensuring transactions are secure and accurately recorded.
        
        Modular Design: Each module is designed to handle specific aspects of the retail process, making the system flexible and easy to maintain.

Installation:
    To use this system, you'll need to have Python installed on your machine.


Run the tests: Before running the system, you can test the inventory management functionality:
    use pytest in the terminal. 



Run the program: 
    python3 cash_register.py

Usage:
    Start the System: Run the cash_register.py script to initiate the cash register system.
    
    Manage Inventory: Use the inventory management features to add, update, and check product stock levels.
    
    Process Sales: Handle customer transactions, manage payments, and update the inventory accordingly.
    
    Packaging: Ensure products are correctly packaged before delivery.



README.md was generated using ChatGPT. 