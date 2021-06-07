""" 线上的 rap2.taobao 的 mock 数据生成,
还可以部署 easymock 和 Mockoon """
import requests
class OnlineMock:
	'''使用线上 mock服务 rap2.taobao
	当 mock_url为空时,使用默认网址,也可以自定义, 之后使用 response_ori方法,使用字典下标 返回数据'''
	def __init__(self,mock_url=None):
		if mock_url == None:
			self.mock_url = 'http://rap2api.taobao.org/app/mock/data/1634844'
		else:
			self.mock_url = mock_url

	def response_ori(self):
		_response_ori = requests.get(self.mock_url).json()
		return _response_ori



# # 测试函数
# if __name__ == '__main__':
# 	print(OnlineMock().response_ori())
