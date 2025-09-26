import requests
import execjs
import os
from dotenv import load_dotenv
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 加载环境变量
load_dotenv()

# 从环境变量中获取密钥
KEY = os.getenv("AES_KEY", "EB444973714E4A40876CE66BE45D5930")
IV = os.getenv("AES_IV", "B5A8904209931867")

js_code = open("src/crypto.js").read()
js_compile = execjs.compile(js_code)

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://ggzyfw.fujian.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ggzyfw.fujian.gov.cn/business/list/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

json_data = {
    'pageNo': 5,
    'pageSize': 20,
    'total': 2813,
    'AREACODE': '',
    'M_PROJECT_TYPE': '',
    'KIND': 'GCJS',
    'GGTYPE': '1',
    'PROTYPE': '',
    'timeType': '6',
    'BeginTime': '2024-10-09 00:00:00',
    'EndTime': '2025-04-09 23:59:59',
    'createTime': '',
    'ts': 1744203721471,
}

try:
    sign = js_compile.call("d", json_data)
    logger.info(f"sign::: {sign}")

    headers['portal-sign'] = sign

    response = requests.post('https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo', headers=headers, json=json_data)
    response.raise_for_status()  # 检查HTTP错误
    logger.info(response.text)
    data = response.json().get("Data")

    # 响应解密
    logger.info(data)
    data = js_compile.call("b", data)
    logger.info(data)
except requests.exceptions.RequestException as e:
    logger.error(f"请求错误: {e}")
except execjs.Error as e:
    logger.error(f"JavaScript执行错误: {e}")
except Exception as e:
    logger.error(f"其他错误: {e}")