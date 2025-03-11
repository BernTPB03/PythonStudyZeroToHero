import os

try:
    project_id = os.environ["PROJECT_ID"]
except KeyError:
    project_id = input("Please enter your project_id (hit enter): ")

from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

print([model.name for model in ModelTypes])

model_id = ModelTypes.STARCODER

from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

parameters = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 100,
    GenParams.STOP_SEQUENCES: [""]
}

from ibm_watson_machine_learning.foundation_models import Model

model = Model(
    model_id=model_id,
    params=parameters,
    credentials=wml_credentials,
    project_id=project_id
)

instruction = """Using the directions below, generate Python code for the given task.

Input:
# Write a Python function that prints 'Hello World!' string 'n' times.

Output:
def print_n_times(n):
    for i in range(n):
        print("Hello World!")
"""

question = """Input:
# Write a Python function, which generates sequence of prime numbers.
# The function 'primes' will take the argument 'n', an int. It will return a list which contains all primes less than 'n'."""

result = model.generate_text(" ".join([instruction, question]))

code_as_text = result.split('Output:')[1].split('')[0]

print(code_as_text)

exec(code_as_text)

n = 25
primes(n)