const API_KEY = "YOUR_OPENAI_API_KEY"; // Replace with OpenAI API Key
const chatWindow = document.getElementById("chat-window");
const messageInput = document.getElementById("message");
const sendButton = document.getElementById("send");
const searchReasonButton = document.getElementById("search-reason");
const imageUploadButton = document.getElementById("image-upload");

// Event Listeners
sendButton.addEventListener("click", sendMessage);
messageInput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") sendMessage();
});

// Sending Messages
async function sendMessage() {
    let messageText = messageInput.value.trim();
    if (messageText === "") return;

    displayMessage(messageText, "user-message");
    messageInput.value = "";
    
    displayTypingIndicator();

    try {
        let response = await fetch("https://api.openai.com/v1/chat/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${API_KEY}`
            },
            body: JSON.stringify({
                model: "gpt-3.5-turbo",
                messages: [{ role: "user", content: messageText }]
            })
        });

        let data = await response.json();
        removeTypingIndicator();

        if (data.choices && data.choices.length > 0) {
            let botResponse = data.choices[0].message.content;
            displayMessage(botResponse, "bot-message");
        } else {
            displayMessage("hey how are you i m not funtoinal i m only non funtoinal clone", "bot-message");
        }

    } catch (error) {
        removeTypingIndicator();
        displayMessage("Error: Could  connect to AI.", "bot-message");
    }
}

// Display Messages
function displayMessage(text, className) {
    let messageDiv = document.createElement("div");
    messageDiv.classList.add("message", className);
    messageDiv.textContent = text;
    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

// Typing Indicator
function displayTypingIndicator() {
    let typingDiv = document.createElement("div");
    typingDiv.classList.add("typing-indicator");
    typingDiv.id = "typing-indicator";
    typingDiv.textContent = "ChatGPT is typing...";
    chatWindow.appendChild(typingDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function removeTypingIndicator() {
    let typingDiv = document.getElementById("typing-indicator");
    if (typingDiv) typingDiv.remove();
}

// Image Upload Feature (To Be Implemented)
imageUploadButton.addEventListener("click", () => {
    alert("Image upload feature coming soon!");
});
