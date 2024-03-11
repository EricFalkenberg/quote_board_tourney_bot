## Quote Board Tourney Bot
A discord bot written to scrape our `#quote-board` channel and parse the data into a CSV file so that we can vote on the top quotes of the year. It assumes that the quote board will consist of individual messages that take the following format:
```
Alice: Why did the chicken cross the road?
Bob: Wait, are we having this conversation in a github repo's README?
Alice: Alas, it seems we are. Do you think our lives have meaning?
Bob: Probably not beyond this conversation being an example of some sort. I am now sad.
```
### Installation
Pull the git repo and then install the requirements with `pip install -r requirements.txt`. Preferably do that in a virtual environment.
### Config
If this fits your use case, create your own discord bot and fill out the `config.toml` file with your bots private token and the channel ID for the discord channel you want to scrape.
### Running
You know the drill. `python main.py`
The results will create the file `quotes.csv` and write the output into it.
