import json
import requests
import pkg_resources
import openai
from xblock.core import XBlock
from xblock.fields import Integer, String, Scope
from xblock.fragment import Fragment


class ChatgptXBlock(XBlock):
    # Define the fields of the XBlock
    question = String(
        default='',
        scope=Scope.user_state,
        help='The question asked by the user'
    )
    answer = String(
        default='',
        scope=Scope.user_state,
        help='The answer provided by ChatGPT'
    )

    api_key = String(
        default="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",
        scope=Scope.settings,
        help="Your OpenAI API key",
    )

    # TO-DO: Add any additional fields you need here.

    editable_fields = [
        'api_key',
    ]

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the ChatgptXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/chatgptxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/chatgptxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/chatgptxblock.js"))
        frag.initialize_js('ChatgptXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions. You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def get_answer(self, data, suffix=''):
        # Get the user's question
        question = data['question']
        self.question = question

        # Add context to the prompt for better domain-specific responses
        context = "We are the Quantum Computing Research Group in The Centre for Quantum Technologies (CQT) in Singapore. Quantum computing is a field of study focused on the development of computer technologies based on the principles of quantum theory. It involves the use of quantum bits or qubits, which can exist in multiple states simultaneously, allowing for more efficient and powerful computation."
        prompt = f"{context}\n\nQuestion: {question}\nAnswer:"

        # Send the user's question to the text-davinci-002 model using the OpenAI API
        model = "curie"
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=["\n"],
            temperature=0.5,
        )

        # Extract the response from the OpenAI API and store it
        answer = response.choices[0].text.strip()
        self.answer = answer

        # Return the response to the JavaScript function in the HTML file
        return {'answer': answer}


    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ChatgptXBlock",
             """<chatgptxblock/>
             """),
            ("Multiple ChatgptXBlock",
             """<vertical_demo>
                <chatgptxblock/>
                <chatgptxblock/>
                <chatgptxblock/>
                </vertical_demo>
             """),
        ]
