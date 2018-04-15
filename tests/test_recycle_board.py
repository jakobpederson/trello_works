import logging
import logging.config
from trello import TrelloClient
from random import randint
from unittest import TestCase

from scripts.recycle_board import RecycleBoard
from scripts.tokens import API_KEY, API_TOKEN


class RecycleBoardTests(TestCase):

    @classmethod
    def setUpClass(cls):
        logging.config.dictConfig({"version": 1, "loggers": {"requests": {"level": "INFO"}}})

    def setUp(self):
        self.client = TrelloClient(api_key=API_KEY, token=API_TOKEN)
        self.org = self.client.get_organization('deletetheseboards')
        for board in self.org.get_boards(list_filter='open'):
            board.close()
        recycler = RecycleBoard(API_KEY, API_TOKEN, org_id='deletetheseboards')
        self.name = 'NEW BOARD {}'.format(randint(0, 1000))
        self.recycled_board = recycler.recycle_board(self.name)

    def tearDown(self):
        if self.recycled_board:
            self.recycled_board.close()

    def test_name_change(self):
        self.assertEqual(self.recycled_board.name, self.name)

    def test_cards_deleted(self):
        self.assertCountEqual(self.recycled_board.open_cards(), [])
