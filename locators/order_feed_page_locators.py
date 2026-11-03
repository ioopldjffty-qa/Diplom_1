from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    SEARCH_FEED_TITLE_TEXT = (By.XPATH, '//h1[@class="text text_type_main-large mt-10 mb-5" and text()="Лента заказов"]')
    SEARCH_MADE_ORDER = (By.XPATH, '//li[.//a[contains(@href, "/feed/") and .//p[starts-with(text(), "#")] and .//h2[contains(@class, "text_type_main-medium")]]]')
    SEARCH_ORDER_DETAILS_TEXT = (By.XPATH, '//p[contains(@class, "text") and contains(@class, "text_type_main-medium")'
                                           ' and contains(@class, "mb-8") and text()="Cостав"]')
    SEARCH_LAST_ORDER_ID_IN_HISTORY = (By.XPATH, f"(//p[contains(@class, 'text_type_digits-default')])[last()]")
    SEARCH_ORDER_ID_IN_FEED = (By.XPATH,  '//ul/li//p[contains(@class, "text") and contains(@class, "text_type_digits-default")]')
    SEARCH_COUNTER_OF_ALL_TIME_IN_FEED = (By.XPATH,
                                          '//div[p[contains(@class, "text_type_main-medium") and text()="Выполнено за все время:"]]/p[contains(@class, "OrderFeed_number")]')
    SEARCH_COUNTER_FOR_TODAY_IN_FEED = (By.XPATH, '//div[p[contains(@class, "text_type_main-medium") and text()="Выполнено за сегодня:"]]/p[contains(@class, "OrderFeed_number")]')
    SEARCH_ORDER_IN_WORK = (By.XPATH, './/ul[contains(@class,"OrderFeed_orderListReady")]/li')
    SEARCH_ORDERS_IN_WORK_DONE = (By.XPATH, './/li[text()="Все текущие заказы готовы!"]')

