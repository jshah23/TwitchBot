document.addEventListener('DOMContentLoaded', function() {
    const fetchClipsButton = document.getElementById('fetchClips');
    const broadcasterIdInput = document.getElementById('broadcasterId');
    const clipsContainer = document.getElementById('clips');

    fetchClipsButton.addEventListener('click', function() {
        const broadcasterId = broadcasterIdInput.value.trim();
        if (broadcasterId !== '') {
            fetch(`http://localhost:5000/clips?broadcaster_id=${broadcasterId}`)
                .then(response => response.json())
                .then(data => {
                    clipsContainer.innerHTML = '';
                    data.forEach(clip => {
                        const clipElement = document.createElement('div');
                        clipElement.classList.add('clip');
                        clipElement.innerHTML = `
                            <h3>${clip.title}</h3>
                            <p>URL: <a href="${clip.url}" target="_blank">${clip.url}</a></p>
                        `;
                        clipsContainer.appendChild(clipElement);
                    });
                })
                .catch(error => {
                    console.error(error);
                    clipsContainer.innerHTML = '<p>Error fetching clips</p>';
                });
        }
    });
});
