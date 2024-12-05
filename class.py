class pork_belly: # 1: 한식, 본연의 맛
    def __init__(self):
        self.name = '삼겹살'
        self.src = './image/삼겹살.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class sushi: # 2: 일식, 본연의 맛
    def __init__(self):
        self.name = '초밥'
        self.src = './image/초밥.jpg'
        self.chinese = 0
        self.japanese = 1
        self.western = 0
        self.korean = 0
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class sashimi: # 3: 일식, 본연의 맛
    def __init__(self):
        self.name = '회'
        self.src = './image/회.jpg'
        self.chinese = 0
        self.japanese = 1
        self.western = 0
        self.korean = 0
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class steak: # 4: 양식, 본연의 맛
    def __init__(self):
        self.name = '스테이크'
        self.src = './image/스테이크.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 1
        self.korean = 0
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class skinon_pork_belly: # 5: 한식, 본연의 맛
    def __init__(self):
        self.name = '오겹살'
        self.src = './image/오겹살.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class fried_chicken: # 6: 양식, 패스트 푸드, 짠 맛
    def __init__(self):
        self.name = '후라이드 치킨'
        self.src = './image/후라이드 치킨.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 1
        self.korean = 0
        self.fastfood = 1
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 0

class pork_ribs: # 7: 한식, 단 맛, 짠 맛
    def __init__(self):
        self.name = '돼지갈비'
        self.src = './image/돼지갈비.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 0

class ramen: # 8: 한식, 짠 맛
    def __init__(self):
        self.name = '라면'
        self.src = './image/라면.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 0

class kimchi_stew: # 9: 한식, 짠 맛, 매운 맛
    def __init__(self):
        self.name = '김치찌개'
        self.src = './image/김치찌개.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 1

class beef_tartare: # 10: 한식, 본연의 맛
    def __init__(self):
        self.name = '육회'
        self.src = './image/육회.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class braised_pork_galbi_and_kimchi: # 11: 한식, 단 맛, 매운 맛
    def __init__(self):
        self.name = '등갈비 김치찜'
        self.src = './image/등갈비 김치찜.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 0
        self.spicy = 1

class tteokbokki: # 12: 한식, 단 맛, 매운 맛
    def __init__(self):
        self.name = '떡볶이'
        self.src = './image/떡볶이.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 0
        self.spicy = 1

class beef_intestines: # 13: 한식, 본연의 맛
    def __init__(self):
        self.name = '곱창'
        self.src = './image/곱창.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class shabu_shabu: # 14: 한식, 본연의 맛
    def __init__(self):
        self.name = '샤브샤브'
        self.src = './image/샤브샤브.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class gamjatang: # 15: 한식, 짠 맛, 매운 맛
    def __init__(self):
        self.name = '감자탕'
        self.src = './image/감자탕.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 1

class seasoned_spicy_chicken: # 16: 양식, 힌식, 패스트 푸드, 짠 맛, 매운 맛
    def __init__(self):
        self.name = '양념치킨'
        self.src = './image/양념치킨.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 1
        self.korean = 1
        self.fastfood = 1
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 1

class pork_and_ricesoup: # 17: 한식, 짠 맛, 본연의 맛
    def __init__(self):
        self.name = '돼지국밥'
        self.src = './image/돼지국밥.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 1
        self.spicy = 0

class grilled_galbi: # 18: 한식, 단 맛, 짠 맛
    def __init__(self):
        self.name = '소갈비'
        self.src = './image/소갈비.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 0

class steamed_snow_crab: # 19: 한식, 짠 맛, 본연의 맛
    def __init__(self):
        self.name = '대게찜'
        self.src = './image/대게찜.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 1
        self.spicy = 0

class grilled_pork_neck: # 20: 한식, 본연의 맛
    def __init__(self):
        self.name = '항정살'
        self.src = './image/항정살.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class kimchi_fried_rice: # 21: 한식, 짠 맛, 매운 맛
    def __init__(self):
        self.name = '김치볶음밥'
        self.src = './image/김치볶음밥.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 1

