/* Javascript for ChatgptXBlock. */
function ChatgptXBlock(runtime, element) {
  // Get elements
  var questionInput = $('#question-input', element);
  var submitBtn = $('#submit-btn', element);
  var answerText = $('#answer-text', element);
  var errorMessage = $('#error-message',element);

  // Reflection elements
  var reflectionInput = $('#reflection-input', element);
  var reflectionBtn =$('#reflection-submit-btn', element);

  // Handler URLs
  var getAnswerUrl = runtime.handlerUrl(element, 'get_answer');
  var reflectionUrl = runtime.handlerUrl(element, 'submit_reflection');

  // (8) Helper function to show errors in the UI
  function showError(msg) {
      errorMessage.textContent = msg;
  }

  // (2) Submit question for conversation
  submitBtn.click(function (eventObject) {
      var question = questionInput.val();
      if (!question) {
          showError('Please enter a question.');
          return;
      }
      // Clear any previous error, show a 'loading...' or similar if desired
      showError('');
      answerText.text('Loading...');

      $.ajax({
          type: "POST",
          url: getAnswerUrl,
          data: JSON.stringify({ question: question }),
          success: function(response) {
              // If there's an 'answer' key, show it. Otherwise, show an error.
              if (response.answer) {
                  answerText.text(response.answer);
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
  reflectionBtn.click(function() {
      var reflectionText = reflectionInput.val();
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
                  reflectionInput.text('');
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
