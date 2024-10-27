import cv2
import tkinter as tk
from tkinter import filedialog, simpledialog

def zoom_image(image_path, zoom_factor):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)

    zoomed_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    return zoomed_image

def zoom_callback():
    root.withdraw()
    img_path = filedialog.askopenfilename(title="Aks ro entekhabkonid", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if not img_path:
        return
    
    zoom_factor = simpledialog.askfloat("Input", "mizan zoom ro vared konid (1 = 100% va 2 = 200% va ...)")
    
    zoomed_img = zoom_image(img_path, zoom_factor)
    cv2.imwrite("zoomedimage.png", zoomed_img)
    print("aks zoom shode save shod ba esm zoomedimage.png")

    cv2.imshow("Zoomed Image", zoomed_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

root = tk.Tk()
root.title("ImageZoomer")

btn_zoom = tk.Button(root, text="Zoom Image", command=zoom_callback)
btn_zoom.pack(pady=20)
root.mainloop()
