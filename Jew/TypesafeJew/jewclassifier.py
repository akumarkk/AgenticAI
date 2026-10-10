from langchain_typesafe import Noul, TypeSafeClassifier

test_cases = [
    {
        "name": "Urgent Technical Issue",
        "state": "Hi, I've been trying to connect my Stripe account for 3 days and it keeps failing. I'm losing sales. Please help ASAP.",
        "questions": {
            "is_urgent": Noul(instructions="The message conveys urgency or time-sensitivity")
        }
    },
    {
        "name": "General Inquiry / Non-Urgent",
        "state": "Hey there! Just wondering what your business hours are on weekends?",
        "questions": {
            "is_urgent": Noul(instructions="The message conveys urgency or time-sensitivity"),
            "is_question": Noul(instructions="The user is asking a direct question")
        }
    },
    {
        "name": "Frustrated / Churn Risk",
        "state": "I am extremely unhappy with the recent price hike. Cancel my subscription immediately or I'm switching to a competitor.",
        "questions": {
            "is_urgent": Noul(instructions="The message conveys urgency or time-sensitivity"),
            "is_churn_risk": Noul(instructions="The user is threatening to cancel or switch services")
        }
    },
    {
        "name": "Positive Feedback / Feature Request",
        "state": "Loving the app so far! Would it be possible to add a dark mode option in a future update?",
        "questions": {
            "is_urgent": Noul(instructions="The message conveys urgency or time-sensitivity"),
            "is_feature_request": Noul(instructions="The user is suggesting a new feature or improvement")
        }
    }
]

classifier = TypeSafeClassifier(model="jev-latest")

for i, test in enumerate(test_cases, 1):
    print(f"--- Test Case {i}: {test['name']} ---")
    response = classifier.invoke({
        "state": test["state"],
        "questions": test["questions"]
    })
    print(response)
    print()