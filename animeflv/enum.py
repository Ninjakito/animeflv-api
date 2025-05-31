from enum import Enum

class LibraryAction(str, Enum):
    FAVORITES = "favorite"
    FOLLOWING = "follow"
    WATCHLIST = "pending"
    
class Action(int, Enum):
    ADD = 0
    REMOVE = 1
    SEEN = 1
    UNSEEN = 0
