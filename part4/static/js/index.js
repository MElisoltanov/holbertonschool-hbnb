document.addEventListener("DOMContentLoaded", () => {

    /* -----------------------------------------
       GET COOKIE
    --------------------------------------------*/
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(";").shift();
        return null;
    }

    /* -----------------------------------------
       LOGIN PAGE HANDLING
    --------------------------------------------*/
    const loginForm = document.getElementById("login-form");
    const errorMessage = document.getElementById("error-message");

    if (loginForm) {
        loginForm.addEventListener("submit", async (event) => {
            event.preventDefault();

            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("password").value.trim();

            try {
                const response = await fetch("http://127.0.0.1:5000/api/v1/auth/login", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ email, password })
                });

                const data = await response.json();

                if (!response.ok) {
                    errorMessage.style.display = "block";
                    errorMessage.textContent = data.error || "Invalid credentials";
                    return;
                }

                // Save token
                document.cookie = `token=${data.access_token}; path=/;`;

                // Redirect after login
                window.location.href = "index.html";

            } catch (err) {
                errorMessage.style.display = "block";
                errorMessage.textContent = "Network error";
            }
        });
    }

    /* -----------------------------------------
       FETCH PLACES FROM API
    --------------------------------------------*/
    async function fetchPlaces(token) {
        try {
            const response = await fetch("http://127.0.0.1:5000/api/v1/places/", {
                headers: { "Authorization": `Bearer ${token}` }
            });

            const places = await response.json();

            if (!response.ok) {
                console.error("Error loading places:", places);
                return;
            }

            displayPlaces(places);
            enableFiltering();

        } catch (err) {
            console.error("Fetch error:", err);
        }
    }

    /* -----------------------------------------
       DISPLAY PLACES
    --------------------------------------------*/
    function displayPlaces(places) {
        const container = document.getElementById("places-list");
        container.innerHTML = "";  // Clear old cards

        places.forEach(place => {
            const card = document.createElement("div");
            card.classList.add("place-card");
            card.dataset.price = place.price;

            card.innerHTML = `
                <img src="https://picsum.photos/400/250?random=${place.id}">
                <h3>${place.title}</h3>
                <p><strong>$${place.price}</strong> / night</p>
                <a href="place.html?id=${place.id}" class="details-button">View Details</a>
        `;

            container.appendChild(card);
        });
}

    /* -----------------------------------------
       FILTER PLACES
    --------------------------------------------*/
    function enableFiltering() {
        const priceFilterEl = document.getElementById("price-filter");

        priceFilterEl.addEventListener("change", () => {
            const maxPrice = priceFilterEl.value;
            const cards = document.querySelectorAll(".place-card");

            cards.forEach(card => {
                const price = parseInt(card.dataset.price);

                if (maxPrice === "All" || price <= parseInt(maxPrice)) {
                    card.style.display = "block";
                } else {
                    card.style.display = "none";
                }
            });
        });
    }

    /* -----------------------------------------
       CHECK AUTHENTICATION ON INDEX PAGE
    --------------------------------------------*/
    const loginLink = document.getElementById("login-link");

    const token = getCookie("token");

    if (loginLink) {
        if (!token) {
            loginLink.style.display = "block";
        } else {
            loginLink.style.display = "none";
            fetchPlaces(token);
        }
    }

});

    /* -----------------------------------------
       Extract Place ID
    --------------------------------------------*/

function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get("id");
}

    /* -----------------------------------------
      Fetch place details
    --------------------------------------------*/
    async function fetchPlaceDetails(token, placeId) {
        try {
            const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
                headers: token ? { "Authorization": `Bearer ${token}` } : {}
            });

            const data = await response.json();

            if (!response.ok) {
                console.error("Error fetching place details:", data);
                return;
            }

            displayPlaceDetails(data);

        } catch (err) {
            console.error("Network error:", err);
        }
    }

    /* -----------------------------------------
    Display the place details
    --------------------------------------------*/

    function displayPlaceDetails(place) {
    const container = document.getElementById("place-details");
    container.innerHTML = ""; // clear old

    const div = document.createElement("div");
    div.classList.add("place-detail-card");

    div.innerHTML = `
        <h1>${place.title}</h1>
        <img src="https://picsum.photos/600/350?random=${place.id}">
        <p><strong>Price:</strong> $${place.price}</p>
        <p><strong>Description:</strong> ${place.description}</p>

        <h3>Amenities</h3>
        <ul>
            ${place.amenities.map(a => `<li>${a}</li>`).join("")}
        </ul>

        <h3>Reviews</h3>
        <div id="reviews">
            ${
                place.reviews.length === 0
                ? "<p>No reviews yet.</p>"
                : place.reviews.map(r => `<p><strong>${r.user}</strong>: ${r.text}</p>`).join("")
            }
        </div>
    `;

    container.appendChild(div);
}

    /* -----------------------------------------
    Display load place page
    --------------------------------------------*/

    function loadPlacePage() {
        const placeId = getPlaceIdFromURL();
        const token = getCookie("token");
        const addReviewSection = document.getElementById("add-review");

        if (!placeId) {
            console.error("Missing place ID");
            return;
        }

        // Show / hide review form
        if (!token) {
            addReviewSection.style.display = "none";
            fetchPlaceDetails(null, placeId);
        } else {
            addReviewSection.style.display = "block";
            fetchPlaceDetails(token, placeId);
        }
    }

document.addEventListener("DOMContentLoaded", () => {
    if (window.location.pathname.includes("place.html")) {
        loadPlacePage();
    }
});