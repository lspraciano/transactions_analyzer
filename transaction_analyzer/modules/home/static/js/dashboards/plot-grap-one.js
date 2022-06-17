export const plotGrapOne = (labels, values) => {
    const canvasGraphOne = document.getElementById('graph-one').getContext('2d');

    const data = {
        labels: labels,
        datasets: [{
            label: 'Total de Transações / Dia',
            data: values,
            fill: true,
            backgroundColor: 'rgba(82,83,163,0.25)',
            borderColor: 'rgba(82,83,163,0.7)',
            tension: 0.1,
        }]
    }

    const config = {
        type: 'line',
        data: data,
        options: {
            plugins: {
                legend: {
                    display: false
                },
                title: {
                    display: true,
                    text: 'Transações /  Dia',
                    font: {
                        size: 20,
                    }
                }
            },
            maintainAspectRatio: false,
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        },
        animation: {
            x: {
                duration: 3000,
                from: 0
            },
            y: {
                duration: 2000,
                from: 500
            }
        }
    };

    const myChart = new Chart(canvasGraphOne, config);
}