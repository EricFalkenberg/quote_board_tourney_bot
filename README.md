## Quote Board Tourney Bot
A discord bot written to scrape our `#quote-board` channel and parse the data into a CSV file so that we can vote on the top quotes of the year.
This really isn't anything to look at.

### Installation
Pull the git repo and then install the requirements with `pip install -r requirements.txt`. Preferably do that in a virtual environment.

### Config
If this somehow fits your use case, create your own discord bot and fill out the `config.toml` file with your bots private token and the channel ID for the discord channel you want to scrape.


### Running
You know the drill. `python main.py`
The results will create the file `quotes.csv` and write the output into it.
