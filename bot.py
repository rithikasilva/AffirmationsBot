import discord
import config
import affirmationsScraper
from discord.ext import tasks

# Initialized Client
client = discord.Client()


# Function that wraps desired text input into discord bot wrapper
def wrap_box(to_be_wrapped):
    return "```" + to_be_wrapped + "```"


# Function that repeats every hour to send affirmation to the specified channel
@tasks.loop(hours=1)
async def my_task():
    # Ensures that the loop doesn't begin before the client is initialized
    await client.wait_until_ready()

    # Changes the bots presence in order to inform the users that the bot is scraping for affirmations
    await client.change_presence(activity=discord.Game('Scraping affirmation...'))

    # Sets the channel ID to the specified ID
    channel = client.get_channel(config.affirmations_channel)

    # Runs the scraping function to get an affirmation
    content = affirmationsScraper.get_affirmation()

    # Sends the affirmation
    await channel.send(wrap_box(content))

    # Changes the bots presence in order to the default state
    await client.change_presence(activity=discord.Game('The Game of Life'))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Bot is ready.')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('The Game of Life'))


# Function that ensures that bot doesn't reply to itself
@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return


# Function that provides output based on user input
@client.event
async def on_message(message):

    # If the user asks for an affirmation, the program gathers and prints an affirmation
    if message.content.startswith('!affirmation'):
        content = affirmationsScraper.get_affirmation()
        await message.channel.send(wrap_box(content))



# Start the four hour checks for news
my_task.start()
# Run the bot
client.run(config.bot_key)