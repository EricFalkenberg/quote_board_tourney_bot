import csv
import discord
import toml
from datetime import datetime
from util import format_date, parse_message, reaction_count

with open('config.toml') as config_file:
    config = toml.load(config_file)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = await client.fetch_channel(config['discord']['quote_channel'])
    with open('quotes.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Date', 'Submitter', 'Person Quoted', 'Quote', 'Reactions', 'Points'])
        async for message in channel.history(before=datetime.now(), after=datetime(2023, 4, 2)):
            row = [format_date(message.created_at), message.author.global_name]
            row += parse_message(message.content)
            row += [reaction_count(message), 0]
            csvwriter.writerow(row)
    await client.close()


if __name__ == '__main__':
    client.run(config['discord']['token'])
