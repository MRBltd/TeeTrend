document.addEventListener('DOMContentLoaded', function() {
  var icons = document.querySelectorAll('.mb-wishlist-icon');
  icons.forEach(function(icon) {
      icon.addEventListener('click', function() {
          if (icon.style.color === 'red') {
              // The icon is currently red, so change it to white
              icon.style.color = 'white';
              console.log('white');
          } else {
              // The icon is not red, so change it to red
              icon.style.color = 'red';
              console.log('red');
          }
      });
  });
});

var count = 0;
document.addEventListener('DOMContentLoaded', function() {
  var icons = document.querySelectorAll('.product-whishlist');
  var wishCount = document.querySelector('.wishlist-count-value');
  icons.forEach(function(icon, index) {
    var dsIcon1 = icon.querySelector('.ds-wish-icon-1');
    var dsIcon2 = icon.querySelector('.ds-wish-icon-2');
    var wishlistTxt = icon.querySelector('.ds-wish-txt');
    var tshirtId = icon.getAttribute('data-tshirt-id');  
    var tshirtTitle = icon.getAttribute('data-title');
    var tshirtName = icon.getAttribute('data-name');
    // Load state from localStorage
    var state = localStorage.getItem('wishlist-' + index);
    if (state === 'active') {
      icon.style.backgroundColor = "rgb(71, 71, 71)";
      dsIcon1.style.display = "none";
      dsIcon2.style.display = "block";
      wishlistTxt.style.color = "white";
      count += 1;
    }
    icon.addEventListener('click', function() {
      var xhr = new XMLHttpRequest();
      if (state === 'active') {
        // If the item is already in the wishlist, remove it
        xhr.open('POST', 'remove_from_wishlist/' + tshirtId + '/');  // Replace with the correct URL
        icon.style.backgroundColor = "";
        dsIcon1.style.display = "block";
        dsIcon2.style.display = "none";
        wishlistTxt.style.color = "";
        count -= 1;
        console.log(count);
        state = null;
        localStorage.removeItem('wishlist-' + index);
      } else {
        // If the item is not in the wishlist, add it
        xhr.open('POST', 'add_to_wishlist/' + tshirtTitle + '/' + tshirtName + '/' + tshirtId + '/');
        icon.style.backgroundColor = "rgb(71, 71, 71)";
        dsIcon1.style.display = "none";
        dsIcon2.style.display = "block";
        wishlistTxt.style.color = "white";
        count += 1;
        console.log(count);
        state = 'active';
        localStorage.setItem('wishlist-' + index, 'active');
      }
      // Get the CSRF token and set it as a header
      var csrftoken = getCookie('csrftoken');
      xhr.setRequestHeader('X-CSRFToken', csrftoken);
      xhr.send();
      xhr.onload = function() {
        if (xhr.status == 200) {
          var message = state === 'active' ? 'Item added to wishlist' : 'Item removed from wishlist';
          var messageElement = document.querySelector('.wish-messages');
          messageElement.style.display = "block";
          messageElement.textContent = message;
          messageElement.classList.remove('wish-slide-up'); // Remove the class to allow the animation to run again
          setTimeout(function() {
            messageElement.classList.remove('wish-slide-up'); // Ensure the class is removed before adding it again
            messageElement.classList.add('wish-slide-up');
          }, 3000);
          console.log(state === 'active' ? 'Item added to wishlist' : 'Item removed from wishlist');
        } else {
          console.log('Error: ' + xhr.status);
        }
      }
    });
  });
});
document.querySelector('.wish-messages').addEventListener('animationend', function(event) {
  if (event.animationName === 'wish-slide-up') {
    this.classList.remove('wish-slide-up');
  }
});
// Function to get a cookie by name
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// The items adding to cart
document.addEventListener('DOMContentLoaded', function() {
  var addToCartBtns = document.querySelectorAll('.move-to-bag-btn');
  addToCartBtns.forEach(function(addToCartBtn) {
    var tshirtId = addToCartBtn.getAttribute('data-tshirt-id');  
    var tshirtTitle = addToCartBtn.getAttribute('data-title');
    var tshirtName = addToCartBtn.getAttribute('data-name');
    var state = localStorage.getItem('cart-' + tshirtId);
    addToCartBtn.addEventListener('click', function() {
      var itemInCart = localStorage.getItem('cart-' + tshirtId);
      if (itemInCart !== 'active') {
        var xhr = new XMLHttpRequest();
        var csrftoken = getCookie('csrftoken');
        // If the item is not in the cart, add it
        xhr.open('POST', 'add_to_cart/' + tshirtTitle + '/' + tshirtName + '/' + tshirtId + '/');
        addToCartBtn.innerHTML = '<button style="background-color: red; color: white;" class="move-to-bag-btn" data-tshirt-id="' + tshirtId + '" data-title="' + tshirtTitle + '" data-name="' + tshirtName + '" onclick="location.href=\'/tshirt/cart\'">View the Bag</button>';
        state = 'active';
        localStorage.setItem('cart-' + tshirtId, 'active');
        // Get the CSRF token and set it as a header
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
        xhr.send();
        xhr.onload = function() {
          if (xhr.status == 200) {
            var message = 'Item added to cart';
            var messageElement = document.querySelector('.wish-messages');
            messageElement.style.display = "block";
            messageElement.textContent = message;
            messageElement.classList.remove('wish-slide-up'); // Remove the class to allow the animation to run again
            setTimeout(function() {
              messageElement.classList.remove('wish-slide-up'); // Ensure the class is removed before adding it again
              messageElement.classList.add('wish-slide-up');
            }, 3000);
          } else {
            console.log('Error: ' + xhr.status);
          }
        }
      }
    });    
  });
});
document.querySelector('.wish-messages').addEventListener('animationend', function(event) {
  if (event.animationName === 'wish-slide-up') {
    this.classList.remove('wish-slide-up');
  }
});

document.addEventListener('DOMContentLoaded', function() {
  var removeIcons = document.querySelectorAll('.js-cart-remove-icon');
  removeIcons.forEach(function(removeIcon) {
    var tshirtId = removeIcon.getAttribute('data-tshirt-id');  
    var state = localStorage.getItem('cart-' + tshirtId);
    removeIcon.addEventListener('click', function() {
      var itemInCart = localStorage.getItem('cart-' + tshirtId);
      if (itemInCart === 'active') {
        var xhr = new XMLHttpRequest();
        var csrftoken = getCookie('csrftoken');
        // If the item is in the cart, remove it
        xhr.open('POST', 'remove_from_cart/' + tshirtId + '/');
        state = null;
        localStorage.removeItem('cart-' + tshirtId);
        // Get the CSRF token and set it as a header
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
        xhr.send();
        xhr.onload = function() {
          if (xhr.status == 200) {
            var message = 'Item removed from cart';
            var messageElement = document.querySelector('.wish-messages');
            messageElement.style.display = "block";
            messageElement.textContent = message;
            messageElement.classList.remove('wish-slide-up'); // Remove the class to allow the animation to run again
            setTimeout(function() {
              messageElement.classList.remove('wish-slide-up'); // Ensure the class is removed before adding it again
              messageElement.classList.add('wish-slide-up');
            }, 3000);
          } else {
            console.log('Error: ' + xhr.status);
          }
        }
      }
    });    
  });
});
document.querySelector('.wish-messages').addEventListener('animationend', function(event) {
  if (event.animationName === 'wish-slide-up') {
    this.classList.remove('wish-slide-up');
  }
});