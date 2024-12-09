from flask import Flask, render_template, request, redirect, url_for, flash
from calculations import calculate_tank_requirements

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Collect user inputs from the form
        household_size = int(request.form['household_size'])
        tank_type = request.form['tank_type']
        wastewater_flow = float(request.form['wastewater_flow'])
        retention_time = float(request.form['retention_time'])
        
        # Optional inputs for 3-chambered tanks
        soil_type = request.form.get('soil_type')
        groundwater_depth = request.form.get('groundwater_depth')
        borehole_distance = request.form.get('borehole_distance')

        # Prepare inputs for calculations
        user_inputs = {
            "household_size": household_size,
            "tank_type": tank_type,
            "wastewater_flow": wastewater_flow,
            "retention_time": retention_time,
            "soil_type": soil_type,
            "groundwater_depth": groundwater_depth,
            "borehole_distance": borehole_distance,
        }

        # Perform calculations
        results = calculate_tank_requirements(user_inputs)

        return render_template('result.html', results=results)

    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        return redirect(url_for('home'))

@app.route('/knowledge')
def knowledge():
    return render_template('knowledge.html')

if __name__ == '__main__':
    app.run(debug=True)
