
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


def format_date(created_at):
    return f'{created_at.month}/{created_at.day}/{created_at.year}'