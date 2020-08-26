from django.db import models


class Ticker(models.Model):
    class TickerType(models.TextChoices):
        STOCK = "stk", "주식"
        ETF = "etf", "ETF"
        FUTURE = "ftr", "선물"

    symbol = models.CharField(max_length=30, null=True, blank=True)
    is_deprecated = models.BooleanField(default=False)
    # TODO: choices 추가하기
    locale = models.CharField(max_length=20)
    # TODO: choices 추가하기
    market_name = models.CharField(max_length=30)
    ticker_type = models.CharField(
        max_length=3, choices=TickerType.choices, default=TickerType.STOCK
    )
