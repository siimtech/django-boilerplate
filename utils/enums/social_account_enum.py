from enum import Enum

class SocialAccountEnum(Enum):
    kakao = '카카오'
    naver = '네이버'
    apple = '애플'

    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]
