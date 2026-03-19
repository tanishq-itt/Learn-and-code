from models.creator import Creator
from strategies.ad_strategy import AdStrategy
from strategies.subscription_strategy import SubscriptionStrategy
from strategies.brand_strategy import BrandStrategy
from strategies.live_gift_strategy import LiveGiftStrategy


def main():
    creator = Creator("Tanishq", views=10000, subscribers=500, base_amount=2000)

    creator.add_strategy(AdStrategy())
    creator.add_strategy(SubscriptionStrategy())
    creator.add_strategy(BrandStrategy())
    creator.add_strategy(LiveGiftStrategy(500))

    creator.display()


if __name__ == "__main__":
    main()