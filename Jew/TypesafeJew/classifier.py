#from langchain_typesafe import TypeSafeClassifier
from langchain_typesafe import Noul, TypeSafeClassifier

# Initialize the Jev decision classifier
classifier = TypeSafeClassifier(model="jev-latest")

# Invoke with a state and structured question
response = classifier.invoke({
    "state": "Hi, I've been trying to connect my Stripe account for 3 days and it keeps failing. I'm losing sales. Please help ASAP.",
    "questions": {
        # FIX: Wrap the raw dict inside Noul()
        "is_urgent": Noul(
            instructions="The message conveys urgency or time-sensitivity"
        )
    }
})

print(response)

