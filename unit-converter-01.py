import streamlit as st
import numpy as np

# Set page config
st.set_page_config(
    page_title="Unit Converter",
    page_icon="📏",
    layout="centered"
)

# Title and description
st.title("📏 Unit Converter")
st.markdown("Convert between different units of measurement easily!")

# Dictionary of conversion factors
conversion_factors = {
    "Length": {
        "Meters": 1,
        "Kilometers": 1000,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
        "Miles": 1609.34,
        "Feet": 0.3048,
        "Inches": 0.0254,
        "Yards": 0.9144
    },
    "Temperature": {
        "Celsius": 1,
        "Fahrenheit": 1,
        "Kelvin": 1
    },
    "Weight": {
        "Kilograms": 1,
        "Grams": 0.001,
        "Milligrams": 0.000001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
        "Tons": 907.185
    },
    "Volume": {
        "Liters": 1,
        "Milliliters": 0.001,
        "Cubic Meters": 1000,
        "Gallons": 3.78541,
        "Quarts": 0.946353,
        "Pints": 0.473176,
        "Cups": 0.236588
    }
}

# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    # Convert to Celsius first
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:
        celsius = value
    
    # Convert from Celsius to target unit
    if to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    else:
        return celsius

# Function to convert other units
def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    
    # Get conversion factors
    from_factor = conversion_factors[category][from_unit]
    to_factor = conversion_factors[category][to_unit]
    
    # Convert to base unit first, then to target unit
    base_value = value * from_factor
    return base_value / to_factor

# Main app
def main():
    # Select conversion category
    category = st.selectbox(
        "Select Conversion Category",
        list(conversion_factors.keys())
    )
    
    # Get units for selected category
    units = list(conversion_factors[category].keys())
    
    # Create two columns for input and output
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox(
            "From",
            units,
            key="from_unit"
        )
        value = st.number_input(
            "Value",
            min_value=0.0,
            value=1.0,
            step=0.1,
            key="value"
        )
    
    with col2:
        to_unit = st.selectbox(
            "To",
            units,
            key="to_unit"
        )
        
        # Calculate and display result
        if category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        else:
            result = convert_units(value, from_unit, to_unit, category)
        
        st.metric(
            "Result",
            f"{result:.6f}",
            f"{to_unit}"
        )

if __name__ == "__main__":
    main()
    
    

