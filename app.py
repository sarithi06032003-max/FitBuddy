from flask import Flask, request, render_template, jsonify
from workout_generator import generate_workout_plan
from nutrition_generator import generate_nutrition_tip
from plan_updater import update_workout_plan
from storage import save_user_plan, get_user_plans

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    plan = generate_workout_plan(data)
    tip = generate_nutrition_tip(data)
    save_user_plan(data.get('user_id','test_user'), data, plan)
    return jsonify({"workout_plan": plan, "nutrition_tip": tip})

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    new_plan = update_workout_plan(data['original_plan'], data['feedback'])
    return jsonify({"updated_plan": new_plan})

if __name__ == '__main__':
    app.run(debug=True)