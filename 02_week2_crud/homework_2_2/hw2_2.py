__author__ = 'dvanichkina'

import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")


def removelowestscore():
    # get a handle to the school database
    db = connection.students
    grades = db.grades
    # If you select homework grade-documents, sort by student and then by score, you can iterate through
    # and find the lowest score for each student by noticing a change in student id. As you notice that
    # change of student_id, remove the document.
    try:
        query = {'type': 'homework'}
        projection = {'student_id': 1 , '_id': 1 }
        docs = grades.find(query, projection).sort([('student_id', pymongo.ASCENDING),('score', pymongo.ASCENDING)])

        previous_id = None
        student_id = None
        
        for doc in docs:
            student_id = doc['student_id']
            if student_id != previous_id:
                previous_id = student_id
                grades.remove({'_id' : doc['_id']})

    except Exception as e:
        print "Exception: ", type(e), e


removelowestscore()
