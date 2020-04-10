from flask_restplus import fields, reqparse

from satcog.rest import api

# Paginations

class GetRequestLandsat8:

    parser = reqparse.RequestParser()
    parser.add_argument('data', type=str, required=True, help='Which data?')


# Models

class GetResponseLandsat8Model:

    model = api.model('GetResponseLandsat8Model', {
        'data': fields.String()
    })
