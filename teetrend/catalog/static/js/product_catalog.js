// back to top 
// Get the 'back-to-top' button element by its ID
let mybutton = document.getElementById("back-to-top");
// Attach a scroll event listener to the window
window.onscroll = function() {
  scrollFunction() // Call the scrollFunction when the user scrolls
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
  topFunction() // Call the topFunction when the button is clicked
};
// Function to scroll to the top of the page when the 'back-to-top' button is clicked
function topFunction() {
  // Scroll to the top of the document for various browsers
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
}

// Get the modal
var modal = document.getElementById("myModal");
// Get the image and insert it inside the modal
var modalImg = document.getElementById("img01");
function openImage(src) {
  modal.style.display = "block";
  modalImg.src = src;
}
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}

// The selecting the specific image in the thumbnails
// Event listener when the window is loaded
window.onload = function() {
  // Get the modal, main image, and thumbnail buttons
  var modal = document.getElementById('myModal');
  var mainImage = document.getElementById('img01');
  var thumbnailButtons = document.getElementsByClassName('tees-desktop-modal-image-thumbnail-button');
  // Add an event listener to each thumbnail button
  for (var i = 0; i < thumbnailButtons.length; i++) {
    thumbnailButtons[i].addEventListener('click', function() {
      // Get the thumbnail image within the clicked button
      var thumbnailImage = this.getElementsByTagName('img')[0];
      // Update the main image's src to match the thumbnail's src
      mainImage.src = thumbnailImage.src;
      // Remove the 'selected' class from all thumbnails
      for (var j = 0; j < thumbnailButtons.length; j++) {
        thumbnailButtons[j].classList.remove('selected');
      }
      // Add the 'selected' class to the clicked thumbnail
      this.classList.add('selected');
    });
  }
};