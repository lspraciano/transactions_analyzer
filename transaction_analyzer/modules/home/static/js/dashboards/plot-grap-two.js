export const plotGrapTwo = (labels, values) => {
    const canvasGraphTwo = document.getElementById('graph-two').getContext('2d');
    const data = {
        labels: labels,
        datasets: [{
            label: 'Transsações / Banco',
            data: values,
            hoverOffset: 4,
            backgroundColor: [
                'rgba(82,83,163,0.9)',
                'rgba(163,82,82,0.9)',
                'rgba(82,163,144,0.9)',
                'rgba(190,186,93,0.9)',
                'rgb(84,84,84)',
            ],
        }]
    };

    const config = {
        type: 'doughnut',
        data: data,
        options: {
            plugins: {
                title: {
                    display: true,
                    text: 'Transações /  Banco',
                    font: {
                        size: 20,
                    }
                }
            },
            maintainAspectRatio: false,
            responsive: true,
        },
    };

    const myChart = new Chart(canvasGraphTwo, config);
}