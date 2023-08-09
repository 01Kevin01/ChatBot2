import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageTk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gelişmiş Çizim Uygulaması")
        
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH, side=tk.BOTTOM)
        
        self.line_color = "black"
        self.line_width = 5
        self.drawing = False
        self.last_x = 0
        self.last_y = 0
        self.auto_size = True
        self.image_path = None
        self.loaded_image = None
        self.zoom_factor = 1.0
        
        self.root.bind("<Button-1>", self.start_drawing)
        self.root.bind("<B1-Motion>", self.draw)
        self.root.bind("<ButtonRelease-1>", self.stop_drawing)
        self.root.bind("<Escape>", self.exit_app)
        self.root.bind("<KeyPress>", self.key_press)
        self.root.bind("<MouseWheel>", self.zoom)
        
        self.create_buttons()

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)
        
        self.create_tool_buttons(button_frame)
        
        load_button = tk.Button(button_frame, text="Yükle", command=self.load_canvas)
        load_button.pack(side=tk.TOP, padx=5, anchor="w")
        
        save_button = tk.Button(button_frame, text="Kaydet", command=self.save_canvas)
        save_button.pack(side=tk.TOP, padx=5, anchor="w")
        
        clear_button = tk.Button(button_frame, text="Temizle", command=self.clear_canvas)
        clear_button.pack(side=tk.TOP, padx=5, anchor="w")

    def create_tool_buttons(self, frame):
        tool_label = tk.Label(frame, text="Araçlar")
        tool_label.pack(pady=10, anchor="w")
        
        tools = ["pen", "line", "rectangle", "oval", "square", "triangle", "circle"]
        for tool in tools:
            button = tk.Button(frame, text=tool.capitalize(), command=lambda t=tool: self.select_tool(t))
            button.pack(side=tk.TOP, padx=5, anchor="w")
            
        color_button = tk.Button(frame, text="Renk Seç", command=self.choose_color)
        color_button.pack(side=tk.TOP, padx=5, anchor="w")

    def zoom(self, event):
        if event.delta > 0:
            self.zoom_in()
        else:
            self.zoom_out()
            
    def zoom_in(self):
        self.zoom_factor *= 1.1
        self.canvas.scale("all", self.last_x, self.last_y, 1.1, 1.1)
        
    def zoom_out(self):
        self.zoom_factor /= 1.1
        self.canvas.scale("all", self.last_x, self.last_y, 1/1.1, 1/1.1)
        
    def select_tool(self, tool):
        self.selected_tool = tool
        
    def start_drawing(self, event):
        self.drawing = True
        self.last_x = event.x
        self.last_y = event.y
        
    def draw(self, event):
        if self.drawing:
            x = event.x
            y = event.y
            if self.selected_tool == "pen":
                self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.line_color, width=self.line_width)
            elif self.selected_tool == "line":
                self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.line_color, width=self.line_width)
            elif self.selected_tool in ["rectangle", "oval", "square", "triangle", "circle"]:
                self.canvas.delete("temp")
                if self.selected_tool == "rectangle":
                    self.draw_rectangle(self.last_x, self.last_y, x, y)
                elif self.selected_tool == "oval":
                    self.draw_oval(self.last_x, self.last_y, x, y)
                elif self.selected_tool == "square":
                    self.draw_square(self.last_x, self.last_y, x, y)
                elif self.selected_tool == "triangle":
                    self.draw_triangle(self.last_x, self.last_y, x, y)
                elif self.selected_tool == "circle":
                    self.draw_circle(self.last_x, self.last_y, x, y)
            self.last_x = x
            self.last_y = y

    def draw_rectangle(self, x1, y1, x2, y2):
        if self.auto_size:
            self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.line_color, width=self.line_width)
        else:
            size = self.line_width * 2
            self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.line_color, width=size)
            
    def draw_oval(self, x1, y1, x2, y2):
        if self.auto_size:
            self.canvas.create_oval(x1, y1, x2, y2, outline=self.line_color, width=self.line_width)
        else:
            size = self.line_width * 2
            self.canvas.create_oval(x1, y1, x2, y2, outline=self.line_color, width=size)
            
    def draw_square(self, x1, y1, x2, y2):
        if self.auto_size:
            size = min(abs(x2 - x1), abs(y2 - y1))
            self.canvas.create_rectangle(x1, y1, x1 + size, y1 + size, outline=self.line_color, width=self.line_width)
        else:
            size = self.line_width * 2
            self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.line_color, width=size)
            
    def draw_triangle(self, x1, y1, x2, y2):
        if self.auto_size:
            x3 = x1 * 2 - x2
            y3 = y2
            self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline=self.line_color, width=self.line_width)
        else:
            size = self.line_width * 2
            self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.line_color, width=size)
            
    def draw_circle(self, x1, y1, x2, y2):
        if self.auto_size:
            radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
            self.canvas.create_oval(x1 - radius, y1 - radius, x1 + radius, y1 + radius, outline=self.line_color, width=self.line_width)
        else:
            size = self.line_width * 2
            self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.line_color, width=size)
            
    def stop_drawing(self, event):
        self.drawing = False
        
    def choose_color(self):
        color = colorchooser.askcolor(title="Renk Seç")
        if color[1]:
            self.line_color = color[1]
            
    def clear_canvas(self):
        self.canvas.delete("all")
        
    def save_canvas(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.canvas.postscript(file=file_path)

    def load_canvas(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
        if file_path:
            self.clear_canvas()
            self.loaded_image = Image.open(file_path)
            self.loaded_image.thumbnail((self.canvas.winfo_width(), self.canvas.winfo_height()))
            self.loaded_image = ImageTk.PhotoImage(self.loaded_image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.loaded_image)
        
    def exit_app(self, event):
        self.root.quit()
        
    def increase_line_width(self):
        self.line_width += 1
        
    def decrease_line_width(self):
        if self.line_width > 1:
            self.line_width -= 1
            
    def key_press(self, event):
        if event.keysym == "equal":
            self.increase_line_width()
        elif event.keysym == "minus":
            self.decrease_line_width()

root = tk.Tk()
app = PaintApp(root)
root.mainloop()
