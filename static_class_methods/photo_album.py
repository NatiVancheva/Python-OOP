from math import ceil
class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)] #извеждаме празна матрица в която се съдържат снимките (4)

    @classmethod
    def from_photos_count(cls, photos_count):
        # pages_needed = photos_count // cls.PHOTOS_PER_PAGE # снимките необходими на една страница
        # if photos_count % cls.PHOTOS_PER_PAGE != 0:
        #     pages_needed += 1 #добавяне на нова страница при остатък
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))
    
    def add_photo(self, label):
        # for page_index in range(len(self.photos)): 
        #     for slot_index in range(len(self.photos[page_index])): #обикаля всички слотове на страницата
        #         if self.photos[page_index][slot_index] is None: #проверява дали мястото е свободно
        #             self.photos[page_index][slot_index] = label #поставя снимката
        for i, page in enumerate(self.photos):
            if len(page) < self.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        # result = []
        # for page in self.photos:
        #     result.append("-----------")
        #     page_content = " ".join("[]" for photo in page if photo)
        #     result.append(page_content)
        # result.append("-----------")
        # return "\n".join(result)
        sep = "-" * 11 + "\n"
        result = sep
        for page in self.photos:
            result += " ".join(["[]" for _ in page]) + "\n"
            result += sep
        return result.strip()

album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())