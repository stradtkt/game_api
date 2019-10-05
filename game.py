import sqlite3
from flask import Flask, request
from flask_restful import Resource, reqparse

class Game(Resource):
    def get(self, name):
        game = self.find_by_name(name)
        if game:
            return game
        return {"message": "Game not found"}

    @classmethod
    def find_by_name(cls, name):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "SELECT * FROM games WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        conn.close()
        if row:
            return {"game": {"name": row[0], "platform": row[1], "price": row[2], "description": row[3], "release date": row[4], "category": row[5], "players": row[6]}}

    @classmethod
    def find_by_id(cls, id):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "SELECT * FROM games WHERE id=?"
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        conn.close()
        if row:
            return {"game": {"name": row[0], "platform": row[1], "price": row[2], "description": row[3], "release date": row[4], "category": row[5], "players": row[6]}}

    @classmethod
    def insert(cls, game):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "INSERT INTO games VALUES (?,?,?,?,?,?,?)"
        cursor.execute(query, (game['name'], game['platform'], game['price'], game['description'], game['release_date'], game['category'], game['players']))
        conn.commit()
        conn.close()

    @classmethod
    def update(cls, game):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "UPDATE games SET platform=?, price=?, description=?, release_date=?, category=?, players=? WHERE name=?"
        cursor.execute(query, (game['platform'], game['price'], game['description'], game['release_date'], game['category'], game['players'], game['name']))
        conn.commit()
        conn.close()

    def post(self, name):
        data = Game.parser.parse_args()
        game = {"name": name, "platform": data["platform"], "price": data["price"], "description": data["description"], "release_date": data["release_date"], "category": data["category"], "players": data["players"]}
        try:
            self.insert(game)
        except:
            return {"message": "An error occurred inserting the item."}, 500
        return game, 201

    def delete(self, id):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "DELETE FROM games WHERE id=?"
        cursor.execute(query, (id,))
        conn.commit()
        conn.close()
        return {"message": "Game deleted"}
