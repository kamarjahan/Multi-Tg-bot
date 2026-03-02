import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Random images for the bot to use
START_IMAGES = [
    "https://kamarjahan.in/profile.png",
    "https://kamarjahan.in/profile.png",
]

def get_random_image():
    return random.choice(START_IMAGES)

# Bot Texts
TEXTS = {
    "home": "Welcome to the system, **{name}**!\n\nI am an advanced, private multi-purpose bot. Please choose an option below.",
    "help": "❓ **Help Menu**\n\nHere are the instructions on how to use my features. Click the buttons below to navigate.",
    "about": "ℹ️ **About**\n\nVersion: 1.0\nFramework: Pyrogram\nStatus: Highly Advanced & Private.",
    "dev": "👨‍💻 **Developer Info**\n\nDeveloped by a master coder. For inquiries, contact the admin."
}

# Bot Keyboards
KEYBOARDS = {
    "home": InlineKeyboardMarkup([
        [InlineKeyboardButton("❓ Help", callback_data="help")],
        [
            InlineKeyboardButton("ℹ️ About", callback_data="about"),
            InlineKeyboardButton("👨‍💻 Developer", callback_data="dev")
        ]
    ]),
    "help": InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠 Home", callback_data="home")],
        [InlineKeyboardButton("ℹ️ About", callback_data="about")]
    ]),
    "about": InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠 Home", callback_data="home")],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ]),
    "dev": InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠 Home", callback_data="home")]
    ])
}