import unittest
from laba6 import find_unreachable_cities

class TestGasSupply(unittest.TestCase):
    def test_all_reachable(self):
        cities = ["Львів", "Стрий"]
        storages = ["Сховище_1"]
        pipelines = [["Сховище_1", "Львів"], ["Львів", "Стрий"]]
        # Всі міста мають бути досяжні
        self.assertEqual(find_unreachable_cities(cities, storages, pipelines), [])

    def test_some_unreachable(self):
        cities = ["Львів", "Стрий", "Долина"]
        storages = ["Сховище_1"]
        pipelines = [["Сховище_1", "Львів"]]
        # Стрий та Долина не мають газу
        expected = [["Сховище_1", ["Стрий", "Долина"]]]
        self.assertEqual(find_unreachable_cities(cities, storages, pipelines), expected)

    def test_empty_pipelines(self):
        cities = ["Львів"]
        storages = ["Сховище_1"]
        pipelines = []
        expected = [["Сховище_1", ["Львів"]]]
        self.assertEqual(find_unreachable_cities(cities, storages, pipelines), expected)

if __name__ == "__main__":
    unittest.main()
