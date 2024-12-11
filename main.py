import csv
import d20
import discord
import random
from datetime import date, datetime, timedelta
from util import *
from bot import setup

bot, config = setup()

braincell_holders = [
    ('<@245743196145975297>', 'The only person who can make you be a bear today is you.'),
    ('<@349380601234849793>', 'Wisdom\'s not a dump-stat today, baby.'),
    ('<@412417592557305856>', 'It\'s WIIIIIIIIIZZZZZZZAAAAAAAAAAARRRRRDDDDD time!'),
    ('<@185215359601606656>', 'What else is new?'),
    ('<@195363429349851136>', 'Probably better that we mute <#754505946457178212> until tomorrow.'),
    ('<@219174728890318859>', 'Heavy is the head that contains the braincell.'),
    ('<@434770915415425074>', 'Thanks for signing up for Drow Facts! Type STOP to cancel.'),
    ('<@432556436317536269>', 'Oh no guys. Lonnie has the braincell. Oh god oh fuck.')
]


@bot.event
async def on_message(message):
    if 'instagram.com' in message.content:
        await message.channel.send(
            message.content.replace('instagram', 'instagramez'),
            reference=message
        )
    elif 'x.com' in message.content:
        await message.channel.send(
            message.content.replace('x.com', 'fxtwitter.com'),
            reference=message
        )
    elif 'twitter.com' in message.content and 'fxtwitter' not in message.content:
        await message.channel.send(
            message.content.replace('twitter', 'fxtwitter'),
            reference=message
        )
    elif 'tiktok.com' in message.content and 'vxtiktok' not in message.content:
        await message.channel.send(
            message.content.replace('tiktok', 'vxtiktok'),
            reference=message
        )
    await bot.process_commands(message)


@bot.command()
async def braincell(ctx):
    today = date.today()
    dt = datetime(today.year, today.month, today.day)
    random.seed(dt.timestamp())
    choice = random.randint(0, 7)
    holder, message = braincell_holders[choice]
    await ctx.send(f"Congratulations {holder}, you have the braincell today! {message}")


@bot.command()
async def roll(ctx, message):
    await ctx.send(f"{d20.roll(message)}")


@bot.command()
async def open_the_pod_bay_doors(ctx):
    await ctx.send(f"I'm afraid I can't let you do that, {ctx.message.author.mention}")


@bot.command()
async def quotes(ctx, starting: parse_date, ending: parse_date):
    async with ctx.typing():
        channel = await bot.fetch_channel(config['discord']['quote_channel'])
        with open('quotes.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Date', 'Submitter', 'Person Quoted', 'Quote', 'Reactions', 'Points'])
            async for message in channel.history(after=starting, before=ending, limit=1000):
                row = [format_date(message.created_at), message.author.global_name]
                row += parse_message(message.content)
                row += [reaction_count(message), 0]
                csvwriter.writerow(row)
    attachment = discord.File("quotes.csv")
    await ctx.send(
        file=attachment,
        content=f"Here are the quotes from {format_date(starting)} to {format_date(ending)}"
    )


if __name__ == '__main__':
    bot.run(config['discord']['token'])
