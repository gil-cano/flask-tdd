from selenium import webdriver


browser = webdriver.Firefox()

# Edith has heard about a cool new online app. She goes
# to check out its homepage
browser.get('http://localhost:5000')

# She notices the page title and header mention word counter
assert 'Word Counter' in browser.title, "Browser title was " + browser.title

# Satisfied, she goes back to sleep
browser.quit()
