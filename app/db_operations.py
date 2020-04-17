import sqlite3
from app.api.classes import Flashcard
from flask import current_app
import json

def create_flashcard(title: str, description='', source='', image_url='', tags=[]):
    with sqlite3.connect(current_app.config['DB']) as db:
        c = db.cursor()
        c.execute(
            """
            INSERT INTO
                flashcards
                (
                    title,
                    description,
                    source,
                    image_url,
                    tags
                )
            VALUES
                (?, ?, ?, ?, ?)
            """,
            (
                title,
                description,
                source,
                image_url,
                json.dumps(tags)
            )
        )
        
        return c.lastrowid

def retrieve_all_flashcards(start: int=0, qty:int=None):
    """
    Retrieves all flashcards in ascending order (max 250 at a time) or using basic pagination returns `qty` flashcards occuring after `start`. 
    """
    qty = 250 if qty == None else qty
    
    with sqlite3.connect(current_app.config['DB']) as db:
        c = db.cursor()
        c.execute("""
            SELECT
                id,
                title,
                description,
                source,
                image_url,
                tags
            FROM
                flashcards
            WHERE
                id >= ?
            ORDER BY
                id ASC
            LIMIT 
                ?
            """, (start, qty)
        )
        
        raw_cards = c.fetchall()
        cards = []
        for card in raw_cards:
            cards.append(
                Flashcard(
                    id=card[0],
                    title=card[1],
                    description=card[2],
                    source=card[3],
                    image_url=card[4],
                    tags=json.loads(card[5])
                )
            )
        return cards
            
def retrieve_flashcard(id):
    """
    Returns 
    """
    with sqlite3.connect(current_app.config['DB']) as db:
        c = db.cursor()
        c.execute("""
            SELECT
                id,
                title,
                description,
                source,
                image_url,
                tags
            FROM
                flashcards
            WHERE
                id=?
            """, (id,)
        )
        
        r = c.fetchone()
        
        if not r:
            return None
        return Flashcard(
            id=r[0],
            title=r[1],
            description=r[2],
            source=r[3],
            image_url=r[4],
            tags=json.loads(r[5])
        )
        
    