class steamed_kingcrab: # 22: 한식, 짠 맛, 본연의 맛
    def __init__(self):
        self.name = '킹크랩 찜'
        self.src = './image/킹크랩 찜.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 1
        self.korean = 0
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 1
        self.spicy = 0

class budaejjigae: # 23: 한식, 짠 맛, 매운 맛
    def __init__(self):
        self.name = '부대찌개'
        self.src = './image/부대찌개.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 1

class bossam: # 24: 한식, 짠 맛, 매운 맛, 본연의 맛
    def __init__(self):
        self.name = '보쌈'
        self.src = './image/보쌈.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 1
        self.spicy = 1

class makchang: # 25: 한식, 본연의 맛
    def __init__(self):
        self.name = '막창'
        self.src = './image/막창.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class ganjang_gejang: # 26: 한식, 짠 맛, 본연의 맛
    def __init__(self):
        self.name = '간장게장'
        self.src = './image/간장게장.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 1
        self.spicy = 0

class chicken_foot: # 27: 한식, 짠 맛, 매운 맛
    def __init__(self):
        self.name = '닭발'
        self.src = './image/닭발.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 1

class smoked_pork_belly: # 28: 한식, 본연의 맛
    def __init__(self):
        self.name = '훈제삼겹살'
        self.src = './image/훈제삼겹살.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class doenjang_stew: # 28: 한식, 본연의 맛
    def __init__(self):
        self.name = '된장찌개'
        self.src = './image/된장찌개.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class stir_fried_spicy_pork: # 29: 한식, 단 맛, 짠 맛, 본연의 맛, 매운 맛
    def __init__(self):
        self.name = '제육볶음'
        self.src = './image/제육볶음.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 1
        self.spicy = 1

class barbecue_pork_ribs: # 30: 양식, 단 맛, 짠 맛
    def __init__(self):
        self.name = '바베큐 폭립'
        self.src = './image/바베큐 폭립.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 1
        self.korean = 0
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 0

class buldak_stirfried_noodles: # 31: 한식, 매운 맛
    def __init__(self):
        self.name = '불닭볶음면'
        self.src = './image/불닭볶음면.jpg
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 0
        self.spicy = 1

class beef_tadaki: # 32: 일식, 본연의 맛
    def __init__(self):
        self.name = '소고기타다끼'
        self.src = './image/소고기타다끼.jpg'
        self.chinese = 0
        self.japanese = 1
        self.western = 0
        self.korean = 0
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class hamburger: # 33: 양식, 패스트 푸드, 단 맛, 짠 맛, 신 맛, 매운 맛
    def __init__(self):
        self.name = '햄버거'
        self.src = './image/햄버거.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 1
        self.korean = 0
        self.fastfood = 1
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 1
        self.original = 0
        self.spicy = 1

class pork_backbone_hangover_soup: # 34: 한식, 짠 맛, 매운 맛
    def __init__(self):
        self.name = '뼈다귀 해장국'
        self.src = './image/뼈다귀 해장국.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 1

class sundae_and_rice_soup: # 35: 한식, 짠 맛
    def __init__(self):
        self.name = '순대국밥'
        self.src = './image/순대국밥.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 0

class spicy_stir_fried_chicken: # 36: 한식, 단 맛, 짠 맛, 매운 맛
    def __init__(self):
        self.name = '닭갈비'
        self.src = './image/닭갈비.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 1

class grilled_lobster_butter: # 37: 양식, 단 맛, 짠 맛, 본연의 맛
    def __init__(self):
        self.name = '랍스터 버터구이'
        self.src = './image/랍스터 바터구이.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 1
        self.korean = 0
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 1
        self.spicy = 0

class dakgangjeong: # 38: 한식, 단 맛, 짠 맛, 매운 맛
    def __init__(self):
        self.name = '닭강정'
        self.src = './image/닭강정.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 1

