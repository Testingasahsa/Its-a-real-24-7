import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Its time')

@client.command()
async def Version(ctx):

    myEmbed = discord.Embed(title="Current Version", description="Initial release", color=0x00ff00)
    myEmbed.add_field(name="Version code", value="v.1.0.0", inline=False)
    myEmbed.add_field(name="release date", value="20 Feb 2021", inline=False)
    myEmbed.set_footer(text="sample footer")

    await ctx.send(embed=myEmbed)


@client.command()
async def Profile(ctx):
    
    MeEmbed = discord.Embed(title=f'{ctx.author.name}`s Profile', description='Test', color=0x00f00)
    MeEmbed.add_field(name='Profile', value='Test', inline=False)
    MeEmbed.set_thumbnail(url=ctx.author.avatar_url)
    MeEmbed.set_footer(text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar_url)

    await ctx.send(embed=MeEmbed)



client.run('ODE0MDM5MDY2MjkwNTUyODcy.YDYC9Q.EL72wC1G5avyC1GFWypdw3I3XxQ')
