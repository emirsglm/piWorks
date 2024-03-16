import pandas as pd
import re

# Sample DataFrame (replace with your actual DataFrame)
data = {
    'Device_Type': ['AXO145', "TRU151", "ZOD231", "YRT326", "LWR245" ],
    'Stats_Access_Link': ['<url>https://xcd32112.smart_meter.com</url>', 
                          '<url>http://tXh67.dia_meter.com</url>', 
                          '<url>http://yT5495.smart_meter.com</url>', 
                          '<url>https://ret323_TRu.crown.com</url>',
                          '<url>https://luwr3243.celcius.com</url>']
}

df = pd.DataFrame(data)

# Function to extract pure URL information
def extract_url(stats_access_link):
    # Regular expression to extract the URL
    pattern = r'//([^</]+)'
    
    match = re.search(pattern, stats_access_link)
    if match:
        return match.group(1)
    else:
        return None

# Apply the function to each row based
df['Pure_URL'] = df.apply(lambda row: extract_url(row['Stats_Access_Link']), axis=1)

# Display the result
print(df)
