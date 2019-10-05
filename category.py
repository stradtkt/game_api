import sqlite3
from flask_restful import Resource

class Category(Resource):
    def get(self, name):
        game = self.find_by_name(name)
        if game:
            return game
        return {"message": "Platform not found"}

    @classmethod
    def find_by_name(cls, name):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "SELECT * FROM categories WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        conn.close()
        if row:
            return {"category": {"name": row[0]}}

    @classmethod
    def find_by_id(cls, id):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "SELECT * FROM categories WHERE id=?"
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        conn.close()
        if row:
            return {"category": {"name": row[0]}}

    @classmethod
    def insert(cls, cat):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "INSERT INTO categories VALUES (?,?,?,?,?,?,?)"
        cursor.execute(query, (cat['name']))
        conn.commit()
        conn.close()

    @classmethod
    def update(cls, cat):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "UPDATE categories SET name=? WHERE name=?"
        cursor.execute(query, (cat['name']))
        conn.commit()
        conn.close()

    def post(self, name):
        data = Category.parser.parse_args()
        category = {"name": name}
        try:
            self.insert(category)
        except:
            return {"message": "An error occurred inserting the platform."}, 500
        return category, 201

    def delete(self, id):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "DELETE FROM categories WHERE id=?"
        cursor.execute(query, (id,))
        conn.commit()
        conn.close()
        return {"message": "Platform deleted"}

    def put(self, id):
        data = Category.parser.parse_args()
        category = self.find_by_id(id)
        updated_category = {"name": data['name']}
        if category is None:
            try:
                self.insert(updated_category)
            except:
                return {"message": "An error occurred inserting the Category."}
        else:
            try:
                self.update(updated_category)
            except:
                return {"message": "An error occurred inserting the Category."}
        return updated_category


class CategoryList(Resource):
    def get(self):
        conn = sqlite3.connect('games.db')
        cursor = conn.cursor()
        query = "SELECT * FROM categories"
        result = cursor.execute(query)
        categories = []
        for row in result:
            categories.append({"name": row[0]})
        conn.close()
        return {"categories": categories}
