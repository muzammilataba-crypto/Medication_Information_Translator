import streamlit as st

from fda_client import FDAClient
from ai_translator import AITranslator
from search_history import SearchHistory


# -----------------------------------
# APPLICATION CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Medication Information Translator",
    page_icon="💊",
    layout="wide"
)


# -----------------------------------
# APPLICATION TITLE
# -----------------------------------

st.title("💊 Medication Information Translator")

st.write(
    "Search for medications and understand "
    "complicated medical information using AI."
)

st.info(
    "This application provides educational medication "
    "information. It does not replace professional "
    "medical advice."
)


# -----------------------------------
# INITIALIZE APPLICATION COMPONENTS
# -----------------------------------

fda = FDAClient()

history_manager = SearchHistory()


# -----------------------------------
# SESSION STATE
# -----------------------------------

if "medication" not in st.session_state:

    st.session_state.medication = None

if "ai_explanation" not in st.session_state:

    st.session_state.ai_explanation = None


# -----------------------------------
# MEDICATION SEARCH
# -----------------------------------

st.header("Search Medication")

with st.form("medication_search_form"):

    medication_name = st.text_input(
        "Enter medication name",
        placeholder="Example: Paracetamol"
    )

    search_button = st.form_submit_button(
        "Search Medication"
    )


if search_button:

    if not medication_name.strip():

        st.warning("Please enter a medication name.")

    else:

        with st.spinner("Searching FDA database..."):

            medication = fda.search_medication(
                medication_name.strip()
            )

        if medication:

            st.session_state.medication = medication

            st.session_state.ai_explanation = None

            history_manager.add_search(
                medication_name.strip()
            )

            st.success("Medication information retrieved!")

        else:

            st.session_state.medication = None

            st.error(
                "We could not find this medication. "
                "Try another name."
            )


# -----------------------------------
# DISPLAY MEDICATION INFORMATION
# -----------------------------------

if st.session_state.medication:

    medication = st.session_state.medication

    st.divider()

    st.header("Medication Information")

    st.subheader(medication.name)

    information = medication.get_information()

    for category, details in information.items():

        if category == "Medication Name":

            continue

        with st.expander(category, expanded=True):

            st.write(details)


    # -----------------------------------
    # AI TRANSLATION
    # -----------------------------------

    st.divider()

    st.header("🤖 Understand with AI")

    st.write(
        "Let Gemini AI explain the medical information "
        "in simpler, everyday English."
    )

    if st.button("Simplify Medical Information"):

        medical_text = f"""
        Medication: {medication.name}

        Uses:
        {medication.uses}

        Dosage and Instructions:
        {medication.dosage}

        Side Effects:
        {medication.side_effects}

        Warnings:
        {medication.warnings}
        """

        with st.spinner("AI is simplifying the information..."):

            try:

                translator = AITranslator()

                explanation = translator.simplify(
                    medical_text
                )

                st.session_state.ai_explanation = explanation

            except Exception as error:

                st.error(
                    f"Unable to initialize AI translator: {error}"
                )


    # -----------------------------------
    # DISPLAY AI EXPLANATION
    # -----------------------------------

    if st.session_state.ai_explanation:

        st.success("AI explanation generated!")

        st.markdown(
            st.session_state.ai_explanation
        )

        st.warning(
            "AI-generated explanations may contain errors. "
            "Always verify medical instructions with a "
            "qualified healthcare professional."
        )


# -----------------------------------
# SEARCH HISTORY
# -----------------------------------

st.divider()

st.header("📚 Previous Searches")

history = history_manager.get_history()

if history:

    for record in history:

        st.write(
            f"💊 {record['medication']} "
            f"— {record['date']}"
        )

    if st.button("Clear Search History"):

        history_manager.clear_history()

        st.rerun()

else:

    st.write("You haven't searched for any medications yet.")


# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.caption(
    "Medication Information Translator | "
    "Powered by OpenFDA and Google Gemini AI"
)