from app.api.classes import Flashcard
from . import api_bp
from app.db_operations import *
from flask import request, redirect, url_for

import json

data = {
    25: Flashcard("Barak Obama", "44th President of the United States"),
    24: Flashcard("George W. Bush", "43rd President of the United States. Not to be confused with his father, the 41st president, George H.W. Bush")
}

@api_bp.route('/flashcards/', methods=['GET'])
def get_all_flashcards():
    all_cards = retrieve_all_flashcards()
    return json.dumps([(card.id, card.title) for card in all_cards])

@api_bp.route('/flashcards/<int:id>', methods=['GET'])
def get_flashcard(id):
    card = retrieve_flashcard(id)
    
    return json.dumps({'description': card.description, 'title': card.title }) if card is not None else {}, 404

@api_bp.route('/flashcards/new', methods=['POST'])
def new_flashcard():
    create_flashcard(
        request.form['title'],
        request.form['description']
    )
    
    return redirect(url_for('api_bp.get_all_flashcards'))

