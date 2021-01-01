# Database Schema

## Patient Database

Patient
| PATIENT_ID | AGE_WEEKS | GENDER | WEIGHT | HEIGHT | ... |
| --- | --- | --- | ---| --- | --- |

Data
| PATIENT_ID | BED_ID | HEART_RATE | O2 | BLOOD_PRESSURE | TIME | ... |
| --- | --- | --- | --- | --- | --- | --- |

# Explanation

The data database is going to hold all of the records (in the hundreds of thousands if not millions for the test data set) for the patients in the bed at a given time. Using the patient ID, you can go to the patient table to find the patients age in weeks.  The rest of the data in the patient table can be ignored, but is there because the real database might have similar fields so that you can't do SELECT * FROM Patient.

The data table holds all of the data records.  Each record has a patient ID (see above), a bed ID telling you in which bed they reside (Bed ID's will probably range from 1-90).  HEART_RATE and BLOOD_PRESSURE can be ignored, and O2 is the oxygen level for the infant.  I am currently planning on expressing O2 as a percent, so it will range between 1 and 100.
