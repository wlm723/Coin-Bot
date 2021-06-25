import asyncio

async def facepalm_message(ctx, username):
	await ctx.send(f'Let us all give a huge facepalm to {username} <:PepeLaugh:815111733541863454>')
	await asyncio.sleep(1)
	await ctx.send('https://tenor.com/view/disappointed-face-palm-seriously-exasperated-gif-7304550')