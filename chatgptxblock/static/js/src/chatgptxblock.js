/* Javascript for ChatgptXBlock. */
function ChatgptXBlock(runtime, element) {
  // Get elements
  var questionInput = element.querySelector('#question-input');
  var submitBtn = element.querySelector('#submit-btn');
  var answerText = element.querySelector('#answer-text');
  var errorMessage = element.querySelector('#error-message');

  // Reflection elements
  var reflectionInput = element.querySelector('#reflection-input');
  var reflectionBtn = element.querySelector('#reflection-submit-btn');

  // Handler URLs
  var getAnswerUrl = runtime.handlerUrl(element, 'get_answer');
  var reflectionUrl = runtime.handlerUrl(element, 'submit_reflection');

  // (8) Helper function to show errors in the UI
  function showError(msg) {
      errorMessage.textContent = msg;
  }

  // (2) Submit question for conversation
  submitBtn.addEventListener('click', function() {
      var question = questionInput.value.trim();
      if (!question) {
          showError('Please enter a question.');
          return;
      }
      // Clear any previous error, show a 'loading...' or similar if desired
      showError('');
      answerText.innerHTML = 'Loading...';

      $.ajax({
          type: "POST",
          url: getAnswerUrl,
          data: JSON.stringify({ question: question }),
          success: function(response) {
              // If there's an 'answer' key, show it. Otherwise, show an error.
              if (response.answer) {
                  answerText.innerHTML = response.answer;
              } else {
                  showError('No answer received.');
              }
          },
          error: function() {
              showError('Error sending question to server.');
          }
      });
  });

  // (6) Submit reflection
  reflectionBtn.addEventListener('click', function() {
      var reflectionText = reflectionInput.value.trim();
      if (!reflectionText) {
          showError('Reflection text is empty. Please type something.');
          return;
      }
      // Clear error
      showError('');

      $.ajax({
          type: "POST",
          url: reflectionUrl,
          data: JSON.stringify({ reflection: reflectionText }),
          success: function(response) {
              if (response.status === 'success') {
                  // Simple success feedback. You could do more advanced UI changes.
                  alert(response.message);
                  reflectionInput.value = '';
              } else {
                  showError(response.message);
              }
          },
          error: function() {
              showError('Error sending reflection to server.');
          }
      });
  });
}
