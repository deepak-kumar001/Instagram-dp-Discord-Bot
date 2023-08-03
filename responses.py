import discord
import instaloader

def insta_dp(username):
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context,
                                                    username)
    except:
        return 0
    profile_pic_url = profile.profile_pic_url
    name = profile.full_name
    return name,profile_pic_url

def handle_response(message):
    if message.startswith("dp "):

        username = message.split(" ")[1]

        info = insta_dp(username)
        if info == 0:
            return "`Username not found`"
        embed = discord.Embed(
            title=info[0],
            color=discord.Color.blurple()
        )
        embed.set_image(url=info[1])
        return embed

    if message == "dp":
        embed = discord.Embed(
            title="Correct Usage:",
            description="`-dp <username>`"
        )
        return embed

    if message == "help":
        embed = discord.Embed(
            title="Bot Commands",
            colour=discord.Color.blurple()
        )
        embed.add_field(name='-dp <username>', value='Gives profile picture of instagram username', inline=False)
        embed.set_footer(text="Created By | [×͜×]ʙᴜᴍʙʟᴇʙᴇᴇ#2503")
        return embed