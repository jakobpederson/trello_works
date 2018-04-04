import logging
import logging.config
from trello import TrelloClient
from unittest import TestCase

from scripts.recycle_board import RecycleBoard
from scripts.tokens import API_KEY, API_TOKEN


class RecycleBoardTests(TestCase):

    @classmethod
    def setUpClass(cls):
        logging.config.dictConfig({"version": 1, "loggers": {"requests": {"level": "INFO"}}})

    def test_x(self):
        self.client = TrelloClient(api_key=API_KEY, token=API_TOKEN)
        recycler = RecycleBoard(API_KEY, API_TOKEN)
        expected = len(self.client.list_boards(board_filter='closed')) - 1
        print(expected)
        self.fail('x')

        # expected = len(self.client.list_boards(board_filter='closed')) - 1
        # recycler = RecycleBoard(API_KEY, API_TOKEN)
        # recycler.recycle_board('test_board')
        # result = len(self.client.list_boards(board_filter='closed'))
        # self.assertEqual(expected, result)
