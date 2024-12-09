from flask import Flask, render_template, request, flash, redirect, url_for
import os  # For reading environment variables
from constants import MIN_BOREHOLE_DISTANCE
from calculations import calculate_tank_requirements

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route('/')
def index():
    """Render the home page."""
    return render_template('home.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    """Handle GET and POST requests for the calculation page."""
    if request.method == 'POST':
        try:
            # Collect common inputs
            household_size = int(request.form.get('household_size', 0))
            tank_type = request.form.get('tank_type')
            seasonal_factor = float(request.form.get('seasonal_factor', 1.0))
            effluent_reuse = request.form.get('effluent_reuse') == "yes"
            prone_to_flooding = request.form.get('flooding_risk') == "yes"
            wastewater_flow = float(request.form.get('wastewater_flow', 0))  # Added input
            retention_time = float(request.form.get('retention_time', 0))  # Added input

            # Initialize optional inputs
            soil_type = request.form.get('soil_type', None)
            groundwater_flow = request.form.get('groundwater_flow', None)
            groundwater_depth = request.form.get('groundwater_depth', None)
            borehole_distance = request.form.get('borehole_distance', None)

            # Validate three-chamber-specific inputs
            if tank_type == "3":
                missing_fields = []
                if not soil_type:
                    missing_fields.append("Soil Type")
                if not groundwater_flow:
                    missing_fields.append("Groundwater Flow Direction")
                if not groundwater_depth:
                    missing_fields.append("Groundwater Depth")
                if not borehole_distance:
                    missing_fields.append("Distance to Borehole")

                if missing_fields:
                    flash(
                        f"Please fill in the following fields for 3-chambered tanks: {', '.join(missing_fields)}.",
                        "warning"
                    )
                    return redirect(url_for('calculate'))

                # Convert numeric fields
                groundwater_depth = float(groundwater_depth)
                borehole_distance = float(borehole_distance)

                if borehole_distance < MIN_BOREHOLE_DISTANCE:
                    flash(
                        f"Warning: Distance to borehole must be at least {MIN_BOREHOLE_DISTANCE} meters.",
                        "warning"
                    )
                    return redirect(url_for('calculate'))
            else:
                # Reset unused inputs for 4-chambered tanks
                soil_type = None
                groundwater_flow = None
                groundwater_depth = None
                borehole_distance = None

            # Collect user inputs into a dictionary
            user_inputs = {
                "household_size": household_size,
                "tank_type": tank_type,
                "soil_type": soil_type,
                "groundwater_flow": groundwater_flow,
                "groundwater_depth": groundwater_depth,
                "borehole_distance": borehole_distance,
                "seasonal_factor": seasonal_factor,
                "effluent_reuse": effluent_reuse,
                "prone_to_flooding": prone_to_flooding,
                "wastewater_flow": wastewater_flow,
                "retention_time": retention_time,
            }

            # Perform calculations
            results = calculate_tank_requirements(user_inputs)

            # Render the results page with calculated data
            return render_template('result.html', results=results)

        except ValueError as ve:
            flash(f"Invalid input: {str(ve)}. Please enter valid numerical values.", "danger")
            return redirect(url_for('calculate'))
        except KeyError as ke:
            flash(f"Missing required input: {str(ke)}. Please fill in all required fields.", "danger")
            return redirect(url_for('calculate'))
        except Exception as e:
            flash(f"Unexpected error: {str(e)}", "danger")
            return redirect(url_for('calculate'))

    # Render the form for GET requests
    return render_template('calculate.html')

@app.route('/knowledge')
def knowledge():
    """Render the Knowledge Guide page."""
    return render_template('knowledge.html')

if __name__ == "__main__":
    # Use the `PORT` environment variable (if available) or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)