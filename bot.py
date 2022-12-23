import discord
import os
import random
import requests
import json

# Open the token from a JSON file
with open('token.json', 'r') as file:
    token = json.load(file)['token']

client = discord.Client(intents=discord.Intents.default())

sheet = 'current commands:\n\n'
sheet += '**$hellosofia**\n'
sheet += '*Say hello to Sofia!*\n\n'
sheet += '**$rickroll**\n'
sheet += '*Generates a rickroll video to trick your friends :)*\n\n'
sheet += '**$help**\n'
sheet += '*You just did it. Duh.*\n\n'
sheet += '**$pat**\n'
sheet += '*Pat da Cat*\n\n'
sheet += '**$rating**\n'
sheet += '*Find out how epic gamer you are* \n\n'
sheet += '**$cat**\n'
sheet += '*Get a random image of a cat\n\n*'
sheet += 'You can go to our website at: \n **https://sofiathecat.mightyspaceman.com/**'

rickroll = ["https://www.youtube.com/watch?v=Uj1ykZWtPYI&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=3","https://www.youtube.com/watch?v=EE-xtCF3T94&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=3","https://www.youtube.com/watch?v=V-_O7nl0Ii0&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=4","https://www.youtube.com/watch?v=vkbQmH5MPME&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=5","https://www.youtube.com/watch?v=8O_ifyIIrN4&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=6","https://www.youtube.com/watch?v=ikFZLI4HLpQ&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=7","https://www.youtube.com/watch?v=0SoNH07Slj0&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=8","https://www.youtube.com/watch?v=xfr64zoBTAQ&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=9","https://www.youtube.com/watch?v=cqF6M25kqq4&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=10","https://www.youtube.com/watch?v=j5a0jTc9S10&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=11","https://www.youtube.com/watch?v=dPmZqsQNzGA&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=12","https://www.youtube.com/watch?v=ID_L0aGI9bg&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=13","https://www.youtube.com/watch?v=nHRbZW097Uk&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=15""https://www.youtube.com/watch?v=bIXm-Q-Xa4s&list=PLQcpjwveNrhLk4gB6c87VACB9mBS0ibas""https://www.youtube.com/watch?v=aqOoTQ-G-r4&list=PLQcpjwveNrhLk4gB6c87VACB9mBS0ibas&index=2""https://www.youtube.com/watch?v=4-kg9y5mq1M&list=PLQcpjwveNrhLk4gB6c87VACB9mBS0ibas&index=3"]

cat = ["https://petcentral.chewy.com/wp-content/uploads/2018/05/black-cat-breeds-and-history.jpg", "https://66.media.tumblr.com/c32ac346c238eaef8dafb56beba4353e/tumblr_ozrt94Ntyx1vaexlvo1_500.jpg", "https://p-cdn6pet.jmsinf.com/tmp/image-thumbnails/meow-mix/cat-care/image-thumb__9422__auto_c9b5482fc415ef6a2d0d9a179e40d153/6-Fun-Facts-About-Black-Cats-1.jpg", "https://pbs.twimg.com/media/DWs5k4aU0AE7uog.jpg", "https://cutecatshq.com/wp-content/uploads/2014/09/My-Sweet-Boy-Conner.jpg", "https://redrover.org/wp-content/uploads/2017/08/Onyx_kitty_300px.jpg", "https://th.bing.com/th/id/Ra86ee629901c5872f436ddf43c8366c7?rik=Ez6jAVgB%2fnJuxg&riu=http%3a%2f%2fwww.kittyconnection.net%2fwp-content%2fuploads%2f2014%2f11%2fVader-800x757-300x283.jpg&ehk=Y%2bVqFXUWecMcyi%2fLTCsCJUEFunXT7p9rHKZIlo6fC9k%3d&risl=&pid=ImgRaw", "https://th.bing.com/th/id/R37b3bd8e2065d06e94ece535f2a8d5c6?rik=TYhMnmLKfbNwdg&riu=http%3a%2f%2fm5.paperblog.com%2fi%2f18%2f185140%2fwordless-wednesday-cat-in-a-box-L-7k98e0.png&ehk=6GhhZmrPnlRCXzV%2fBw5%2bYneGF8TBypyruf6JbJGZ5mc%3d&risl=&pid=ImgRaw", "https://live.staticflickr.com/3151/2994106279_239780cfb9_n.jpg", "https://lh5.googleusercontent.com/proxy/XSeKaOPDgKeweOSAM1TdCV5qkaKxE-uM_ARuZLPGse1OLmSdlXb0KLKioUku0a39MxTl_x4eq10sAQyUzQH3v5Q0XVEpXS49_tTgBkPdgKd7=s0-d", "https://i.redd.it/pzi9ii00k8b51.jpg", "https://tenor.com/view/sassy-cats-angry-mad-ok-gif-9934420"]


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('$help'))
  print('we have logged in as {0.user}'.format(client))

  @client.event 
  async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('$rickroll'):
      await message.channel.send(random.choice(rickroll))
    
    if message.content.startswith('$pat'):
      await message.channel.send('purr! purr! thank you for patting me, {}! \n {}'.format(message.author, random.choice(cat)))

    if message.content.startswith('$cat'):
      await message.channel.send("kat\n", requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url'])

    if message.content.startswith('$help'):
      await message.channel.send(sheet)

    if message.content.startswith('$purr'):
      await message.channel.send("purr! purr!")

    if message.content.startswith('$purr'):
      await message.channel.send("purr! purr!")

    if message.content.startswith('$hellosofia'):
      await message.channel.send('Greetings, Hooman!')
      
    if message.content.startswith('$play'):
      await message.channel.send("thank you for play, i think its very OK! \n https://tenor.com/view/cat-jumping-excited-play-time-gif-9841068")


    if message.content.startswith('$rating'):
      await message.channel.send('*{}s gamer rating:* \n **{}%**'.format(message.author, random.randint(1, 100)))


client.run(token)
