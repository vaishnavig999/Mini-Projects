import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "<Your GOOGLE_API_KEY>"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def main():

    st.set_page_config(page_title = "SQL Query Generator", page_icon=":robot:")
    st.markdown(
        """
            <div style = "text-align: center;">
            <h1>SQL Query Generator 🤖🦾</h1>
            <h3>I can generate SQL queries for you!!!<h3>
            <p> This tool is a simple tool that allows you to generate SQL queries based on your data</p>

            </div>
        """,
        unsafe_allow_html=True,
    )
   
    # Text area for natural language query input
    text_input = st.text_area("Enter your query in natural language:")

    # Submit button
    submit_button = st.button("Generate")

    if submit_button:
        with st.spinner("Generating sql query..."):
            template="""
                Create a SQL query snippet using below text:

                ```
                    {text_input}
                ```
                I just want a SQL query.

                """
            formatted_template = template.format(text_input = text_input)

            st.write(formatted_template)

            response = model.generate_content(formatted_template)
            sql_query = response.text.strip("```sql")
            # st.write(sql_query)

            with st.container():
                st.success("SQL query generated successfully! Check below: ")
                st.code(sql_query, language = "sql")
        
            with st.expander("Expected Output"):
            # ... Code for expected output generation
                expected_output="""
                    What would be the expected response of this SQL query snippet:
                            ```
                                {sql_query}
                            ```
                    Provide sample tabular response with no explaination

                """
                expected_output_formatted = expected_output.format(sql_query = sql_query)
                eoutput = model.generate_content(expected_output_formatted)
                eoutput = eoutput.text
                # st.write(eoutput)
                st.markdown(eoutput)

            with st.expander("Explain SQL Query"):
            # ... Code for explanation generation
                explaination_output="""
                Explain this sql query:

                    ```
                        {sql_query}
                    ```
                Please provide a simplest explanation of the query in bullet points.

                """
                explaination_output_formatted = explaination_output.format(sql_query = sql_query)
                explaination_output = model.generate_content(explaination_output_formatted)
            
                explaination_output = explaination_output.text
                # st.write(explaination_output)
                st.markdown(explaination_output)

            
            

        
main()