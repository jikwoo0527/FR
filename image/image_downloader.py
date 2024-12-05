import requests

class pork_belly: # 1: 한식, 본연의 맛
    def __init__(self):
        self.name = '삼겹살'
        self.src = 'https://i.namu.wiki/i/oFHlYDjoEh8f-cc3lNK9jAemRkbXxNGwUg7XiW5LGS6DF1P2x8GCeNQxbQhVIwtUS1u53YPw-uoyqpmLtrGNJA.webp'
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
        self.src = 'https://cdn.mindgil.com/news/photo/202111/72857_11039_5046.jpg'
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
        self.src = 'https://ecimg.cafe24img.com/pg242b54296577026/sk44166/web/product/big/20240218/1d1d2ec27c0b3eac21bbf5bddd738f31.jpg'
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
        self.src = 'https://www.sbfoods-worldwide.com/ko/recipes/deq4os00000008l9-img/10_Stake_A.jpg'
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
        self.src = 'https://cdn.oasis.co.kr:48581/product/83209/thumb/e8d700f0-6acb-4bad-b1a9-c5f4f1a2312e.jpg'
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
        self.src = 'https://www.bhc.co.kr/upload/bhc/menu/%ED%95%AB%ED%9B%84%EB%9D%BC%EC%9D%B4%EB%93%9C-%EC%8A%A4%ED%8B%B1_410x271.png'
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
        self.src = 'https://www.saenong.com/assets/upload/detailimage1/20230511_9667730266924.jpg'
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
        self.src = 'https://i.namu.wiki/i/8s7OaNPsZ8KC1e8RQ6QZEwgfFUoIVVOIm0jA72-UO6Imw0OgI1aEK_DulMeXWbg4tstts3IQFMJS0jmYKD9rzQ.webp'
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
        self.src = 'https://i.namu.wiki/i/8drgvI-cQLUfJDC00zbl2ZolK4W3o4ZkVSpR-zM5FZk_QzT58vYnx_7ohk0qwGYYiSLPiZgwccyIEFUtYKDjUQ.webp'
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
        self.src = 'https://www.hyun-deok.com/data/goods/1/2023/03/39_temp_16798979884045view.png'
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
        self.src = 'https://recipe1.ezmember.co.kr/cache/recipe/2023/02/24/e91f8889c788b5a5b30ed4f09599fc411.jpg'
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
        self.src = 'https://img.shoppingntmall.com/goods/200/12137200_h.jpg'
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
        self.src = 'https://d12zq4w4guyljn.cloudfront.net/750_750_20240712093427_photo2_4b53c8b60da4.jpg'
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
        self.src = 'https://recipe1.ezmember.co.kr/cache/recipe/2018/11/06/174f3f62b1b602520845eef94b35de3a1.jpg'
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
        self.src = 'https://lh4.googleusercontent.com/proxy/jlGlFTQudU3GbsigA1tK687GxPZEFRW0KGP8gLMLautPf9JxVmXJibiaTKw8X53Krvilh9yJdtyYjKTJW5VcWU5VXgDmJDR4ZfgFFaPk3xvr'
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
        self.src = 'https://mblogthumb-phinf.pstatic.net/MjAyMDA0MTNfMTEw/MDAxNTg2Nzc3NDYyNDM5.I57eOPQd7OGh1uIEeSWPTyDmlscEjDNyOfcToP0O0dgg.c5YdQkbDxwSEHjgL_fJhHiBV0ZcbzGov9YqW4B15jJUg.PNG.kizaki56/09.png?type=w800'
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
        self.src = 'https://lh5.googleusercontent.com/proxy/hG-R2f3Zkk3aGB61XOkDSuMJ4fWWReTA1R4YmYUmHvFE5baW8qltpIMVLeJ19IOXcLuTgvg_PaUb4hIHTZBxJy9IO8XfFQ'
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

