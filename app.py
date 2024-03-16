from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/<token>',methods=['POST','GET'])
def ap(token):
	#method = request.form['method']
	number ='01017818013'
	#token = request.form['token']
	ul=f"https://web.vodafone.com.eg/services/dxl/ramadanpromo/promotion?@type=RamadanHub&channel=website&msisdn={number}"
	
	
	hd={
	    "Host": "web.vodafone.com.eg",
	    "Connection": "keep-alive",
	    "msisdn": number,
	    "api-host": "PromotionHost",
	    "Accept-Language": "AR",
	    "Authorization": "Bearer "+token,
	    'Content-Type': 'application/json',
	    'x-dtreferer': 'https://web.vodafone.com.eg/spa/portal/hub',
	    'Accept': 'application/json',
	    'clientId': 'WebsiteConsumer',
	    'Referer': 'https://web.vodafone.com.eg/spa/portal/hub',
	    'Accept-Encoding': 'gzip, deflate, br',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.94 Mobile Safari/537.36',
	    'channel': 'WEB',
	}
	r =requests.get(ul, headers=hd).json()
	print (r)
	return r
	
	#return {'method': method,'number':number, 'url': url, 'token': token}
	
if __name__ == '__main__':
	app.run()
