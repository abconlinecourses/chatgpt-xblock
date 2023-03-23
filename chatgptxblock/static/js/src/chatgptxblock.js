/* Javascript for ChatgptXBlock. */
function ChatgptXBlock(runtime, element) {
// Get the input field and submit button
var questionInput = element.querySelector('#question-input');
var submitBtn = element.querySelector('#submit-btn');

// Add a click event listener to the submit button
submitBtn.addEventListener('click', function() {
  // Get the user's question from the input field
  var question = questionInput.value;

  // Send the user's question to the XBlock's handler
  var handlerUrl = runtime.handlerUrl(element, 'get_answer');
  $.ajax({
    type: "POST",
    url: handlerUrl,
    data: JSON.stringify({
      question: question
    }),
    success: function(response) {
      // Display the response from the XBlock's handler
      var answerText = element.querySelector('#answer-text');
      answerText.innerHTML = response.answer;
    },
    error: function() {
      console.log('Error sending question to server.');
    }
  });
});
}