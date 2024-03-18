from datetime import datetime
from discord.ext import commands


def parse_message(message):
    lines = message.split('\n')
    authors = set()
    messages = []
    for line in lines:
        tokens = line.split(':')
        authors.add(tokens[0].strip())
        messages += [line]
    return ['\n'.join(authors), '\n'.join(messages)]


def reaction_count(message):
    count = 0
    for reaction in message.reactions:
        count += reaction.count
    return count


def format_date(created_at: datetime):
    return created_at.strftime("%m/%d/%Y")


def today_as_string():
    return format_date(datetime.now())


def parse_date(input_date: str):
    try:
        return datetime.strptime(input_date, "%d/%m/%y")
    except ValueError:
        pass
    try:
        return datetime.strptime(input_date, "%d/%m/%Y")
    except ValueError:
        raise commands.BadArgument(f"Incorrect date format {input_date}. Expected dd/mm/yyyy format.")