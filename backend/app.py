from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import create_agent
from db import init_db, save_message, get_history

init_db()

app = Flask(__name__)
CORS(app)
agent, kb = create_agent()

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_input = data.get("message", "")
        
        if not user_input:
            return jsonify({"reply": "Please enter a message."}), 400
        
        print("👤 USER SAID:", user_input)

        history = get_history()
        formatted_history = "\n".join([f"{h['role']}: {h['content']}" for h in history])

        # Use invoke for RunnableSequence
        response = agent.invoke({
            "history": formatted_history,
            "user_input": user_input
        })

        # Extract content from the response
        if hasattr(response, 'content'):
            response_content = response.content
        else:
            response_content = str(response)

        # Save to database
        save_message("user", user_input)
        save_message("assistant", response_content)

        print("🤖 AI RESPONSE:", response_content)

        return jsonify({"reply": response_content}), 200

    except Exception as e:
        print("❌ ERROR:", str(e))
        import traceback
        traceback.print_exc()
        return jsonify({"reply": "Sorry, I encountered an error processing your request."}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)