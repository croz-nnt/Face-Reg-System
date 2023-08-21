import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyCCA7vixEir-HLexU4cHzDgfpnUpUtwly4",
  "authDomain": "truccodeidentifyface.firebaseapp.com",
  "databaseURL": "https://truccodeidentifyface-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "truccodeidentifyface",
  "storageBucket": "truccodeidentifyface.appspot.com",
  "messagingSenderId": "319431023142",
  "appId": "1:319431023142:web:5037003c2df05102d064e7",
  "measurementId": "G-8CGYSDGW3V" }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
data = {"name": "Mortimer 'Morty' Smith"}
db.child("class").child("students").set(data)