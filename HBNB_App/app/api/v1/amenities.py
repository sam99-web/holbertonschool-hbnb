from flask import request
from flask_restx import Resource, fields, marshal
from app.api.v1.api_blueprint import api_v1
from app.services.facade import HBnBFacade

# Initialize facade (in production, use dependency injection)
facade = HBnBFacade()

# Define API models for documentation & serialization
amenity_model = api_v1.model('Amenity', {
    'id': fields.String(readonly=True, description='Amenity ID'),
    'name': fields.String(required=True, description='Amenity name', min_length=1, max_length=50),
    'description': fields.String(description='Amenity description', max_length=255),
    'created_at': fields.DateTime(readonly=True, description='Creation timestamp'),
    'updated_at': fields.DateTime(readonly=True, description='Last update timestamp')
})

amenity_input_model = api_v1.model('AmenityInput', {
    'name': fields.String(required=True, description='Amenity name', min_length=1, max_length=50),
    'description': fields.String(description='Amenity description', max_length=255)
})

@api_v1.route('/amenities')
class AmenityList(Resource):
    """Amenity collection endpoint"""
    
    @api_v1.doc('list_amenities')
    @api_v1.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        amenities = facade.get_all_amenities()
        return [amenity.to_dict() for amenity in amenities], 200
    
    @api_v1.doc('create_amenity')
    @api_v1.expect(amenity_input_model)
    @api_v1.marshal_with(amenity_model, code=201)
    def post(self):
        """Create a new amenity"""
        data = api_v1.payload
        
        # Validation
        if not data.get('name'):
            api_v1.abort(400, 'Name is required')
        
        try:
            amenity = facade.create_amenity(
                name=data['name'],
                description=data.get('description', '')
            )
            return amenity.to_dict(), 201
        except ValueError as e:
            api_v1.abort(400, str(e))

@api_v1.route('/amenities/<string:amenity_id>')
class AmenityResource(Resource):
    """Single amenity endpoint"""
    
    @api_v1.doc('get_amenity')
    @api_v1.marshal_with(amenity_model)
    @api_v1.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Retrieve a specific amenity"""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api_v1.abort(404, 'Amenity not found')
        return amenity.to_dict(), 200
    
    @api_v1.doc('update_amenity')
    @api_v1.expect(amenity_input_model)
    @api_v1.marshal_with(amenity_model)
    @api_v1.response(404, 'Amenity not found')
    @api_v1.response(400, 'Invalid input or conflict')
    def put(self, amenity_id):
        """Update an existing amenity"""
        data = api_v1.payload
        
        # Check if amenity exists
        existing = facade.get_amenity(amenity_id)
        if not existing:
            api_v1.abort(404, 'Amenity not found')
        
        try:
            updated = facade.update_amenity(amenity_id, data)
            if not updated:
                api_v1.abort(404, 'Amenity not found')
            return updated.to_dict(), 200
        except ValueError as e:
            api_v1.abort(400, str(e))

# Register endpoints with namespace
api_v1.add_resource(AmenityList, '/amenities')
api_v1.add_resource(AmenityResource, '/amenities/<string:amenity_id>')
