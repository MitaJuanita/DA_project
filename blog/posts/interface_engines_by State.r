import pandas as pd

# Create a condensed table of states and integration engines with examples
data = [
    ("California", "Rhapsody", "Children’s Hospital Los Angeles"),
    ("California", "Cloverleaf", "Keck Medicine of USC"),
    ("California", "Mirth Connect", "SCHIO (Santa Cruz HIE)"),
    ("California", "Corepoint", "Emanate Health"),
    ("Connecticut", "Iguana", "Connecticut Children’s Medical Center"),
    ("Connecticut", "Cloverleaf", "UConn Health, Waterbury Hospital"),
    ("Delaware", "Cloverleaf", "Bayhealth"),
    ("Florida", "Qvera", "Millennium Physician Group"),
    ("Florida", "Health Connect", "Unnamed large multi-state health system"),
    ("Illinois", "Qvera", "AllianceChicago"),
    ("Indiana", "Rhapsody", "Marion General Hospital"),
    ("Michigan", "Health Connect", "Holland Hospital"),
    ("Michigan", "Cloverleaf", "Beaumont Health (historical)"),
    ("New Jersey", "Cloverleaf", "Hackensack University Medical Center"),
    ("New York", "Cloverleaf", "Mount Sinai South Nassau, RUMC"),
    ("New York", "Rhapsody", "New York State Department of Health"),
    ("Ohio", "Mirth Connect", "University of Toledo Medical Center"),
    ("Texas", "Corepoint", "OakBend Medical Center"),
    ("Texas", "Rhapsody", "ETMC"),
    ("Texas", "Iguana", "Large unnamed cancer research hospital"),
    ("Utah", "Qvera", "Revere Health"),
    ("Vermont", "Rhapsody", "Vermont Information Technology Leaders (VITL)"),
    ("Virginia", "Cloverleaf", "Virginia Premier Health Plan"),
    ("Virginia", "Qvera", "Virginia Women’s Center"),
    ("Virginia", "Rhapsody", "Virginia Dept. of Health (public health use)"),
    ("West Virginia", "Corepoint", "WVU Medicine"),
    ("Wisconsin", "Rhapsody", "WISHIN (Wisconsin HIE)"),
    ("Wisconsin", "Cloverleaf", "UW Health, Aurora Health Care")
]

df = pd.DataFrame(data, columns=["State", "Integration Engine", "Example Health System"])

# Display the table to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="State-by-State Integration Engine Adoption", dataframe=df)
