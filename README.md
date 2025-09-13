# Project Overview-
This project is a Tkinter-based Grocery Store Application developed in Python. It simulates a shopping experience for customers where they can scan a QR code, browse categories, add items to the cart, verify their details with OTP, and make payments through UPI or Card. The application generates a bill summary, calculates GST, and provides a feedback section for customer reviews.

Currently, this project is designed only for the customer-side interface. It does not include a cashier/administrator dashboard yet, and no database has been connected. The QR code feature is implemented but not fully functional at this stage.



Features Implemented

QR Code Access – Customers enter the store by scanning a QR code (placeholder, not fully functional).

Category Selection – Items are organized into categories like Fruits, Vegetables, Home Grocery, and Stationery.

Add to Cart – Customers can select items, enter quantity, and reserve stock.

Cart & Billing – The application generates subtotal, GST (18%), and final payable amount.

Customer Details – Input fields for customer name and phone number.

OTP Verification – A random OTP is generated to verify customer details before payment.

Payment Options – Customers can choose between UPI and Card payments.

Bill Summary – Displays a detailed summary of purchased items, including customer details and a generated bill number.

Feedback Section – Customers can rate their experience with stars and leave text reviews.



Python Functions and Libraries Used

Tkinter – For GUI development (frames, buttons, labels, text fields, etc.).

ttk (Themed Tkinter Widgets) – For improved input fields and labels.

messagebox – For alerts, confirmations, and error messages.

qrcode – To generate store QR codes.

Pillow (PIL) – For image processing and displaying product images/logo.

random – To generate OTP, bill numbers, and store IDs.



Current Limitations

No database integration – item stock and customer details are stored in memory only.

QR code scanning is not yet functional.

No cashier/administrator interface.

Future Improvements

Add database connectivity to store products, customer details, and transactions.

Make QR code scanning fully functional for secure store entry.

Develop a cashier/manager interface to manage stock, verify orders, and handle payments.

Improve UI with responsive layouts and better product image handling.
