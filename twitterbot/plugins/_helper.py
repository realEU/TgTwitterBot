# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterBot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client, filters
from twitterbot import AUTH, HELP_MARKUP, TLOGO, HNDLR, REPO
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


START_MSG = """
︂︃︅︇
"""

def limit_check(client, query):
    if len(query.query)==0:
        return True
    return False


@Client.on_inline_query(~filters.user(AUTH))
async def _andshow(client, query):
    res = InlineQueryResultArticle(title="Fuck Off!",
        description="@xDune",
        url=REPO,
        input_message_content=InputTextMessageContent("Leave It Already!"), 
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="@xDuneBot",url=REPO)]]))
    await query.answer([res], switch_pm_text="Fuck Off!😊",
                       switch_pm_parameter="start")


@Client.on_message(filters.command("start", prefixes=HNDLR)
                   & filters.user(AUTH))
async def startmsg(client, message):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="@xDune",
                              url="https://telegram.me/xDune")],
        [InlineKeyboardButton(
            text="@xDuneBot",
            url=REPO)]])
    await message.reply_text(
        START_MSG.format(frm=message.from_user.mention,
                         HLR=HNDLR),
        reply_markup=reply_markup,
        quote=True)


@Client.on_inline_query(filters.user(AUTH) & limit_check)
async def myinline(client, query):
    if query.from_user.id not in AUTH:
        return
    out = [InlineQueryResultArticle(
        title="TwitterBot",
        description="Help Menu",
        thumb_url=TLOGO,
        input_message_content=InputTextMessageContent(
            "Telegram - Twitter - Bot"),
        reply_markup=HELP_MARKUP)]
    await query.answer(out,
                       switch_pm_text="HELP Portal",
                       switch_pm_parameter="start")


HEMENU = f"""
**Available Commands**

`{HNDLR}tweet <reply to a message>`
- Post the Replied Message as Tweet on Twitter.
"""


@Client.on_message(filters.command("help", prefixes=HNDLR)
                   & filters.user(AUTH))
async def shelpmsg(client, message):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="INLINE HELP", callback_data="openmenu")]])
    await message.reply_text(HEMENU,
                             reply_markup=reply_markup,
                             quote=True)
