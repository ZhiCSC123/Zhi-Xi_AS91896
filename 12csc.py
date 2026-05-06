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
