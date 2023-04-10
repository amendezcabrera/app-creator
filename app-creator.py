import openai
from dotenv import load_dotenv
import os

print("Welcome to the app creator script!")
print("This script will generate code for several screens based on provided descriptions and tests.")
print("Please ensure that you have the OpenAI API key set up correctly before continuing. Add it to a `.env` file next to this with the next format: OPENAI_API_KEY=MY_API_KEY")

load_dotenv()

# set up OpenAI API credentials
openai.api_key = os.getenv('OPENAI_API_KEY')

# define screens and their respective descriptions
screens = [
    {
        "name": "main_screen",
        "description": "A screen with a side Drawer containing a profile picture and a list of items, a map and a Floating Action Button that opens a new form dialog screen."
    }
]

# loop through each screen and request tests and generate code based on the description
for screen in screens:
    # use the OpenAI API to request tests for the screen based on the description
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Flutter mobile testing expert and I need you to provide the source code required for the test suite."},
            {"role": "user", "content": "The tests to fill the requirements of the following screen: " + screen['description']},
        ]
    )

    # extract the generated tests from the API response
    tests = response['choices'][0]['message']['content'].strip()
    print("Tests")
    print(tests)

    # use the OpenAI API to generate code that passes the provided tests
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Flutter mobile development and testing expert and I need you to provide the source code required for the screen"},
            {"role": "user", "content": "Given the following tests:\n{}For the screen:\n{}\nWrite the Flutter Widget source code:".format(tests, screen['description'])},
        ]
    )

    # extract the generated code from the API response
    code = response['choices'][0]['message']['content'].strip()
    print("Source code")
    print(code)

    # save the generated code to a file with a suffix based on the screen name
    with open(screen['name'] + "_sc.txt", "w") as f:
        f.write(code)

    # save the generated tests to a file with a suffix based on the screen name
    with open(screen['name'] + "_test.txt", "w") as f:
        f.write(tests)

print("Code generation complete!")
