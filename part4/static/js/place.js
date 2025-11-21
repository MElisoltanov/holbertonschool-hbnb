/* ============================================================
   GLOBAL UTILITIES (needed by both index and place page)
==============================================================*/

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
    return null;
}

/* ============================================================
   PLACE PAGE ONLY
==============================================================*/

/* --- Extract place ID from URL --- */
function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get("id");
}

/* --- Fetch place details from API --- */
async function fetchPlaceDetails(token, placeId) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
            headers: token ? { "Authorization": `Bearer ${token}` } : {}
        });

        const data = await response.json();
        console.log(data)
        if (!response.ok) {
            console.error("Error fetching place details:", data);
            return;
        }

        displayPlaceDetails(data);

    } catch (err) {
        console.error("Network error:", err);
    }
}

/* --- Render the place details into HTML --- */
function displayPlaceDetails(place) {
    const container = document.getElementById("place-details");
    container.innerHTML = ""; // clear existing

    const div = document.createElement("div");
    div.classList.add("place-detail-card");
    div.innerHTML = `
        <h1>${place.title}</h1>
        <img src="https://picsum.photos/600/350?random=${place.id}">
        <p><strong>Price:</strong> $${place.price}</p>
        <p><strong>Description:</strong> ${place.description}</p>

        <h3>Amenities</h3>
        <ul>
            ${place.amenities.map(a => `<li>${a.name}</li>`).join("")}
        </ul>

    `;

    container.appendChild(div);
}

/* --- Load logic ONLY for place.html --- */
function loadPlacePage() {
    // Detect if you're ON place.html
    if (!document.getElementById("place-details")) {
        return; // Not on place page → do nothing
    }

    const reviewButton = document.getElementById("add-review-link");
    const token = getCookie("token");
    const placeId = getPlaceIdFromURL();
    const reviewSection = document.getElementById("add-review");

    // Hide review form if not logged in
    if (!token) {
        if (reviewSection) reviewSection.style.display = "none";
    } else {
        if (reviewSection) reviewSection.style.display = "block";
    }

    if (reviewButton && placeId) {
    reviewButton.href = `add_review.html?id=${placeId}`;
    }

    // Fetch the place information
    fetchPlaceDetails(token, placeId);

        // Fetch reviews
    fetchReviews(placeId);
}

async function fetchReviews(placeId) {
    try {
        const res = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}/reviews`);
        const data = await res.json();

        if (!res.ok) {
            console.error("Failed to load reviews:", data);
            return;
        }

        displayReviews(data);

    } catch (err) {
        console.error("Network error loading reviews:", err);
    }
}
    // Display reviews

    function displayReviews(reviews) {
        const reviewsList = document.getElementById("reviews-list");
        reviewsList.innerHTML = "";

        reviews.forEach((review) => {

            const reviewCard = document.createElement("div");
            reviewCard.classList.add("review-card");

            const username = review.user?.name || review.user?.email || "Unknown user";

            reviewCard.innerHTML = `
                <p><strong>User:</strong> ${username}</p>
                <p><strong>Rating:</strong> ${review.rating}</p>
                <p>${review.text}</p>
                <hr>
            `;

            reviewsList.appendChild(reviewCard);
        });
    }

/* --- Run automatically when page loads --- */
document.addEventListener("DOMContentLoaded", loadPlacePage);
