from constants import (
    SLUDGE_ACCUMULATION_RATE,
    RETENTION_TIME_MULTIPLIER,
    LEACH_FIELD_MULTIPLIER,
    PERCOLATION_RATE_SANDY,
    PERCOLATION_RATE_LOAM,
    PERCOLATION_RATE_CLAY,
    SAFETY_MARGIN,
    H2S_EMISSION_ESTIMATE,
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
    tank_volume = daily_flow * retention_time * SAFETY_MARGIN
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

        leach_field_area = (daily_flow / percolation_rate) * LEACH_FIELD_MULTIPLIER

    # Adjust tank volume for flooding risk
    adjusted_tank_volume = (
        tank_volume * RETENTION_TIME_MULTIPLIER if prone_to_flooding else tank_volume
    )

    # Additional calculated metrics
    h2s_emissions = H2S_EMISSION_ESTIMATE * household_size
    sand_thickness = (
        daily_flow / 1000 if soil_type == "sandy" else 0.8  # Example sand thickness logic
    )

    # Tank dimensions (example calculations)
    tank_width = adjusted_tank_volume ** (1 / 3)  # Approximation for cubic tank
    tank_height = tank_width * 0.8
    tank_depth = tank_width * 1.2

    # Output dictionary
    results = {
        "Volume of Liquid (L/day)": daily_flow,
        "Total Tank Volume (L)": adjusted_tank_volume,
        "Volume of Sludge (L)": sludge_volume,
        "H2S Emissions (g/day)": h2s_emissions,
        "Sand Thickness (m)": sand_thickness,
        "Tank Dimensions": {
            "Width (m)": round(tank_width, 2),
            "Height (m)": round(tank_height, 2),
            "Depth (m)": round(tank_depth, 2),
        },
    }

    if leach_field_area:
        results["Leach Field Area (m²)"] = round(leach_field_area, 2)

    return results