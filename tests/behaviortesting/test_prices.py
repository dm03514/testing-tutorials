import unittest
from unittest.mock import patch, MagicMock
from testingtutorials.behaviortesting.prices import PriceAnalytics_Redis, PriceAnalyticsEvolvable, \
    PriceAnalytics_MigrateMemcache


class PriceAnalytics_Redis_TestCase(unittest.TestCase):

    @patch('testingtutorials.behaviortesting.prices.Redis')
    def test_avg_price_success(self, mock_redis):
        redis_instance = mock_redis.return_value
        redis_instance.prices.return_value = [1, 1]

        analytics = PriceAnalytics_Redis()

        self.assertEqual(
            1,
            analytics.avg_price(),
        )

        redis_instance.prices.assert_called_once()


class PriceAnalytics_MigrateMemcache_TestCase(unittest.TestCase):

    @patch('testingtutorials.behaviortesting.prices.Redis')
    def test_avg_price_success(self, mock_redis):
        redis_instance = mock_redis.return_value
        redis_instance.prices.return_value = [1, 1]

        analytics = PriceAnalytics_MigrateMemcache()

        self.assertEqual(
            1,
            analytics.avg_price(),
        )

        redis_instance.prices.assert_called_once()


class PriceAnalyticsEvolvableTestCase(unittest.TestCase):

    def test_avg_price_success(self):
        ds = MagicMock(
            prices=MagicMock(
                return_value=[1, 1]
            )
        )

        analytics = PriceAnalyticsEvolvable(
            datasource=ds
        )

        self.assertEqual(
            1,
            analytics.avg_price(),
        )