class grilled_galbi: # 18: 한식, 단 맛, 짠 맛 - 이미지 다운시 오류
    def __init__(self):
        self.name = '소갈비'
        self.src = 'https://chosunhwarojib.com/upload/menu_01/2020_03_24/hero_TVsHi_2020_03_24_12_58_57.jpg'
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
        self.src = 'https://recipe1.ezmember.co.kr/cache/board/2014/02/20/11761da5217b44ab0bbcd4b09acfacf9.jpg'
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
        self.src = 'https://cdn.011st.com/11dims/resize/600x600/quality/75/11src/product/5727967374/B.jpg?908000000'
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
        self.src = 'https://recipe1.ezmember.co.kr/cache/recipe/2023/08/26/41eb2344b4e6a719c209ca55ed91c3f31.jpg'
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
        self.src = 'https://image.utoimage.com/preview/cp871385/2019/02/201902010294_500.jpg'
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
        self.src = 'https://cdn.imweb.me/thumbnail/20210923/11799350a5b66.jpg'
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
        self.src = 'https://modo-phinf.pstatic.net/20150917_218/1442473505803E1WCR_JPEG/mosaONxp7p.jpeg?type=w720'
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
        self.src = 'https://oasisprodproduct.edge.naverncp.com/80339/detail/0_7ff75038-b755-4398-ad45-39e036250b67.jpg'
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
        self.src = 'https://cdn.oasis.co.kr:48581/product/56225/thumb/thumb_56225ea164b39-a92b-43cc-87c3-eef0c19fe84e.jpg'
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
        self.src = 'https://i.namu.wiki/i/tzA654thy3GWQmlD9R-iyC3wFX_Dy8UvI1goaauMhmaeYgIiG9f9BY0nTN3gpLKuCiOke5UKUusas55jlIkBSw.webp'
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
        self.src = 'https://image.8dogam.com/resized/product/asset/v1/upload/7f9f95b0a8504bd7a8c44cb7e375e4e5.jpeg?type=big&res=2x&ext=jpg'
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
        self.src = 'https://mealkit101.com/cdn/shop/files/2020-08-24_42785455210_434x.png?v=1731284781'
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
        self.src = 'https://i.ytimg.com/vi/aenoy50ea-s/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDBo72mS5KwzGx9vyzNjhYjspLpVQ'
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

class barbecue_pork_ribs: # 30: 양식, 단 맛, 짠 맛 - 이미지 다운시 오류
    def __init__(self):
        self.name = '바베큐 폭립'
        self.src = 'https://m.tamyook.com/web/product/big/202204/9b6951dc357b3aee116483d4fe365925.png'
        self.src = 'https://m.tamyook.com/web/product/big/202204/9b6951dc357b3aee116483d4fe365925.png'
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
        self.src = 'https://cdn.iconsumer.or.kr/news/photo/202108/20714_23857_244.jpg'
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
        self.src = 'https://ai.esmplus.com/foodjang01/images/221406894_b_1.jpg'
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
        self.src = 'https://health.chosun.com/site/data/img_dir/2024/04/19/2024041901914_0.jpg'
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

