# Updated from master based on API v3 updates
# https://www.mercadobitcoin.com.br/api-doc/
# **some code structure was changed to allow for easier updates and modeled after Geminipy

import requests


class Base(object):
    """
    Base API class

    This only includes data, not trades
    """

    def __init__(self):
        self.base_url = "https://www.mercadobitcoin.net"
        self.api_url = "{}/api".format(self.base_url)


class Api(Base):
    """market data"""

    def ticker(self, coin):
        """
        Returns information with the summary of the last 24 hours of negotiations.

        :param coin: digital currency symbol
        :return:
        high: Highest unit price of the last 24 hours.
        Type: Decimal

        low:  Lowest unit price of the last 24 hours.
        Type: Decimal

        vol:  Quantity traded in the last 24 hours.
        Type: Decimal

        last: Unit price of the last negotiation.
        Type: Decimal

        buy:  The highest purchase bid price of the last 24 hours.
        Type: Decimal

        sell: Lowest offer price for the last 24 hours.
        Type: Decimal

        date: Date and time of information in Era Unix
        Type: Integer
        """
        url = "{}/{}/ticker".format(self.api_url, coin)

        return requests.get(url)

    def orderbook(self, coin):
        """
        Book of offers consists of two lists:
        (1) a list with purchase offers ordered by the highest value;
        (2) a list of sales offers ordered by the lowest value. The book shows up to 1000 purchase offers and up to 1000 sales offers.

        :param coin: digital currency symbol
        :return:
        bids: List of shopping offers, sorted from highest to lowest price.
        Type: Array
            [0]: Unit price of the purchase offer.
            Type: Decimal

            [1]: Quantity of the purchase offer.
            Type: Decimal

        asks: List of sale offers, sorted from lowest to highest price.
        Type: Array
            [0]: Unit price of the sale offer.
            Type: Decimal

            [1]: Quantity of the sale offer.
            Type: Decimal
        """
        url = "{}/{}/orderbook".format(self.api_url, coin)

        return requests.get(url)

    def trades(self, coin, since=None, from_unix=None, to_unix=None):
        """
        History of negotiations

        :param coin: digital currency symbol
        :param since: trade id, returns up to 1000 trades since the id of this trade
        :param from_unix: returns up to 1000 trades from the date entered
        :param to_unix: used with from to query an interval
        :return:
        []: List of negotiations carried out.
        date: Date and time of trading in Era Unix
        Type: Decimal

        price: Unit price of the negotiation.
        Type: Decimal

        amount: Quantity of the negotiation.
        Type: Decimal

        tid: Identifier of the negotiation.
        Type: Integer

        type: Indicates the executing point of the negotiation
        Type: String
            Data Domain:
            buy: indicates purchase order execora
            sell: indicates executor sales order

        NOTE: this either takes (since) or (from) or (from & to) as parameters.  Other combinations not allowed
        """
        if since is not None:
            url = "{}/{}/trades".format(self.api_url, coin)
            params = {
                'since': since
            }

            return requests.get(url, params)

        elif from_unix is not None:
            if to_unix is not None:  # create request with from and to
                url = "{}/{}/trades/{}/{}/".format(self.api_url, coin, from_unix, to_unix)

                return requests.get(url)

            else:  # create request with just from
                url = "{}/{}/trades/{}/".format(self.api_url, coin, from_unix)
                return requests.get(url)

        else:  # create request with no optional parameters
            url = "{}/{}/trades/".format(self.api_url, coin)

            return requests.get(url)

    def day_summary(self, coin, year, month, day):
        """
        Returns daily summary of trades made

        :param coin: digital currency symbol
        :param year: year of day summary
        :param month: month of day summary.  No leading zero needed.
        :param day: day of day summary.  No leading zero needed
        :return:
        date: Daily summary date
        Type: String
        Format: YYYY-MM-DD, example: 2013-06-20

        opening: Trading unit opening price on the day.
        Type: Decimal

        closing: Unit price closing trading day.
        Type: Decimal

        lowest: Lowest unit price of trading on the day.
        Type: Decimal

        highest: Higher unit price trading on the day.
        Type: Decimal

        volume: Volume of Reais (BRL) traded on the day.
        Type: Decimal

        quantity: Quantity of digital currency traded on the day.
        Type: Decimal

        amount: Number of trades made on the day.
        Type: Integer

        avg_price: Average unit price of the trades on the day.
        Type: Decimal
        """

        url = "{}/{}/day-summary/{}/{}/{}/".format(self.api_url, coin, year, month, day)

        return requests.get(url)
