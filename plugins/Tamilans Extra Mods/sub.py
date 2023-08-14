from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest
from info import CHANNEL_ONE, CHANNEL_TWO
from database.users_chats_db import db

@Client.on_chat_join_request(
    filters.chat(CHANNEL_ONE) | filters.chat(CHANNEL_TWO)
)
async def join_reqs(self: Client, join_req: ChatJoinRequest):
    user_id = join_req.from_user.id
    if join_req.chat.id == CHANNEL_ONE:
        try:
            await db.add_req_one(user_id)
        except Exception as e:
            print(f"Error adding join request to req_one: {e}")
    elif join_req.chat.id == CHANNEL_TWO:
        try:
            await db.add_req_two(user_id)
        except Exception as e:
            print(f"Error adding join request to req_two: {e}")
