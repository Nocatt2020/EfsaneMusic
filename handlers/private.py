from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://telegra.ph/file/764705778ddb95fc06a99.jpg",
                caption=(f"""**Salam {message.from_user.mention} 🎵\nMən {bot}!\nSəsli sohbətlərdə mahnı oxuya bilən botam. Ban yetkisiz, Səsli söhbətləri idarə yetkisi verip, Asistanı gruba atın zəhmət olmasa.\n\nDüzen Tasarım [Trend Müzik 🎙️](https://t.me/Alay57Chat).**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Grubuna Ekle ❱ ➕", url=f"https://t.me/MusicoLCroBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/TrendMusicAsistan"
                    ),
                    InlineKeyboardButton(
                        "💬 Sohbət", url="https://t.me/Alay57Chat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Resmi Kanal 🇦🇿", url=f"https://t.me/Alay57Resmi"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Not:\n Botun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔴 Userler üçün əmrlər", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "⚫ Adminler üçün əmrlər", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Ana menü🏠", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "⚙ Qurucu", url="https://t.me/s1yahımsın")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Not:\nBotun aktif çalışması için şu üç yetkiye ihtiyaç vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "✨Herkes üçün əmrlər", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👑Admin əmrləri",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🏠Ana Menü", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "⚙ Qurucu", url="https://t.me/s1yahımsın")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun herkes için komut menüsü 😉\n\n ▶️ /oynat - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /oynat <song name> - istediğiniz şarkıyı çal\n 🔴 \n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Qurucu", url="https://t.me/s1yahımsın")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBu botun adminler için komut menüsü 🤩\n\n ▶️ /devam - şarkı çalmaya devam et\n ⏸️ /durdur - çalan parçayı duraklatmak için\n 🔄 /atla- Sıraya alınmış müzik parçasını atlatır.\n ⏹ /son - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n\n ⚪ /asistan - Müzik asistanı grubunuza katılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Qurucu", url="https://t.me/s1yahımsın")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Merhaba {query.from_user.mention} 🎵\nBen {bot}!\nSesli sohbetlerde müzik çalabilen botum. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.\n\nDüzen Tasarım [Trend Müzik 🎙️](https://t.me/Alay57Chat).**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Grubuna Ekle ❱ ➕", url=f"https://t.me/MusicoLCroBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/TrendMusicAsistan"
                    ),
                    InlineKeyboardButton(
                        "💬 Sohbət", url="https://t.me/Alay57Chat"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌀 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Resmi Kanal 🇦🇿", url=f"https://t.me/Alay57Resmi"
                    )
                ]
                
           ]
        ),
    )
