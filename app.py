"""
Entry point for Render deployment
This file simply imports and runs the bot
"""
from bot import app

if __name__ == "__main__":
    print("🤖 Starting Telegram Reaction Bot on Render...")
    app.run()
