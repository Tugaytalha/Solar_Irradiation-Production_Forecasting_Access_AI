from flask import Flask, request, jsonify
import pandas as pd
import joblib
import datetime
from elevation_api import get_elevation  # Assuming elevation_api.py is in the same directory
from calculate_azimuth import max_azimuth  # Replace with the actual module where max_azimuth is defined

# Load the model and scaler
model = joblib.load('best_solar_model.pkl')
scaler = joblib.load('scaler.pkl')

app = Flask(__name__)


@app.route('/predict_energy', methods=['POST'])
def predict_energy():
    try:
        # Get the request data
        data = request.json
        latitude = float(data['latitude'])
        longitude = float(data['longitude'])
        kwh_price = float(data['kwh_price'])

        # Optional inputs, either area+efficiency or wattage
        panel_area = data.get('panel_area')
        panel_efficiency = data.get('panel_efficiency')
        panel_wattage = data.get('panel_wattage')

        # Validate the optional inputs
        if panel_wattage is not None:
            panel_wattage = float(panel_wattage)
        if panel_area is not None and panel_efficiency is not None:
            panel_area = float(panel_area)
            panel_efficiency = float(panel_efficiency)

        # Get the current year and month
        current_time = datetime.datetime.now()
        year = current_time.year
        month = current_time.month

        # Calculate elevation using get_elevation function
        try:
            elevation = get_elevation(latitude, longitude)[0]
        except:
            elevation = 100

        # # Calculate azimuth (month_number * 30 + 15 for the day of year)
        # day_of_year = (month * 30) + 15
        # azimuth = max_azimuth(latitude, longitude, day_of_year)
        #
        #
        # input_data = {
        #     'Azimuth (deg)': [float(azimuth)],
        #     'Longitude': [float(longitude)],
        #     'Elevation': [float(elevation)],
        #     'Latitude': [float(latitude)],
        #     'Year': [float(year)],
        #     'Month': [float(month)]
        # }

        input_frames = []
        # Prepare the yearly input for the model
        for i in range(0, 12):
            # Calculate azimuth (month_number * 30 + 15 for the day of year)
            day_of_year = (i * 30) + 15
            azimuth = max_azimuth(latitude, longitude, day_of_year)

            input_data = {
                'Azimuth (deg)': [float(azimuth)],
                'Longitude': [float(longitude)],
                'Elevation': [float(elevation)],
                'Latitude': [float(latitude)],
                'Year': [float(year)],
                'Month': [float(i)]
            }
            # Create a DataFrame for the model input and ensure all values are floats
            custom_input = pd.DataFrame(input_data)

            # Normalize the custom input
            custom_input[['Azimuth (deg)', 'Longitude', 'Elevation', 'Latitude', 'Year', 'Month']] = scaler.transform(custom_input)

            input_frames.append(custom_input)



        # # Create a DataFrame for the model input and ensure all values are floats
        # custom_input = pd.DataFrame(input_data)
        #
        # # Normalize the custom input
        # custom_input[['Azimuth (deg)', 'Longitude', 'Elevation', 'Latitude', 'Year', 'Month']] = scaler.transform(custom_input)

        # Predict solar irradiation using the loaded model
        predicted_irradiations = model.predict(input_frames)

        # Predicted irradiation for the next month
        predicted_irradiation = predicted_irradiations[month % 12][0]

        coeff = 0
        # Calculate energy output
        if panel_wattage:
            # If wattage is provided, use it directly
            coeff = panel_wattage
            energy_output = coeff * predicted_irradiation / 1000  # Convert Wh to kWh
        else:
            # Calculate energy using area and efficiency
            coeff = panel_area * panel_efficiency
            energy_output = coeff * predicted_irradiation / 1000  # Convert Wh/m² to kWh

        # Calculate the monthly and yearly profit
        monthly_profit = energy_output * kwh_price

        yearly_profit = 0
        # Calculate the yearly profit
        for i in range(0, 12):
            predicted_irradiation = predicted_irradiations[i][0]
            energy_output = coeff * predicted_irradiation / 1000
            monthly_profit = energy_output * kwh_price
            yearly_profit += monthly_profit




        # Return the result as JSON
        return jsonify({
            'monthly_energy_output_kWh': energy_output,
            'monthly_profit': monthly_profit,
            'yearly_profit': yearly_profit
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        })



if __name__ == '__main__':
    app.run(host="0.0.0.0")