class hamburger: # 33: 양식, 패스트 푸드, 단 맛, 짠 맛, 신 맛, 매운 맛
    def __init__(self):
        self.name = '햄버거'
        self.src = 'https://health.chosun.com/site/data/img_dir/2024/04/19/2024041901914_0.jpg'
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
        self.src = 'https://dn.joongdo.co.kr/mnt/images/file/2019y/08m/22d/2019082201001894200082461.jpg'
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
        self.src = 'https://sitem.ssgcdn.com/80/49/02/item/1000059024980_i1_750.jpg'
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
        self.src = 'https://d12zq4w4guyljn.cloudfront.net/750_750_20230527011034330_photo_5ffea3357f5f.jpg'
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
        self.src = 'https://image.utoimage.com/preview/cp871385/2019/04/201904012495_500.jpg'
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
        self.src = 'https://gwchild114.firstmall.kr/data/goods/1/2021/06/42953_tmp_166ec1bc70603d22f90bcb81e357a33d3084large.png'
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
        self.src = 'https://content.foodspring.co.kr/vendor/1354/images/49_8666176726_r.png'
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
        self.src = 'https://ws.cconma.com/Upload/Product/400x350/2013/12/04/4307523349.jpg'
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
        self.src = 'https://static.megamart.com/product/image/0382/03825211/03825211_1_960.jpg'
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
        self.src = 'https://kurlylog-img.kurly.com/recipe/beef-rib-soup-golden-recipe-step-0.jpg'
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
        self.src = 'https://mblogthumb-phinf.pstatic.net/MjAyMzA2MDFfMTc1/MDAxNjg1NTQ1OTAxOTAz.fN3S1jjHBLMUNivrxdXyBe4vBCN1rOzlC6wKLY48kA0g.oM7vZ9SanT8oszeAqmNTBx9BObrBlyI-fw59Zgk7Z2Mg.JPEG.bhl1960/20230531_131325.jpg?type=w800'
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
        self.src = 'https://i.namu.wiki/i/umI-heVYVS9miQNqXM13FRUOHHL4l1nzsZgN9XRLFG7nI_7Dyf-Myr6HmiWf9Qd7SAZQz3WYSQHPXXtGAwLTag.webp'
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
        self.src = 'https://cdn.oasis.co.kr:48581/product/54180/thumb/thumb_5418003341f82-82f8-4da9-94f7-6b30daf0f57d.jpg'
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
        self.src = 'https://image.hnsmall.com/images/goods/794/19783794_g.jpg'
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
        self.src = 'https://dimg.donga.com/wps/NEWS/IMAGE/2023/07/17/120279505.2.jpg'
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
        self.src = 'https://cdnweb01.wikitree.co.kr/webdata/editor/202012/01/img_20201201124407_672e1b16.webp'
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
        self.src = 'https://cafe24.poxo.com/ec01/dangjinshop/jNWAR67N/rbqGfE/mXzgXbeFphX0Sg4dA2NR6qHgmw6gHdAY6JjC3P6QxLEKFUMT/pVQ7Sne2458vz8e7/FyiA==/_/web/product/big/202407/edd270ada223bf112684e8859768dd86.jpg'
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
        self.src = 'https://sitem.ssgcdn.com/30/16/69/item/1000063691630_i2_750.jpg'
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

class noodle_soup_with_seafood: # 51: 한식, 짠 맛, 본연의 맛 - 이미지 다운시 오류
    def __init__(self):
        self.name = '해물칼국수'
        self.src = 'https://www.sk5.co.kr/img_src/s600/1220//12200287.jpg'
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
        self.src = 'https://sitem.ssgcdn.com/08/65/44/item/1000528446508_i1_750.jpg'
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
        self.src = 'https://recipe1.ezmember.co.kr/cache/recipe/2023/12/27/c2752c0bf2159e59cde761d5fd8707731.jpg'
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
        self.src = 'https://image.thebanchan.co.kr/dwmall/static_root/model_img/main/783/78316_1_a.jpg'
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

