from enum import Enum

class LibraryType(str, Enum):
    FAVORITES = "favoritos"
    FOLLOWING = "siguiendo"
    WATCHLIST = "lista_espera"