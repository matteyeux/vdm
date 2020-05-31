from vdm import api

@api.app.errorhandler(404)
def page_not_found(error):
	return {'message': 'Not found'}, 404

