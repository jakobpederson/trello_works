from unittest import TestCase

from scripts.board_builder import BoardBuilder


class BoardBuilderTests(TestCase):

    def setUp(self):
        self.master_board = DummyBoard('Q1 master_board')
        self.builder = BoardBuilder(self.master_board)
        self.boards = []
        for i in range(0, 3):
            self.master_board.add_list('List {}'.format(i))
            self.boards.append(DummyBoard('List {}'.format(i)))

    def test_get_board_that_matches_list(self):
        test_board = self.builder.get_matching_board('List 2', self.boards)
        self.assertEqual(test_board.name, 'List 2')


class DummyBoard():

    def __init__(self, name):
        self.name = name
        self.trello_lists = []

    def add_list(self, name):
        self.trello_lists.append(DummyList(name))

    def open_lists(self):
        return self.trello_lists


class DummyList():

    def __init__(self, name):
        self.name = name
