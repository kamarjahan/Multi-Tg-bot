import os
import asyncio
import yt_dlp
from pyrogram import Client, filters
from pyrogram.types import Message

# Helper function to run yt-dlp synchronously
def extract_and_download(url: str, output_path: str):
    """Downloads the best quality video using yt-dlp."""
    ydl_opts = {
        'outtmpl': output_path, 
        'format': 'best[ext=mp4]/best', 
        'quiet': True,          
        'no_warnings': True,
        'geo_bypass': True,     
        'cookiefile': 'cookies.txt',  # 👈 ADD THIS LINE HERE
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_path

@Client.on_message(filters.command(["dl", "download"]) & filters.private)
async def handle_download(client: Client, message: Message):
    """Handles the /dl [url] command."""
    
    # 1. Check if the user actually provided a link
    if len(message.command) < 2:
        await message.reply_text(
            "❌ **Error:** No link provided.\n\n"
            "**Usage:** `/dl [video link]`\n"
            "*Works for YouTube, TikTok, Instagram, X/Twitter, and more!*"
        )
        return

    url = message.command[1]
    
    # 2. Send a status message so the user knows the bot is working
    status_msg = await message.reply_text("⏳ **Processing link...** Please wait.")

    # 3. Create a unique filename (so if 2 users download at once, files don't mix up)
    # We will use the user's ID and the message ID to make it unique
    os.makedirs("downloads", exist_ok=True) # Ensure the folder exists
    temp_file = f"downloads/vid_{message.from_user.id}_{message.id}.mp4"

    try:
        # 4. Download the video in a background thread so the bot doesn't freeze
        await status_msg.edit_text("⬇️ **Downloading video...** This might take a moment.")
        await asyncio.to_thread(extract_and_download, url, temp_file)
        
        # 5. Upload the video back to Telegram
        await status_msg.edit_text("📤 **Uploading to Telegram...**")
        await message.reply_video(
            video=temp_file,
            caption=f"✅ **Downloaded successfully!**\n🔗 Source: [Link]({url})",
            supports_streaming=True # Allows users to watch without fully downloading
        )
        
        # 6. Clean up: Delete the status message and the temporary file
        await status_msg.delete()
        if os.path.exists(temp_file):
            os.remove(temp_file)
            
    except Exception as e:
        # If the link is invalid, private, or restricted, catch the error
        await status_msg.edit_text(f"❌ **Download Failed.**\n\n`{str(e)[:200]}`")
        
        # Ensure we still delete the temp file if it partially downloaded
        if os.path.exists(temp_file):
            os.remove(temp_file)