import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from src.events import register
from src import telethn as tbot

VENOM = "https://telegra.ph/file/3d67ebcbd3a6373946a82.mp4"

@register(pattern=("/start"))
async def awake(event):
  TEXT = f"Heya [{event.sender.first_name}](tg://user?id={event.sender.id}), My name is Emilia - I'm an Animed themed Group Management Bot, Here to help you manage your groups! Use /help to know about my Full Potential.\n\n"
  TEXT += "Join my [Updates Channel](t.me/PikachuUpdates) to get information on all the latest updates."
  BUTTON = [[Button.url("➕Add Me To Your Group➕", "https://t.me/EmiliaProBot?startgroup=true"),]]
  await tbot.send_file(event.chat_id, VENOM, caption=TEXT, buttons=BUTTON)
