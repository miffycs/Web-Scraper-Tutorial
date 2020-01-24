import pandas as pd
from requests_html import HTMLSession       # https://pypi.org/project/requests-html/

# starts an HTMLSession
session = HTMLSession()

# gets the webpage
r = session.get('https://miffychen.tech/cs601/about.html')

# find desired link selector using Chrome DevTool lol
selector_first_link = 'body > main > section.profile_card > div.container_profile_card > div > div.card_right > div > ul > div:nth-child(1) > li.col-9.link > a'

# modify selector to select all links in container_profile_card
selector = 'body > main > section.profile_card > div.container_profile_card > div > div.card_right > div > ul > div > li > a'

# creates a list of all the elements found using the selector
results = r.html.find(selector)

# print(results[0].absolute_links)              # still in list form
# print(results[0].text)                        # text of the a tag
# print(list(results[0].absolute_links)[0])     # link by itself

# automate getting links from a selector
def get_text_link_from_sel(selector):
    rlist = []
    try:
        results = r.html.find(selector)
        for result in results:
            rtext = result.text
            rlink = list(result.absolute_links)[0]
            rlist.append((rtext, rlink))
        return rlist
    except:
        return None

# print(get_text_link_from_sel(selector))

# DataFrame == pretty
df = pd.DataFrame(get_text_link_from_sel(selector), columns=['Text', 'Link'])
print(df)

# Save to CSV, encoding=for_CH_chars(utf-8=bad), index=want_row#_or_not
df.to_csv('output.csv', encoding='utf_8_sig', index=False)
