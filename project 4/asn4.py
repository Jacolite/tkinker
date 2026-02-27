import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class FoodGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Food Selector")
        self.root.geometry("500x400")

        # ===== IntVar to store radio choice =====
        self.var = tk.IntVar()
        self.var.set(0)

        # ===== Frames =====
        self.radio_frame = tk.Frame(root)
        self.radio_frame.pack(side="left", padx=20, pady=20)

        self.img_frame = tk.Frame(root)
        self.img_frame.pack(side="right", padx=20, pady=20)

        # ===== Image size (CHANGE THIS if needed) =====
        size = (200, 200)

        # ===== Load + resize images =====
        self.imgChicken = ImageTk.PhotoImage(
            Image.open("chicken.jpg").resize(size, Image.LANCZOS)
        )

        self.imgPie = ImageTk.PhotoImage(
            Image.open("pie.jpg").resize(size, Image.LANCZOS)
        )

        self.imgPizza = ImageTk.PhotoImage(
            Image.open("pizza.jpg").resize(size, Image.LANCZOS)
        )

        self.imgSalad = ImageTk.PhotoImage(
            Image.open("steak.jpg").resize(size, Image.LANCZOS)
        )
        
        # ===== Label to show image =====
        self.lbl = tk.Label(self.img_frame, image="")
        self.lbl.pack()

        # ===== Radio buttons =====
        foods = [
            ("Chicken", 1),
            ("Pie", 2),
            ("Pizza", 3),
            ("Steak", 4)
        ]

        for text, val in foods:
            rb = tk.Radiobutton(
                self.radio_frame,
                text=text,
                variable=self.var,
                value=val,
                command=self.on_radio_select
            )
            rb.pack(anchor="w")

    # ===== Method called when radio selected =====
    def on_radio_select(self):

        choice = self.var.get()

        # Debug message (remove later if not needed)
        # messagebox.showinfo("Choice", f"You selected {choice}")

        if choice == 1:
            self.lbl.config(image=self.imgChicken)

        elif choice == 2:
            self.lbl.config(image=self.imgPie)

        elif choice == 3:
            self.lbl.config(image=self.imgPizza)

        elif choice == 4:
            self.lbl.config(image=self.imgSalad)


# ===== Run app =====
root = tk.Tk()
app = FoodGUI(root)
root.mainloop()
