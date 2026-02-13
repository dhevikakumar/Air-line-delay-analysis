import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json

def create_visualizations():
    """Create all visualizations for the airline delay analysis"""
    
    # Load data
    print("Loading data...")
    df = pd.read_csv('airline_delays.csv')
    
    # Create output directory for charts
    import os
    os.makedirs('charts', exist_ok=True)
    
    # Color scheme - vibrant and modern
    colors = {
        'primary': '#6366f1',
        'secondary': '#8b5cf6',
        'accent': '#ec4899',
        'success': '#10b981',
        'warning': '#f59e0b',
        'danger': '#ef4444',
        'background': '#0f172a',
        'surface': '#1e293b'
    }
    
    # 1. DELAY DISTRIBUTION HISTOGRAM
    print("Creating delay distribution chart...")
    fig1 = go.Figure()
    fig1.add_trace(go.Histogram(
        x=df['delay_minutes'],
        nbinsx=50,
        marker=dict(
            color=colors['primary'],
            line=dict(color='white', width=1)
        ),
        name='Delay Distribution',
        hovertemplate='Delay: %{x} min<br>Count: %{y}<extra></extra>'
    ))
    
    fig1.update_layout(
        title='Distribution of Flight Delays',
        xaxis_title='Delay (minutes)',
        yaxis_title='Number of Flights',
        template='plotly_dark',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font=dict(family='Inter, sans-serif', size=12),
        hovermode='x unified',
        height=500
    )
    fig1.write_html('charts/delay_distribution.html')
    
    # 2. AIRLINE COMPARISON
    print("Creating airline comparison chart...")
    airline_stats = df.groupby('airline').agg({
        'delay_minutes': ['mean', 'count']
    }).reset_index()
    airline_stats.columns = ['airline', 'avg_delay', 'total_flights']
    airline_stats = airline_stats.sort_values('avg_delay', ascending=True)
    
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        y=airline_stats['airline'],
        x=airline_stats['avg_delay'],
        orientation='h',
        marker=dict(
            color=airline_stats['avg_delay'],
            colorscale='Viridis',
            line=dict(color='white', width=1)
        ),
        text=airline_stats['avg_delay'].round(1),
        textposition='auto',
        hovertemplate='<b>%{y}</b><br>Avg Delay: %{x:.1f} min<extra></extra>'
    ))
    
    fig2.update_layout(
        title='Average Delay by Airline',
        xaxis_title='Average Delay (minutes)',
        yaxis_title='',
        template='plotly_dark',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font=dict(family='Inter, sans-serif', size=12),
        height=500
    )
    fig2.write_html('charts/airline_comparison.html')
    
    # 3. DELAYS BY HOUR OF DAY
    print("Creating hourly delay analysis...")
    hourly_stats = df.groupby('hour_of_day')['delay_minutes'].mean().reset_index()
    
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=hourly_stats['hour_of_day'],
        y=hourly_stats['delay_minutes'],
        mode='lines+markers',
        line=dict(color=colors['accent'], width=3),
        marker=dict(size=10, color=colors['accent'], line=dict(color='white', width=2)),
        fill='tozeroy',
        fillcolor=f'rgba(236, 72, 153, 0.2)',
        hovertemplate='Hour: %{x}:00<br>Avg Delay: %{y:.1f} min<extra></extra>'
    ))
    
    fig3.update_layout(
        title='Average Delay by Hour of Day',
        xaxis_title='Hour of Day',
        yaxis_title='Average Delay (minutes)',
        template='plotly_dark',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font=dict(family='Inter, sans-serif', size=12),
        xaxis=dict(tickmode='linear', tick0=0, dtick=2),
        height=500
    )
    fig3.write_html('charts/hourly_delays.html')
    
    # 4. DELAY REASONS BREAKDOWN
    print("Creating delay reasons chart...")
    reason_stats = df[df['delay_category'] != 'On Time']['delay_reason'].value_counts()
    
    fig4 = go.Figure(data=[go.Pie(
        labels=reason_stats.index,
        values=reason_stats.values,
        hole=0.4,
        marker=dict(
            colors=['#6366f1', '#8b5cf6', '#ec4899', '#f59e0b', '#10b981', '#3b82f6', '#06b6d4', '#14b8a6'],
            line=dict(color='white', width=2)
        ),
        textposition='auto',
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>Flights: %{value}<br>Percentage: %{percent}<extra></extra>'
    )])
    
    fig4.update_layout(
        title='Delay Reasons Distribution (Delayed Flights Only)',
        template='plotly_dark',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font=dict(family='Inter, sans-serif', size=12),
        height=500
    )
    fig4.write_html('charts/delay_reasons.html')
    
    # 5. DELAY CATEGORIES
    print("Creating delay categories chart...")
    category_order = ['On Time', 'Minor Delay', 'Moderate Delay', 'Severe Delay']
    category_stats = df['delay_category'].value_counts().reindex(category_order)
    
    fig5 = go.Figure(data=[go.Bar(
        x=category_stats.index,
        y=category_stats.values,
        marker=dict(
            color=[colors['success'], colors['warning'], colors['accent'], colors['danger']],
            line=dict(color='white', width=2)
        ),
        text=category_stats.values,
        textposition='auto',
        hovertemplate='<b>%{x}</b><br>Flights: %{y}<extra></extra>'
    )])
    
    fig5.update_layout(
        title='Flight Count by Delay Category',
        xaxis_title='Delay Category',
        yaxis_title='Number of Flights',
        template='plotly_dark',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font=dict(family='Inter, sans-serif', size=12),
        height=500
    )
    fig5.write_html('charts/delay_categories.html')
    
    # 6. MONTHLY TRENDS
    print("Creating monthly trends chart...")
    df['month_num'] = pd.to_datetime(df['date']).dt.month
    monthly_stats = df.groupby('month_num').agg({
        'delay_minutes': 'mean',
        'flight_number': 'count'
    }).reset_index()
    
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_stats['month_name'] = monthly_stats['month_num'].apply(lambda x: month_names[x-1])
    
    fig6 = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig6.add_trace(
        go.Bar(
            x=monthly_stats['month_name'],
            y=monthly_stats['flight_number'],
            name='Flight Count',
            marker=dict(color=colors['primary'], opacity=0.6),
            hovertemplate='Month: %{x}<br>Flights: %{y}<extra></extra>'
        ),
        secondary_y=False
    )
    
    fig6.add_trace(
        go.Scatter(
            x=monthly_stats['month_name'],
            y=monthly_stats['delay_minutes'],
            name='Avg Delay',
            mode='lines+markers',
            line=dict(color=colors['accent'], width=3),
            marker=dict(size=10),
            hovertemplate='Month: %{x}<br>Avg Delay: %{y:.1f} min<extra></extra>'
        ),
        secondary_y=True
    )
    
    fig6.update_layout(
        title='Monthly Trends: Flight Volume and Average Delays',
        template='plotly_dark',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font=dict(family='Inter, sans-serif', size=12),
        hovermode='x unified',
        height=500
    )
    fig6.update_xaxes(title_text="Month")
    fig6.update_yaxes(title_text="Number of Flights", secondary_y=False)
    fig6.update_yaxes(title_text="Average Delay (minutes)", secondary_y=True)
    
    fig6.write_html('charts/monthly_trends.html')
    
    # 7. TOP DELAYED ROUTES
    print("Creating top delayed routes chart...")
    df['route'] = df['origin'] + ' → ' + df['destination']
    route_stats = df.groupby('route').agg({
        'delay_minutes': 'mean',
        'flight_number': 'count'
    }).reset_index()
    route_stats = route_stats[route_stats['flight_number'] >= 10]  # Filter routes with at least 10 flights
    route_stats = route_stats.sort_values('delay_minutes', ascending=False).head(15)
    
    fig7 = go.Figure()
    fig7.add_trace(go.Bar(
        y=route_stats['route'],
        x=route_stats['delay_minutes'],
        orientation='h',
        marker=dict(
            color=route_stats['delay_minutes'],
            colorscale='Plasma',
            line=dict(color='white', width=1)
        ),
        text=route_stats['delay_minutes'].round(1),
        textposition='auto',
        hovertemplate='<b>%{y}</b><br>Avg Delay: %{x:.1f} min<br>Flights: ' + 
                      route_stats['flight_number'].astype(str) + '<extra></extra>'
    ))
    
    fig7.update_layout(
        title='Top 15 Most Delayed Routes (Min. 10 flights)',
        xaxis_title='Average Delay (minutes)',
        yaxis_title='',
        template='plotly_dark',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font=dict(family='Inter, sans-serif', size=12),
        height=600
    )
    fig7.write_html('charts/top_delayed_routes.html')
    
    # Generate summary statistics for the dashboard
    print("Generating summary statistics...")
    stats = {
        'total_flights': int(len(df)),
        'avg_delay': float(df['delay_minutes'].mean()),
        'median_delay': float(df['delay_minutes'].median()),
        'ontime_percentage': float((df['delay_category'] == 'On Time').sum() / len(df) * 100),
        'severe_delay_percentage': float((df['delay_category'] == 'Severe Delay').sum() / len(df) * 100),
        'most_delayed_airline': airline_stats.iloc[-1]['airline'],
        'least_delayed_airline': airline_stats.iloc[0]['airline'],
        'worst_delay_reason': df[df['delay_category'] != 'On Time']['delay_reason'].mode()[0],
        'peak_delay_hour': int(hourly_stats.loc[hourly_stats['delay_minutes'].idxmax(), 'hour_of_day'])
    }
    
    with open('charts/stats.json', 'w') as f:
        json.dump(stats, f, indent=2)
    
    print("\n" + "="*60)
    print("[SUCCESS] All visualizations created successfully!")
    print("="*60)
    print(f"Charts saved in: charts/")
    print("- delay_distribution.html")
    print("- airline_comparison.html")
    print("- hourly_delays.html")
    print("- delay_reasons.html")
    print("- delay_categories.html")
    print("- monthly_trends.html")
    print("- top_delayed_routes.html")
    print("- stats.json")

if __name__ == '__main__':
    create_visualizations()
