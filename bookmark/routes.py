from flask import Blueprint, request
from flask_restful import Api, Resource
from .models import *


api = Blueprint('api', __name__)
rest_api = Api(api)


class LinkItem(Resource):
    def get(self, linkId):
        link = get_link(linkId)
        return link

    def put(self, linkId):
        link = update_link(linkId, request.json)
        return link

    def delete(self, linkId):
        link = delete_link(linkId)
        return link


class LinkListItem(Resource):
    def get(self):
        links = get_links()
        return [link for link in links]

    def post(self):
        link = create_link(request.json)
        return link


rest_api.add_resource(LinkItem, '/link/<linkId>')
rest_api.add_resource(LinkListItem, '/links')
