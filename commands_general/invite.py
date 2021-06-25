import discord

async def invite(ctx):
	embed = discord.Embed(
		title = 'Invite',
		description = 'Hey! Thanks for inviting me! Invite me here:',
		color = 0x006AFF
		)
	embed.add_field(
		name = 'Invite link',
		value = 'https://discord.com/api/oauth2/authorize?client_id=815556341766553600&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.events.stdlib.com%2Fdiscord%2Fauth%2F&scope=bot',
		inline = False
		)
	embed.set_image(url = 'https://media.istockphoto.com/vectors/thank-you-retro-card-vector-id1151005360?k=6&m=1151005360&s=612x612&w=0&h=4x0Z0Qn9ntaK3tbDOKWOq4dj4YlNgK50grxEvQgLoXo=')
	await ctx.send(embed = embed)