
#GenAI: Gemini for GUI implementation

import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
from filters import apply_filter

class ImageFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Image Filter App")
        self.root.geometry("900x600")

        self.image_path = None
        self.original_image = None
        self.filtered_image = None

        # --- Control Panel Frame ---
        control_frame = tk.Frame(root, pady=10)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        self.upload_btn = tk.Button(control_frame, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(side=tk.LEFT, padx=10)

        self.filter_var = tk.StringVar(value="Averaging")
        self.filter_dropdown = ttk.Combobox(control_frame, textvariable=self.filter_var, 
                                            values=["Averaging", "Sharpening", "Gaussian", "Laplacian"], state="readonly")
        
        self.filter_dropdown.pack(side=tk.LEFT, padx=10)

        self.filter_btn = tk.Button(control_frame, text="Filter", command=self.process_image)
        self.filter_btn.pack(side=tk.LEFT, padx=10)

        # --- Display Panel Frame ---
        display_frame = tk.Frame(root)
        display_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Original Image Window
        self.orig_label_frame = tk.LabelFrame(display_frame, text="Original Image")
        self.orig_label_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        self.orig_canvas = tk.Label(self.orig_label_frame)
        self.orig_canvas.pack(fill=tk.BOTH, expand=True)

        # Filtered Image Window
        self.filt_label_frame = tk.LabelFrame(display_frame, text="Filtered Image")
        self.filt_label_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        self.filt_canvas = tk.Label(self.filt_label_frame)
        self.filt_canvas.pack(fill=tk.BOTH, expand=True)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            self.image_path = file_path
            # Load image using Pillow and ensure it's in RGB mode
            self.original_image = Image.open(file_path).convert("RGB")
            self.display_image(self.original_image, self.orig_canvas)

    def process_image(self):
        if self.original_image is None:
            return
        selected_filter = self.filter_var.get()
        # Pass the PIL Image to your custom filter function
        self.filtered_image = apply_filter(self.original_image, selected_filter)
        self.display_image(self.filtered_image, self.filt_canvas)

    def display_image(self, img, canvas):
        # Resize for display fit while maintaining aspect ratio
        img_copy = img.copy()
        img_copy.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img_copy)
        
        canvas.config(image=img_tk)
        canvas.image = img_tk  # Prevent garbage collection

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageFilterApp(root)
    root.mainloop()