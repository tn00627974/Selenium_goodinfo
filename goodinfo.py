from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#指定 WebDriver 的路徑，並創建一個瀏覽器實例。
driver = webdriver.Chrome()

driver.get('https://goodinfo.tw/tw/index.asp')

# 使用 Selenium 提供的方法與網頁元素交互，如點擊按鈕、輸入文本等。
search_box = driver.find_element(By.ID, 'txtStockCode')
search_box.send_keys('2330')
search_box.submit()

# 等待元素加載完成，最多等待3秒，資料才會加載完畢
element = WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.b1.p4_2.r10.box_shadow')) #抓取台積電的表格
)

print(element.text)

# import pandas as pd
# from io import StringIO

# text_data = """
# 股票代號,股票名稱,成交價,昨收,漲跌價,漲跌幅,振幅,開盤,最高,最低
# 2330,台積電,819,783,+36,+4.6%,3.58%,795,820,792
# """

# 使用 StringIO 將文字資料轉換為文件流
# text_stream = StringIO(text_data)

# 讀取 CSV 資料並轉換為 DataFrame
# df = pd.to_csv(text_stream)

# 打印 DataFrame
# print(df.to_csv)

