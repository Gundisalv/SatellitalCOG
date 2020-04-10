from satcog.rest.landsat.landsat_8 import schemas
from satcog.rest.landsat import ns 
#from satcog.rest.landsat.landsat_8.service import Landsat8Service
from flask_restplus import Resource
from satcog.rest import api

@ns.route('/l8')
class Landsat8(Resource):
    
    @ns.expect(schemas.GetRequestLandsat8.parser)
    @ns.marshal_with(schemas.GetResponseLandsat8Model.model, code=200)
    def get(self):
        args = schemas.GetRequestLandsat8.parser.parse_args()
        return [args]
