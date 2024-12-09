# constants.py

# Minimum distances and safety
MIN_BOREHOLE_DISTANCE = 30  # Minimum distance in meters
MIN_GROUNDWATER_DEPTH = 1.5  # Minimum depth in meters to avoid contamination
SAND_MIN_THICKNESS = 0.6  # Minimum thickness for sand layer in meters
SAND_MAX_THICKNESS = 1.2  # Maximum thickness for sand layer in meters

# Borehole distance assumptions
BOREHOLE_DISTANCE_CONDITIONS = {
    "low_risk": (30, 50),  # Distance range in meters for low-risk areas
    "moderate_risk": (50, 75),  # Distance range for moderate-risk areas
    "high_risk": (75, 100),  # Distance range for high-risk areas
    "extreme_risk": (100, 200),  # Distance range for extreme-risk areas
}

# Sludge accumulation and flow constants
SLUDGE_ACCUMULATION_RATE = 0.04  # m³ per capita per year
FLUSH_COUNT = 5  # Flush count per person per day
CISTERN_SIZE = 0.009  # m³ (volume per flush)
LIQUID_DEPTH = 1.0  # Liquid depth in meters
FREEBOARD = 0.3  # Safety margin for overflow

# Mixed media filtration constants (Adjusted ranges for sand)
MIXED_MEDIA_THICKNESS = {
    "low_flow": {
        "coconut_husk": 0.3,
        "activated_charcoal": 0.2,
        "wood_chips": 0.3,
        "sand": SAND_MIN_THICKNESS,
        "cinder_rocks": 0.2,
    },
    "moderate_flow": {
        "coconut_husk": 0.5,
        "activated_charcoal": 0.3,
        "wood_chips": 0.5,
        "sand": 1.0,
        "cinder_rocks": 0.3,
    },
    "high_flow": {
        "coconut_husk": 0.7,
        "activated_charcoal": 0.5,
        "wood_chips": 0.7,
        "sand": SAND_MAX_THICKNESS,
        "cinder_rocks": 0.3,
    },
}

# Environmental and safety factors
RETENTION_TIME_MULTIPLIER = 1.5  # Adjusts retention time for reuse
SAFETY_MARGIN = 1.25  # Multiplier for safety factor
H2S_EMISSION_ESTIMATE = 0.1  # Hydrogen Sulfide emissions, g/person/day

# Leach field calculations
LEACH_FIELD_MULTIPLIER = 1.5  # Adjustment factor for leach field area
EFFLUENT_REUSE_FACTOR = 0.8  # Reduction in leach field area for effluent reuse

# Soil Percolation Rates (liters per square meter per day)
PERCOLATION_RATE_SANDY = 30
PERCOLATION_RATE_LOAM = 15
PERCOLATION_RATE_CLAY = 5

# Seasonal factors
SEASONAL_FLOODING_MULTIPLIER = 1.2  # Multiplier for areas prone to flooding
SEASONAL_USAGE_FACTOR = 0.85  # Reduction for low seasonal usage

# Groundwater depth categories
GROUNDWATER_DEPTH = {
    "low_water_table": (3, 5),  # Depth in meters
    "high_water_table": (5, 30),  # Depth in meters
}

# Tank dimension scaling factors
TANK_DIMENSION_SCALING = {
    "width_ratio": 2.0,  # Width scaling factor
    "height_ratio": 1.4,  # Height scaling factor (relative to width)
    "depth_adjustment": 2.5,  # Depth adjustment factor
}