from model_loader import load_model
from chat_memory import ChatMemory

def main():
    chatbot = load_model()
    memory = ChatMemory(max_turns=3)

    print("🤖 Flan-T5 Base Chatbot ready! Type /exit to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "/exit":
            print("Bot: Exiting chatbot. Goodbye!")
            break

        # Build prompt using context from memory
        context = memory.get_context()
        # Combine memory into one paragraph
        context = memory.get_context()
        prompt = f"Answer this question clearly and accurately: {user_input}"


        result = chatbot(prompt, max_new_tokens=100)

        response = result[0]['generated_text'].strip()

        # Show response and update memory
        print(f"AI: {response}\n")
        memory.add_turn(user_input, response)

if __name__ == "__main__":
    main()
