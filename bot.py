import discord
import responses

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        print(response)
        if type(response) == str:
            await message.channel.send(response)
        else:
            await message.channel.send(embed=response)

    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
    # client = discord.Client()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    botPrefix = "-"

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        await client.change_presence(activity=discord.Game(name="Stalker | -help"))

    @client.event
    async def on_message(message):

        if message.content.startswith(botPrefix):
            # Get data about the user
            username = str(message.author)
            user_message = message.content
            channel = str(message.channel)

            # Debug printing
            print(f"{username} said: '{user_message}' ({channel})")
            await send_message(message, user_message[1:]) # [1:] Removes the '-'

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)
