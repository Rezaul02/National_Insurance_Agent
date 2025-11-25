const input = document.getElementById("input");
const messages = document.getElementById("messages");
const sendBtn = document.getElementById("send-btn");


function addMessage(sender, text) {
    const div = document.createElement("div");
    div.className = "message-block";
    div.innerHTML = `<strong>${sender}:</strong> ${text}`;

    div.style.padding = "10px";
    div.style.margin = "10px 0";
    div.style.borderRadius = "8px";
    div.style.backgroundColor = sender === "You" ? "#e3f2fd" : "#fff3cd";

    messages.appendChild(div);

    messages.scrollTop = messages.scrollHeight; 

    return div;
}


function sendMessage() {
    const text = input.value.trim();
    if (!text) return;


    addMessage("You", text);
    input.value = "";

    
    const thinking = addMessage("AI", "⏳ Thinking...");

 
    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })
    })
    .then(res => res.json())
    .then(data => {
       
        thinking.innerHTML = `<strong>AI:</strong> ${data.reply}`;
    })
    .catch(err => {
        thinking.innerHTML = `<strong>AI:</strong>  Error: ${err.message}`;
    });
}

sendBtn.onclick = sendMessage;


input.addEventListener("keypress", e => {
    if (e.key === "Enter") sendMessage();
});


window.onload = () => {
    addMessage("AI", "Hello! Ask me anything about life insurance.");
};
