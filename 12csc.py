import tkinter as tk

# list of questions in the quiz
quiz_data = [
    {
        "q": "What section of a car is this?",
        "image_path": r"IMAGE\transmission.jpg",
        "options": ["Transmission", "Brake Pad", "Engine", "Exhaust"],
        "a": "Transmission"
    },

    {
        "q": "What section of a car is this?",
        "image_path": r"IMAGE\rims.png",
        "options": ["Engine", "Accelerator", "Tyre", "Rim"],
        "a": "Rim"
    },

    {
        "q": "What section of a car is this?",
        "image_path": r"IMAGE\footbrake.png",
        "options": ["Brake", "Foot Brake", "Accelerator", "Hand Brake"],
        "a": "Foot Brake"
    },

    {
        "q": "What section of a car is this?",
        "image_path": r"IMAGE\cooltank.png",
        "options": ["Engine", "Accelerator", "Coolant Tank", "Oil Tank"],
        "a": "Coolant Tank"
    },

    {
        "q": "What section of a car is this?",
        "image_path": r"IMAGE\oil.png",
        "options": ["Engine", "Coolant", "Oil Tank", "Dipstick"],
        "a": "Oil Tank"
    },

    {
        "q": "What is a Dipstick used for?",
        "image_path": r"IMAGE\oildipstick.png",
        "options": ["To check coolant levels", "To check oil levels", "To jump start the car",
                    "To check water tank levels"],
        "a": "To check oil levels"
    },

    {
        "q": "How do you know if you need to replace your coolant?",
        "image_path": r"IMAGE\coolantlvls.png",
        "options": ["Dashboard displays overheating symbol", "When the dashboard displays TCL/TCS",
                    "Temperature on dashboard rises", "When the car stops running"],
        "a": "Temperature on dashboard rises"
    },

    {
        "q": "When should you replace your car battery?",
        "image_path": r"IMAGE\carbat.png",
        "options": ["When the lights start to go dim", "When you have hit the 5 year mark",
                    "When your battery starts whistling high pitched noises",
                    "If your headlights are way too bright at night"],
        "a": "When the lights start to go dim"
    },

    {
        "q": "How do you know if you need to replace your oil",
        "image_path": r"IMAGE\oilpour.png",
        "options": ["If the dipstick turns black", "When your engine starts making knocking sounds",
                    "The sticker on the windshield", "When the oil on the dip stick goes below the marked line"],
        "a": "When the oil on the dip stick goes below the marked line"
    },

    {
        "q": "What is the purpose of a muffler?",
        "image_path": r"IMAGE\muffler.png",
        "options": ["Regulate exhaust flow", "Acts as a filter...", "It is needed to prevent a car from overheating",
                    "Maximize engine power"],
        "a": "Regulate exhaust flow"
    },
]

# colours used in the program
BG = "#0b1622"
CARD = "#1b2a38"
BTN = "#3a4a5a"
ACCENT = "#4da6ff"
GREEN = "#2ecc71"
RED = "#e74c3c"
WHITE = "white"


