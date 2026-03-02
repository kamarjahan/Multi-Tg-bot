import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from begin.ui import TEXTS, KEYBOARDS, get_random_image

# --- Auto-Delete Helper ---
async def delete_after(message: Message, delay_seconds: int = 120):
    """Waits for a specified time and then deletes the message."""
    await asyncio.sleep(delay_seconds)
    try:
        await message.delete()
    except Exception as e:
        print(f"Could not delete message: {e}")

# --- Command Handlers ---
@Client.on_message(filters.command(["start", "help", "about", "dev"]) & filters.private)
async def handle_all_commands(client: Client, message: Message):
    """Handles /start, /help, /about, and /dev commands dynamically."""
    
    # Determine which command was used (remove the "/")
    command = message.command[0].lower()
    
    # Map the command to our UI keys (start -> home, dev -> dev, etc.)
    ui_key = "home" if command == "start" else command
    
    # Format the text (injecting the user's name if it's the home screen)
    text = TEXTS[ui_key].format(name=message.from_user.first_name)
    keyboard = KEYBOARDS[ui_key]
    
    # Send the photo with the corresponding caption and keyboard
    sent_msg = await message.reply_photo(
        photo=get_random_image(),
        caption=text,
        reply_markup=keyboard
    )
    
    # Schedule the auto-deletion for the bot's message (120 seconds = 2 minutes)
    asyncio.create_task(delete_after(sent_msg, 120))
    
    # Optionally, delete the user's command message immediately to keep chat clean
    await message.delete()