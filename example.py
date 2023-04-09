import asyncio
from aiohelpersms import HelperSMS, HelperSMSError

token = 'your_api_token'

async def main(token):
	client = HelperSMS(token)

	try:
		balance = await client.get_balance()
		print(balance)

		countries = await client.get_countries()
		print(countries)

	except HelperSMSError as e:
		print(e)


if __name__ == '__main__':
	asyncio.run(main(token))