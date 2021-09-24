import unittest
import random

from cards import Hand, Card, Deck

class TestDeck(unittest.TestCase):
    
    def setUp(self):
        self.deck = Deck()
        
    def test52(self):
        self.assertEqual(len(self.deck), 52)
        
    def test_no_dupes(self):
        seen = set()
        for card in self.deck:
            self.assertNotIn(card, seen)
            seen.add(card)
            
    def test_repr_string(self):
        "smoke test"
        self.assertIsInstance(repr(self.deck), str)
        
    def test_shuffle(self):
        deck2 = Deck()
        random.shuffle(deck2)
        self.assertNotEqual(self.deck.cards, deck2.cards)
        
    def test_deal_5(self):
        hand = self.deck.deal(5)
        self.assertEqual(len(hand), 5)
        
    def test_draw(self):
        hand = self.deck.deal(5)
        self.deck.draw(hand)
        self.assertEqual(len(hand), 6)
            
class TestCards(unittest.TestCase):
    
    def test_repr_string(self):
        self.assertIsInstance(repr(Card(rank='A', suit='club')), str)
            
    def test_same_card(self):
        c0 = Card(rank='A', suit='club')
        c1 = Card(rank='A', suit='club')
        self.assertEqual(c0, c1)
        
    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank='B', suit='club')
            
    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank='A', suit='clubs')
            

class TestHand(unittest.TestCase):
    
    def test_simple(self):
        hand = Hand([Card(rank='5', suit='spade')])
        self.assertEqual(hand.score(), 5)
        
    def test_soft_17(self):
        hand = Hand([
            Card(rank='A', suit='spade'),
            Card(rank='6', suit='spade'),
        ])
        self.assertEqual(hand.score(), 17)
            
    def test_hard_17(self):
        hand = Hand([
            Card(rank='A', suit='spade'),
            Card(rank='K', suit='spade'),
            Card(rank='6', suit='spade'),
        ])
        self.assertEqual(hand.score(), 17)
        
    def test_really_hard_14(self):
        hand = Hand([
            Card(rank='A', suit='spade'),
            Card(rank='A', suit='club'),
            Card(rank='A', suit='heart'),
            Card(rank='A', suit='diamond'),
            Card(rank='K', suit='spade')
        ])
        self.assertEqual(hand.score(), 14)
        
