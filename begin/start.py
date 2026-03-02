import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# High-quality fallback images
START_IMAGES = [
    "https://kamarjahan.in/profile.png",
    "https://kamarjahan.in/profile.png"
]

@Client.on_message(filters.command("start") & filters.private)
async def fresh_start(client: Client, message: Message):
    # 🚨 This print statement will prove the bot heard you!
    print(f"\n✅ SUCCESS! Received /start from {message.from_user.first_name}\n")
    
    # Create the buttons
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("❓ Help", callback_data="help")],
        [
            InlineKeyboardButton("ℹ️ About", callback_data="about"),
            InlineKeyboardButton("👨‍💻 Developer", callback_data="dev")
        ]
    ])
    
    # Send the random photo with caption and buttons
    await message.reply_photo(
        photo=random.choice(START_IMAGES),
        caption=(
            f"Hello **{message.from_user.first_name}**!\n\n"
            f"Welcome to the Advanced Multi-Bot system. "
            f"Please choose an option below to begin."
        ),
        reply_markup=keyboard
    )