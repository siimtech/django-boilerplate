from enum import Enum

class PaymentMethodEnum(Enum):
    계좌입금 = ('01', '계좌입금')
    신용카드 = ('02', '신용카드')
    현금 = ('03', '현금')
    기타 = ('04', '기타')

    @classmethod
    def choices(cls):
        return [(item.value[0], item.value[1]) for item in cls]
    
