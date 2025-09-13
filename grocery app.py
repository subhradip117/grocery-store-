import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk
import random


# Product categories with stock availability
grocery_items = {
    "Fruits": {
        "Apple": {"price": 50, "quantity": 10},
        "Banana": {"price": 20, "quantity": 15},
        "Mango": {"price": 151, "quantity": 5}
    },
    "Vegetables": {
        "Potato": {"price": 30, "quantity": 20},
        "Tomato": {"price": 40, "quantity": 18},
        "Onion": {"price": 35, "quantity": 25}
    },
    "Home Grocery": {
        "Rice": {"price": 80, "quantity": 50},
        "Flour": {"price": 60, "quantity": 30},
        "Sugar": {"price": 50, "quantity": 40}
    },
    "Stationery": {"Pencil": {"price": 5, "quantity": 50},
                   "Eraser": {"price": 10, "quantity": 30}, 
                   "Notebook": {"price": 50, "quantity": 40}}
}

class GroceryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crazy Grocery Shop")
        self.root.geometry("500x500")
        self.cart = {}
        self.history = []
        self.store_id = self.generate_qr()
        self.qr_screen()
        self.otp = None  # Store OTP for verification

    def clear_screen(self):
        """Clears the screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def generate_qr(self):
        """Generates a QR code for store access."""
        store_id = f"Store-{random.randint(1000, 9999)}"
        qr = qrcode.make(store_id)
        qr.save("store_qr.png")
        return store_id

    def qr_screen(self):
        """Displays the QR code."""
        self.clear_screen()
        tk.Label(self.root, text="Scan the QR Code to Access Inventory", font=("Arial", 14, "bold")).pack(pady=10)
        qr_img = Image.open("store_qr.png").resize((200, 200))
        qr_img = ImageTk.PhotoImage(qr_img)
        tk.Label(self.root, image=qr_img).pack()
        self.root.qr_img = qr_img  # Prevent garbage collection
        tk.Button(self.root, text="Proceed to Shop", font=("Arial", 12, "bold"), command=self.welcome_screen, bg="#28a745", fg="white").pack(pady=10)


    def welcome_screen(self):
        self.clear_screen()

    # Load and place header image
        try:
            logo_image = Image.open("C:/Users/PC/Downloads/image-removebg-preview.png")  
            logo_image = logo_image.resize((50, 50))
            self.logo_photo = ImageTk.PhotoImage(logo_image)  # Store reference
        except:
            self.logo_photo = None

        header_frame = tk.Frame(self.root, bg="#343a40", pady=10)
        header_frame.pack(fill="x")

        header_content = tk.Frame(header_frame, bg="#343a40")
        header_content.pack()

        title_label = tk.Label(header_content, text="The Happy Basket", fg="white", bg="#343a40", font=("Arial", 18, "bold"))
        title_label.pack()

        if self.logo_photo:
            logo_label = tk.Label(header_content, image=self.logo_photo, bg="#343a40")
            logo_label.pack(side="top", padx=10)

    # Load and place a welcome image
        try:
           welcome_img = Image.open("C:/Users/PC/Downloads/ChatGPT Image Mar 31, 2025, 12_42_04 PM.png").resize((200, 200))
           self.welcome_img = ImageTk.PhotoImage(welcome_img)  # Store reference
           tk.Label(self.root, image=self.welcome_img).pack(pady=10)
        except:
           tk.Label(self.root, text="[Image Not Found]", font=("Arial", 12, "bold"), fg="red").pack(pady=10)

        ttk.Button(self.root, text="Go to Main Menu", command=self.show_main_menu).pack(pady=20)

        self.add_back_button(self.qr_screen)


    def show_main_menu(self):
        """Displays categories in a tile format with a header."""
        self.clear_screen()

    # Header
        try:
            logo_image = Image.open("C:/Users/PC/Downloads/image-removebg-preview.png")  
            logo_image = logo_image.resize((50, 50))
            self.logo_photo = ImageTk.PhotoImage(logo_image)  # Store reference
        except:
            self.logo_photo = None

        header_frame = tk.Frame(self.root, bg="#343a40", pady=10)
        header_frame.pack(fill="x")

        header_content = tk.Frame(header_frame, bg="#343a40")
        header_content.pack()

        title_label = tk.Label(header_content, text="The Happy Basket", fg="white", bg="#343a40", font=("Arial", 18, "bold"))
        title_label.pack()

        if self.logo_photo:
            logo_label = tk.Label(header_content, image=self.logo_photo, bg="#343a40")
            logo_label.pack(side="top", padx=10)
    
    # Main Menu
        tk.Label(self.root, text="Select a Category", font=("Arial", 14, "bold")).pack(pady=10)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        row, col = 0, 0
        for category in grocery_items.keys():
         btn = tk.Button(frame, text=category, font=("Arial", 12), width=15, height=2,
                        command=lambda c=category: self.show_items(c), bg="#ffcc00")
         btn.grid(row=row, column=col, padx=10, pady=10)

         col += 1
         if col > 1:  # Adjust for 2 columns per row
            col = 0
            row += 1

# Cart Button
        tk.Button(self.root, text="🛒 View Cart", font=("Arial", 12, "bold"), command=self.show_cart,
          bg="#17a2b8", fg="white").pack(pady=10)

        self.add_back_button(self.welcome_screen)  # Ensuring it's added only once

    
    def show_items(self, category):
     self.current_category = category
     self.clear_screen()

     tk.Label(self.root, text=f"{category} Items", font=("Arial", 16, "bold"), fg="#333").pack(pady=10)

     items_frame = tk.Frame(self.root)
     items_frame.pack(padx=20, pady=10)

     row, col = 0, 0

     for item, details in grocery_items[category].items():
         price = details["price"]
         quantity = details["quantity"]

         item_card = tk.Frame(items_frame, bd=2, relief="groove", padx=10, pady=10, bg="#f8f9fa")
         item_card.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")

        # Load image if available
         try:
            image_path = f"C:/Users/PC/OneDrive/Documents/college work/2nd sem/python/miniproject/{item}.jpg"
            img = Image.open(image_path).resize((100, 100), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            item_card.image = photo  # Store reference to prevent GC
            tk.Label(item_card, image=photo, bg="#f8f9fa").pack(pady=5)
         except Exception as e:
            print(f"Image for {item} not found: {e}")
            tk.Label(item_card, text="No Image", width=15, height=5, bg="#f8f9fa", fg="gray").pack(pady=5)

         tk.Label(item_card, text=item, font=("Arial", 12, "bold"), bg="#f8f9fa", fg="#333").pack()
         tk.Label(item_card, text=f"₹{price} | Stock: {quantity}", font=("Arial", 10), fg="#d9534f", bg="#f8f9fa").pack()

         tk.Button(item_card, text="Add to Cart", font=("Arial", 10, "bold"),
                  command=lambda i=item, p=price: self.select_quantity(i, p),
                  bg="#28a745", fg="white", width=15).pack(pady=5)

        # Move to next column or row
         col += 1
         if col > 1:
            col = 0
            row += 1



  
    
    def select_quantity(self, item, price):
        """Asks user to select quantity"""
        self.clear_screen()
        tk.Label(self.root, text=f"Enter quantity for {item}:", font=("Arial", 12, "bold")).pack(pady=10)
        self.qty_entry = tk.Entry(self.root)
        self.qty_entry.pack(pady=5)
        tk.Button(self.root, text="Add to Cart", font=("Arial", 12), command=lambda: self.add_to_cart(item, price), bg="#28a745", fg="white").pack(pady=10)
        
        self.add_back_button(lambda: self.show_items)
    
    def add_to_cart(self, item, price):
       """Adds item to cart if stock is available and reserves stock"""
       try:
          qty = int(self.qty_entry.get())
          if qty <= 0:
            raise ValueError

          category = next(cat for cat in grocery_items if item in grocery_items[cat])
          stock = grocery_items[category][item]["quantity"]

          if qty > stock:
            messagebox.showerror("Error", f"Only {stock} left in stock for {item}!")
            return

          # Reserve stock while in cart
          grocery_items[category][item]["quantity"] -= qty

          if item in self.cart:
            self.cart[item] += qty
          else:
            self.cart[item] = qty

          messagebox.showinfo("Success", f"{item} added to cart!")
          self.show_main_menu()

       except ValueError:
        messagebox.showerror("Error", "Please enter a valid quantity!")

    def show_cart(self):
       """Displays cart items."""
       self.clear_screen()
       tk.Label(self.root, text="🛒 Cart Items:", font=("Arial", 14, "bold"), fg="#333").pack(pady=10)

       subtotal = sum(
        qty * grocery_items[next(cat for cat in grocery_items if item in grocery_items[cat])][item]["price"]
        for item, qty in self.cart.items()
       )
       gst = subtotal * 0.18  # 18% GST
       total = subtotal + gst

       for item, qty in self.cart.items():
         price = grocery_items[next(cat for cat in grocery_items if item in grocery_items[cat])][item]["price"]
         tk.Label(self.root, text=f"{item} x {qty} = ₹{qty * price}", font=("Arial", 12)).pack()

       tk.Label(self.root, text=f"Subtotal: ₹{subtotal}", font=("Arial", 12)).pack()
       tk.Label(self.root, text=f"GST (18%): ₹{gst:.2f}", font=("Arial", 12)).pack()
       tk.Label(self.root, text=f"Total: ₹{total:.2f}", font=("Arial", 14, "bold"), fg="#d9534f").pack(pady=10)

    # User details input
       ttk.Label(root, text="Enter Your Name:", font=("Arial", 12)).pack(pady=(10, 2))
       self.customer_name_var = tk.StringVar()
       name_entry = ttk.Entry(root, textvariable=self.customer_name_var, font=("Arial", 12))
       name_entry.pack(pady=(0, 10))

       ttk.Label(root, text="Enter Your Phone Number:", font=("Arial", 12)).pack(pady=(10, 2))
       self.phone_number_var = tk.StringVar()
       phone_entry = ttk.Entry(root, textvariable=self.phone_number_var, font=("Arial", 12))
       phone_entry.pack(pady=(0, 10))
       
              
       tk.Button(self.root, text="Confirm Details", font=("Arial", 12, "bold"),
              command=lambda: self.send_otp(total)).pack(pady=10)

       self.add_back_button(self.show_main_menu)

  
    def send_otp(self, grand_total):
        """Sends a random OTP for verification before payment."""
        self.otp = str(random.randint(1000, 9999))
        messagebox.showinfo("OTP Sent", f"Your OTP is {self.otp}")

        self.clear_screen()
        tk.Label(self.root, text="Enter OTP:", font=("Arial", 12, "bold")).pack(pady=10)
        self.otp_entry = tk.Entry(self.root)
        self.otp_entry.pack(pady=5)
        tk.Button(self.root, text="Verify OTP", font=("Arial", 12, "bold"), command=lambda: self.verify_otp(grand_total)).pack(pady=10)

    def verify_otp(self, grand_total):
        """Verifies OTP before proceeding to payment."""
        if self.otp_entry.get() == self.otp:
           messagebox.showinfo("Success", "OTP Verified Successfully!")
           self.ask_payment_method(grand_total)  # Now asks for UPI or Card
        else:
           messagebox.showerror("Error", "Incorrect OTP! Try again.")

    def ask_payment_method(self, grand_total):
       """Asks user to select payment method after OTP verification."""
       self.customer_name = self.customer_name_var.get().strip() or "[Not Provided]"
       self.phone_number = self.phone_number_var.get().strip() or "[Not Provided]"
       self.clear_screen()

       tk.Label(self.root, text="Select Payment Method:", font=("Arial", 14, "bold")).pack(pady=10)

       tk.Button(self.root, text="💳 Pay via Card", font=("Arial", 12, "bold"),
              command=lambda: self.payment_screen(grand_total, "Card"), bg="#007bff", fg="white").pack(pady=10)

       tk.Button(self.root, text="📲 Pay via UPI", font=("Arial", 12, "bold"),
              command=lambda: self.payment_screen(grand_total, "UPI"), bg="#28a745", fg="white").pack(pady=10)

       self.add_back_button(self.show_cart)

    def payment_screen(self, grand_total, payment_method):
       """Finalizes payment and updates stock."""
    
    # Store history of items before clearing cart
       self.history = [(item, qty, grocery_items[next(cat for cat in grocery_items if item in grocery_items[cat])][item]["price"])
                    for item, qty in self.cart.items()]

    # Clear cart
       self.cart.clear()

       self.clear_screen()
       tk.Label(self.root, text=f"Payment of ₹{grand_total:.2f} via {payment_method} Successful! 🎉",
             font=("Arial", 14, "bold"), fg="#28a745").pack(pady=10)

       tk.Button(self.root, text="Bill Summary", font=("Arial", 12, "bold"),
              command=self.show_bill_summary, bg="#28a745", fg="white").pack(pady=10)


       self.cart.clear()
    def show_bill_summary(self):
        """Displays a bill summary after proceeding."""
        self.clear_screen()
        
        try:
            logo_image = Image.open("C:/Users/PC/Downloads/image-removebg-preview.png")  
            logo_image = logo_image.resize((50, 50))
            self.logo_photo = ImageTk.PhotoImage(logo_image)  # Store reference
        except:
            self.logo_photo = None

        header_frame = tk.Frame(self.root, bg="#343a40", pady=10)
        header_frame.pack(fill="x")

        header_content = tk.Frame(header_frame, bg="#343a40")
        header_content.pack()

        title_label = tk.Label(header_content, text="The Happy Basket", fg="white", bg="#343a40", font=("Brush Script MT", 30, "bold"))
        title_label.pack()

        bill_frame = tk.Frame(self.root, padx=20, pady=10)
        bill_frame.pack()

        ttk.Label(bill_frame, text="🧾 Purchase Summary", font=("Arial", 14, "bold")).pack()
        
        # Generate Random Bill Number
        bill_number = random.randint(100000, 999999)

        ttk.Label(bill_frame, text=f"🧾 Bill No: {bill_number}", font=("Arial", 14, "bold"), foreground="blue").pack()

    # Get user details
        name = getattr(self, 'customer_name', '[Not Provided]')
        phone = getattr(self, 'phone_number', '[Not Provided]')
        tk.Label(bill_frame, text=f"Customer Name: {name}", font=("Arial", 12, "bold")).pack()
        tk.Label(bill_frame, text=f"Phone Number: {phone}", font=("Arial", 12, "bold")).pack()
    # If no cart data, show a warning
        if not self.history:
          tk.Label(bill_frame, text="⚠️ No purchases found!", font=("Arial", 12, "bold"), fg="red").pack()
          ttk.Button(bill_frame, text="Back", command=self.welcome_screen).pack(pady=10)
          return

    # Display previous cart (stored before clearing)
        subtotal = 0
        for item, qty, price in self.history:
           tk.Label(bill_frame, text=f"{item} x {qty} = ₹{qty * price}", font=("Arial", 12)).pack()
           subtotal += qty * price

        gst = subtotal * 0.18  # 18% GST
        total = subtotal + gst

        tk.Label(bill_frame, text=f"Subtotal: ₹{subtotal:.2f}", font=("Arial", 12)).pack()
        tk.Label(bill_frame, text=f"GST (18%): ₹{gst:.2f}", font=("Arial", 12)).pack()
        tk.Label(bill_frame, text=f"Total: ₹{total:.2f}", font=("Arial", 14, "bold"), fg="#d9534f").pack(pady=10)

    # Mark as Paid
        tk.Label(bill_frame, text="✅ Paid", font=("Arial", 14, "bold"), fg="green").pack(pady=10)

    # Verify or Not Verified Options
        button_frame = tk.Frame(bill_frame)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="✅ Verify", command=self.feedback_section).pack(side="left", padx=10)
        ttk.Button(button_frame, text="❌ Not Verified", command=self.not_verified_order).pack(side="right", padx=10)

        ttk.Button(bill_frame, text="Go to Main Menu", command=self.show_main_menu).pack(pady=10)
        self.add_back_button(self.welcome_screen)
        
        ttk.Button(bill_frame, text="🖨️ Print Bill", command=self.greeting_text).pack(pady=10)
        self.add_back_button(self.feedback_section)

        
    def feedback_section(self):
        """Creates a customer feedback section with star rating."""
        feedback_frame = tk.Frame(self.root)
        feedback_frame.pack(pady=10)

        tk.Label(feedback_frame, text="Rate Your Experience:", font=("Arial", 12, "bold")).pack()

        self.stars = []
        for i in range(5):
            star = tk.Label(feedback_frame, text="☆", font=("Arial", 20), fg="black")
            star.bind("<Button-1>", lambda e, idx=i: self.set_rating(idx + 1))
            star.pack(side="left", padx=5)
            self.stars.append(star)

    def set_rating(self, rating):
        """Updates star colors based on rating."""
        self.rating = rating
        for i in range(5):
            if i < rating:
                self.stars[i].config(text="★", fg="gold")
            else:
                self.stars[i].config(text="☆", fg="black")
        self.get_review()

      # Add this import at the beginning

    def get_review(self):
     """Navigates to a new page to collect customer feedback."""
     self.clear_screen()

     tk.Label(self.root, text="Customer Feedback", font=("Arial", 16, "bold")).pack(pady=10)
     tk.Label(self.root, text="Please write your review:", font=("Arial", 12)).pack(pady=5)
     review_entry = tk.Text(self.root, width=50, height=5, wrap="word", font=("Arial", 12))
     review_entry.pack(pady=10, padx=20)


     def submit_review():
        review = review_entry.get("1.0", "end-1c").strip()
        if review:
            tk.Label(self.root, text="Thank you for your feedback!", fg="green", font=("Arial", 12)).pack(pady=5)
        else:
            tk.Label(self.root, text="Please enter a review.", fg="red", font=("Arial", 12)).pack(pady=5)

     tk.Button(self.root, text="Submit", command=submit_review, bg="#28a745", fg="white").pack(pady=10)

    # Back button to return to the main menu
     self.add_back_button(self.welcome_screen)


    def add_back_button(self, previous_page):
        """Adds a back button."""
        tk.Button(self.root, text="⬅️", font=("Arial", 12), command=previous_page).pack(pady=5)

# Run the application
root = tk.Tk()
app = GroceryApp(root)
root.mainloop()
