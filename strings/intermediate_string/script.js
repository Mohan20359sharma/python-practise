// Track the current user (toggle between user1 and user2)
let isUser1 = true;

// Event listener for the send button
document.getElementById('send-button').addEventListener('click', sendMessage);

// Event listener for the Enter key
document.getElementById('message-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Function to send a message
function sendMessage() {
    const input = document.getElementById('message-input');
    const messageText = input.value.trim();

    if (messageText) {
        const chatBox = document.getElementById('chat-box');
        const messageElement = document.createElement('div');

        // Assign message class based on the user
        messageElement.classList.add('chat-message', isUser1 ? 'user1' : 'user2');
        messageElement.textContent = messageText;
        
        // Append message to chat box
        chatBox.appendChild(messageElement);
        
        // Clear input field
        input.value = '';

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;

        // Toggle user for the next message
        isUser1 = !isUser1;
    }
}
