from pyrogram import Client
from pyrogram.types import CallbackQuery
from begin.ui import TEXTS, KEYBOARDS

@Client.on_callback_query()
async def handle_button_clicks(client: Client, query: CallbackQuery):
    """Handles all inline button clicks and edits the message caption."""
    
    # The callback_data string we set in ui.py (e.g., "help", "home")
    data = query.data 
    
    # Check if the data exists in our UI dictionary
    if data in TEXTS and data in KEYBOARDS:
        
        # Format the text (just in case they go back to home, we need their name)
        text = TEXTS[data].format(name=query.from_user.first_name)
        keyboard = KEYBOARDS[data]
        
        # Edit the caption and the buttons of the current message
        await query.edit_message_caption(
            caption=text,
            reply_markup=keyboard
        )
        
        # Answer the callback query so the loading icon on the button stops spinning
        await query.answer()
    else:
        # Fallback if the button data is unknown
        await query.answer("Unknown action!", show_alert=True)