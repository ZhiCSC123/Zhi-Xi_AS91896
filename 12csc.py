import tkinter as tk


    # Questions
quiz_data = [
    {"q": "What section of a car is this?", "options": ["Transmission", "Brake Pad", "Engine", "Exhaust"], "a": "Transmission"},
    {"q": "What section of a car is this?", "options": ["Engine", "Accelerator", "Tyre", "Rim"], "a": "Rim"},
    {"q": "What section of a car is this?", "options": ["Brake", "Foot Brake", "Accelerator", "Hand Brake"], "a": "Foot Brake"},
    {"q": "What section of a car is this?", "options": ["Engine", "Accelerator", "Coolant Tank", "Oil Tank"], "a": "Coolant Tank"},
    {"q": "What section of a car is this?", "options": ["Engine", "Coolant", "Oil Tank", "Dipstick"], "a": "Oil Tank"},
    {"q": "What is a Dipstick used for?", "options": ["To check coolant levels", "To check oil levels", "To jump start the car", "To check water tank levels"], "a": "To check oil levels"},
    {"q": "How do you know if you need to replace your coolant?", "options": ["When your dashboard says your car is overheating", "When your car dashboard displays TCL/TCS", "The temperature gauge on your dashboard rises", "When the car suddenly stops running"], "a": "The temperature gauge on your dashboard rises"},
    {"q": "When should you replace your car battery?", "options": ["When the lights start to go dim", "When you have hit the 5 year mark", "When your battery starts whistling high pitched noises", "If your headlights are way too bright at night”"], "a": "When the lights start to go dim"},
    {"q": "Corolla maker?", "options": ["Honda", "Toyota", "Subaru", "Mazda"], "a": "Toyota"},
    {"q": "What is the purpose of a muffler?", "options": ["Regulate exhaust flow", "Acts as a filter for solid parts to prevent solid parts entering the exhaust pipes of the vehicle.", "It is needed to prevent a car from overheating”", "Maximize engine power"], "a": "Regulate exhaust flow"}
]


BG = "#0b1622"
CARD = "#1b2a38"
BTN = "#3a4a5a"
ACCENT = "#4da6ff"
GREEN = "#2ecc71"
RED = "#e74c3c"
WHITE = "white"


    # App
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Quiz")
        self.root.geometry("900x600")
        self.root.config(bg=BG)


        self.q_index = 0
        self.score = 0
        self.answers = []
        self.username = ""


        self.start_screen()

    # UI

    def rounded_button(self, parent, text, command, width=220):
        canvas = tk.Canvas(parent, width=width, height=45, bg=BG, highlightthickness=0)
        canvas.pack(pady=8)

        rect = canvas.create_rectangle(5, 5, width - 5, 40, fill=BTN, outline=BTN, width=2)
        label = canvas.create_text(width // 2, 22, text=text, fill=WHITE, font=("Arial", 12, "bold"))

        def on_click(event):
            command()

        canvas.bind("<Button-1>", on_click)
        return canvas

    def progress_bar(self, parent):
        self.pb_canvas = tk.Canvas(parent, width=600, height=30, bg=BG, highlightthickness=0)
        self.pb_canvas.pack(pady=20)

        self.pb_canvas.create_rectangle(0, 10, 600, 25, fill="#999", outline="")
        self.progress_fill = self.pb_canvas.create_rectangle(0, 10, 0, 25, fill=GREEN, outline="")
        self.progress_dot = self.pb_canvas.create_oval(0, 5, 20, 25, fill="red", outline="")

    def update_progress(self):
        progress = self.q_index / len(quiz_data)
        width = int(600 * progress)

        self.pb_canvas.coords(self.progress_fill, 0, 10, width, 25)
        self.pb_canvas.coords(self.progress_dot, width - 10, 5, width + 10, 25)

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

# UI
    def rounded_button(self, parent, text, command, width=220):
        canvas = tk.Canvas(parent, width=width, height=45, bg=BG, highlightthickness=0)
        canvas.pack(pady=8)


        rect = canvas.create_rectangle(5, 5, width-5, 40, fill=BTN, outline=BTN, width=2)
        label = canvas.create_text(width//2, 22, text=text, fill=WHITE, font=("Arial", 12, "bold"))


        def on_click(event):
            command()


        canvas.bind("<Button-1>", on_click)
        return canvas


    def progress_bar(self, parent):
        self.pb_canvas = tk.Canvas(parent, width=600, height=30, bg=BG, highlightthickness=0)
        self.pb_canvas.pack(pady=20)


        self.pb_canvas.create_rectangle(0, 10, 600, 25, fill="#999", outline="")
        self.progress_fill = self.pb_canvas.create_rectangle(0, 10, 0, 25, fill=GREEN, outline="")


    def update_progress(self):
        progress = self.q_index / len(quiz_data)
        width = int(600 * progress)


        self.pb_canvas.coords(self.progress_fill, 0, 10, width, 25)
        self.pb_canvas.coords(self.progress_dot, width-10, 5, width+10, 25)


    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()


# start screen
    def start_screen(self):
        self.clear()


        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True)


        tk.Label(frame, text="Welcome to the", fg=WHITE, bg=BG,
                 font=("Arial", 28)).pack()


        tk.Label(frame, text="Ultimate Car Quiz", fg=WHITE, bg=BG,
                 font=("Arial", 32, "bold", "underline")).pack(pady=10)


        tk.Label(frame, text="Enter your username:", fg="#ccc", bg=BG,
                 font=("Arial", 16)).pack(pady=20)

self.entry = tk.Entry(frame, font=("Arial", 14), justify="center", width=25)
        self.entry.pack(ipady=5)


        self.rounded_button(frame, "Start Quiz", self.start_quiz)


    def start_quiz(self):
        self.username = self.entry.get()
        if not self.username:
            return
        self.q_index = 0
        self.score = 0
        self.answers = []
        self.quiz_screen()
