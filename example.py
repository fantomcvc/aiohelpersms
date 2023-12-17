import asyncio
from aiohelpersms import AioHelperSMS, BadApiKeyProvidedException

token = 'your_api_token'

async def main(token):
	client = AioHelperSMS(token)

	try:
		balance = await client.get_balance()
		print(balance)

		countries = await client.get_countries()
		print(countries)

	except BadApiKeyProvidedException as e:
		print(e)


if __name__ == '__main__':
	asyncio.run(main(token))
