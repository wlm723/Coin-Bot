import requests
import discord

async def joke_message(ctx):
	joke = requests.get('https://official-joke-api.appspot.com/random_joke').json()
	
	if joke["type"] == "error":
		embed = discord.Embed(
			title = "Error",
			description = "Oops!! Too many requests to the jokes api...",
			color = 0xff000
		)

		embed.add_field(
			name= "Details",
			value = "We use an API to get you all a good funny joke. However, the api has a time limit... And if you exceed that, **No Jokes For you**",
      inline = False
		)

	else:
		try:
			setup = joke["setup"]
		except:
			setup = ""
		try: 
			punchline = joke["punchline"]
		except: 
			punchline = ""

		embed = discord.Embed(
			title = "I hope this makes you laugh!!!",
			description = f"{setup} \n {punchline} \n\n Did you laugh??? I hope so XD",
			color = 0x0373fc
		)

	await ctx.send(embed=embed)