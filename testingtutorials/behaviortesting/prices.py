import json
from abc import abstractmethod, ABC
from typing import List

from pymemcache.client.base import Client
import redis


class Memcache:
    def __init__(self):
        self._client = Client(('localhost', 11211))

    def prices(self) -> List[float]:
        """
        Prices returns an array of all prices in the system.

        :return:
        """
        # makes call to memcached...
        return json.loads(self._client.get('prices'))


class Redis:
    def __init__(self):
        self._client = redis.StrictRedis()

    def prices(self) -> List[float]:
        """
        Prices returns an array of all prices in the system.

        :return:
        """
        # makes call to redis...
        return self._client.lrange('prices', 0, -1)


class PriceAnalytics_Redis:
    def __init__(self):
        self.redis = Redis()

    def avg_price(self) -> float:
        prices = self.redis.prices()
        return sum(prices) / float(len(prices))


class PriceAnalytics_MigrateMemcache:
    def __init__(self):
        self.memcache = Memcache()

    def avg_price(self) -> float:
        prices = self.memcache.prices()
        return sum(prices) / float(len(prices))


class Datasource(ABC):
    @abstractmethod
    def prices(self) -> List[float]:
        pass


class PriceAnalyticsEvolvable:
    def __init__(self, datasource: Datasource):
        self.datasource = datasource

    def avg_price(self) -> float:
        prices = self.datasource.prices()
        return sum(prices) / float(len(prices))

