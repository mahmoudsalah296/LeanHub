import requests
import json

# Flask app URL
BASE_URL = "http://0.0.0.0:5000"


def test_similarity_en(professor_answer, student_answer):
    # Endpoint URL
    url = f"{BASE_URL}/calculate_similarity_en"

    # JSON payload
    payload = {"professor_answer": professor_answer, "student_answer": student_answer}

    # Send POST request
    response = requests.post(url, json=payload)

    # Parse and print response
    if response.status_code == 200:
        data = json.loads(response.text)
        similarity_score = data["similarity_score"]
        print(f"Similarity score (English): {similarity_score}")
    else:
        print(f"Error {response.status_code}: {response.text}")


def test_similarity_ar(professor_answer, student_answer):
    # Endpoint URL
    url = f"{BASE_URL}/calculate_similarity_ar"

    # JSON payload
    payload = {"professor_answer": professor_answer, "student_answer": student_answer}

    # Send POST request
    response = requests.post(url, json=payload)

    # Parse and print response
    if response.status_code == 200:
        data = json.loads(response.text)
        similarity_score = data["similarity_score"]
        print(f"Similarity score (Arabic): {similarity_score}")
    else:
        print(f"Error {response.status_code}: {response.text}")


if __name__ == "__main__":
    # Test English similarity
    test_similarity_en(
	    "I don't like this course. It's boring.",
	    "I dislike this course. It's not interesting.")

    # Test Arabic similarity
    test_similarity_ar("لم يعجبني هذا الفيلم لقد كان مملا", "لقد كرهت ذلك الفيلم لم يكن مشوقا.")
