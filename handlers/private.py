from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Tarik Sist Semongko, Yuhuuu Guys saya {bn} 🎵

Aku bisa memutar musik di panggilan suara grup kamu. Dikembangkan oleh [Gungg](https://t.me/aestheticboyy2).

Tambahkan aku ke grup kamu dan mainkan musik dengan bebas!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/Razer-Cynosa/NadaMusicBot")
                  ],[
                    InlineKeyboardButton(
                        "👤 Pemilik", url="https://t.me/aestheticboyy2"
                    ),
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/viraltwittergrup"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Tambahkan Ke Grup Anda ➕", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Tarik Sist Semongkoo 🍻**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Grup", url="https://t.me/viraltwittergrup")
                ]
            ]
        )
   )


