import streamlit as st

from helper_gemini import gemini_text
from helper_openai import openai_text

time_complexity = False
space_complexity = False
generate_test_data = False
integrate_test_cases = False
perform_code_review = False
explain_code = False
add_error_handling = False

my_output = None


def scrollable_text(text):
    return f'<div style="border: 1px solid black; border-radius: 10px; padding: 20px; overflow-y: scroll; height: 590px; box-shadow: 1px 1px 1px gray, -1px -1px 1px gray, 1px -1px 1px gray, -1px 1px 1px gray;">{text}</div>'


def main():
    st.set_page_config(layout="wide")
    st.title("AI Coding Companion")
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""
    if "prompt" not in st.session_state:
        st.session_state.prompt = ""
    if "output_text" not in st.session_state:
        st.session_state.output_text = ""

    # Configuration sidebar
    st.sidebar.header('Configuration')
    selected_language = st.sidebar.radio(
        'Select AI Model', ['ChatGPT', 'Gemini'])
    st.session_state.api_key = st.sidebar.text_input(label=f'{selected_language} API Key',
                                                     type='password')
    save_key = st.sidebar.button('Save')
    if save_key:
        print("API Key : "+st.session_state.api_key)
        # st.session_state.api_key = api_key

    # write a session state variable with the name prompt
    st.session_state.prompt = st.text_area(
        label="Enter your prompt", value="")

    # Using columns to create two columns, make one column 2/3 and other 1/3
    col1, col2 = st.columns([2, 1])

    # Adding content to the first column
    with col1:
        my_output = st.markdown(scrollable_text(st.session_state.output_text),
                                unsafe_allow_html=True)

    # Adding content to the second column
    with col2:
        st.header("Customize")
        # Perform Analysis
        st.subheader("Perform Analysis")
        col1, col2 = st.columns(2)
        with col1:
            global time_complexity
            time_complexity = st.checkbox("Time Complexity")
        with col2:
            global space_complexity
            space_complexity = st.checkbox("Space Complexity")

        # Select the language
        st.subheader("Change Language")
        language = st.selectbox(
            label="Select Language",
            options=["Select Language", "Python",
                     "JAVA", "C++", "C#", "JavaScript",
                     "Pascal", "TypeScript",
                     "TSX", "JSX", "Vue", "Go",
                     "C", "Visual Basic .NET",
                     "SQL", "Assembly Language", "PHP", "Ruby",
                     "Swift", "SwiftUI", "Kotlin", "R", "Objective-C",
                     "Perl", "SAS", "Scala", "Dart", "Rust", "Haskell",
                     "Lua", "Groovy", "Elixir", "Clojure", "Lisp", "Julia",
                     "Matlab", "Fortran", "COBOL", "Bash", "Powershell",
                     "PL/SQL", "CSS", "Racket", "HTML", "NoSQL", "CoffeeScript"]
        )

        # Testing Tools
        st.subheader("Testing Tools")
        col1, col2 = st.columns(2)
        with col1:
            global generate_test_data
            generate_test_data = st.checkbox("Generate Test Data")
        with col2:
            global integrate_test_cases
            integrate_test_cases = st.checkbox("Integrate Test Cases")

        # More Actions
        st.subheader("More Actions")
        col1, col2 = st.columns(2)

        with col1:
            global perform_code_review
            perform_code_review = st.checkbox("Perform Code Review")

        with col2:
            global explain_code
            explain_code = st.checkbox("Explain Code")

        with col1:
            global add_error_handling
            add_error_handling = st.checkbox("Add Error Handling")

        send = st.button("Send", use_container_width=True)
        if send:
            if st.session_state.prompt:
                st.session_state.prompt = f"Perform the following functions.\n \
                    - {st.session_state.prompt}"
                if time_complexity:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Find time complexity of the generated code."
                if space_complexity:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Find space complexity of the generated code."
                if language != "Select Language":
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Convert this code into {language}."
                if generate_test_data:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Generate test data for the generated code."
                if integrate_test_cases:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Integrate test cases for the generated code."
                if perform_code_review:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Perform code review for the generated code."
                if explain_code:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Explain the generated code."
                if add_error_handling:
                    st.session_state.prompt = st.session_state.prompt + \
                        f"\n - Add error handling for the generated code."
                print("Prompt : "+st.session_state.prompt)
                print("API Key : "+st.session_state.api_key)
                print("Selected Language : "+selected_language)
                if selected_language == 'ChatGPT':
                    st.session_state.output_text = openai_text(
                        st.session_state.prompt, st.session_state.api_key)
                elif selected_language == 'Gemini':
                    st.session_state.output_text = gemini_text(
                        st.session_state.prompt, st.session_state.api_key)
                my_output.markdown(scrollable_text(
                    st.session_state.output_text),
                    unsafe_allow_html=True)

        # # Button to reset the form
        # with col2:
        #     reset = st.button("Reset")


if __name__ == "__main__":
    main()
