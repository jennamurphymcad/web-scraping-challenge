import pandas as pd
import requests
import pymongo
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # Define the 'MarsDB' database in Mongo
    db = client.MarsDB

    client.list_database_names()

    db.list_collection_names()

    url = 'https://redplanetscience.com/'

    response = requests.get(url)


    soup = BeautifulSoup(response.text, 'lxml')


    print(soup.prettify())

    title = soup.title.text
    print(title)


    #set up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    url_red_planet = 'https://redplanetscience.com/'
    browser.visit(url_red_planet)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.find_all('div', class_='content_title')

    for title in titles:
        print(title.text)
    # categories = sidebar.find_all('li')

    # category_list = []
    # url_list = []
    # book_url_list = []
    # for category in categories:
    #     title = category.text.strip()
    #     category_list.append(title)
    #     book_url = category.find('a')['href']
    #     url_list.append(book_url)

    # book_url_list = ['http://books.toscrape.com/' + url for url in url_list]

    # titles_and_urls = zip(category_list, book_url_list)

    # try:
    #     for title_url in titles_and_urls:
    #         browser.links.find_by_partial_text('next').click()
    # except ElementDoesNotExist:
    #     print("Scraping Complete")



    article_teaser = soup.find_all('div', class_='article_teaser_body')

    for article in article_teaser:
        print(article.text)



    url = 'https://spaceimages-mars.com/'
    browser.visit(url)



    # Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
    # featured_image_url

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
    featured_image = soup.find_all('img', class_='headerimage fade-in')

    featured_image_src = ""
    # Make sure to save a complete url string for this image.
    for image in featured_image:
        featured_image_src = image['src']

    # # Example:
    # featured_image_url = featured_image['src'].text

    print(featured_image_src)

    featured_image_url = 'https://spaceimages-mars.com/' + featured_image_src


    print(featured_image_url)


    url_facts = 'https://galaxyfacts-mars.com/'


    tables = pd.read_html(url_facts)
    tables


    df_mars_facts = tables[0]
    df_mars_facts.head()


    html_table = df_mars_facts.to_html()
    html_table


    html_table.replace('\n', '')

    # df.to_html('table.html')
    df_mars_facts.to_html('table.html')


    # get_ipython().system('open table.html')



    url_mars_hem = 'https://marshemispheres.com/'
    browser.visit(url_mars_hem)



    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
    featured_link = soup.find_all('a', class_='itemLink product-item')

    # featured_link['href']

    # # paragraphs = soup.find_all('p')
    # for link in paragraphs:
    #     print(paragraph.text)



    print(featured_link)




    href_link = []
    href_list = []
    title = []
    title_list = []
    link_click_href = []
    for link in featured_link:
    #     if link not in link_click_href:
        href_link = link['href']
        link_click_href.append(href_link)
        for i in link_click_href:
            if i not in href_list and i != '#':
                href_list.append(i)

                


    print(href_list)


    hem_url_list = ['https://marshemispheres.com/' + url for url in href_list]

    # titles_and_urls = zip(category_list, book_url_list)

    # try:
    #     for url in hem_url_list:
    #         browser.links.find_by_partial_text('next').click()
    # except ElementDoesNotExist:
    #     print("Scraping Complete")


    print(hem_url_list)



    img_url_link = []
    url_new = ""
    title_list = []
    new={}
    content = []


    for link in hem_url_list:
        url_new = link
        browser.visit(url_new)
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain book information
        featured_title = soup.find_all('h2', class_="title")

        featured_link_test = soup.find_all('a')
        
    #     t_text = title.text
    #     l_text = link['href']
    #     if any(d['title'] == title.text for d in content):

        for title in featured_title:
        #       if title.text not in content.items():
        #             title_list.append(title.text)
                    new['title'] = title.text
                    content.append(new)

        for link in featured_link_test:
    #         if not any(d['img_url'] == link['href'] for d in content):
        #         if link['href'] not in content.items():
                if link.text == 'Sample':
        #                 img_url_link.append(link['href'])
                    new['img_url'] = 'https://marshemispheres.com/' + link['href']
                    content.append(new)        

    mars_data = {
        "featured_img": featured_image_url,
        "news_titles": titles,
        "article_preview": article_teaser,
        "hemispheres": content
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data


    # # print(content)
    # return print("content")


