from pyrogram import Client, filters
from pyrogram.types import Message
import os
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize the bot
app = Client(
    "reaction_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Available reactions
REACTIONS = {
    "👍": "👍",
    "❤": "❤",
    "🔥": "🔥",
    "👏": "👏",
    "😁": "😁",
    "🤔": "🤔",
    "🤯": "🤯",
    "😱": "😱",
    "🤬": "🤬",
    "😢": "😢",
    "🎉": "🎉",
    "🤩": "🤩",
    "🤮": "🤮",
    "💩": "💩",
    "🙏": "🙏",
    "👌": "👌",
    "🕊": "🕊",
    "🤡": "🤡",
    "🥱": "🥱",
    "🥴": "🥴",
    "😍": "😍",
    "🐳": "🐳",
    "❤‍🔥": "❤‍🔥",
    "🌚": "🌚",
    "🌭": "🌭",
    "💯": "💯",
    "🤣": "🤣",
    "⚡": "⚡",
    "🍌": "🍌",
    "🏆": "🏆",
    "💔": "💔",
    "🤨": "🤨",
    "😐": "😐",
    "🍓": "🍓",
    "🍾": "🍾",
    "💋": "💋",
    "🖕": "🖕",
    "😈": "😈",
    "😴": "😴",
    "😭": "😭",
    "🤓": "🤓",
    "👻": "👻",
    "👨‍💻": "👨‍💻",
    "👀": "👀",
    "🎃": "🎃",
    "🙈": "🙈",
    "😇": "😇",
    "😨": "😨",
    "🤝": "🤝",
    "✍": "✍",
    "🤗": "🤗",
    "🫡": "🫡",
    "🎅": "🎅",
    "🎄": "🎄",
    "☃": "☃",
    "💅": "💅",
    "🤪": "🤪",
    "🗿": "🗿",
    "🆒": "🆒",
    "💘": "💘",
    "🙉": "🙉",
    "🦄": "🦄",
    "😘": "😘",
    "💊": "💊",
    "🙊": "🙊",
    "😎": "😎",
    "👾": "👾",
    "🤷‍♂": "🤷‍♂",
    "🤷": "🤷",
    "🤷‍♀": "🤷‍♀",
    "😡": "😡",
}


@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    """Handle /start command"""
    # React to the command message with random emoji
    random_emoji = random.choice(list(REACTIONS.keys()))
    await message.react(emoji=random_emoji)
    
    await message.reply_text(
        "👋 **Welcome to Reaction Bot!**\n\n"
        "I can react to your messages with emojis!\n\n"
        "**Available Commands:**\n"
        "/react [emoji] - React to the replied message\n"
        "/reactions - See all available reactions\n"
        "/stats - Show bot statistics\n"
        "/help - Show this help message\n"
        "/ping - Check bot status\n\n"
        "**Usage:**\n"
        "Reply to any message with `/react ❤` to add a heart reaction!"
    )


@app.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    """Handle /help command"""
    # React to the command message with random emoji
    random_emoji = random.choice(list(REACTIONS.keys()))
    await message.react(emoji=random_emoji)
    
    await message.reply_text(
        "**How to use Reaction Bot:**\n\n"
        "1. Reply to any message\n"
        "2. Use `/react [emoji]` command\n"
        "3. I'll add that reaction to the message!\n\n"
        "**Examples:**\n"
        "`/react 👍` - Add thumbs up\n"
        "`/react ❤` - Add heart\n"
        "`/react 🔥` - Add fire\n\n"
        "Use /reactions to see all available reactions!"
    )


@app.on_message(filters.command("reactions"))
async def reactions_command(client: Client, message: Message):
    """Show all available reactions"""
    # React to the command message with random emoji
    random_emoji = random.choice(list(REACTIONS.keys()))
    await message.react(emoji=random_emoji)
    
    reaction_list = " ".join(REACTIONS.keys())
    await message.reply_text(
        "**Available Reactions:**\n\n"
        f"{reaction_list}\n\n"
        "Reply to a message with `/react [emoji]` to use any of these!"
    )


@app.on_message(filters.command("react"))
async def react_command(client: Client, message: Message):
    """Handle /react command"""
    
    # React to the command message with random emoji
    random_emoji = random.choice(list(REACTIONS.keys()))
    await message.react(emoji=random_emoji)
    
    # Check if the message is a reply
    if not message.reply_to_message:
        await message.reply_text(
            "❌ Please reply to a message to add a reaction!\n\n"
            "Example: Reply to a message and type `/react ❤`"
        )
        return
    
    # Get the emoji from command
    command_parts = message.text.split(maxsplit=1)
    
    if len(command_parts) < 2:
        await message.reply_text(
            "❌ Please specify an emoji!\n\n"
            "Example: `/react ❤`\n"
            "Use /reactions to see all available reactions"
        )
        return
    
    emoji = command_parts[1].strip()
    
    # Check if emoji is available
    if emoji not in REACTIONS:
        await message.reply_text(
            f"❌ Reaction '{emoji}' is not available!\n\n"
            "Use /reactions to see all available reactions"
        )
        return
    
    try:
        # Send reaction to the replied message
        await message.reply_to_message.react(emoji=emoji)
        
        # Confirm the reaction was sent
        await message.reply_text(f"✅ Reacted with {emoji}!")
        
    except Exception as e:
        await message.reply_text(
            f"❌ Failed to send reaction: {str(e)}\n\n"
            "Make sure the message can receive reactions!"
        )


@app.on_message(filters.command("stats"))
async def stats_command(client: Client, message: Message):
    """Show bot statistics"""
    # React to the command message with random emoji
    random_emoji = random.choice(list(REACTIONS.keys()))
    await message.react(emoji=random_emoji)
    
    # Get basic bot info
    me = await client.get_me()
    
    stats_text = (
        "📊 **Bot Statistics**\n\n"
        f"🤖 Bot: @{me.username}\n"
        f"👤 Name: {me.first_name}\n"
        f"🆔 Bot ID: `{me.id}`\n"
        f"✨ Available Reactions: {len(REACTIONS)}\n"
        f"⚡ Status: Online\n\n"
        "Use /reactions to see all available emojis!"
    )
    
    await message.reply_text(stats_text)


@app.on_message(filters.command("ping"))
async def ping_command(client: Client, message: Message):
    """Check if bot is alive"""
    # React to the command message with random emoji
    random_emoji = random.choice(list(REACTIONS.keys()))
    await message.react(emoji=random_emoji)
    
    await message.reply_text("🏓 Pong! Bot is running!")


# Run the bot
if __name__ == "__main__":
    print("🤖 Starting Reaction Bot...")
    app.run()
