import customtkinter as ctk
import matplotlib
from customtkinter import filedialog
import matplotlib.pyplot as plt
from colorthief import ColorThief

matplotlib.use('TkAgg')
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# Function to select the image for color extraction
def select_image():
    try:
        global selected_image
        selected_image = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        ct = ColorThief(selected_image)
        dominant_color = ct.get_color(quality=1)
        status_label.configure(text="RGB: " + str(dominant_color))
        plt.imshow([[dominant_color]])
        plt.show()
    except Exception as e:
        print(f"Error: {str(e)}")


# Global variable to store the selected image path
selected_image = None

# Create the main customtkinter window
root = ctk.CTk()
root.title("Dominant Color Extractor")
root.geometry("375x130")
root.resizable(False, False)

frame = ctk.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

select_button = ctk.CTkButton(master=frame, text="Select Image", command=select_image)
select_button.pack(pady=20, padx=10)

status_label = ctk.CTkLabel(master=frame, text="Please select an image.")
status_label.pack(pady=5, padx=10)


root.mainloop()
