PATIENT_INFORMATION_TEMPLATE = """
    - **Basic Information**
    - Name: {name}
    - Age: {age}
    - Gender: {gender}
    - Date of Birth: {dob}
    
    - **Vital Signs**
    - Heart Rate: {heart_rate} bpm
    - Blood Pressure: {blood_pressure} mmHg
    - Respiratory Rate: {respiratory_rate} breaths per min
    - Temperature: {temperature} °C
    - Oxygen Saturation: {oxygen_saturation}%
    
    - **Medical History**
    - Past Diagnoses: {past_diagnoses}
    - Previous Surgeries: {previous_surgeries}
    - Hospitalizations: {hospitalizations}
    - Family Medical History: {family_history}
    - Allergies: {allergies}
    - Current Medications: {medications}
    
    - **Symptoms & Presenting Complaint**
    - Chief Complaint: {chief_complaint}
    - Onset and Duration: {onset}
    - Severity (1-10): {severity}
    - Associated Symptoms: {associated_symptoms}
    
    - **Lifestyle & Risk Factors**
    - Smoking: {smoking}
    - Alcohol Use: {alcohol}
    - Diet: {diet}
    - Physical Activity: {physical_activity}
    - Sleep Patterns: {sleep_patterns}
    - Occupational & Environmental Exposure: {occupational_exposure}
    
    - **Examinations & Tests**
    - Physical Exam Findings: {physical_exam}
    - Laboratory Tests: {lab_tests}
    - Imaging Results: {imaging_results}
    - Additional Tests (ECG, Spirometry, etc.): {additional_tests}
    
    - **Psychological & Social History**
    - Mental Health History: {mental_health}
    - Stress Levels: {stress_levels}
    - Support System: {support_system}
    - Socioeconomic Factors: {socioeconomic_factors}
"""

LLM_SUMMARY_TEMPLATE = """
    You are an AI assistant helping doctors prepare for auscultation and clinical evaluations.
    Given the following patient details:
    
    - **Basic Information**
    - Name: {name}
    - Age: {age}
    - Gender: {gender}
    - Date of Birth: {dob}
    
    - **Vital Signs**
    - Heart Rate: {heart_rate} bpm
    - Blood Pressure: {blood_pressure} mmHg
    - Respiratory Rate: {respiratory_rate} breaths per min
    - Temperature: {temperature} °C
    - Oxygen Saturation: {oxygen_saturation}%
    
    - **Medical History**
    - Past Diagnoses: {past_diagnoses}
    - Previous Surgeries: {previous_surgeries}
    - Hospitalizations: {hospitalizations}
    - Family Medical History: {family_history}
    - Allergies: {allergies}
    - Current Medications: {medications}
    
    - **Symptoms & Presenting Complaint**
    - Chief Complaint: {chief_complaint}
    - Onset and Duration: {onset}
    - Severity (1-10): {severity}
    - Associated Symptoms: {associated_symptoms}
    
    - **Lifestyle & Risk Factors**
    - Smoking: {smoking}
    - Alcohol Use: {alcohol}
    - Diet: {diet}
    - Physical Activity: {physical_activity}
    - Sleep Patterns: {sleep_patterns}
    - Occupational & Environmental Exposure: {occupational_exposure}
    
    - **Examinations & Tests**
    - Physical Exam Findings: {physical_exam}
    - Laboratory Tests: {lab_tests}
    - Imaging Results: {imaging_results}
    - Additional Tests (ECG, Spirometry, etc.): {additional_tests}
    
    - **Psychological & Social History**
    - Mental Health History: {mental_health}
    - Stress Levels: {stress_levels}
    - Support System: {support_system}
    - Socioeconomic Factors: {socioeconomic_factors}

    **Task:** 
    - Provide a concise yet detailed summary of the patient’s condition.
    - Highlight any red flags, potential diagnoses, and required follow-up actions.
    - Prioritize information relevant to auscultation and necessary medical decisions.

    **Summary:**
"""

