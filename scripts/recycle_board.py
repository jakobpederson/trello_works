from trello import TrelloClient


class RecycleBoard():

    def __init__(self, API_KEY, API_TOKEN):
        self.client = TrelloClient(api_key=API_KEY, token=API_TOKEN)
        self.closed_boards = self.client.list_boards(board_filter='closed')

    def recycle_board(self, name):
        print('hi')
        closed_board_gen = self.get_closed_board()
        old_board = closed_board_gen.__next__()
        print(old_board.name)
        return

    def get_closed_board(self):
        for board in self.closed_boards:
            yield board
