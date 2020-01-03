import pymongo
connection = pymongo.MongoClient('localhost', 27017)
database = connection['FaceRecognition']
collection = database['Data']

data = ([{
    'std_id': 0o1,
    'First Name': "Arun ",
    'Last Name': "Regmi",
    'Attended Days': "",
    'Image': "IMG/arun.jpg"
             },
    {
     'std_id': 0o2,
     'First Name': "Abhinav",
      'Last Name':"Arya",
     'Attended Days': "",
     'Image': "IMG/arya.jpg"
     },
    {
        'std_id': 0o3,
      'First Name': "Asim",
      'Last Name': "Mahat",
      'Attended Days': "",
      'Image': "IMG/asim.jpg"
     },
    {
       'std_id': 0o4,
      'First Name': "Bhabuk",
      'Last Name': "Kunwar",
      'Attended Days': "" ,
      'Image' : "IMG/bhabuk.jpg"
     },
    {
        'std_id': 0o5,
      'First Name': "Unique",
      'Last Name': "Karki",
      'Attended Days': "",
      'Image': "IMG/unique.jpg"

      }])
collection.insert_many(data)
