import csv
import discord
from util import *
from bot import setup

bot, config = setup()


@bot.command()
async def spreadsheet(ctx, starting: parse_date, ending: parse_date):
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
