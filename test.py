from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

desiredCapabilities={
"browserName":"chrome"
}

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities = desiredCapabilities);

driver.get('https://www.google.com')
element = driver.find_element_by_link_text('Privacy')
ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .click(element) \
    .key_up(Keys.CONTROL) \
    .perform()
print(driver.title)
driver.quit()