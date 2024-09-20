from openai import OpenAI
import streamlit as st

# Predefined dataset of questions and answers
qa_data = [
    {
        "question": "What does the eligibility verification agent (EVA) do?",
        "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    },
    {
        "question": "What does the claims processing agent (CAM) do?",
        "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    },
    {
        "question": "How does the payment posting agent (PHIL) work?",
        "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
    },
    {
        "question": "Tell me about Thoughtful AI's Agents.",
        "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
    },
    {
        "question": "What are the benefits of using Thoughtful AI's agents?",
        "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
    }
]

# Generate the system prompt dynamically based on the predefined Q&A
def generate_system_prompt(qa_data):
    prompt = "You are a helpful AI assistant. Answer the following questions using the exact responses provided if the user asks the same or a similar question. If the question is different, generate an appropriate response.\n\n"
    
    for qa in qa_data:
        prompt += f"Question: {qa['question']}\nAnswer: {qa['answer']}\n\n"
    
    return prompt

# Streamlit app UI
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/Avidness/tai_simple_chatbot)"

st.title("💬 Thoughtful AI Customer Support Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI with predefined answers for Thoughtful AI")

# Initialize message session state if not already done
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you with Thoughtful AI?"}]

# Show past conversation history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input through chat interface
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    # Add user's question to session state messages
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Generate the system prompt with predefined questions and answers
    system_prompt = generate_system_prompt(qa_data)
    
    # Initialize OpenAI client
    client = OpenAI(api_key=openai_api_key)

    # Append the system prompt as the first message in the conversation
    st.session_state.messages.insert(0, {"role": "system", "content": system_prompt})

    # Call the OpenAI API using the messages in session state
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state["messages"]
        )
        msg = response.choices[0].message.content

        # Add the assistant's response to the session state messages
        st.session_state["messages"].append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

    except Exception as e:
        st.error(f"An error occurred: {e}")
