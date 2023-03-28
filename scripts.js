document.addEventListener("DOMContentLoaded", function () {
    const courseCards = document.querySelectorAll(".course-card");

    courseCards.forEach((card) => {
        card.addEventListener("click", (event) => {
            // Check if the click event originated from a PDF button
            if (event.target.classList.contains("pdf-button")) {
                return; // Do not perform the closing action
            }

            if (card.classList.contains("expanded")) {
                card.classList.remove("expanded");
                // Add a small delay before showing other cards
                setTimeout(() => {
                    courseCards.forEach((otherCard) => {
                        otherCard.style.display = "block";
                    });
                }, 250);
            } else {
                // Hide all other cards when expanding the current card
                courseCards.forEach((otherCard) => {
                    otherCard.style.display = "none";
                });
                card.style.display = "block";
                card.classList.add("expanded");
            }
        });
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            courseCards.forEach((card) => {
                card.classList.remove("expanded");
                // Add a small delay before showing all cards
                setTimeout(() => {
                    card.style.display = "block";
                }, 250);
            });
        }
    });
});
