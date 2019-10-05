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