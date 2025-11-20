from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade
from app.Extensions import db

# -----------------------
# NAMESPACE
# -----------------------
api = Namespace('reviews', description='Review operations')

# -----------------------
# REVIEW MODEL
# -----------------------
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'place_id': fields.String(required=True, description='ID of the place')
})

# -----------------------
# LIST / CREATE REVIEWS
# -----------------------
@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @api.doc(security='BearerAuth')
    @jwt_required()
    def post(self):
        """Register a new review"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)

        data = request.json
        data['user_id'] = current_user_id  # force user_id

        place = facade.get_place(data['place_id'])
        if not place:
            return {"message": "Place not found"}, 404

        # Only non-admins are restricted from reviewing their own places
        if place.owner_id == current_user_id and not is_admin:
            return {"message": "You cannot review your own place."}, 400

        existing_review = facade.get_user_review_for_place(current_user_id, data['place_id'])
        if existing_review and not is_admin:
            return {"message": "You have already reviewed this place."}, 400

        review = facade.create_review(data)
        return review.to_dict(), 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        return [r.to_dict() for r in reviews], 200

# -----------------------
# GET / UPDATE / DELETE REVIEW
# -----------------------
@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        review = facade.get_review(review_id)
        if not review:
            return {"message": "Review not found"}, 404
        return review.to_dict(), 200

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized')
    @api.doc(security='BearerAuth')
    @jwt_required()
    def put(self, review_id):
        """Update a review (author or admin)"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)

        review = facade.get_review(review_id)
        if not review:
            return {"message": "Review not found"}, 404

        if review.user_id != current_user_id and not is_admin:
            return {"message": "Unauthorized action"}, 403

        data = request.json
        updated_review = facade.update_review(review_id, data)
        return {"message": "Review updated successfully"}, 200

    @jwt_required()
    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized')
    @api.doc(security='BearerAuth')
    def delete(self, review_id):
        """Delete a review (author or admin)"""

        user_id = get_jwt_identity()
        claims = get_jwt()  # <-- FIXED

        if not claims.get("is_admin"):
            return {'error': 'Admin privileges required'}, 403
        is_admin = claims.get('is_admin', False)

        review = facade.get_review(review_id)
        if not review:
            return {"message": "Review not found"}, 404

        # Only owner or admin can delete
        user = facade.get_user(user_id)

        if review.user_id != user_id and not user.is_admin:
            return {"error": "Unauthorized"}, 403

        facade.review_repo.delete(review.id)
        db.session.commit()

        return {"message": "Review deleted"}, 200

# -----------------------
# LIST REVIEWS FOR A PLACE
# -----------------------
@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            return {"message": "Place not found"}, 404
        reviews = facade.get_reviews_by_place(place_id)
        return [r.to_dict() for r in reviews], 200