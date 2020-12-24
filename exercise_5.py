from selenium import webdriver
from selenium.webdriver.common.by import By

#1.UTM settings on Newsletter design page:
UTM_settings = (By.CSS_SELECTOR, "label[for='enableUtmSettings']")
# for check console $$("label[for='enableUtmSettings']")
#utm_settings_xpath = (By.XPATH, ".//*label[@for='enableUtmSettings']")

#2. input warning message, for example, on Journey SMS page when we try to save empty title input
input_warning_message = (By.XPATH, ".//*[text()= 'The Your Message field is required.']")
# for check console $x(".//*[text()= 'The Your Message field is required.']")
warning_message = (By.XPATH, "//div[@class = 'dynamicAttributes smsMessage']//P")[1]

#3.	on Journey do list filter input
list_filter_input = (By.XPATH, "//input[@id='search-value']")
filter_input = (By.CSS_SELECTOR, "input[name='searchValue']")
#$x("//input[@id='search-value']")
list_filter = (By.ID, "search-value")


#4.	'Test' radio button on smart recommender launch step
test_radio_button = (By.XPATH, "//input[@id='Test']")  #only button
#$x("//input[@id='Test']")
radio_button_test = (By.CSS_SELECTOR, "label[for='Test']") #label

#5.	on Journey do list how to click exactly needed campaign’s Statistics button if there is more than 1 campaigns in the list
statistic_button = (By.XPATH, "//*[@class='vuetable-slot statistics']")

statistic = (By.XPATH, "//*[@id='filter-dropdown']/div[2]/div[1]/div/table/tbody/tr[3]/td[8]")

statistic_b = (By.XPATH, "//*[@class= 'vuetable-body']/tr[3]/td[8]")

s_button = (By.CSS_SELECTOR, ".vuetable-slot.statistics")[3]

#6.	on Message box design page remove variation cross icon
remove = (By.XPATH, "//*[@id='delete']")
delete_button = (By.CSS_SELECTOR, "button#delete")

remove_button = (By.ID, "delete")
#7.	Remove/ Change element buttons on Journey canvas page
change_element_button = (By.XPATH, "//*[@class='options']")
change_button = (By.CSS_SELECTOR, "options") #class name = options

#8. Alert toaster on any page of panel
alert_toaster = (By.XPATH, "//*[@class='messageAlertBox messageAlertBoxHidden animationHalf']")
alert_t = (By.CSS_SELECTOR, ".messageAlertBox.messageAlertBoxHidden.animationHalf")

#9. on Social Proof ‘Create New Personalization’
create_button = (By.XPATH, "//*[@id='create-mobile-campaign']")
create_personalization_button = (By.CSS_SELECTOR, "#create-mobile-campaign")
