import streamlit as st
from dotenv import load_dotenv

from data.patients import LLM_SUMMARY_TEMPLATE, PATIENTS

load_dotenv()


# https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps

from secret.secret_chat_server import SecretChat

secret_chat = SecretChat()


# Streamlit UI
st.set_page_config(layout="wide")
st.title("Doctor's Auscultation Assistant")


def generate_summary(data):
    message = LLM_SUMMARY_TEMPLATE.format(**data)
    messages = [
        ("human", message),
    ]
    response = secret_chat.invoke(messages, stream=False)
    return response.content


col1, col2 = st.columns([1, 1])


# Initialize session state for selected patient
if "selected_patient" not in st.session_state:
    st.session_state.selected_patient = next(iter(PATIENTS))

# Sidebar for patient selection with styled buttons
st.sidebar.header("Patients of the Day")
selected_patient = st.session_state.selected_patient
st.sidebar.markdown(f"### Selected Patient: **{selected_patient}**")

for patient in PATIENTS.keys():
    if st.sidebar.button(
        patient,
        use_container_width=True,
        key=patient,
        help="Click to select this patient",
        disabled=patient == selected_patient,
    ):
        st.session_state.selected_patient = patient


patient_data = PATIENTS[selected_patient]

with col1:
    st.header("Patient Information")

    with st.expander("Basic Information"):
        name = st.text_input(
            "Full Name", value=patient_data.get("Full Name", selected_patient)
        )
        age = st.number_input(
            "Age", min_value=0, max_value=150, step=1, value=patient_data.get("Age", 0)
        )
        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"],
            index=["Male", "Female", "Other"].index(patient_data.get("Gender", "Male")),
        )
        dob = st.date_input("Date of Birth", value=patient_data.get("Date of Birth"))

    with st.expander("Vital Signs"):
        heart_rate = st.number_input(
            "Heart Rate (bpm)", value=patient_data.get("Heart Rate (bpm)", 0)
        )
        blood_pressure = st.text_input(
            "Blood Pressure (mmHg)", value=patient_data.get("Blood Pressure (mmHg)", "")
        )
        respiratory_rate = st.number_input(
            "Respiratory Rate (breaths per min)",
            value=patient_data.get("Respiratory Rate (breaths per min)", 0),
        )
        temperature = st.number_input(
            "Temperature (°C)", value=patient_data.get("Temperature (°C)", 0.0)
        )
        oxygen_saturation = st.number_input(
            "Oxygen Saturation (%)", value=patient_data.get("Oxygen Saturation (%)", 0)
        )

    with st.expander("Medical History"):
        past_diagnoses = st.text_area(
            "Past Diagnoses", value=patient_data.get("Past Diagnoses", "")
        )
        previous_surgeries = st.text_area(
            "Previous Surgeries", value=patient_data.get("Previous Surgeries", "")
        )
        hospitalizations = st.text_area(
            "Hospitalizations", value=patient_data.get("Hospitalizations", "")
        )
        family_history = st.text_area(
            "Family Medical History",
            value=patient_data.get("Family Medical History", ""),
        )
        allergies = st.text_area("Allergies", value=patient_data.get("Allergies", ""))
        medications = st.text_area(
            "Current Medications", value=patient_data.get("Current Medications", "")
        )

    with st.expander("Symptoms & Presenting Complaint"):
        chief_complaint = st.text_area(
            "Chief Complaint", value=patient_data.get("Chief Complaint", "")
        )
        onset = st.text_input(
            "Onset and Duration of Symptoms",
            value=patient_data.get("Onset and Duration of Symptoms", ""),
        )
        severity = st.slider(
            "Severity (1-10)", 1, 10, value=patient_data.get("Severity", 1)
        )
        associated_symptoms = st.text_area(
            "Associated Symptoms", value=patient_data.get("Associated Symptoms", "")
        )

    with st.expander("Lifestyle & Risk Factors"):
        smoking = st.radio(
            "Smoking",
            ["Yes", "No"],
            index=["Yes", "No"].index(patient_data.get("Smoking", "No")),
        )
        alcohol = st.radio(
            "Alcohol Use",
            ["Yes", "Occasionally", "No"],
            index=["Yes", "Occasionally", "No"].index(
                patient_data.get("Alcohol Use", "No")
            ),
        )
        diet = st.text_area(
            "Diet and Nutrition", value=patient_data.get("Diet and Nutrition", "")
        )
        physical_activity = st.text_area(
            "Physical Activity Level",
            value=patient_data.get("Physical Activity Level", ""),
        )
        sleep_patterns = st.text_area(
            "Sleep Patterns", value=patient_data.get("Sleep Patterns", "")
        )
        occupational_exposure = st.text_area(
            "Occupational & Environmental Exposure",
            value=patient_data.get("Occupational & Environmental Exposure", ""),
        )

    with st.expander("Examinations & Tests"):
        physical_exam = st.text_area(
            "Physical Exam Findings",
            value=patient_data.get("Physical Exam Findings", ""),
        )
        lab_tests = st.text_area(
            "Recent Laboratory Tests",
            value=patient_data.get("Recent Laboratory Tests", ""),
        )
        imaging_results = st.text_area(
            "Imaging Results", value=patient_data.get("Imaging Results", "")
        )
        additional_tests = st.text_area(
            "ECG, Spirometry, etc.", value=patient_data.get("ECG, Spirometry, etc.", "")
        )

    with st.expander("Psychological & Social History"):
        mental_health = st.text_area(
            "Mental Health History", value=patient_data.get("Mental Health History", "")
        )
        stress_levels = st.text_area(
            "Stress Levels", value=patient_data.get("Stress Levels", "")
        )
        support_system = st.text_area(
            "Support System", value=patient_data.get("Support System", "")
        )
        socioeconomic_factors = st.text_area(
            "Socioeconomic Factors", value=patient_data.get("Socioeconomic Factors", "")
        )

    submit = st.button("Generate Summary")

with col2:
    st.header("LLM Chat and Summary")
    st.caption(
        "Note: we are using Secret AI SDK allowing to maintain privacy during the exchange."
    )

    if submit:
        # Get the variables from the page
        patient_data = {key: value for key, value in locals().items()}

        summary = generate_summary(patient_data)
        st.subheader("Summary")
        st.write(summary)

    st.subheader("Ask the LLM")
    user_query = st.text_input("Ask a question about the patient")
    if user_query:
        # response = llm(user_query)
        st.write("response")


# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = [
#         {
#             "role": "assistant",
#             "content": "You are my therapist. Help me with my issues.",
#         }
#     ]

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Accept user input
# if prompt := st.chat_input("What is up?"):
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Display assistant response in chat message container
#     with st.chat_message("assistant"):
#         assistant_response = secret_chat.invoke(st.session_state.messages)

#         # FIXME: loader input?

#         message_placeholder = st.empty()
#         # full_response = ""
#         # assistant_response = random.choice(
#         #     [
#         #         "Hello there! How can I assist you today?",
#         #         "Hi, human! Is there anything I can help you with?",
#         #         "Do you need help?",
#         #     ]
#         # )
#         # Simulate stream of response with milliseconds delay

#         print(assistant_response)

#         message_placeholder.markdown(assistant_response)
#     #     for chunk in assistant_response.split():
#     #         full_response += chunk + " "
#     #         time.sleep(0.05)
#     #         # Add a blinking cursor to simulate typing
#     #         message_placeholder.markdown(full_response + "▌")
#     #     message_placeholder.markdown(full_response)
#     # # Add assistant response to chat history
#     st.session_state.messages.append(
#         {"role": "assistant", "content": assistant_response}
#     )
