"""
Basic example of a Trading bot with a strategy pattern.
"""
import statistics
from dataclasses import dataclass
from typing import Callable

from exchange import Exchange

TradingStrategyFunction = Callable[[list[int]], bool]

# create fn that returns TradingStratergyFn and pass parameters to that fn 
# that passes parameters to closure it creates and return fn use in trading stratergy
# fn return is still a function that uses list of prices. Closure fn gets extra parameters
def should_buy_avg_closure(window_size: int) -> TradingStrategyFunction:
    def should_buy_avg(prices: list[int]) -> bool:
        list_window = prices[-window_size:]
        return prices[-1] < statistics.mean(list_window)

    return should_buy_avg


def should_sell_avg_closure(window_size: int) -> TradingStrategyFunction:
    def should_sell_avg(prices: list[int]) -> bool:
        list_window = prices[-window_size:]
        return prices[-1] > statistics.mean(list_window)

    return should_sell_avg


def should_buy_minmax_closure(max_price: int) -> TradingStrategyFunction:
    def should_buy_minmax(prices: list[int]) -> bool:
        # buy if it's below the max price
        return prices[-1] < max_price

    return should_buy_minmax


def should_sell_minmax_closure(min_price: int) -> TradingStrategyFunction:
    def should_sell_minmax(prices: list[int]) -> bool:
        # sell if it's above the min price
        return prices[-1] > min_price

    return should_sell_minmax


@dataclass
class TradingBot:
    """Trading bot that connects to a crypto exchange and performs trades."""

    exchange: Exchange
    buy_strategy: TradingStrategyFunction
    sell_strategy: TradingStrategyFunction

    def run(self, symbol: str) -> None:
        prices = self.exchange.get_market_data(symbol)
        if self.buy_strategy(prices):
            self.exchange.buy(symbol, 10)
        elif self.sell_strategy(prices):
            self.exchange.sell(symbol, 10)
        else:
            print(f"No action needed for {symbol}.")


def main() -> None:
    # create the exchange and connect to it
    exchange = Exchange()
    exchange.connect()

    # create the trading bot and run the bot once
    bot = TradingBot(
        exchange,
        should_buy_minmax_closure(max_price=32_000),
        should_sell_minmax_closure(min_price=38_000),
    )
    bot.run("BTC/USD")


if __name__ == "__main__":
    main()
