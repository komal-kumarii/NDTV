import requests
from bs4 import BeautifulSoup
import pprint

def scrape_ndtv_details():
    url="Https://www.ndtv.com/india/page-3"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    # main_div=soup.find("div",class_="ins_wid990",id="").ul
    divs=soup.find("div",id="ins_storylist",class_="new_storylising").ul
    li_s=divs.find_all("li")
    # return(li_s)
    url_img=[]
    headlines=[]
    date=[]
    news_information=[]
    # return(ul)
    for li in range(0,len(li_s)):
        # return(li_s[5])
        if li ==3 or li==7:
            continue
        else:
            img_=li_s[li].find("div",class_="new_storylising_img").a
            head =li_s[li].find("div",class_="new_storylising_contentwrap")
            img_url=img_.img["src"]
            # print(img_url)
            url_img.append(img_url)
    # return(url_img)
            h2_tag=head.find('h2',class_="nstory_header").a.get_text().strip() 
        # header=head.find(a)
            # print(h2_tag)
            a=[]
            headlines.append(h2_tag)
            day=head.find("div",class_="nstory_dateline").get_text().strip()
            data = day.split("|")
            days=data[-1]
            date.append(days)
        for j in range(0,len(url_img)):
            dic={}
            dic["News_Headline"]=headlines[j]
            dic["Pic_Url"]=url_img[j]
            dic["News_information_time"]=date[j]
        news_information.append(dic)
    return(news_information)

pprint.pprint(scrape_ndtv_details())





