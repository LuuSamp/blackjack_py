from enum import Enum

class Number(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def __int__(self):
        match self:
            case Number.ACE: return 1
            case Number.TWO: return 2
            case Number.THREE: return 3
            case Number.FOUR: return 4
            case Number.FIVE: return 5
            case Number.SIX: return 6
            case Number.SEVEN: return 7
            case Number.EIGHT: return 8
            case Number.NINE: return 9
            case Number.TEN: return 10
            case Number.JACK: return 10
            case Number.QUEEN: return 10
            case Number.KING: return 10

    def __str__(self):
        match self:
            case Number.ACE: return 'ACE'
            case Number.TWO: return 'TWO'
            case Number.THREE: return 'THREE'
            case Number.FOUR: return 'FOUR'
            case Number.FIVE: return 'FIVE'
            case Number.SIX: return 'SIX'
            case Number.SEVEN: return 'SEVEN'
            case Number.EIGHT: return 'EIGHT'
            case Number.NINE: return 'NINE'
            case Number.TEN: return 'TEN'
            case Number.JACK: return 'JACK'
            case Number.QUEEN: return 'QUEEN'
            case Number.KING: return 'KING'