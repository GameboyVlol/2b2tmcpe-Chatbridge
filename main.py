import discord
from discord.ext import commands
from aiohttp import ClientSession

b=commands.Bot(command_prefix='=', self_bot=True, help_command=None)

TOKEN = OTgwOTUyNjU5NDUwMjg2MDkx.GnxuvP.zQ7Ne_CvVgJqgKFcgwYL2ROnO0CGuAy4949iBU

@b.event
async def on_connect():
  print("Stay halal")
  await b.change_presence(status=discord.Status.invisible)

@b.event
async def on_message(ctx):
  if ctx.channel.id==915274436347826227:
    if ctx.author.id==700275401314009168:
      channel=b.get_channel() 980950340096655390
      content=str(ctx.content).replace("@", "[at]")
      await channel.send(content)
    else:
      WEBHOOK_URL="" https://discord.com/api/webhooks/980957007177723955/eoDkWsGwunyVoolTY2CQ7IPfZ9GYJ-cIHxylLAAZJ6NePADU3Stfm8_NgR9rQspbTn60
      async with ClientSession() as session:
        webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.AsyncWebhookAdapter(session))
        await webhook.send(content=str(ctx.content).replace("@", "[at]"), username=ctx.author.name, avatar_url=ctx.author.avatar_url)

b.run(TOKEN)
