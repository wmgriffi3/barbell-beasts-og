import pandas as pd

body_url = 'https://raw.githubusercontent.com/wmgriffi3/barbell-beasts/master/FitNotes_BodyTracker_Export.csv'
body_data = pd.read_csv(body_url, error_bad_lines=False)

standards_url = 'https://raw.githubusercontent.com/wmgriffi3/barbell-beasts/master/weight_lifting_standards.csv'
standards_data = pd.read_csv(standards_url, error_bad_lines=False)

exercise_url = 'https://raw.githubusercontent.com/wmgriffi3/barbell-beasts/master/FitNotes_Export.csv'
exercise_data = pd.read_csv(exercise_url, error_bad_lines=False)


body_data.head()
standards_data.head()
exercise_data.head()
