from enum import Enum

class Card(Enum):
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
            case Card.ACE: return 1
            case Card.TWO: return 2
            case Card.THREE: return 3
            case Card.FOUR: return 4
            case Card.FIVE: return 5
            case Card.SIX: return 6
            case Card.SEVEN: return 7
            case Card.EIGHT: return 8
            case Card.NINE: return 9
            case Card.TEN: return 10
            case Card.JACK: return 10
            case Card.QUEEN: return 10
            case Card.KING: return 10

    def __str__(self):
        match self:
            case Card.ACE: return 'ACE'
            case Card.TWO: return 'TWO'
            case Card.THREE: return 'THREE'
            case Card.FOUR: return 'FOUR'
            case Card.FIVE: return 'FIVE'
            case Card.SIX: return 'SIX'
            case Card.SEVEN: return 'SEVEN'
            case Card.EIGHT: return 'EIGHT'
            case Card.NINE: return 'NINE'
            case Card.TEN: return 'TEN'
            case Card.JACK: return 'JACK'
            case Card.QUEEN: return 'QUEEN'
            case Card.KING: return 'KING'