# class 변수 선언
pork_belly = pork_belly() # 1
sushi = sushi() # 2
sashimi = sashimi() # 3
steak = steak() # 4
skinon_pork_belly = skinon_pork_belly() # 5
fried_chicken = fried_chicken() # 6
pork_ribs = pork_ribs() # 7
ramen = ramen() # 8
kimchi_stew = kimchi_stew() # 9
beef_tartare = beef_tartare() # 10
braised_pork_galbi_and_kimchi = braised_pork_galbi_and_kimchi() # 11
tteokbokki = tteokbokki() # 12
beef_intestines = beef_intestines() # 13
shabu_shabu = shabu_shabu() # 14
gamjatang = gamjatang() # 15
seasoned_spicy_chicken = seasoned_spicy_chicken() # 16
pork_and_ricesoup = pork_and_ricesoup() # 17
grilled_galbi = grilled_galbi() # 18
steamed_snow_crab = steamed_snow_crab() # 19
grilled_pork_neck = grilled_pork_neck() # 20
kimchi_fried_rice = kimchi_fried_rice() # 21
steamed_kingcrab = steamed_kingcrab() # 22
budaejjigae = budaejjigae() # 23
bossam = bossam() # 24
makchang = makchang() # 25
ganjang_gejang = ganjang_gejang() # 26
chicken_foot = chicken_foot() # 27
smoked_pork_belly = smoked_pork_belly() # 28
stir_fried_spicy_pork = stir_fried_spicy_pork() # 29
barbecue_pork_ribs = barbecue_pork_ribs() # 30
buldak_stirfried_noodles = buldak_stirfried_noodles() # 31
beef_tadaki = beef_tadaki() # 32
hamburger = hamburger() # 33
pork_backbone_hangover_soup = pork_backbone_hangover_soup() # 34
sundae_and_rice_soup = sundae_and_rice_soup() # 35
spicy_stir_fried_chicken = spicy_stir_fried_chicken() # 36
grilled_lobster_butter = grilled_lobster_butter() # 37
dakgangjeong = dakgangjeong() # 38
boiled_pork_slice_and_rice_soup = boiled_pork_slice_and_rice_soup() # 39
beef_brisket = beef_brisket() # 40
skirtmeat = skirtmeat() # 41
braised_galbi = braised_galbi() # 42
smoked_salmon_rice = smoked_salmon_rice() # 43
pizza = pizza() # 44
braised_chicken = braised_chicken() # 45
lamb_chops = lamb_chops() # 46
lamb_skewers = lamb_skewers() # 47
galbitang = galbitang() # 48
broiled_eels = broiled_eels() # 49
pork_cutlet = pork_cutlet() # 50
noodle_soup_with_seafood = noodle_soup_with_seafood() # 51
spicy_braised_chicken = spicy_braised_chicken() # 52
chapagetti = chapagetti() # 53
jajangmyeon = jajangmyeon() # 54



food_eng = [
    "pork_belly", "sushi", "sashimi", "steak", "skinon_pork_belly",
    "fried_chicken", "pork_ribs", "ramen", "kimchi_stew", "beef_tartare",
    "braised_pork_galbi_and_kimchi", "tteokbokki", "beef_intestines",
    "shabu_shabu", "gamjatang", "seasoned_spicy_chicken",
    "pork_and_ricesoup", "grilled_galbi", "steamed_snow_crab",
    "grilled_pork_neck", "kimchi_fried_rice", "steamed_kingcrab",
    "budaejjigae", "bossam", "makchang", "ganjang_gejang",
    "chicken_foot", "smoked_pork_belly", "stir_fried_spicy_pork",
    "barbecue_pork_ribs", "buldak_stirfried_noodles", "beef_tadaki",
    "hamburger", "pork_backbone_hangover_soup", "sundae_and_rice_soup",
    "spicy_stir_fried_chicken", "grilled_lobster_butter",
    "dakgangjeong", "boiled_pork_slice_and_rice_soup", "beef_brisket",
    "skirtmeat", "braised_galbi", "smoked_salmon_rice", "pizza",
    "braised_chicken", "lamb_chops", "lamb_skewers", "galbitang",
    "broiled_eels", "pork_cutlet", "noodle_soup_with_seafood",
    "spicy_braised_chicken", "chapagetti", "jajangmyeon"
]




def download_image(image_url, save_path):
    """
    인터넷에서 이미지를 다운로드하여 로컬에 저장하는 함수.

    Args:
        image_url (str): 다운로드할 이미지의 URL
        save_path (str): 저장할 파일 경로 (예: 'image.jpg')

    Returns:
        bool: 성공적으로 저장되었으면 True, 아니면 False
    """
    try:
        # 이미지 데이터를 요청
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # 요청 실패 시 예외 발생

        # 바이너리 데이터를 파일로 저장
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):  # 1KB 단위로 저장
                file.write(chunk)

        print(f"이미지가 성공적으로 저장되었습니다: {save_path}")
        return True
    except Exception as e:
        print(f"이미지 다운로드 중 오류 발생: {e}")
        return False


# 사용 예제
i = 0
for food_name in food_eng:
    cls = globals()[food_name]
    image_url = cls.src
    save_path = cls.name + '.jpg'  # 저장할 파일 이름을 지정
    download_image(image_url, save_path)
