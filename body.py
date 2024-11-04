from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

number_pressed = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def button_pressed():
    global number_pressed
    data = request.json

    clicked = data.get("clicked", False)

    if clicked:
        click_count += 1
        print("button pressed ", click_count)
        
    return jsonify({"status": "1"})

if __name__ == '__main__':
    app.run(debug=True)