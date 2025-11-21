document.addEventListener("DOMContentLoaded", () => {

    // ---------------------------
    // GET COOKIE
    // ---------------------------
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(";").shift();
        return null;
    }

    // ---------------------------
    // AUTH CHECK
    // ---------------------------
    function checkAuth() {
        const token = getCookie("token");
        if (!token) {
            window.location.href = "index.html"; 
        }
        return token;
    }

    const token = checkAuth();


    // ---------------------------
    // GET PLACE ID FROM URL
    // ---------------------------
    function getPlaceId() {
        const params = new URLSearchParams(window.location.search);
        return params.get("id");
    }

    const placeId = getPlaceId();
    if (!placeId) {
        alert("Invalid place ID.");
        window.location.href = "index.html";
    }


    // ---------------------------
    // SELECT FORM + ELEMENTS
    // ---------------------------
    const form = document.getElementById("review-form");
    const message = document.getElementById("review-message");

    if (!form) {
        console.error("review-form not found in DOM!");
        return;
    }

    // ---------------------------
    // HANDLE SUBMIT
    // ---------------------------
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const text = document.getElementById("review-text").value.trim();
        const rating = document.getElementById("review-rating").value;

        if (!text) {
            message.textContent = "Review cannot be empty.";
            message.style.color = "red";
            return;
        }

        try {
            const res = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}/reviews`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}`
                },
                body: JSON.stringify({
                    place_id: placeId,   // REQUIRED BY BACKEND
                    rating: Number(rating),
                    text: text
                })
            });

            const data = await res.json();

            if (!res.ok) {
                console.log("Backend error:", data);
                message.textContent = data.message || data.error || "Failed to submit review.";
                message.style.color = "red";
                return;
            }

            message.textContent = "Review submitted successfully!";
            message.style.color = "green";
            form.reset();

        } catch (err) {
            message.textContent = "Network error.";
            message.style.color = "red";
        }
    });

});
