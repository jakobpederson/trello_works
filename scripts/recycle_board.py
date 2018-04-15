from trello import TrelloClient


class RecycleBoard():

    def __init__(self, API_KEY, API_TOKEN, org_id=None):
        self.client = TrelloClient(api_key=API_KEY, token=API_TOKEN)
        self.org = self.client.get_organization(org_id) if org_id else None
        self.closed_board_gen = self.get_closed_board()
        self.board = self.closed_board_gen.__next__()

    def recycle_board(self, name):
        self.board.open()
        self.delete_cards()
        self.board.set_name(name)
        return self.board

    def delete_cards(self):
        for card in self.board.open_cards():
            card.delete()

    def get_closed_board(self):
        get_boards = (self.org.get_boards, self.client.list_boards)
        if self.org:
            for board in get_boards[0](list_filter='closed'):
                yield board
        for board in get_boards[1](board_filter='closed'):
            yield board
