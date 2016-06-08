
# Suit
Diamonds = 1
Clubs = 2
Hearts = 3
Spades = 4

Unsuitable = -1

#  Figure Sequence
Figures = [3,4,5,6,7,8,9,10,11,12,13,1,2]

FiguresRank = [-1, 12, 13, 1,2,3,4,5,6,7,8,9,10,11]




class Card:

    def __init__(self, suit, figure):

        if suit >4 or suit<1 or figure<1 or figure > 13:
            raise Exception("invalid input")

        self.suit = suit
        self.figure = figure
        self.rank = FiguresRank[figure]


class CardStack:

    # figureRank
    # suitRank

    def __init__(self, cards):
        pass;

    @staticmethod
    def create(cards):
        if CardStack.ValidCardsPlay(cards):
            return CardStack(cards);
        else:
            return None

    @staticmethod
    def ValidCardsPlay(cards):

        cardsLength = len(cards)
        if cardsLength < 5:
            # 小于5张必须同一点数
            return Deck.IsSameFigure(cards)
        elif cardsLength == 5:

            # 同花
            if Deck.IsSameSuit(cards):

                return True;

            figureGroup = Deck.GroupByFigure(cards);

            # 3带2 4带1
            if len(figureGroup) == 2:
                return True;

            # 顺子
            if len(figureGroup) == 5 and (figureGroup[4].rank - figureGroup[0].rank) == 4:
                return True;

            # 其它
            return False;
        else:
            # Max is 5
            return False;
class Deck:

    def __init__(self):
        self.deck = Deck.initialFigures()
        self.shuffle();

    def shuffle(self):
        pass


    @staticmethod
    def IsSameFigure(cards):

        returnVal = True;
        last = Unsuitable;
        for card in cards:
            if last == Unsuitable:
                last = card.figure;
                continue;

            if card.figure != last:
                returnVal = True;
                break;

        return returnVal;


    @staticmethod
    def IsSameSuit(cards):

        returnVal = True;
        last = Unsuitable;
        for card in cards:
            if last == Unsuitable:
                last = card.suit;
                continue;

            if card.suit != last:
                returnVal = True;
                break;

        return returnVal;

    @staticmethod
    def GroupByFigure(cards):
        # group by figure, sort in number descending
        figureDict = {};
        for card in cards:
            if not figureDict.has_key(card.figure):
                figureDict[card.figure] = [];
            figureDict[card.figure].append(card);

        figureDictSorted = sorted(figureDict.values(), key=lambda x : len(x))

        return figureDictSorted;

    @staticmethod
    def GroupBySuit(cards):
        # group by suit, sort in number descending
        suitDict = {};
        for card in cards:
            if not suitDict.has_key(card.suit):
                suitDict[card.suit] = [];
            suitDict[card.suit].append(card);

        suitDictSorted = sorted(suitDict.values(), key=lambda x : len(x))

        return suitDictSorted;

    @staticmethod
    def initialDeck():
        returnVal = []
        returnVal.append(Deck.initialFigures(Diamonds))
        returnVal.append(Deck.initialFigures(Clubs))
        returnVal.append(Deck.initialFigures(Hearts))
        returnVal.append(Deck.initialFigures(Spades))

        return returnVal

    @staticmethod
    def initialFigures(suit):
        returnVal = []
        for i in Figures:
            returnVal.append(Card(suit, i));

        return returnVal