# app
class QuizApp:

    # sets up the start screen

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

        # ui
        # makes a custom button

    def rounded_button(self, parent, text, command, width=220):
        canvas = tk.Canvas(parent, width=width, height=45, bg=BG, highlightthickness=0)
        canvas.pack(pady=8)

        canvas.create_rectangle(5, 5, width - 5, 40, fill=BTN, outline=BTN)
        canvas.create_text(width // 2, 22, text=text, fill=WHITE, font=("Arial", 12, "bold"))

        canvas.bind("<Button-1>", lambda e: command())

        return canvas

    # the progression bar

    def progress_bar(self, parent):
        self.pb_canvas = tk.Canvas(parent, width=600, height=30, bg=BG, highlightthickness=0)
        self.pb_canvas.pack(pady=20)

        self.pb_canvas.create_rectangle(0, 10, 600, 25, fill="#999", outline="")
        self.progress_fill = self.pb_canvas.create_rectangle(0, 10, 0, 25, fill=GREEN, outline="")

    # makes the progression bar fill up and update as the quiz continues

    def update_progress(self):
        progress = self.q_index / len(quiz_data)
        width = int(300 * progress)
        self.pb_canvas.coords(self.progress_fill, 0, 10, width, 25)

    # clears the screen
    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    # start screen
    def start_screen(self):
        self.clear()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True)

        tk.Label(frame, text="Welcome to the", fg=WHITE, bg=BG, font=("Arial", 28)).pack()
        tk.Label(frame, text="Ultimate Car Quiz", fg=WHITE, bg=BG, font=("Arial", 32, "bold")).pack(pady=10)

        self.entry = tk.Entry(frame, font=("Arial", 14), justify="center", width=25)
        self.entry.pack(ipady=5)

        # placeholder username for entering the user's username
        placeholder = "Enter Your Username:"
        self.entry.insert(0, placeholder)
        self.entry.config(fg="grey")

        self.entry.bind("<FocusIn>", lambda e: self.entry.delete(0, tk.END)
        if self.entry.get() == placeholder else None)

        self.entry.bind("<FocusOut>", lambda e: self.entry.insert(0, placeholder)
        if self.entry.get() == "" else None)

        self.rounded_button(frame, "Start Quiz", self.start_quiz)

    # start quiz

    def start_quiz(self):
        self.username = self.entry.get()

        if not self.username or self.username == "Enter Your Username:":
            return

        self.q_index = 0
        self.score = 0
        self.answers = []

        # main page
        self.quiz_screen()

    def quiz_screen(self):
        self.clear()

        # top: question
        top = tk.Frame(self.root, bg=BG)
        top.pack(fill="x", pady=10)

        self.q_label = tk.Label(
            top,
            text="",
            fg=WHITE,
            bg=BG,
            font=("Arial", 20, "bold"),
            justify="center"
        )
        self.q_label.pack(anchor="center")

        # main layout
        main = tk.Frame(self.root, bg=BG)
        main.pack(expand=True, fill="both", padx=20, pady=20)

        main.grid_columnconfigure(0, weight=1)
        main.grid_columnconfigure(1, weight=1)

        # left side: image and progress bar
        left = tk.Frame(main, bg=CARD)
        left.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        left_inner = tk.Frame(left, bg=CARD)
        left_inner.pack(expand=True, fill="both", padx=10, pady=10)

        # image
        self.image_label = tk.Label(left_inner, bg=CARD)
        self.image_label.pack(expand=True, fill="both", pady=(10, 10))

        # progress bar
        self.pb_canvas = tk.Canvas(left_inner, width=300, height=30, bg=CARD, highlightthickness=0)
        self.pb_canvas.pack(pady=10)

        self.pb_canvas.create_rectangle(0, 10, 300, 25, fill="#999", outline="")
        self.progress_fill = self.pb_canvas.create_rectangle(0, 10, 0, 25, fill=GREEN, outline="")

        # right side: options and submit
        right = tk.Frame(main, bg=BG)
        right.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.selected = tk.StringVar()
        self.option_buttons = []

        options_frame = tk.Frame(right, bg=BG)
        options_frame.pack(expand=True)

        for _ in range(4):
            btn = tk.Radiobutton(
                options_frame,
                text="",
                variable=self.selected,
                indicatoron=0,
                width=30,
                font=("Arial", 12),
                bg=BTN,
                fg=WHITE,
                selectcolor=ACCENT,
                pady=10
            )

            btn.selection_clear()

            btn.pack(fill="x", pady=8)
            self.option_buttons.append(btn)

        # submit button
        self.rounded_button(right, "Submit", self.next_q)

        self.load_q()

    # loads the questions
    def load_q(self):
        q = quiz_data[self.q_index]

        self.q_label.config(
            text=f"Question {self.q_index + 1} of {len(quiz_data)}\n{q['q']}"
        )

        # load image
        if "image_path" in q:
            try:
                img = tk.PhotoImage(file=q["image_path"])

                # force scale down (adjust numbers as needed)
                # bigger numbers = smaller image
                img = img.subsample(2, 2)

                self.photo = img
                self.image_label.config(image=self.photo)
                self.image_label.image = self.photo

            except Exception as e:
                print("Image error:", e)
                self.image_label.config(image="")
        else:
            self.image_label.config(image="")

        for i, opt in enumerate(q["options"]):
            self.option_buttons[i].config(text=opt, value=opt)

        self.update_progress()

    # switches to the next question
    def next_q(self):
        if not self.selected.get():
            return

        ans = self.selected.get()
        self.answers.append(ans)

        if ans == quiz_data[self.q_index]["a"]:
            self.score += 1

        self.q_index += 1

        if self.q_index < len(quiz_data):
            self.load_q()
        else:
            self.result_screen()

    # the results screen
    def result_screen(self):
        self.clear()

        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True)

        passed = self.score >= 7

        tk.Label(
            frame,
            text="You Passed!" if passed else "You Failed!",
            fg=WHITE,
            bg=BG,
            font=("Arial", 28, "bold")
        ).pack()

        tk.Label(
            frame,
            text=f"{self.username}, Score: {self.score}/10",
            fg=WHITE,
            bg=BG,
            font=("Arial", 18)
        ).pack(pady=20)

        self.rounded_button(frame, "Play Again", self.start_screen)

        self.help_screen()

    def help_screen(self):
        self.clear()

        tk.Label(
            frame,
            text="You Passed!",
            fg=WHITE,
            bg=BG,
            font=("Arial", 28, "bold")
        ).pack()


# runs the app
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
