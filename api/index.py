from flask import Flask, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["JSON_SORT_KEYS"] = False


class Shop:
    def __init__(self, name, url, desc, img):
        self.name = name
        self.url = url
        self.desc = desc
        self.img = img


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/sehir/<string:sehir>')
def sehir(sehir: str):
    # html_content = requests.get(f"https://rehber.vedatmilor.com/loc/{sehir}").text
    html_content = requests.get(f"https://rehber.vedatmilor.com/loc/{sehir}/?=&count=40&orderby=date&order=DESC").text
    soup = BeautifulSoup(html_content, "html.parser")
    shops = soup.find_all("div", attrs={"class": "item-title"})
    shop_list = []
    for s in shops:
        name = s.find("h3").text
        url = s.find("a").get("href")
        html_content_shop = requests.get(url).text
        soup_shop = BeautifulSoup(html_content_shop, "html.parser")
        desc = soup_shop.find("div", attrs={"class": "entry-content"}).find("p").text
        # img = soup_shop.find("div", attrs={"class": "page-title has-bg"})
        shop_list.append(Shop(name, url, desc, None))
    return jsonify([ob.__dict__ for ob in shop_list])
