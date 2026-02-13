3// Load statistics and update the dashboard
async function loadStats() {
    try {
        const response = await fetch('charts/stats.json');
        const stats = await response.json();
        
        // Update stat cards
        document.getElementById('total-flights').textContent = stats.total_flights.toLocaleString();
        document.getElementById('avg-delay').textContent = stats.avg_delay.toFixed(1);
        document.getElementById('ontime-pct').textContent = stats.ontime_percentage.toFixed(1);
        document.getElementById('severe-delay-pct').textContent = stats.severe_delay_percentage.toFixed(1);
        
        // Update insights
        document.getElementById('most-delayed-airline').textContent = stats.most_delayed_airline;
        document.getElementById('least-delayed-airline').textContent = stats.least_delayed_airline;
        document.getElementById('worst-reason').textContent = stats.worst_delay_reason;
        document.getElementById('peak-hour').textContent = formatHour(stats.peak_delay_hour);
        
        // Animate stat values
        animateStats();
    } catch (error) {
        console.error('Error loading statistics:', error);
    }
}

// Format hour for display
function formatHour(hour) {
    if (hour === 0) return '12:00 AM';
    if (hour < 12) return `${hour}:00 AM`;
    if (hour === 12) return '12:00 PM';
    return `${hour - 12}:00 PM`;
}

// Animate stat numbers
function animateStats() {
    const statValues = document.querySelectorAll('.stat-value');
    
    statValues.forEach((stat, index) => {
        stat.style.opacity = '0';
        stat.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            stat.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
            stat.style.opacity = '1';
            stat.style.transform = 'translateY(0)';
        }, index * 100);
    });
}

// Smooth scroll to section
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

// Add fade-in animation to chart cards as they come into view
function observeCharts() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('fade-in');
                }, index * 100);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    document.querySelectorAll('.chart-card').forEach(card => {
        observer.observe(card);
    });
}

// Device detection and mobile restriction
function checkDevice() {
    const screenWidth = window.innerWidth;
    const mobileMessage = document.getElementById('mobile-message');
    const mainContent = document.querySelector('main');
    const header = document.querySelector('header');
    const footer = document.querySelector('footer');

    if (screenWidth < 768) {
        // Mobile device - show restriction message
        mobileMessage.style.display = 'flex';
        if (mainContent) mainContent.style.display = 'none';
        if (header) header.style.display = 'none';
        if (footer) footer.style.display = 'none';
    } else {
        // Tablet or larger - show content
        mobileMessage.style.display = 'none';
        if (mainContent) mainContent.style.display = 'block';
        if (header) header.style.display = 'block';
        if (footer) footer.style.display = 'block';
    }
}

// Initialize dashboard
document.addEventListener('DOMContentLoaded', () => {
    checkDevice();
    loadStats();
    observeCharts();

    // Add hover effects to stat cards
    document.querySelectorAll('.stat-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s ease';
        });
    });

    // Check device on window resize
    window.addEventListener('resize', checkDevice);
});

// Refresh data (for future use with real-time data)
function refreshData() {
    console.log('Refreshing data...');
    loadStats();
    
    // Reload iframes
    document.querySelectorAll('iframe').forEach(iframe => {
        iframe.src = iframe.src;
    });
}

// Export functionality (for future enhancement)
function exportReport() {
    console.log('Exporting report...');
    alert('Export functionality coming soon!');
}

// Print dashboard
function printDashboard() {
    window.print();
}