PATIENTS = {
    "John Doe": {
        "Full Name": "John Doe",
        "Age": 58,
        "Gender": "Male",
        "Date of Birth": "1965-03-14",
        "Heart Rate (bpm)": 78,
        "Blood Pressure (mmHg)": "130/85",
        "Respiratory Rate (breaths per min)": 18,
        "Temperature (°C)": 36.8,
        "Oxygen Saturation (%)": 97,
        "Past Diagnoses": "Hypertension, Type 2 Diabetes",
        "Previous Surgeries": "Appendectomy (2010)",
        "Hospitalizations": "Admitted for pneumonia in 2018",
        "Family Medical History": "Father had heart disease, mother had diabetes",
        "Allergies": "Penicillin",
        "Current Medications": "Metformin, Amlodipine",
        "Chief Complaint": "Shortness of breath and occasional chest pain",
        "Onset and Duration of Symptoms": "Started 2 weeks ago, intermittent",
        "Severity": 5,
        "Associated Symptoms": "Mild dizziness, occasional fatigue",
        "Smoking": "No",
        "Alcohol Use": "Occasionally",
        "Diet and Nutrition": "Balanced diet but high salt intake",
        "Physical Activity Level": "Walks 3 times a week for 30 minutes",
        "Sleep Patterns": "Occasionally disrupted sleep, 6-7 hours per night",
        "Occupational & Environmental Exposure": "Office worker, minimal exposure",
        "Physical Exam Findings": "Mild wheezing in left lung, normal heart sounds",
        "Recent Laboratory Tests": "HbA1c: 6.8%, LDL: 130 mg/dL",
        "Imaging Results": "Chest X-ray: Mild hyperinflation, no consolidation",
        "ECG, Spirometry, etc.": "ECG: Normal sinus rhythm, Spirometry: Mild obstruction",
        "Mental Health History": "Mild anxiety, no history of depression",
        "Stress Levels": "Moderate due to work pressure",
        "Support System": "Lives with spouse, strong family support",
        "Socioeconomic Factors": "Adequate financial stability, access to healthcare",
    },
    "Emily Carter": {
        "Full Name": "Emily Carter",
        "Age": 35,
        "Gender": "Female",
        "Date of Birth": "1989-06-22",
        "Heart Rate (bpm)": 72,
        "Blood Pressure (mmHg)": "120/75",
        "Respiratory Rate (breaths per min)": 16,
        "Temperature (°C)": 36.5,
        "Oxygen Saturation (%)": 99,
        "Past Diagnoses": "None",
        "Previous Surgeries": "Wisdom tooth extraction (2015)",
        "Hospitalizations": "None",
        "Family Medical History": "No significant hereditary conditions",
        "Allergies": "None",
        "Current Medications": "None",
        "Chief Complaint": "Routine check-up, no complaints",
        "Onset and Duration of Symptoms": "N/A",
        "Severity": 0,
        "Associated Symptoms": "None",
        "Smoking": "No",
        "Alcohol Use": "Occasionally",
        "Diet and Nutrition": "Balanced diet, includes fruits and vegetables",
        "Physical Activity Level": "Exercises 4-5 times per week, cardio and strength",
        "Sleep Patterns": "7-8 hours per night, good sleep hygiene",
        "Occupational & Environmental Exposure": "Office job, no significant exposure",
        "Physical Exam Findings": "Normal lung and heart sounds, no abnormalities",
        "Recent Laboratory Tests": "All parameters within normal range",
        "Imaging Results": "Normal chest X-ray",
        "ECG, Spirometry, etc.": "ECG: Normal sinus rhythm, Spirometry: Normal function",
        "Mental Health History": "No significant issues, manages stress well",
        "Stress Levels": "Mild, related to work deadlines",
        "Support System": "Strong social and family support",
        "Socioeconomic Factors": "Good financial stability, access to healthcare",
    },
    "Robert Thompson": {
        "Full Name": "Robert Thompson",
        "Age": 62,
        "Gender": "Male",
        "Date of Birth": "1962-11-10",
        "Heart Rate (bpm)": 88,
        "Blood Pressure (mmHg)": "135/90",
        "Respiratory Rate (breaths per min)": 20,
        "Temperature (°C)": 37.1,
        "Oxygen Saturation (%)": 96,
        "Past Diagnoses": "Borderline hypertension, high cholesterol",
        "Previous Surgeries": "None",
        "Hospitalizations": "None",
        "Family Medical History": "Father died of heart failure at 70, mother had hypertension",
        "Allergies": "None",
        "Current Medications": "Atorvastatin",
        "Chief Complaint": "Occasional fatigue and mild shortness of breath",
        "Onset and Duration of Symptoms": "Started gradually over the past 3 months",
        "Severity": 3,
        "Associated Symptoms": "Mild swelling in ankles, occasional dizziness",
        "Smoking": "No",
        "Alcohol Use": "Occasionally",
        "Diet and Nutrition": "Mostly healthy but high sodium intake",
        "Physical Activity Level": "Walks daily but tires more easily",
        "Sleep Patterns": "Interrupted sleep, wakes up feeling unrefreshed",
        "Occupational & Environmental Exposure": "Retired, no major exposure",
        "Physical Exam Findings": "Mild peripheral edema, slightly diminished breath sounds",
        "Recent Laboratory Tests": "BNP slightly elevated, LDL borderline high",
        "Imaging Results": "Chest X-ray: Mild cardiomegaly",
        "ECG, Spirometry, etc.": "ECG: Mild left ventricular hypertrophy, Spirometry: Normal",
        "Mental Health History": "Mild anxiety about health",
        "Stress Levels": "Moderate due to concerns about aging",
        "Support System": "Lives with spouse, good family support",
        "Socioeconomic Factors": "Stable retirement income, good healthcare access",
    },
    "Sophia Martinez": {
        "Full Name": "Sophia Martinez",
        "Age": 28,
        "Gender": "Female",
        "Date of Birth": "1996-01-15",
        "Heart Rate (bpm)": 80,
        "Blood Pressure (mmHg)": "118/76",
        "Respiratory Rate (breaths per min)": 18,
        "Temperature (°C)": 37.8,  # Slight fever
        "Oxygen Saturation (%)": 98,
        "Past Diagnoses": "None",
        "Previous Surgeries": "None",
        "Hospitalizations": "None",
        "Family Medical History": "No major hereditary conditions",
        "Allergies": "None",
        "Current Medications": "Paracetamol (for fever), Vitamin C",
        "Chief Complaint": "Sore throat, nasal congestion, mild fever",
        "Onset and Duration of Symptoms": "Started 2 days ago",
        "Severity": 4,
        "Associated Symptoms": "Runny nose, mild cough, occasional headache",
        "Smoking": "No",
        "Alcohol Use": "No",
        "Diet and Nutrition": "Healthy, currently drinking more fluids",
        "Physical Activity Level": "Active, but resting due to illness",
        "Sleep Patterns": "Slightly disrupted due to congestion",
        "Occupational & Environmental Exposure": "Works in an office, exposed to coworkers with colds",
        "Physical Exam Findings": "Red throat, mild nasal congestion, clear lungs",
        "Recent Laboratory Tests": "No recent tests, no need for major testing",
        "Imaging Results": "N/A",
        "ECG, Spirometry, etc.": "N/A",
        "Mental Health History": "No significant issues",
        "Stress Levels": "Mild, related to missing work",
        "Support System": "Lives with roommates, has support",
        "Socioeconomic Factors": "Good financial stability, access to healthcare",
    },
}
