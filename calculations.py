from constants import SLUDGE_ACCUMULATION_RATE, RETENTION_TIME_MULTIPLIER

def calculate_tank_requirements(user_inputs):
    """Perform calculations for septic tank design."""
    # Unpack inputs
    household_size = user_inputs["household_size"]
    wastewater_flow = user_inputs["wastewater_flow"]
    retention_time = user_inputs["retention_time"]

    # Calculate basic metrics
    daily_flow = household_size * wastewater_flow
    tank_volume = daily_flow * retention_time
    sludge_volume = SLUDGE_ACCUMULATION_RATE * household_size

    # Output dictionary
    return {
        "Daily Flow (L/day)": daily_flow,
        "Tank Volume (L)": tank_volume,
        "Sludge Volume (L)": sludge_volume,
    }
