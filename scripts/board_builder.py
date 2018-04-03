from trello import TrelloClient


class BoardBuilder():


    def __init__(self, source):
        self.source = source
        self.open_lists = source.open_lists()

    def build_boards(self, organization_id=None):
        permission_level = 'org' if organization_id else None
        new_boards = [
            self.client.add_board(
                trello_list.name,
                organization_id=organization_id,
                permission_level=permission_level
            ) for trello_list in self.open_lists
        ]
        return new_boards

    def get_matching_board(self, trello_list_name, new_boards):
        for board in new_boards:
            print(board.name)
            if trello_list_name == board.name:
                return board
        return None
