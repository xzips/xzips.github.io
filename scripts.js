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



// Define a function to append the ordinal suffix to a day number
function ordinalSuffix(day) {
    const j = day % 10;
    const k = day % 100;
    if (j === 1 && k !== 11) {
      return day + "st";
    }
    if (j === 2 && k !== 12) {
      return day + "nd";
    }
    if (j === 3 && k !== 13) {
      return day + "rd";
    }
    return day + "th";
  }
  
  // Define the GitHub repository owner, repository name, and branch name
  const owner = 'xzips'; // Replace 'username' with the GitHub username
  const repo = 'xzips.github.io'; // Replace 'repository-name' with the name of the repository
  const branch = 'main'; // Replace 'main' with the branch name (e.g., 'gh-pages')
  
  // Construct the URL for the GitHub API to fetch the latest commit information
  const apiUrl = `https://api.github.com/repos/${owner}/${repo}/commits/${branch}`;
  
  // Fetch the commit data from the GitHub API
  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      // Extract the relevant commit information
      const commitMessage = data.commit.message;
      const commitAuthor = data.commit.author.name;
      const commitDate = new Date(data.commit.author.date);
  
      // Format the date using Intl.DateTimeFormat and the ordinalSuffix function
      const formattedDate = new Intl.DateTimeFormat('en-US', { month: 'long' }).format(commitDate) + ' ' +
        ordinalSuffix(commitDate.getDate()) + ', ' + commitDate.getFullYear() +
        ', ' + commitDate.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit', hour12: true });
  
      // Construct the HTML content to display the commit information
      const commitInfoHtml = `
      <div class="commit-info-box">
          <h3 class="commit-info-title">Live Website Changes</h3>
          <p><strong>Last Commit:</strong> ${commitMessage}</p>
          <p><strong>Date:</strong> ${formattedDate}</p>
      </div>
      `;
  
      // Insert the commit information into the container on the webpage
      document.getElementById('commit-info-container').innerHTML = commitInfoHtml;
    })
    .catch(error => {
      console.error('Error fetching commit data:', error);
    });








    








    function openModal(projectCard) {
        const modal = document.querySelector(".project-modal");
        const modalContent = modal.querySelector(".modal-content");
        const projectTitle = projectCard.querySelector(".project-title").textContent;
        modal.querySelector(".modal-title").textContent = projectTitle;
      
        // Get the original card position and size
        const rect = projectCard.getBoundingClientRect();
      
        // Set initial modal position and size based on the card
        modal.style.top = `${rect.top}px`;
        modal.style.left = `${rect.left}px`;
        modal.style.width = `${rect.width}px`;
        modal.style.height = `${rect.height}px`;
      
        // Display the modal
        modal.classList.add("animating");
        modal.style.display = "flex";
      
        // Animate the modal to fill the screen
        setTimeout(() => {
          modal.style.top = "0";
          modal.style.left = "0";
          modal.style.width = "100%";
          modal.style.height = "100%";
        }, 100);
      
        // Animate the content to the center and make it visible
        setTimeout(() => {
          modalContent.style.position = "relative";
          modalContent.style.opacity = "1";
          modal.classList.add("active");
          modal.classList.remove("animating");
        }, 600);
      }
      
      function closeModal(modal) {
        const modalContent = modal.querySelector(".modal-content");
      
        // Hide the content
        modalContent.style.opacity = "0";
        modal.classList.remove("active");
      
        // Animate the modal back to the original position and size
        setTimeout(() => {
          modal.classList.add("animating");
          const rect = modal.style;
          modal.style.top = rect.top;
          modal.style.left = rect.left;
          modal.style.width = rect.width;
          modal.style.height = rect.height;
        }, 100);
      
        // Hide the modal
        setTimeout(() => {
          modal.style.display = "none";
          modal.classList.remove("animating");
          modalContent.style.position = "static";
        }, 600);
      }
      






