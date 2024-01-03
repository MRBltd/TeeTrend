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
let mensToggler = document.querySelector('.mens-toggler');
let womensToggler = document.querySelector('.womens-toggler');
let kidsToggler = document.querySelector('.kids-toggler');
let charToggler = document.querySelector('.cat-toggler');
let mensListItems = document.querySelectorAll('.mens-menu-list-items');
let womensListItems = document.querySelectorAll('.womens-menu-list-items');
let kidsListItems = document.querySelectorAll('.kids-menu-list-items');
let charListItems = document.querySelectorAll('.char-menu-list-items');
// Show the menu bar when the navbar toggler is clicked
navbarToggler.addEventListener('click', function(e) {
  menuBar.classList.add('show');
  e.stopPropagation(); // Prevent this click from triggering body click event
});
// Hide the menu bar when any close button is clicked
menubarClose.forEach(function(closeButton) {
  closeButton.addEventListener('click', function(e) {
    menuBar.classList.remove('show');
    // Reset the list items and arrows
    resetListItems();
    resetArrows();
  });
});
// Hide the menu bar when body is clicked
bodyElement.addEventListener('click', function(e) {
  if (e.target === bodyElement) { // Check if the clicked target is the body itself
    menuBar.classList.remove('show');
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
    // Toggle the display of each item in the list
  rightArrow.addEventListener('click', function(e) {
    listItems.forEach(function(listItem) {
      listItem.style.display = "block";
    });
    rightArrow.style.display = "none";
    downArrow.style.display = "block";
  });

  // Hide the list items when the down arrow is clicked
  downArrow.addEventListener('click', function(e) {
    listItems.forEach(function(listItem) {
      listItem.style.display = "none";
    });
    rightArrow.style.display = "block";
    downArrow.style.display = "none";
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

let suggestions = {
  'men tshirts': 'product_catalog/tshirts/?category=MT',
  'men polo neck tshirts': 'product_catalog/tshirts/?category=MT&subcategory=PN',
  'men half sleeves tshirts': 'product_catalog/tshirts/?category=MT&subcategory=HS',
  'men henley neck tshirts': 'product_catalog/tshirts/?category=MT&subcategory=HLN',
  'men hoodies': 'product_catalog/tshirts/?category=MT&subcategory=HD',
  'men sleeveless tshirts': 'product_catalog/tshirts/?category=MT&subcategory=SL',
  'men sweatshirts': 'product_catalog/tshirts/?category=MT&subcategory=SW',
  'men long sleeves tshirts': 'product_catalog/tshirts/?category=MT&subcategory=LS',
  'men printed tshirts': 'product_catalog/tshirts/?category=MT&subcategory=PT',
  'men colorblock tshirts': 'product_catalog/tshirts/?category=MT&subcategory=CBT',

  'women tshirts': 'product_catalog/tshirts/?category=WT',
  'women half sleeves tshirts': 'product_catalog/tshirts/?category=WT&subcategory=HS',
  'women cold shoulder tshirts': 'product_catalog/tshirts/?category=WT&subcategory=CS',
  'women off shoulder tshirts': 'product_catalog/tshirts/?category=WT&subcategory=OS',
  'women hoodies': 'product_catalog/tshirts/?category=WT&subcategory=HD',
  'women sleeveless tshirts': 'product_catalog/tshirts/?category=WT&subcategory=SL',
  'women sweatshirts': 'product_catalog/tshirts/?category=WT&subcategory=SW',
  'women long sleeves tshirts': 'product_catalog/tshirts/?category=WT&subcategory=LS',
  'women Printed tshirts': 'product_catalog/tshirts/?category=WT&subcategory=PT',
  'women colorblock tshirts': 'product_catalog/tshirts/?category=WT&subcategory=CBT',
  'women high neck tshirts': 'product_catalog/tshirts/?category=WT&subcategory=HN',
  'women polo neck tshirts': 'product_catalog/tshirts/?category=WT&subcategory=PN',
  'women white tshirts': 'product_catalog/tshirts/?category=WT&subcategory=WT',
  'women boyfriend tees': 'product_catalog/tshirts/?category=WT&subcategory=BT',
  'women v neck tshirts': 'product_catalog/tshirts/?category=WT&subcategory=VN',
  'women striped tshirts': 'product_catalog/tshirts/?category=WT&subcategory=ST',

  'kids tshirts': 'product_catalog/tshirts/?category=KT',
  'childrens tshirts' : 'product_catalog/tshirts/?category=KT',
  'kids polo neck tshirts': 'product_catalog/tshirts/?category=KT&subcategory=PN',
  'kids v neck tshirts': 'product_catalog/tshirts/?category=KT&subcategory=VN',
  'kids henley neck tshirts': 'product_catalog/tshirts/?category=KT&subcategory=HLN',
  'kids long sleeves tshirts': 'product_catalog/tshirts/?category=KT&subcategory=LS',
  'kids printed tshirts': 'product_catalog/tshirts/?category=KT&subcategory=PT',
  'kids colorblock tshirts': 'product_catalog/tshirts/?category=KT&subcategory=CBT',
  'kids wide neck off shoulder tshirts': 'product_catalog/tshirts/?category=KT&subcategory=WN',
  'kids yoke neck tshirts': 'product_catalog/tshirts/?category=KT&subcategory=YN',
  'kids douche bag neck tshirts': 'product_catalog/tshirts/?category=KT&subcategory=DB',

  'Cloth Materials': '',
  'Pure Cotton': '',
  'Cotton Blend': '',
  'Wool Blend': '',
  'Lycra Blend': '',
  'Organic Cotton': '',

  'Characters T-Shirts': 'product_catalog/tshirts/?category=CT',
  'Marvel Characters': 'product_catalog/tshirts/?characters=MR',
  'Avengers T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=AVM',
  'Spider-Man T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=SMM',
  'Iron Man T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=IMM',
  'Captain America T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=CAM',
  'Thor T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=TM',
  'Loki T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=LM',
  'Doctor Strange T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=DSM',
  'Deadpool T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=DPM',
  'The Hulk T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=HM',
  'Black Widow T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=BWM',
  'Venom T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=VM',
  'Wandavision T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=WVM',
  'Ant-Man T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=AMM',
  'Captain Marvel T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=CMM',
  'Shang Chi T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=SCM',
  'Thanos T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=TNM',
  'Black Panther T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=BPM',
  'Eternals T-Shirts': 'product_catalog/tshirts/?characters=MR&marvel_subcategory=EM',

  'DC Comics T-Shirts': 'product_catalog/tshirts/?characters=DC',
  'Blue Beetle T-Shirts': 'product_catalog/tshirts/?characters=DC&dc_comics_subcategory=BBD',
  'Justice League T-Shirts': 'product_catalog/tshirts/?characters=DC&dc_comics_subcategory=JLD',
  'Batman T-Shirts': 'product_catalog/tshirts/?characters=DC&dc_comics_subcategory=BMD',
  'The Fish T-Shirts': 'product_catalog/tshirts/?characters=DC&dc_comics_subcategory=TFD',
  'Superman T-Shirts': 'product_catalog/tshirts/?characters=DC&dc_comics_subcategory=SMD',
  'Wonder Woman T-Shirts': 'product_catalog/tshirts/?characters=DC&dc_comics_subcategory=WWD',
  'Shazam T-Shirts': 'product_catalog/tshirts/?characters=DC&dc_comics_subcategory=SD',
  'Joker T-Shirts': 'product_catalog/tshirts/?characters=DC&dc_comics_subcategory=JD',
  'Aquaman T-Shirts': 'product_catalog/tshirts/?characters=DC&dc_comics_subcategory=AMD',
  'Green Lantern T-Shirts': 'product_catalog/tshirts/?characters=DC&dc_comics_subcategory=GLD',
  'Harley Quinn T-Shirts': 'product_catalog/tshirts/?characters=DC&dc_comics_subcategory=HQD',
  'Black Adam T-Shirts': 'product_catalog/tshirts/?characters=DC&dc_comics_subcategory=BAD',
  'Suicide Squad T-Shirts': 'product_catalog/tshirts/?characters=DC&dc_comics_subcategory=SSD',

  'Movies & TV T-Shirts': 'product_catalog/tshirts/?characters=MS',
  'Harry Potter T-Shirts': 'product_catalog/tshirts/?characters=MS&movies_tv_subcategory=HPM',
  'Friends T-Shirts': 'product_catalog/tshirts/?characters=MS&movies_tv_subcategory=FM',
  'Star Wars T-Shirts': 'product_catalog/tshirts/?characters=MS&movies_tv_subcategory=SWM',
  'The Mandalorian T-Shirts': 'product_catalog/tshirts/?characters=MS&movies_tv_subcategory=TMM',
  'House of the Dragon T-Shirts': 'product_catalog/tshirts/?characters=MS&movies_tv_subcategory=HDM',
  'Game of Thrones T-Shirts': 'product_catalog/tshirts/?characters=MS&movies_tv_subcategory=GTM',
  'The Lion King T-Shirts': 'product_catalog/tshirts/?characters=MS&movies_tv_subcategory=LKM',

  'Cartoons / Anime T-Shirts': 'product_catalog/tshirts/?characters=CA',
  'Snoopy T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=SNC',
  'Rick and Morty T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=RMC',
  'Looney Tunes T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=LTC',
  'Bugs Bunny T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=BBC',
  'Tweety T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=TC',
  'Space Jam T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=SJC',
  'Tom and Jerry T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=TJC',
  'Scooby Doo T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=SDC',
  'Disney T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=DC',
  'Mickey Mouse T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=MMC',
  'Donald Duck T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=DDC',
  'Samurai Jack T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=SJ',
  'Ben 10 T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=BC',
  'SpongeBob Square Pants T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=SBC',
  'Fido Dido T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=FDC',
  'Chotta Beam T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=CBC',
  'Motu Patlu T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=MPC',
  'Mowgli T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=MC',
  'Doraemon T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=DMC',
  'Jackie Chan Adventure T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=JAC',
  'Little Krishna T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=LKC',
  'Shiva T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=SC',
  'Dora the Explorer T-Shirts': 'product_catalog/tshirts/?characters=CA&cartoons_anime_subcategory=DEC',

  'Web Series T-Shirts': 'product_catalog/tshirts/?characters=WS',
  'Stranger Things T-Shirts': 'product_catalog/tshirts/?characters=STW',
}

let currentIndex = -1;
function showSuggestions(value) {
  let suggestionsDiv = document.getElementById('suggestions');
  suggestionsDiv.style.display = 'none';
  suggestionsDiv.style.overflowY = 'hidden';
  suggestionsDiv.innerHTML = '';
  if (value.length > 0) {
    suggestionsDiv.style.display = 'block';
    suggestionsDiv.style.overflowY = 'scroll'; 
    let a = document.createElement('a');
    a.id = 'the-search-value';
    a.style.cursor = 'pointer';
    a.style.width = '400px';
    a.textContent = value;
    suggestionsDiv.appendChild(a);
    let filteredSuggestions = Object.keys(suggestions).filter(suggestion => suggestion.includes(value));
    filteredSuggestions.forEach((suggestion, index) => {
      let li = document.createElement('li');
      li.innerHTML = '<a class="search-link" href="' + suggestions[suggestion] + '">' + suggestion + '</a>';
      li.className = 'search-list';
      li.id = 'suggestion-' + index;
      suggestionsDiv.appendChild(li);
    });
  }
  currentIndex = -1;
}
window.onunload = function() {
  document.getElementById('searchBox').value = '';
  document.getElementById('suggestions').innerHTML = '';
}