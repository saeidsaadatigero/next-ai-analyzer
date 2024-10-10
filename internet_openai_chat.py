#internet_openai_chat.py
from openai import OpenAI
from tavily import TavilyClient
import json
import time


class Chatbot:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        self.assistant = self.client.beta.assistants.retrieve(os.getenv("ASSISTANT_ID"))


    def tavily_search(self, query):
        search_result = self.tavily_client.get_search_context(query, search_depth="advanced", max_tokens=8000)
        return search_result

    def wait_for_run_completion(self, thread_id, run_id):
        while True:
            time.sleep(1)
            current_run = self.client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if current_run.status in ['completed', 'failed', 'requires_action']:
                return current_run

    def submit_tool_outputs(self, thread_id, run_id, tools_to_call):
        tool_output_array = []
        for tool in tools_to_call:
            output = None
            tool_call_id = tool.id
            function_name = tool.function.name
            function_args = tool.function.arguments

            if function_name == "tavily_search":
                output = self.tavily_search(query=json.loads(function_args)["query"])

            if output:
                tool_output_array.append({"tool_call_id": tool_call_id, "output": output})

        return self.client.beta.threads.runs.submit_tool_outputs(
            thread_id=thread_id,
            run_id=run_id,
            tool_outputs=tool_output_array
        )

    def get_last_message_from_thread(self, thread_id):
        messages = self.client.beta.threads.messages.list(thread_id=thread_id)
        for msg in messages:
            return msg.role, msg.content[0].text.value

    def create_thread(self):
        thread = self.client.beta.threads.create()
        return thread

    def chat(self, text, thread):
        message = self.client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=text,
        )

        # Create a run
        run = self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=self.assistant.id,
        )

        # Wait for run to complete
        run = self.wait_for_run_completion(thread.id, run.id)

        if run.status == 'requires_action':
            run = self.submit_tool_outputs(thread.id, run.id, run.required_action.submit_tool_outputs.tool_calls)
            run = self.wait_for_run_completion(thread.id, run.id)

        # Print messages from the thread
        role, content = self.get_last_message_from_thread(thread.id)

        return content
