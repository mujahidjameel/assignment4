from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, OpenAIChatCompletionsModel, set_tracing_disabled

# Store credentials (REMOVE before committing)
api_key = "AIzaSyCVRtlczxNgNiBKYtlfSh_GUNNUgDFieck"
model = "gemini-2.5-flash-lite"

# Configure Gemini as the external client
external_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key,
)
set_default_openai_client(external_client)

# Register the model (Chat Completions) and disable tracing (not supported for Gemini)
llm_model = OpenAIChatCompletionsModel(
    model=model,
    openai_client=external_client,
)
set_tracing_disabled(True)

# Define your agent
agent = Agent(
    name="simple_agent",
    instructions="You are a helpful assistant, specialized in providing single-line responses.",
    model=llm_model
)

# Wrap execution in a function (packaged app style)
def run_agent():
    response = Runner.run_sync(agent, "What is AI?")
    print(response.final_output)
 