from flask import Blueprint
from flask_restful import Api, Resource

api = Blueprint('api', __name__)
rest_api = Api(api)


class LinkItem(Resource):
    def get(self, linkId):
        return {"id": linkId}

    def put(self, linkId):
        return {"id": linkId}

    def delete(self, linkId):
        return {"id": linkId}


class LinkListItem(Resource):
    def get(self):
        return [{"id": ""}]

    def post(self):
        return {"id": ""}


rest_api.add_resource(LinkItem, '/link/<linkId>')
rest_api.add_resource(LinkListItem, '/links')
