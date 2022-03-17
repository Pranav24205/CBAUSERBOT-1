import re

from telethon import Button
from telethon.errors import MessageNotModifiedError
from telethon.events import CallbackQuery

from userbot import legend

from ..Config import Config
from ..core.logger import logging
from ..sql_helper.globals import addgvar, delgvar

LOGS = logging.getLogger(__name__)


@legend.tgbot.on(CallbackQuery(data=re.compile(r"^age_verification_true")))
async def age_verification_true(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "Given That It's A Stupid-Ass Decision, I've Elected To Ignore It.",
            alert=True,
        )
    await event.answer("Yes I'm 18+", alert=False)
    buttons = [
        Button.inline(
            text="Unsure / Change of Decision ❔",
            data="chg_of_decision_",
        )
    ]
    try:
        addgvar("ALLOW_NSFW", "true")
        await event.edit(
            text="Done Now Use Again",
            file="https://telegra.ph/file/84925585f2df7cf00d512.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass


@legend.tgbot.on(CallbackQuery(data=re.compile(r"^age_verification_false")))
async def age_verification_false(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "Given That It's A Stupid-Ass Decision, I've Elected To Ignore It.",
            alert=True,
        )
    await event.answer("No I'm Not", alert=False)
    buttons = [
        Button.inline(
            text="Unsure / Change of Decision ❔",
            data="chg_of_decision_",
        )
    ]
    try:
        delgvar("ALLOW_NSFW")
        await event.edit(
            text="BETE CHALE JA !",
            file="https://telegra.ph/file/6c38ad2468c1e5485adb0.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass


@legend.tgbot.on(CallbackQuery(data=re.compile(r"^chg_of_decision_")))
async def chg_of_decision_(event: CallbackQuery):
    u_id = event.query.user_id
    if u_id != Config.OWNER_ID and u_id not in Config.SUDO_USERS:
        return await event.answer(
            "Given That It's A Stupid-Ass Decision, I've Elected To Ignore It.",
            alert=True,
        )
    await event.answer("Unsure", alert=False)
    buttons = [
        (
            Button.inline(text="Yes I'm 18+", data="age_verification_true"),
            Button.inline(text="No I'm Not", data="age_verification_false"),
        )
    ]
    try:
        await event.edit(
            text="**ARE YOU OLD ENOUGH FOR THIS ?**",
            file="https://telegra.ph/file/6c38ad2468c1e5485adb0.jpg",
            buttons=buttons,
        )
    except MessageNotModifiedError:
        pass
