from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(height, weight):
    """Calculate BMI using height (in meters) and weight (in kilograms)."""
    return weight / (height ** 2)

def bmi_category(bmi):
    """Determine the BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def bmi_report(height, weight, gender):
    """Generate a detailed BMI report."""
    bmi = calculate_bmi(height, weight)
    category = bmi_category(bmi)
    
    report = (
        f"Height: {height:.2f} meters\n"
        f"Weight: {weight:.2f} kilograms\n"
        f"Gender: {gender}\n\n"
        f"Your BMI is: {bmi:.2f}\n"
        f"You are classified as: {category}\n\n"
    )
    
    if category == "Underweight":
        report += (
            "Being underweight can be a sign of malnutrition, an eating disorder, "
            "or other health issues. It's important to consult with a healthcare provider.\n"
        )
    elif category == "Normal weight":
        report += (
            "Great job! Maintaining a healthy weight lowers the risk of serious health problems "
            "and helps to manage chronic conditions. Keep up the good work!\n"
        )
    elif category == "Overweight":
        report += (
            "Being overweight increases the risk of a number of health conditions, including heart disease, "
            "high blood pressure, and type 2 diabetes. Consider consulting with a healthcare provider for advice.\n"
        )
    elif category == "Obesity":
        report += (
            "Obesity is associated with a higher risk of various health conditions, including heart disease, "
            "diabetes, and certain cancers. It's important to seek advice from a healthcare provider.\n"
        )
    
    return report

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            gender = request.form['gender']
            report = bmi_report(height, weight, gender)
            return render_template('result.html', report=report)
        except Exception as e:
            # Print the exception to the console for debugging
            print(f"Error: {e}")
            return f"An error occurred: {e}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
