from requests import Session

class ShrtCode:
	def __init__(self) -> None:
		self.api = "https://api.shrtco.de/v2"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36"
		}

	def _get(self, endpoint: str, params: dict = {}) -> dict:
		return self.session.get(
			f"{self.api}{endpoint}", params=params).json()

	def shorten_url(self, url: str) -> dict:
		params = {
			"url": url
		}
		return self._get(f"/shorten", params)
	
	def protect_url(
			self,
			url: str,
			password: str) -> dict:
		params = {
			"url": url,
			"password": password
		}
		return self._get(f"/shorten", params)
	
	def generate_emoji_url(self, url: str) -> dict:
		params = {
			"url": url
		}
		return self._get(f"/shorten?emoji", params)
			
	def get_url_information(self, code: str) -> dict:
		params = {
			"code": code
		}
		return self._get(f"/info", params)
	
	def get_status(self) -> dict:
		return self._get(f"/status")
	
	def generate_custom_url(
			self,
			url: str,
			custom_code: str) -> dict:
		params = {
			"url": url,
			"custom_code": custom_code
		}
		return self._get(f"/shorten", params)
