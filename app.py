from flask import Flask
from flask_restful import Resource,Api,reqparse
import os

app=Flask(__name__)
api=Api(app)

DATA={
    'teams':[
        'arsenal',
        'man city',
        'man utd',
        'spurs',
        'chelsea',
        'liverpool',
        'barcelona',
        'bayern munich',
        'real madrid',
        'juventus',
        'paris st germain'
    ]
}

class Teams(Resource):
    def get(self):
        # return and 200 OK
        return{'data':DATA},200
    def post(self): 
        #parse request parameters
        parser=reqparse.RequestParser()
        parser.add_argument('team',required=True)
        args=parser.parse_args()
        #check if we already  have it in the array
        if args['team'] in DATA['teams']:
            return{
                'message':f"'{args['team']}' already exists"
            },401
        else:
            #if not found append and 200 ok
            DATA['teams'].append(args['team'])
            return{'data':DATA},200
    def delete(self):
        parser=reqparse.RequestParser()
        parser.add_argument('team',required=True)
        args=parser.parse_args()
        # if we do ,remove and 200 ok
           # check if we have given location in places list
        if args['team'] in DATA['teams']:
           # if we do, remove and return data with 200 OK
            DATA['teams'].remove(args['team'])
            return {'data': DATA}, 200
        else:
            # if location does not exist in places list return 404 not found
            return {
                'message': f"'{args['team']}' does not exist."
                }, 404

        

api.add_resource(Teams,'/teams')

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))
