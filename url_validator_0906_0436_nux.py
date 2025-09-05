# 代码生成时间: 2025-09-06 04:36:41
import pandas as pd
import requests
from urllib.parse import urlparse
from datetime import datetime

"""
URL链接有效性验证程序，使用Pandas框架和requests库进行验证。
功能包括：
- 验证提供的URL列表中的每个链接是否有效。
- 记录验证结果，包括URL，状态码，响应时间等。
"""

class URLValidator:
    def __init__(self, url_list):
        """初始化URLValidator类
        :param url_list: 待验证的URL列表"""
        self.url_list = url_list
        self.results = []

    def validate_urls(self):
        """验证URL列表中的每个URL是否有效，并记录验证结果"""
        for url in self.url_list:
            try:
                response = self._validate_url(url)
                self._record_result(url, response)
            except requests.exceptions.RequestException as e:
                # 记录无法连接的URL
                self._record_result(url, None, error=str(e))

    def _validate_url(self, url):
        """验证单个URL是否有效
        :return: requests响应对象或None"""
        try:
            response = requests.head(url, allow_redirects=True, timeout=10)
            response.raise_for_status()  # 检查HTTP响应状态
            return response
        except requests.exceptions.HTTPError as e:
            # 记录HTTP错误
            print(f"HTTP Error: {url} returned {e.response.status_code}")
        except requests.exceptions.ConnectionError:
            # 记录连接错误
            print(f"Connection Error: Unable to connect to {url}")
        except requests.exceptions.Timeout:
            # 记录超时错误
            print(f"Timeout Error: Request timed out for {url}")
        except requests.exceptions.RequestException as e:
            # 记录其他请求错误
            print(f"Request Error: {e}")
        return None

    def _record_result(self, url, response, error=None):
        """记录URL验证结果
        :param url: 待验证的URL
        :param response: requests响应对象
        :param error: 错误信息（如果有）
        :return: None"""
        result = {
            'url': url,
            'status_code': response.status_code if response else None,
            'response_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S') if response else None,
            'error': error
        }
        self.results.append(result)

    def get_results(self):
        """获取URL验证结果
        :return: 包含验证结果的Pandas DataFrame"""
        df = pd.DataFrame(self.results)
        return df

# 示例用法
if __name__ == '__main__':
    url_list = [
        "https://www.google.com",
        "https://www.example.com",
        "https://www.nonexistentwebsite.org"
    ]
    validator = URLValidator(url_list)
    validator.validate_urls()
    results = validator.get_results()
    print(results)