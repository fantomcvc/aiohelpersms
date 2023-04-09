
## Quickstart
1. Copy `aiohelpersms/` folder into your project or `pip install git+https://github.com/fantomcvc/aiohelpersms.git`
2. Install dependencies `pip install -r aiohelpersms/requirements.txt/`
3. See examples
4. Read the [documentation](https://api.helper20sms.ru/docs)

## Usage
1. `from aiohelpersms import HelperSMS, HelperSMSError`
2. `client = HelperSMS('your_api_token')`
3. See example

``` python
balance = await client.get_balance()
print(balance)

countries = await client.get_countries()
print(countries)
```

## Exception handling

``` python
from aiohelpersms import HelperSMS, HelperSMSError

client = HelperSMS(token)
try:
	balance = await client.get_balance()
	print(balance)
except HelperSMSError as e:
	print(e)
```
`> {'detail': 'Bad API key provided'}`

## License

Project Aioantipublic is distributed under the MIT license
