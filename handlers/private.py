from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} π΅

I can play music in your group's voice call. Developed by [ππ»πΆπΈπ²π](https://t.me/anikethacker).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π  κ±α΄α΄Κα΄α΄ α΄α΄α΄α΄ π ", url="https://t.me/anikethacker")
                  ],[
                    InlineKeyboardButton(
                        "π¬ Ι’Κα΄α΄α΄", url="https://t.me/anekhackschat"
                    ),
                    InlineKeyboardButton(
                        "π α΄α΄‘Ι΄α΄Κ", url="https://t.me/anikethacker"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "β α΄α΄α΄ α΄α΄ Κα΄α΄Κ Ι’Κα΄α΄α΄ β", url="https://t.me/Aniketvc_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Ι’Κα΄α΄α΄ α΄α΄κ±Ιͺα΄ α΄Κα΄Κα΄Κ α΄Ι΄ΚΙͺΙ΄α΄ β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π α΄α΄‘Ι΄α΄Κ", url="https://t.me/anikethacker")
                ]
            ]
        )
   )





