import requests, bs4
[[print("quote: %s\nauthor: %s\ntags: %s\n\n" % (element.find("span", class_="text").string, element.find("small", class_="author").string, ", ".join(list(element.find("div", class_="tags").stripped_strings)[1:]))) for element in bs4.BeautifulSoup(requests.get(url).text, "html.parser").find_all("div", class_="quote")] for url in ["https://quotes.toscrape.com/page/%d/" % i for i in range(1, 11)]]

# if you want to save the results to a json file, use the following code instead
# import requests, bs4, json
# open("result.json", "w").write(json.dumps([{"quote":element.find("span", class_="text").string, "author": element.find("small", class_="author").string, "tags": [list(element.find("div", class_="tags").stripped_strings)[1:]]} for url in ["https://quotes.toscrape.com/page/%d/" % i for i in range(1, 11)] for element in bs4.BeautifulSoup(requests.get(url).text, "html.parser").find_all("div", class_="quote")]))
