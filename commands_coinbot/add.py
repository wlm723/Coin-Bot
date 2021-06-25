from get_bank_data import get_bank_data
import json

async def add(user, amount = 0, mode = 'wallet'):
	users = await get_bank_data.get_bank_data()
	if mode == 'wallet' or 'Wallet' == True:
		users[str(user.id)]['Wallet'] += int(amount)
	
	elif mode == 'bank' or 'Bank' == True:
		users[str(user.id)]['Bank'] += int(amount)

	with open('bank.json', 'w') as f:
		json.dump(users, f)

	amt = [users[str(user.id)]['Wallet'], users[str(user.id)]['Bank']]
	return amt
