from flask_restx import Namespace, Resource, fields
from app.models.users import User

api = Namespace("users", description="Operations sur les utilisateurs")

user_model = api.model("User", {
    "first_name": fields.String(required=True),
    "last_name": fields.String(required=True),
    "email": fields.String(required=True),
    "password": fields.String(required=True),
    "is_admin": fields.Boolean(default=False),
})

user_response_model = api.model("UserResponse", {
    "id": fields.String(),
    "first_name": fields.String(),
    "last_name": fields.String(),
    "email": fields.String(),
    "is_admin": fields.Boolean(),
    "created_at": fields.String(),
    "updated_at": fields.String(),
})

users_db = []

@api.route("/")
class UserList(Resource):

    @api.marshal_list_with(user_response_model)
    def get(self):
        return [u.to_dict() for u in users_db], 200

    @api.expect(user_model, validate=True)
    @api.marshal_with(user_response_model, code=201)
    def post(self):
        data = api.payload
        for u in users_db:
            if u.email == data["email"]:
                api.abort(400, "Email deja utilise.")
        try:
            user = User(
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                password=data["password"],
                is_admin=data.get("is_admin", False)
            )
        except ValueError as e:
            api.abort(400, str(e))
        users_db.append(user)
        return user.to_dict(), 201

@api.route("/<string:user_id>")
class UserResource(Resource):

    @api.marshal_with(user_response_model)
    def get(self, user_id):
        user = next((u for u in users_db if u.id == user_id), None)
        if not user:
            api.abort(404, "Utilisateur introuvable.")
        return user.to_dict(), 200