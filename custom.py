import pymongo
connection = pymongo.MongoClient('localhost', 27017)
database = connection['FaceRecognition']
collection = database['Data']
data = ([{
    'First Name': "Arun ",
    'Last Name': "Regmi",
    'StudentNo': 1,
    'Attended Days': "",
    'Image': "IMG/arun.jpg"
             },
    {
     'First Name': "Abhinav",
      'Last Name':"Arya",
     'StudentNo': 2,
     'Attended Days': "",
     'Image': "IMG/arya.jpg"
     },
    {
      'First Name': "Asim",
      'Last Name': "Mahat",
      'StudentNo': 3,
      'Attended Days': "",
      'Image': "IMG/asim.jpg"
     },
    {
      'First Name': "Bhabuk",
      'Last Name': "Kunwar",
      'StudentNo': 4,
      'Attended Days': "" ,
      'Image' : "IMG/bhabuk.jpg"
     },
    {
      'First Name': "Unique",
      'Last Name': "Karki",
      'StudentNo': 5,
      'Attended Days': "",
      'Image': "IMG/unique.jpg"

      }])
collection.insert_many(data)
