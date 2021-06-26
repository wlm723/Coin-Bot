import discord
import json
from commands_coinbot import get_bank_data
from commands_coinbot import add

async def addcoins(ctx, user = discord.Member, mode, amount : int):
  users = await get_bank_data.get_bank_data()

  if mode == 'wallet' or 'Wallet' == True:
	  users[str(user.id)]['Wallet'] -= amount
    
	elif mode == 'bank' or 'Bank' == True:
	  users[str(user.id)]['Bank'] -= amount

	with open('bank.json', 'w') as f:
		json.dump(users, f)

	amt = [users[str(user.id)]['Wallet'], users[str(user.id)]['Bank']]
	return amt
  
  embed = discord.Embed(
    title = f'Adding coins to {user.name}',
    description = f'Hey {ctx.author.name}! You just added {amount} coins to {user.name}\'s bank account!',
    color = 0x006AFF
  )
