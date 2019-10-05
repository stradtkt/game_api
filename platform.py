import sqlite3
from flask import Flask, request
from flask_restful import Resource, reqparse

class Platform(Resource):
    def get(self, name):
        game = self.find_by_name(name)
        if game:
            return game
        return {"message": "Platform not found"}

    @classmethod
    def find_by_name(cls, name):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "SELECT * FROM platforms WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        conn.close()
        if row:
            return {"game": {"name": row[0], "price_first_released": row[1], "release_date": row[2]}}

    @classmethod
    def find_by_id(cls, id):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "SELECT * FROM platforms WHERE id=?"
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        conn.close()
        if row:
            return {"game": {"name": row[0], "price_first_released": row[1], "release_date": row[2]}}

    @classmethod
    def insert(cls, platform):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "INSERT INTO platforms VALUES (?,?,?,?,?,?,?)"
        cursor.execute(query, (platform['name'], platform['price_first_released'], platform['release_date']))
        conn.commit()
        conn.close()

    @classmethod
    def update(cls, platform):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "UPDATE games SET name=?, price_first_released=?, release_date=? WHERE name=?"
        cursor.execute(query, (platform['name'], platform['price_first_released'], platform['release_date'], platform['name']))
        conn.commit()
        conn.close()

    def post(self, name):
        data = Platform.parser.parse_args()
        game = {"name": name, "price_first_released": data["price_first_released"], "release_date": data["release_date"]}
        try:
            self.insert(game)
        except:
            return {"message": "An error occurred inserting the platform."}, 500
        return game, 201

    def delete(self, id):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "DELETE FROM platforms WHERE id=?"
        cursor.execute(query, (id,))
        conn.commit()
        conn.close()
        return {"message": "Platform deleted"}

    def put(self, id):
        data = Platform.parser.parse_args()
        game = self.find_by_id(id)
        updated_platform = {"name": data['name'], "price_first_released": data["price_first_released"], "release_date": data["release_date"]}
        if game is None:
            try:
                self.insert(updated_platform)
            except:
                return {"message": "An error occurred inserting the Platform."}
        else:
            try:
                self.update(updated_platform)
            except:
                return {"message": "An error occurred inserting the platform."}
        return updated_platform


class PlatformList(Resource):
    def get(self):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "SELECT * FROM platforms"
        result = cursor.execute(query)
        platforms = []
        for row in result:
            platforms.append({"name": row[0], "price_first_released": row[1], "release_date": row[2]})
        conn.close()
        return {"platforms": platforms}
