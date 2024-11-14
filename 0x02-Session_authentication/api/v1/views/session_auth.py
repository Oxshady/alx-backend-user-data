#!/usr/bin/env python3
"""Flask view that handles all routes for the Session authentication"""
from api.v1.views import app_views
from flask import request, jsonify, abort
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def sessionAuth():
    """handles all routes for the Session authentication"""
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400
    from models.user import User
    user = User.search({"email": email})
    if not user:
        return {"error": "no user found for this email"}, 404
    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    resp = jsonify(user.to_json())
    resp.set_cookie(getenv("SESSION_NAME"), session_id)
    return resp


@app_views.route('/api/v1/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """logout and destroy session"""
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
