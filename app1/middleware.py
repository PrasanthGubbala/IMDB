import requests
import json

from IMDB.settings import IMDB_FILE


class Imdb:
	def __init__(self,response):
		self.get_response = response
		url = "https://imdb8.p.rapidapi.com/actors/get-all-filmography"
		querystring = {"nconst": "nm0001667"}
		headers = {
			'x-rapidapi-host': "imdb8.p.rapidapi.com",
			'x-rapidapi-key': "ee0fec0f01msh5df54a328aaa2c6p1138b0jsn51b82c51bcc6"
		}
		response = requests.request("GET", url, headers=headers, params=querystring)

		dict_data = json.loads(response.text) # text we converted into dict

		json.dump(dict_data,open(IMDB_FILE,'w'))

	def __call__(self,request,*args,**kwargs):

		response = self.get_response(request)
		return response