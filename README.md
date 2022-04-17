# AmazonReviewToJSON

Small python program for converting the n-line Amazon review file to JSON for importing into mongodb. It also converts the timestamp into an ISO-8601 date string.

Input:

'''
product/productId: B004EPYZQ2
review/userId: A17KTLABQ6CO73
review/profileName: Charlie
review/helpfulness: 0/0
review/score: 4.0
review/time: 1323734400
review/summary: old school epic
review/text: I really enjoyed this movie.  If kinda reminded me of the type of films we grew up on in the 80's.  only thing I didn't like was the sometimes distracting blue streaks that the film maker is know for.  He went a little over board.  Other than that it was good and worth your time.
'''
  
Output:

'''
{"product/productId": "B004EPYZQ2", "review/userId": "A17KTLABQ6CO73", "review/profileName": "Charlie", "review/helpfulness": "0/0", "review/score": "4.0", "review/time": "2011-12-13T01:00:00", "review/summary": "old school epic", "review/text": "I really enjoyed this movie.  If kinda reminded me of the type of films we grew up on in the 80's.  only thing I didn't like was the sometimes distracting blue streaks that the film maker is know for.  He went a little over board.  Other than that it was good and worth your time."}
'''
  
Additionally it holds only one JSON-object in memory and writes it directly into the file, allowing the processing of large files. Tested with 8.7GB Amazon movie reviews from 1997 - 2012 provided by Stanford University (https://snap.stanford.edu/data/web-Movies.html).
