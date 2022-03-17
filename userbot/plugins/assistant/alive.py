from telethon import events

PM_IMG = "https://telegra.ph/file/7a43d71e592d9477a79a2.jpg"
pm_caption = f"⚜ CBA-USERBOT is Online ⚜ \n\n"
pm_caption += f"Owner ~ 『{legend_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Telethon ~ `1.15.0` \n"
pm_caption += f"┣『CBA-USERBOT』~ `{LEGENDversion}` \n"
pm_caption += f"┣Channel ~ [Channel](https://t.me/CBA_USERBOT)\n"
pm_caption += f"┣**Licenece** ~ [Licence](https://github.com/BHAGWANUSERBOT/CBABOT/blob/master/LICENSE)\n"
pm_caption += f"┣Copyright ~ By [CBA-Bot』 ](https://t.me/CBA_SUPPORT)\n"
pm_caption += f"┣Assistant ~  [『CBA-USERBOT』 ](https://t.me/CBA_USERBOT)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『CBA-USERBOT』](https://t.me/CBA_SUPPORT) «««"

from telethon import events


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
