# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Userbot.Edevat.zenginLog import log_yolla, hata_log
from Userbot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "aciklama"  : "Merhaba dünya..",
        "kullanim"  : [
            None
            ],
        "ornekler"  : [
            ".komut"
            ]
    }
})

from pyrogram import Client, filters
from sys import exc_info

@Client.on_message(filters.command(['komut'], ['!','.','/']) & filters.me)
async def komut(client, message):
    # < Başlangıç
    await log_yolla(client, message)
    ilk_mesaj = await message.edit("__Bekleyin..__",
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown"
    )
    #------------------------------------------------------------- Başlangıç >


    await ilk_mesaj.reply("Merhaba dünyalı")

    try:
        hata_denemesi()
    except Exception as hata:
        await hata_log(hata)
        await ilk_mesaj.edit(f'**Hata Var !**\n\n`{exc_info()[0]}`\n\n__{hata}__')