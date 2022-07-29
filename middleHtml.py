import re
from bs4 import BeautifulSoup

ALL_CURRENCIES = '£¥¥฿৳៛₡₥₦₨₩₪₫€₭₮₱₲₴₵₸₹₺₼₽₾₿⃀$$֏؋ƒ﷼'

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''

soup = BeautifulSoup(ITEM_HTML, 'html.parser')


def find_item_name():
    locator = 'article.product_pod h3 a'
    item_link = soup.select_one(locator)
    item_name = item_link.attrs.get('title', [])
    print(f"Item's name: {item_name}")


def find_item_link():
    locator = 'article.product_pod h3 a'
    item_link = soup.select_one(locator).attrs.get('href', [])
    print(f"Item's link: {item_link}")


def find_item_price():
    locator = 'article.product_pod p.price_color'
    matcher = re.search(f"([{ALL_CURRENCIES}+])([0-9]+\.[0-9]*)", soup.select_one(locator).string)
    item_price_value = float(matcher.group(2))
    print(f"Item's price: {matcher.group(1)}{item_price_value}")


def find_item_rating():
    locator = 'article.product_pod p.star-rating'
    star_rating_tag = soup.select_one(locator)
    classes = star_rating_tag.attrs['class']  # ['star-rating', 'Three']
    clean_class = [r for r in classes if r != 'star-rating']  # List comprehension method
    rating_by_filter = list(filter(lambda x: x != 'star-rating', classes))  # Filter method
    print(clean_class[0])
    print(rating_by_filter[0])


find_item_name()
find_item_link()
find_item_price()
find_item_rating()
