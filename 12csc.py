import customtkinter as ctk
from PIL import Image   
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

    # COLOURS

BG = "#0b1622"
CARD = "#0f1c2b"
BTN = "#2a3f55"
BTN_HOVER = "#3b5670"
SELECT = "#1f6aa5"
TEXT_MAIN = "#e6edf3"
TEXT_SUB = "#9fb3c8"
GREEN = "#2ecc71"
RED = "#e74c3c"

questions = [{
    "question": "What part of a car is this?",
    "image": "transmission.jpg",
    "options": ["Brake Pad", "Transmission", "Engine", "Exhaust"]
}]
