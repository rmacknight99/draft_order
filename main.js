let teams;

function generateOrder() {
    fetch('teams.json')
        .then(response => response.json())
        .then(data => {
            teams = data.teams;
            teams.sort(() => Math.random() - 0.5); // Shuffle the array
            localStorage.setItem('teams', JSON.stringify(teams));
            window.location.href = "/draft_order/order.html";
        });
}

function displayOrder() {
    const teams = JSON.parse(localStorage.getItem('teams'));
    const teamList = document.getElementById('team-list');

    teams.forEach(team => {
        const li = document.createElement('li');
        li.textContent = team;
        teamList.appendChild(li);
    });
}