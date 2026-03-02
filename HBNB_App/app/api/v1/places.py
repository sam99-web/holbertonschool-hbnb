from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')


# ── Collection endpoint: /api/v1/places/ ───────────────────────────────────

@api.route('/')
class PlaceList(Resource):

    @api.doc('list_places')
    @api.marshal_list_with(place_list_model)
    def get(self):
        """Retrieve all places (summary view)."""
        places = facade.get_all_places()
        return [p.to_dict() for p in places], 200

    @api.doc('create_place')
    @api.expect(place_input_model, validate=True)
    @api.response(201, 'Place created', place_output_model)
    @api.response(400, 'Validation error')
    @api.response(404, 'Owner or amenity not found')
    def post(self):
        """Create a new place."""
        data = api.payload
        try:
            place = facade.create_place(data)
        except ValueError as e:
            api.abort(400, str(e))

        return _place_response(place), 201


# ── Item endpoint: /api/v1/places/<place_id> ───────────────────────────────

@api.route('/<string:place_id>')
@api.param('place_id', 'The place UUID')
class PlaceResource(Resource):

    @api.doc('get_place')
    @api.response(200, 'Success', place_output_model)
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Retrieve a specific place by ID (full detail with owner & amenities)."""
        place = facade.get_place(place_id)
        if place is None:
            api.abort(404, f"Place '{place_id}' not found")
        return _place_response(place), 200

    @api.doc('update_place')
    @api.expect(place_input_model)          # All fields optional for PUT
    @api.response(200, 'Place updated', place_output_model)
    @api.response(400, 'Validation error')
    @api.response(404, 'Place not found')
    def put(self, place_id):
        """Update an existing place (partial update supported)."""
        place = facade.get_place(place_id)
        if place is None:
            api.abort(404, f"Place '{place_id}' not found")

        data = api.payload or {}
        try:
            updated = facade.update_place(place_id, data)
        except ValueError as e:
            api.abort(400, str(e))

        return _place_response(updated), 200
