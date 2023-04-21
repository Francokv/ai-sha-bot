import discord
from discord.ext import commands
import openai
import settings

openai.api_key = settings.OPENAI_API_KEY

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def gpt(ctx, args):
    try:
        prompt = settings.BASE_CHAT_PROMPT.format(args)
        completion = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.6, max_tokens=180, stop=None)
        await ctx.send(completion.choices[0].text)
    except Exception as e:
        print(e)
        await ctx.send("Error al generar respuesta.")

bot.run(settings.DISCORD_BOT_TOKEN)