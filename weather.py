# https://www.google.com/search?q=weather+karachi&sca_esv=594453044&sxsrf=AM9HkKkGrd4UfEzRc2IkWlel1n64eVxfnQ%3A1703865544443&sou
from requests_html import HTMLSession
import speech_to_text

s = HTMLSession()
query = 'karachi'
url = f'https://www.google.com/search?q=weather+{query}&sca_esv=594453044&sxsrf=AM9HkKkGrd4UfEzRc2IkWlel1n64eVxfnQ%3A1703865544443&sou'
r = s.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})

# Function to get text content if the element is found, otherwise return None
def get_element_text(selector):
    element = r.html.find(selector, first=True)
    return element.text if element else None

# Use the function to get text content with error handling
temperature = get_element_text('span#wob_tm')
unit = get_element_text('span#wob_dc')
desc = get_element_text('span#wob_dcp')

# Print the results
print(temperature)
print(unit)
print(desc)

# temperature = r.html.find('span#wob_tm',first=True).text
# print(temperature)
# unit = r.html.find('span#wob_dc',first=True).text
# print(unit)
# desc = r.html.find('span#wob_dcp',first=True).text
# print(desc)