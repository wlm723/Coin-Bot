import asyncio

async def rickroll_message(ctx):
	await ctx.send('https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')
	await asyncio.sleep(2)
	await ctx.send('Hehehe')
	await asyncio.sleep(1.5)
	await ctx.send('But be honest; you asked for it!')