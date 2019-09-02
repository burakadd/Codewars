# https://www.codewars.com/kata/515bb423de843ea99400000a


class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        from math import floor
        return floor(self.item_count(
            ) / self.items_per_page) + 1

    def page_item_count(self, page_index):
        return -1 if page_index >= self.page_count(
        ) or page_index < 0 else self.items_per_page if page_index < self.page_count(
            ) - 1 else self.item_count() % self.items_per_page

    def page_index(self, item_index):
        from math import floor
        return -1 if item_index >= self.item_count(
            ) or item_index < 0 or not self.item_count(
                ) else floor(item_index / self.items_per_page)
