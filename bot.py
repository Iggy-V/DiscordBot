import os
import discord
from dotenv import load_dotenv
from get_random_problem import LeetCodeRandom


def main():
    load_dotenv()

    BOT_TOKEN = os.getenv('BOT_TOKEN')
    CHANNEL_ID = os.getenv('CHANNEL_ID')

    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')
        channel = client.get_channel(int(CHANNEL_ID))
        if channel:
            try:
                random_problem = LeetCodeRandom()
                await channel.send("Here's the daily LeetCode problem!\n"+random_problem+"\n\nHappy Coding! 🫡 💻")

            except discord.Forbidden:
                print("I do not have permission to send messages in this channel.")
            finally:
                await client.close()
        else:
            print("Channel not found")
            await client.close()

    client.run(BOT_TOKEN)

if __name__ == "__main__":
    main()