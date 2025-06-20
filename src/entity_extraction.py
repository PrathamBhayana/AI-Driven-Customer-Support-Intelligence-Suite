import re

PRODUCTS = [
    'SmartWatch V2', 'UltraClean Vacuum', 'SoundWave 300', 'PhotoSnap Cam',
    'Vision LED TV', 'EcoBreeze AC', 'RoboChef Blender', 'FitRun Treadmill',
    'PowerMax Battery', 'ProTab X1'
]

COMPLAINT_KEYWORDS = [
    'Billing Problem', 'General Inquiry', 'Wrong Item', 'Installation Issue',
    'Late Delivery', 'Product Defect', 'Account Access', 'warranty', 'broken', 'not working', 'late'
]

def extract_entities(text):
    text_lower = text.lower()
    products = [p for p in PRODUCTS if p.lower() in text_lower]
    # Improved date regex for formats like '03 March', '3 March', '03/03/2024'
    dates = re.findall(r'\b\d{1,2}\s+\w+\b', text)
    complaints = [w for w in COMPLAINT_KEYWORDS if w.lower() in text_lower]
    return {
        'products': products,
        'dates': dates,
        'complaint_keywords': complaints
    }