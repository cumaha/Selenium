from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('/home/leo/Downloads/chromedriver')
driver.get("http://your-url")
assert "Post Title" in driver.title
link=driver.find_element_by_link_text("Add new")
NewWindow=link.click()
assert "Save" in driver.page_source

#Add posts
title=driver.find_element_by_name("title")
title.send_keys("Selenium web test")
content=driver.find_element_by_name("content")
content.send_keys("Selenium web test")
category=driver.find_element_by_name("category")
category.send_keys("Selenium web test")

#http://selenium-python.readthedocs.org/en/latest/navigating.html
select = Select(driver.find_element_by_name('published'))
published=select.select_by_value("0")

button=driver.find_element_by_class_name('button')
success=button.click()
assert "Add was successful" in driver.page_source

#Edit Posts
link=driver.find_element_by_link_text("Edit")
NewWindow=link.click()
assert "Save" in driver.page_source

title=driver.find_element_by_name("title")
title.send_keys("Selenium web test edit")
content=driver.find_element_by_name("content")
content.send_keys("Selenium web test edit")
category=driver.find_element_by_name("category")
category.send_keys("Selenium web test edit")

#http://selenium-python.readthedocs.org/en/latest/navigating.html
select = Select(driver.find_element_by_name('published'))
published=select.select_by_value("0")

button=driver.find_element_by_class_name('button')
success=button.click()
assert "Update was successful" in driver.page_source

#Delete Posts
link=driver.find_element_by_link_text("Delete")
newindow=link.click()
assert "Post was deleted successfully" in driver.page_source
driver.close()
