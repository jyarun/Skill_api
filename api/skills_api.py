from flask import Blueprint
from flask import request, jsonify

from service import skills_service

skills_api = Blueprint('skills_api', __name__)

@skills_api.route('/api/skills/all', methods=['GET'])
def get_skills_all():
    results = skills_service.get_all_skills()
    return jsonify(results)


@skills_api.route('/api/skills', methods=['GET'])
def get_skill():
    results = skills_service.get_skill(request)
    return jsonify(results)
    