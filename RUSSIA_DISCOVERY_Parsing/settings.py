from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
options = webdriver.ChromeOptions()

# options.add_argument("start-maximized")
# options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# путь к драйверу
service = Service(executable_path="/soft/chromedriver.exe")

driver = webdriver.Chrome(options=options, service=service)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

print(driver.execute_script("return navigator.userAgent;"))