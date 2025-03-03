import streamlit as st
from pint import UnitRegistry


ureg = UnitRegistry()


categories = {
    "Length": ["meter", "kilometer", "inch", "foot", "yard", "mile"],
    "Mass": ["kilogram", "gram", "pound", "ounce", "stone"], 
    "Speed": ["meter per second", "kilometer per hour", "mile per hour"], 
    "Temperature": ["celsius", "fahrenheit", "kelvin"], 
    "Time": ["second", "minute", "hour", "day", "week", "month", "year"]
}


if "history" not in st.session_state:
    st.session_state.history = []



st.title(" Unit Converter ⚖️")


col1, col2 = st.columns(2)
with col1:
    category = st.selectbox(" Select a category", list(categories.keys()))
with col2:
    value = st.number_input(" Enter a value", value=0.0, step=0.1, format="%.2f")


col3, col4, col5 = st.columns([3, 1, 3])
with col3:
    from_unit = st.selectbox(" Convert from", categories[category])
with col5:
    to_unit = st.selectbox(" Convert to", categories[category])
with col4:
    if st.button(" Swap"):
        from_unit, to_unit = to_unit, from_unit  # Swap units


convert = st.button(" Convert")

if convert:
    try:
        if category == "Temperature":
         
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (value - 32) * 5/9
            elif from_unit == "celsius" and to_unit == "kelvin":
                result = value + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                result = value - 273.15
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value  
        else:
        
            result = (value * ureg(from_unit)).to(to_unit).magnitude

      
        st.session_state.history.insert(0, f"{value} {from_unit} = {result:.4f} {to_unit}")
        st.session_state.history = st.session_state.history[:5]  # Keep last 5 conversions

      
        st.success(f"✅ {value} {from_unit} is equal to **{result:.4f} {to_unit}**")

    except Exception as e:
        st.error(f"❌ Error: {e}")


if st.session_state.history:
    st.markdown("### 🕘 Conversion History")
    for item in st.session_state.history:
        st.write(f"- {item}")

st.markdown("---")
st.markdown("🔹 **Created by Yusra Fatima** | Powered by [Pint](https://pint.readthedocs.io/en/stable/) & Streamlit")
