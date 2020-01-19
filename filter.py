import os
import face_recognition
import pprint
import sys

avtest = []
for root, dirs, files in os.walk("database/"):
    for filename in files:
        if 'jpg' in filename:
            avtest.append("database/" + filename)

class target:
    def __init__(self, f):
        try:
            self.name = f
            self._img = face_recognition.load_image_file(f)
            self.encoding = face_recognition.face_encodings(self._img)[0]
            self.failed = False
        except:
            self.failed = True

extracted = [target(f) for f in avtest if target(f).failed == False]
all_encoding = [f.encoding for f in extracted]
all_name = [f.name for f in extracted]
t_img = face_recognition.load_image_file(sys.argv[1])
t_encoding = face_recognition.face_encodings(t_img)[0]


result = sorted(zip(face_recognition.api.face_distance(all_encoding, t_encoding), all_name))

pprint.pprint(result[0:5])