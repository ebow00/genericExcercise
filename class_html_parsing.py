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


class ParsedItemLocators:
    """
    Locators for an item in the HTML page.

    This allows us to easily see what our code will be looking at
    as well as change it quickly if we notice it is now different
    """

    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


class ParsedItem:
    """
    A class to take in a HTML page (or part of it) and find the properties of an item in it
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParsedItemLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs.get('title', [])
        return item_name

    @property
    def link(self):
        locator = ParsedItemLocators.LINK_LOCATOR
        item_link = self.soup.select_one(locator).attrs.get('href', [])
        return item_link

    @property
    def price(self):
        locator = ParsedItemLocators.PRICE_LOCATOR
        matcher = re.search(f"([{ALL_CURRENCIES}+])([0-9]+\.[0-9]*)", self.soup.select_one(locator).string)
        item_price_value = float(matcher.group(2))
        return item_price_value

    @property
    def rating(self):
        locator = ParsedItemLocators.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']  # ['star-rating', 'Three']
        clean_class = [r for r in classes if r != 'star-rating']  # List comprehension method
        # rating_by_filter = list(filter(lambda x: x != 'star-rating', classes))  # Filter method
        return clean_class[0]
        # print(rating_by_filter[0])


item = ParsedItem(ITEM_HTML)

print(item.name)
print(item.link)
print(item.price)
print(item.rating)