class boiled_pork_slice_and_rice_soup: # 39: 한식, 짠 맛, 본연의 맛, 매운 맛
    def __init__(self):
        self.name = '수육 국밥'
        self.src = './image/수육 국밥.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 1
        self.spicy = 1

class beef_brisket: # 40: 한식, 본연의 맛
    def __init__(self):
        self.name = '차돌박이'
        self.src = './image/차돌박이.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class skirtmeat: # 41: 한식, 본연의 맛
    def __init__(self):
        self.name = '갈매기살'
        self.src = './image/갈매기살.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class braised_galbi: # 42: 한식, 단 맛, 짠 맛, 본연의 맛
    def __init__(self):
        self.name = '소갈비찜'
        self.src = './image/소갈비찜.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 1
        self.spicy = 0

class smoked_salmon_rice: # 43: 한식, 본연의 맛
    def __init__(self):
        self.name = '훈제연어 덮밥'
        self.src = './image/훈제연어 덮밥.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 1
        self.spicy = 0

class pizza: # 44: 양식, 단 맛, 짠 맛, 신 맛, 매운 맛
    def __init__(self):
        self.name = '피자'
        self.src = './image/피자.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 1
        self.korean = 0
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 1
        self.original = 0
        self.spicy = 1

class braised_chicken: # 45: 한식, 단 맛, 짠 맛, 매운 맛
    def __init__(self):
        self.name = '찜닭'
        self.src = './image/찜닭.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 1

class lamb_chops: # 46: 양식, 본연의 맛
    def __init__(self):
        self.name = '양갈비'
        self.src = './image/양갈비.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 1
        self.korean = 0
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class lamb_skewers: # 47: 중식, 본연의 맛
    def __init__(self):
        self.name = '양꼬치'
        self.src = './image/양꼬치.jpg'
        self.chinese = 1
        self.japanese = 0
        self.western = 0
        self.korean = 0
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class galbitang: # 48: 한식, 본연의 맛
    def __init__(self):
        self.name = '갈비탕'
        self.src = './image/갈비탕.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 0
        self.sour = 0
        self.original = 1
        self.spicy = 0

class broiled_eels: # 49: 중식, 일식, 양식, 한식, 단 맛, 짠 맛, 본연의 맛
    def __init__(self):
        self.name = '장어 구이'
        self.src = './image/장어 구이.jpg'
        self.chinese = 1
        self.japanese = 1
        self.western = 1
        self.korean = 1
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 1
        self.spicy = 0

class pork_cutlet: # 50: 일식, 양식, 짠 맛, 신 맛
    def __init__(self):
        self.name = '돈까스'
        self.src = './image/돈까스.jpg'
        self.chinese = 0
        self.japanese = 1
        self.western = 1
        self.korean = 0
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 1
        self.original = 0
        self.spicy = 0

class noodle_soup_with_seafood: # 51: 한식, 짠 맛, 본연의 맛
    def __init__(self):
        self.name = '해물칼국수'
        self.src = './image/해물칼국수.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 1
        self.spicy = 0

class spicy_braised_chicken: # 52: 한식, 단 맛, 짠 맛, 매운 맛
    def __init__(self):
        self.name = '닭도리탕'
        self.src = './image/닭도리탕.jpg'
        self.chinese = 0
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 1
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 1

class chapagetti: # 53: 중식, 한식, 패스트푸드, 짠 맛
    def __init__(self):
        self.name = '짜파게티'
        self.src = './image/짜파게티.jpg'
        self.chinese = 1
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 1
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 0

class jajangmyeon: # 54: 중식, 짠 맛
    def __init__(self):
        self.name = '짜장면'
        self.src = './image/짜장면.jpg'
        self.chinese = 1
        self.japanese = 0
        self.western = 0
        self.korean = 1
        self.fastfood = 0
        self.sweet = 0
        self.bitter = 0
        self.salty = 1
        self.sour = 0
        self.original = 0
        self.spicy = 0
