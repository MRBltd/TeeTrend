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
if(span) {
  // When the user clicks on <span> (x), close the modal
  span.onclick = function() { 
    modal.style.display = "none";
  };
} else {
  console.log('Element with class "close" was not found');
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

window.addEventListener('load', function() {
  var mensCatList = document.getElementById('mens-cat-list');
  var womensCatList = this.document.getElementById('womens-cat-list');
  var mensCatToggler = document.getElementById('mens-cat-toggler');
  var womensCatToggler = document.getElementById('womens-cat-toggler');
  var charactersCatToggler = document.getElementById('Characters-cat-toggler');

  function handleWomensCatToggle(e) {
    mensCatList.style.display = "none";
    womensCatList.style.display = "block";
    mensCatToggler.classList.remove('cat-active');
    charactersCatToggler.classList.remove('cat-active');
    womensCatToggler.classList.add('cat-active');
  }
  if(womensCatToggler) {
    womensCatToggler.addEventListener('click', handleWomensCatToggle);
  } else {
    console.log('Element with id "womensCatToggler" was not found');
  }

  function handleMensCatToggle(e) {
    mensCatList.style.display = "block";
    womensCatList.style.display = "none";
    womensCatToggler.classList.remove('cat-active');
    charactersCatToggler.classList.remove('cat-active');
    mensCatToggler.classList.add('cat-active');
  }
  if(mensCatToggler) {
    mensCatToggler.addEventListener('click' , handleMensCatToggle);
  } else {
    console.log('Element with id "mensCatToggler" was not found');
  }

  function handleCharactersCatToggle(e) {
    mensCatList.style.display = "none";
    womensCatList.style.display = "none";
    womensCatToggler.classList.remove('cat-active');
    mensCatToggler.classList.remove('cat-active');
    charactersCatToggler.classList.add('cat-active');
  }
  if(charactersCatToggler) {
    charactersCatToggler.addEventListener('click' , handleCharactersCatToggle);
  } else {
    console.log('Element with id "charactersCatToggler" was not found');
  }
});