import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store_id."
                        )

    @jwt_required()
    def get(self, name: str):
        item = ItemModel.find_by_name(name=name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name: str):
        if ItemModel.find_by_name(name=name):
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = ItemModel(name=name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}

        return item.json()

    def delete(self, name: str):
        item = ItemModel.find_by_name(name=name)

        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

    def put(self, name: str):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name=name, **data)
        else:
            item.price = data['price']
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    TABLE_NAME = 'items'

    def get(self):
        # items = list(map(lambda item: item.json(), items))
        items = [item.json() for item in ItemModel.get_all()]
        return {'items': items}
