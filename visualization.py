import pandas as pd
import plotly.express as px
from campServicesSort import squad_assignments
import plotly.graph_objects as go

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Example usage (assuming you have already generated squad_assignments)
num_days = 14

# Create a dictionary to store squad assignments
data = {
    'Day': [],
    'Student Cooking': [],
    'Student Table Service': [],
    'Student Dishes': [],
    'Counselor Cooking': [],
    'Counselor Table Service': [],
    'Counselor Dishes': [],
    'Director Cooking': [],
    'Director Table Service': [],
    'Director Dishes': []
}

# Populate the dictionary with squad assignments data
for day in range(num_days):
    data['Day'].append(day + 1)
    data['Student Cooking'].append(', '.join(squad_assignments['students']['cooking'][day]))
    data['Student Table Service'].append(', '.join(squad_assignments['students']['table_service'][day]))
    data['Student Dishes'].append(', '.join(squad_assignments['students']['dishes'][day]))
    data['Counselor Cooking'].append(', '.join(squad_assignments['counselors']['cooking'][day]))
    data['Counselor Table Service'].append(', '.join(squad_assignments['counselors']['table_service'][day]))
    data['Counselor Dishes'].append(', '.join(squad_assignments['counselors']['dishes'][day]))
    data['Director Cooking'].append(', '.join(squad_assignments['directors']['cooking'][day]))
    data['Director Table Service'].append(', '.join(squad_assignments['directors']['table_service'][day]))
    data['Director Dishes'].append(', '.join(squad_assignments['directors']['dishes'][day]))

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

table_trace = go.Figure(data=[go.Table(
    header=dict(values=['Day', 'Student Cooking', 'Student Table Service', 'Student Dishes',
                        'Counselor Cooking', 'Counselor Table Service', 'Counselor Dishes',
                        'Director Cooking', 'Director Table Service', 'Director Dishes'],
                fill_color='paleturquoise',
                align='center',
                font=dict(size=12)),
    cells=dict(values=[df['Day'], df['Student Cooking'], df['Student Table Service'], df['Student Dishes'],
                       df['Counselor Cooking'], df['Counselor Table Service'], df['Counselor Dishes'],
                       df['Director Cooking'], df['Director Table Service'], df['Director Dishes']],
               fill_color='lavender',
               align='center',
               font=dict(size=11))),
])

# Update table layout
table_trace.update_layout(title='Squad Assignments Table')

# Show the table
table_trace.show()