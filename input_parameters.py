def get_user_inputs():
    """Mock user input collection for calculation."""
    household_size = int(input("Enter household size: "))
    tank_type = input("Choose tank type (3 or 4 chambers): ")
    retention_time = float(input("Enter desired retention time (days): "))
    borehole_distance = float(input("Enter borehole distance (meters): "))
    seasonal_factor = float(input("Enter seasonal factor: "))
    effluent_reuse = input("Effluent reuse? (yes or no): ").strip().lower() == "yes"
    prone_to_flooding = input("Prone to flooding? (yes or no): ").strip().lower() == "yes"
    soil_type = input("Enter soil type (sandy, clay, loam): ").strip().lower()
    groundwater_flow = input("Groundwater flow direction (upstream, downstream): ").strip().lower()
    groundwater_depth = float(input("Enter groundwater depth (meters): "))

    return {
        "household_size": household_size,
        "tank_type": tank_type,
        "retention_time": retention_time,
        "borehole_distance": borehole_distance,
        "seasonal_factor": seasonal_factor,
        "effluent_reuse": effluent_reuse,
        "prone_to_flooding": prone_to_flooding,
        "soil_type": soil_type,
        "groundwater_flow": groundwater_flow,
        "groundwater_depth": groundwater_depth,
    }