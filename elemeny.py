# 導入需要的庫
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 設置Chrome驅動器路徑
# 這裡需要替換為你本地的ChromeDriver路徑
# CHROME_DRIVER_PATH ='chromedriver.exe'

# 創建WebDriver實例
driver = webdriver.Chrome()

# 訪問網頁
driver.get("https://example.oxxostudio.tw/python/selenium/demo.html")

# 通過id查找元素
element_by_id = driver.find_element(By.ID, "id_of_element")

# 通過name查找元素
element_by_name = driver.find_element(By.NAME, "name_of_element")

# 通過class name查找元素
element_by_class_name = driver.find_element(By.CLASS_NAME, "class_of_element")

# 通過tag name查找元素
element_by_tag_name = driver.find_element(By.TAG_NAME, "tag_of_element")

# 通過link text查找元素
element_by_link_text = driver.find_element(By.LINK_TEXT, "link_text_of_element")

# 通過partial link text查找元素
element_by_partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "part_of_link_text")

# 通過css selector查找元素
element_by_css_selector = driver.find_element(By.CSS_SELECTOR, "css_selector_of_element")

# 通過xpath查找元素
element_by_xpath = driver.find_element(By.XPATH, "//tagname[@attribute='value']")

# 操作元素，例如輸入文本
element_by_id.send_keys("Hello, World!")

# 關閉瀏覽器
driver.quit()