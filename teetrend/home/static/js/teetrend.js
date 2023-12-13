// Get the 'back-to-top' button element by its ID
let mybutton = document.getElementById("back-to-top");
// Only proceed if mybutton is not null
if (mybutton) {
  // Attach a scroll event listener to the window
  window.onscroll = function() {
    scrollFunction(); // Call the scrollFunction when the user scrolls
  };
  // Function to determine the visibility of the 'back-to-top' button based on scroll position
  function scrollFunction() {
    // Check if the scroll position is greater than 20 pixels from the top
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      mybutton.style.display = "block"; // If true, display the 'back-to-top' button
    } else {
      mybutton.style.display = "none"; // If false, hide the 'back-to-top' button
    }
  }
  // Attach a click event listener to the 'back-to-top' button
  mybutton.onclick = function() {
    topFunction(); // Call the topFunction when the button is clicked
  };
  // Function to scroll to the top of the page when the 'back-to-top' button is clicked
  function topFunction() {
    // Scroll to the top of the document for various browsers
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
  }
} else {
  console.log("Element with ID 'back-to-top' does not exist");
}

// After 5 seconds, add the slide-up class
setTimeout(function() {
  var messageBox = document.getElementById('messageBox');
  // Check if messageBox is not null
  if (messageBox) {
    messageBox.classList.add('slide-up');
    // After the animation ends, hide the message
    messageBox.addEventListener('animationend', function() {
      messageBox.style.display = 'none';
    });
  }
}, 3000);


// The T-shirt list dropdown section
// Select the elements
let menuBar = document.querySelector('.mobile-menu-bar');
let navbarToggler = document.querySelector('.navbar-toggler');
let menubarClose = document.querySelectorAll('.close-menu');
let bodyElement = document.body; // Get the body element
let mensToggler = document.querySelector('.mb-menu-mens-list');
let womensToggler = document.querySelector('.mb-menu-womens-list');
let kidsToggler = document.querySelector('.mb-menu-kids-list');
let charToggler = document.querySelector('.mb-menu-characters-list');
let mensListItems = document.querySelectorAll('.mens-menu-list-items');
let womensListItems = document.querySelectorAll('.womens-menu-list-items');
let kidsListItems = document.querySelectorAll('.kids-menu-list-items');
let charListItems = document.querySelectorAll('.char-menu-list-items');
// Show the menu bar when the navbar toggler is clicked
navbarToggler.addEventListener('click', function(e) {
  menuBar.style.display = "flex";
  menuBar.style.flexDirection = "column";
  e.stopPropagation(); // Prevent this click from triggering body click event
});
// Hide the menu bar when any close button is clicked
menubarClose.forEach(function(closeButton) {
  closeButton.addEventListener('click', function(e) {
    menuBar.style.display = "none";
    // Reset the list items and arrows
    resetListItems();
    resetArrows();
  });
});
// Hide the menu bar when body is clicked
bodyElement.addEventListener('click', function(e) {
  if (e.target === bodyElement) { // Check if the clicked target is the body itself
    menuBar.style.display = "none";
    // Reset the list items and arrows
    resetListItems();
    resetArrows();
  }
});
// Function to reset all arrows
function resetArrows() {
  document.querySelector('.mens-right-arrow').style.display = "block";
  document.querySelector('.mens-down-arrow').style.display = "none";
  document.querySelector('.womens-right-arrow').style.display = "block";
  document.querySelector('.womens-down-arrow').style.display = "none";
  document.querySelector('.kids-right-arrow').style.display = "block";
  document.querySelector('.kids-down-arrow').style.display = "none";
  document.querySelector('.char-right-arrow').style.display = "block";
  document.querySelector('.char-down-arrow').style.display = "none";
}
// The product selection 
// Function to reset all list items
function resetListItems() {
  mensListItems.forEach(function(listItem) {
    listItem.style.display = "none";
  });
  womensListItems.forEach(function(listItem) {
    listItem.style.display = "none";
  });
  kidsListItems.forEach(function(listItem) {
    listItem.style.display = "none";
  });
  charListItems.forEach(function(listItem) {
    listItem.style.display = "none";
  })
}
// Function to handle the toggling of list items and arrows
function toggleItems(toggler, listItems, rightArrow, downArrow) {
  toggler.addEventListener('click', function(e) {
    // Toggle the display of each item in the list
    listItems.forEach(function(listItem) {
      listItem.style.display = (listItem.style.display === "none" || listItem.style.display === "") ? "block" : "none";
    });
    // Toggle the display of the arrows
    let isArrowHidden = rightArrow.style.display === "none";
    rightArrow.style.display = isArrowHidden ? "block" : "none";
    downArrow.style.display = isArrowHidden ? "none" : "block";
  });
}
// Use the function for the Men's and Women's sections
toggleItems(mensToggler, mensListItems, document.querySelector('.mens-right-arrow'), document.querySelector('.mens-down-arrow'));
toggleItems(womensToggler, womensListItems, document.querySelector('.womens-right-arrow'), document.querySelector('.womens-down-arrow'));
toggleItems(kidsToggler , kidsListItems , document.querySelector('.kids-right-arrow') , document.querySelector('.kids-down-arrow'));
toggleItems(charToggler , charListItems , document.querySelector('.char-right-arrow') , document.querySelector('.char-down-arrow'));

// The Cliking Animation in T-shirt lists
// Function to handle the animation
function handleAnimation(toggler) {
  // Define the animation
  let animation = toggler.animate([
    { backgroundSize: '200% 200%', backgroundPosition: '100% 50%' },
    { backgroundSize: '150% 150%', backgroundPosition: '75% 50%' },
    { backgroundSize: '100% 100%', backgroundPosition: '50% 25%' }
  ], {
    duration: 250 , 
    iterations: 1 // The animation will happen only once
  });
  // Pause the animation initially
  animation.pause();
  // Start the animation when the toggler is clicked
  toggler.addEventListener('click', function(e) {
    // Get the click coordinates
    let x = e.clientX - e.target.offsetLeft;
    let y = e.clientY - e.target.offsetTop;
    // Calculate the background position as a percentage
    let xPos = Math.round((x / e.target.offsetWidth) * 100);
    let yPos = Math.round((y / e.target.offsetHeight) * 100);
    // Reset the animation
    animation.cancel();
    // Start the animation
    animation.play();
    // Set the gradient background
    toggler.style.backgroundImage = 'radial-gradient(circle, white , rgba(10, 10, 10, 0.41))';
    toggler.style.backgroundSize = '200% 200%';
    toggler.style.backgroundPosition = `${xPos}% ${yPos}%`;
  });
  // Reset the background when the animation ends
  animation.addEventListener('finish', function() {
    toggler.style.backgroundImage = '';
    toggler.style.backgroundSize = '';
    toggler.style.backgroundPosition = '';
  });
}
// Use the function for the Men's and Women's sections
handleAnimation(mensToggler);
handleAnimation(womensToggler);
handleAnimation(kidsToggler);
handleAnimation(charToggler);