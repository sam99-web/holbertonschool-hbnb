document.addEventListener('DOMContentLoaded', () => {
    const token = getCookie('token');
    const placeId = getPlaceIdFromURL();

    // Redirige si non authentifié
    if (!token) {
        window.location.href = 'index.html';
        return;
    }

    const form = document.getElementById('review-form');
    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const comment = document.getElementById('comment').value;
        const rating = document.querySelector('input[name="rating"]:checked');

        if (!rating) {
            alert('Please select a rating ⭐');
            return;
        }

        try {
            const response = await fetch(`http://localhost:5001/api/v1/reviews/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    text: comment,
                    rating: parseInt(rating.value),
                    place_id: placeId
                })
            });

            if (response.ok) {
                alert('Review submitted! 🎉');
                window.location.href = `place.html?id=${placeId}`;
            } else {
                const data = await response.json();
                alert('Error: ' + JSON.stringify(data));
            }
        } catch (error) {
            alert('Network error: ' + error.message);
        }
    });
});

function getCookie(name) {
    const value = document.cookie
        .split('; ')
        .find(row => row.startsWith(name + '='));
    return value ? value.split('=')[1] : null;
}

function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}