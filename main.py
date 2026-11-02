from agents.data_agent import data_agent
from langchain_core.messages import HumanMessage

if __name__ == "__main__":
    print("\n🤖 AI Data Agent")
    print("Enter a task, or type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            print("Agent stopped.")
            break

        if not user_input:
            continue

        try:
            response = data_agent.invoke({
                "messages": [HumanMessage(content=user_input)],
                "route_response": ""
            })

            messages = response.get("messages", [])
            if messages:
                last_message = messages[-1]
                content = getattr(last_message, "content", "")
                print("\n🤖 Agent:", content or "Task completed. Check the output files.")
            else:
                print("\n🤖 Agent:", response)

        except Exception as e:
            print(f"\nError: {e}")