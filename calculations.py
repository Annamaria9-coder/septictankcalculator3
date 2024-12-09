from constants import (
    SLUDGE_ACCUMULATION_RATE,
    RETENTION_TIME_MULTIPLIER,
    LEACH_FIELD_MULTIPLIER,
    PERCOLATION_RATE_SANDY,
    PERCOLATION_RATE_LOAM,
    PERCOLATION_RATE_CLAY,
)

def calculate_tank_requirements(user_inputs):
    """Perform calculations for septic tank design."""
    # Unpack inputs
    household_size = user_inputs["household_size"]
    wastewater_flow = user_inputs["wastewater_flow"]
    retention_time = user_inputs["retention_time"]
    soil_type = user_inputs.get("soil_type", None)
    prone_to_flooding = user_inputs.get("prone_to_flooding", False)

    # Calculate basic metrics
    daily_flow = household_size * wastewater_flow
    tank_volume = daily_flow * retention_time
    sludge_volume = SLUDGE_ACCUMULATION_RATE * household_size

    # Calculate leach field area (if applicable for 3-chambered tanks)
    leach_field_area = None
    if soil_type:
        if soil_type == "sandy":
            percolation_rate = PERCOLATION_RATE_SANDY
        elif soil_type == "loam":
            percolation_rate = PERCOLATION_RATE_LOAM
        elif soil_type == "clay":
            percolation_rate = PERCOLATION_RATE_CLAY
        else:
            percolation_rate = 1  # Default to avoid division by zero

        leach_field_area = daily_flow / percolation_rate

    # Adjust tank volume for flooding risk
    adjusted_tank_volume = (
        tank_volume * RETENTION_TIME_MULTIPLIER if prone_to_flooding else tank_volume
    )

    # Output dictionary
    results = {
        "Daily Flow (L/day)": daily_flow,
        "Tank Volume (L)": adjusted_tank_volume,
        "Sludge Volume (L)": sludge_volume,
    }

    if leach_field_area:
        results["Leach Field Area (m²)"] = leach_field_area

    return results