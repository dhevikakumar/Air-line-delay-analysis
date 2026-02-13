import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
NUM_FLIGHTS = 5000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2024, 12, 31)

# Airlines
AIRLINES = [
    'American Airlines', 'Delta Air Lines', 'United Airlines', 
    'Southwest Airlines', 'JetBlue Airways', 'Alaska Airlines',
    'Spirit Airlines', 'Frontier Airlines'
]

# Major airports
AIRPORTS = [
    'ATL', 'DFW', 'DEN', 'ORD', 'LAX', 'CLT', 'MCO', 'LAS',
    'PHX', 'MIA', 'SEA', 'IAH', 'JFK', 'EWR', 'SFO', 'BOS',
    'MSP', 'DTW', 'PHL', 'LGA', 'BWI', 'SLC', 'SAN', 'IAD'
]

# Delay reasons
DELAY_REASONS = [
    'Weather', 'Aircraft Issue', 'Crew Issue', 'Airport Congestion',
    'Air Traffic Control', 'Security', 'Baggage Loading', 'Late Arrival',
    'Fueling', 'No Delay'
]

def generate_flight_data():
    """Generate realistic airline delay dataset"""
    
    flights = []
    
    for i in range(NUM_FLIGHTS):
        # Random date
        days_diff = (END_DATE - START_DATE).days
        flight_date = START_DATE + timedelta(days=random.randint(0, days_diff))
        
        # Random airline
        airline = random.choice(AIRLINES)
        
        # Flight number
        flight_number = f"{airline[:2].upper()}{random.randint(100, 9999)}"
        
        # Origin and destination (ensure they're different)
        origin = random.choice(AIRPORTS)
        destination = random.choice([a for a in AIRPORTS if a != origin])
        
        # Scheduled departure time (weighted towards common flight times)
        hour_weights = [2, 2, 1, 1, 3, 5, 8, 10, 9, 8, 7, 6, 7, 8, 9, 10, 9, 8, 10, 9, 7, 5, 4, 3]
        hour = random.choices(range(24), weights=hour_weights)[0]
        minute = random.choice([0, 15, 30, 45])
        scheduled_time = flight_date.replace(hour=hour, minute=minute, second=0)
        
        # Delay generation (70% on-time or minor delays, 30% significant delays)
        if random.random() < 0.7:
            # Minor or no delay
            delay_minutes = max(0, int(np.random.gamma(2, 5)))
            if delay_minutes > 60:
                delay_minutes = random.randint(0, 30)
        else:
            # Significant delay
            delay_minutes = random.randint(30, 300)
        
        # Actual departure time
        actual_time = scheduled_time + timedelta(minutes=delay_minutes)
        
        # Delay category
        if delay_minutes == 0:
            delay_category = 'On Time'
            delay_reason = 'No Delay'
        elif delay_minutes <= 15:
            delay_category = 'Minor Delay'
            delay_reason = random.choice(['Air Traffic Control', 'Baggage Loading', 'Late Arrival'])
        elif delay_minutes <= 60:
            delay_category = 'Moderate Delay'
            delay_reason = random.choice(['Weather', 'Airport Congestion', 'Air Traffic Control', 'Late Arrival'])
        else:
            delay_category = 'Severe Delay'
            delay_reason = random.choice(['Weather', 'Aircraft Issue', 'Crew Issue', 'Airport Congestion'])
        
        # Distance (approximate, for visualization purposes)
        distance = random.randint(200, 3000)
        
        flights.append({
            'flight_number': flight_number,
            'airline': airline,
            'origin': origin,
            'destination': destination,
            'date': flight_date.strftime('%Y-%m-%d'),
            'day_of_week': flight_date.strftime('%A'),
            'month': flight_date.strftime('%B'),
            'scheduled_departure': scheduled_time.strftime('%Y-%m-%d %H:%M:%S'),
            'actual_departure': actual_time.strftime('%Y-%m-%d %H:%M:%S'),
            'delay_minutes': delay_minutes,
            'delay_category': delay_category,
            'delay_reason': delay_reason,
            'distance': distance,
            'hour_of_day': hour
        })
    
    return pd.DataFrame(flights)

if __name__ == '__main__':
    print("Generating airline delay dataset...")
    df = generate_flight_data()
    
    # Save to CSV
    df.to_csv('airline_delays.csv', index=False)
    print(f"[SUCCESS] Generated {len(df)} flight records")
    print(f"[SUCCESS] Saved to airline_delays.csv")
    
    # Display sample and statistics
    print("\n" + "="*60)
    print("DATASET OVERVIEW")
    print("="*60)
    print(f"\nTotal Flights: {len(df)}")
    print(f"Date Range: {df['date'].min()} to {df['date'].max()}")
    print(f"Airlines: {df['airline'].nunique()}")
    print(f"Airports: {len(set(df['origin'].tolist() + df['destination'].tolist()))}")
    
    print("\n" + "-"*60)
    print("DELAY STATISTICS")
    print("-"*60)
    print(f"Average Delay: {df['delay_minutes'].mean():.1f} minutes")
    print(f"Median Delay: {df['delay_minutes'].median():.1f} minutes")
    print(f"Max Delay: {df['delay_minutes'].max()} minutes")
    
    print("\nDelay Categories:")
    print(df['delay_category'].value_counts().to_string())
    
    print("\n" + "-"*60)
    print("SAMPLE DATA (First 5 rows)")
    print("-"*60)
    print(df.head().to_string())
