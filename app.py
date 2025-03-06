from flask import Flask, render_template, request

app = Flask(__name__)

# ✅ Corrected Quiz Data Structure
quizzes = {
    "java_basics": {
        "title": "Java Basics Quiz",
        "questions": [
            {"question": "What is the default value of an int variable in Java?", "options": ["null", "0", "undefined"], "answer": "0"},
            {"question": "Which keyword is used to create a subclass in Java?", "options": ["extends", "inherits", "implements"], "answer": "extends"},
            {"question": "Which of these is not a Java primitive data type?", "options": ["int", "float", "String"], "answer": "String"},
            {"question": "What is the size of a 'long' variable in Java?", "options": ["4 bytes", "8 bytes", "16 bytes"], "answer": "8 bytes"},
            {"question": "Which of these is used to handle exceptions in Java?", "options": ["try-catch", "catch-try", "exception-handler"], "answer": "try-catch"},
            {"question": "What will `System.out.println(10/3);` print?", "options": ["3.33", "3", "Error"], "answer": "3"},
            {"question": "Which of these collections allows duplicate values?", "options": ["Set", "Map", "List"], "answer": "List"},
            {"question": "Which method is called when an object is created in Java?", "options": ["init()", "constructor", "new()"], "answer": "constructor"},
            {"question": "What is the parent class of all Java classes?", "options": ["Object", "Main", "Super"], "answer": "Object"},
            {"question": "Which keyword is used to prevent inheritance in Java?", "options": ["final", "static", "private"], "answer": "final"}
        ]
    }
}

@app.route('/')
def home():
    return render_template('home.html', quizzes=quizzes)

@app.route('/quiz/<quiz_id>', methods=['GET', 'POST'])
def quiz(quiz_id):
    # ✅ Ensure quiz exists
    quiz = quizzes.get(quiz_id)
    if quiz is None:
        return "Quiz not found", 404

    questions = quiz.get("questions", [])

    if request.method == 'POST':
        score = sum(1 for i, q in enumerate(questions) if request.form.get(f'question_{i}') == q['answer'])
        return render_template('result.html', score=score, total=len(questions))

    return render_template('quiz.html', quiz=quiz, quiz_id=quiz_id, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)
