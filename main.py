import uvicorn
import pyrebase
from fastapi import FastAPI
from models import LoginSchema,SignUpSchema
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.requests import Request

app = FastAPI(
    description="This is a simple app to show Firebase Auth with FastAPI",
    title="Firebase Auth",
    docs_url="/"
)



import firebase_admin
from firebase_admin import credentials,auth


if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json") #get your service account keys from firebase
    firebase_admin.initialize_app(cred)


firebaseConfig = {
 "message":"Get your config from firebase"
}

firebase = pyrebase.initialize_app(firebaseConfig)


@app.post('/signup')
async def create_an_account(user_data:SignUpSchema):
    email = user_data.email
    password = user_data.password

    try:
        user = auth.create_user(
            email = email,
            password = password
        )

        return JSONResponse(content={"message" : f"User account created successfuly for user {user.uid}"},
                            status_code= 201
               )
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=400,
            detail= f"Account already created for the email {email}"
        )





@app.post('/login')
async def create_access_token(user_data:LoginSchema):
    email = user_data.email
    password = user_data.password

    try:
        user = firebase.auth().sign_in_with_email_and_password(
            email = email,
            password = password
        )

        token = user['idToken']

        return JSONResponse(
            content={
                "token":token
            },status_code=200
        )

    except:
        raise HTTPException(
            status_code=400,detail="Invalid Credentials"
        )

@app.post('/ping')
async def validate_token(request:Request):
    headers = request.headers
    jwt = headers.get('authorization')

    user = auth.verify_id_token(jwt)

    return user["user_id"]

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)