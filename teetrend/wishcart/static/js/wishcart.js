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


document.addEventListener('DOMContentLoaded', function() {
  var icons = document.querySelectorAll('.product-wishlist');
  icons.forEach(function(icon, index) {
    var dsIcon1 = icon.querySelector('.ds-wish-icon-1');
    var userId = icon.getAttribute('data-user-id');
    var dsIcon2 = icon.querySelector('.ds-wish-icon-2');
    var wishlistTxt = icon.querySelector('.ds-wish-txt');
    var tshirtId = icon.getAttribute('data-tshirt-id');  
    var tshirtTitle = icon.getAttribute('data-title');
    var tshirtName = icon.getAttribute('data-name');
    // Load state from localStorage
    var state = localStorage.getItem('wishlist-' + tshirtId + userId);
    console.log(state);
    console.log(userId);
    if (state === 'active') {
      icon.style.backgroundColor = "rgb(71, 71, 71)";
      dsIcon1.style.display = "none";
      dsIcon2.style.display = "block";
      wishlistTxt.style.color = "white";
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
        state = null;
        localStorage.removeItem('wishlist-' + tshirtId + userId);
      } else {
        // If the item is not in the wishlist, add it
        xhr.open('POST', 'add_to_wishlist/' + tshirtTitle + '/' + tshirtName + '/' + tshirtId + '/');
        icon.style.backgroundColor = "rgb(71, 71, 71)";
        dsIcon1.style.display = "none";
        dsIcon2.style.display = "block";
        wishlistTxt.style.color = "white";
        state = 'active';
        localStorage.setItem('wishlist-' + tshirtId + userId, 'active');
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
document.addEventListener('DOMContentLoaded', (event) => {
  let element = document.querySelector('.wish-messages');
  if (element) {
    element.addEventListener('animationend', function(event) {
      if (event.animationName === 'wish-slide-up') {
        this.classList.remove('wish-slide-up');
      }
    });
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

document.addEventListener('DOMContentLoaded' , function() {
  var removeWishlists = document.querySelectorAll('.wish-cart-remove-icon');
  removeWishlists.forEach(function(removeWishlist) {
    var tshirtId = removeWishlist.getAttribute('data-tshirt-id');
    var userId = removeWishlist.getAttribute('data-user-id');
    var state = localStorage.getItem('wishlist-' + tshirtId + userId);
    removeWishlist.addEventListener('click' , function() {
      var itemInCart = localStorage.getItem('wishlist-' + tshirtId + userId);
      if(itemInCart === 'active') {
        var xhr = new XMLHttpRequest();
        var csrftoken = getCookie('csrftoken');
        // If the item is not in the cart, add it
        xhr.open('POST', 'remove_from_wishlist_nv/' + tshirtId + '/');
        state = null;
        localStorage.removeItem('wishlist-' + tshirtId + userId);
        localStorage.setItem('applyStyles' + tshirtId , 'true');
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
        xhr.send();
        xhr.onload = function() {
          if (xhr.status == 200) {
            var message = 'Remove item from Wishlist';
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
    })
  })
})

// The items adding to cart
document.addEventListener('DOMContentLoaded', function() {
  var addToCartBtns = document.querySelectorAll('.move-to-bag-btn');
  addToCartBtns.forEach(function(addToCartBtn) {
    var userId = addToCartBtn.getAttribute('data-user-id');
    var tshirtId = addToCartBtn.getAttribute('data-tshirt-id');  
    var tshirtTitle = addToCartBtn.getAttribute('data-title');
    var tshirtName = addToCartBtn.getAttribute('data-name');
    var state = localStorage.getItem('wishlist-' + tshirtId + userId);
    var cart = localStorage.getItem('cart-' + tshirtId + userId);
    console.log(localStorage);
    console.log(cart);
    console.log(userId);
    addToCartBtn.addEventListener('click', function() {
      var itemInCart = localStorage.getItem('cart-' + tshirtId + userId);
      if (itemInCart !== 'active') {
        var xhr = new XMLHttpRequest();
        var csrftoken = getCookie('csrftoken');
        // If the item is not in the cart, add it
        xhr.open('POST', 'add_to_cart/' + tshirtTitle + '/' + tshirtName + '/' + tshirtId + '/');
        addToCartBtn.innerHTML = '<button style="background-color: red; color: white;" class="move-to-bag-btn" data-tshirt-id="' + tshirtId + '" data-title="' + tshirtTitle + '" data-name="' + tshirtName + '" onclick="location.href=\'/tshirt/checkout/cart\'">View the Bag</button>';
        cart = 'active';
        state = null;
        localStorage.removeItem('wishlist-' + tshirtId + userId)
        localStorage.setItem('cart-' + tshirtId + userId, 'active');
        localStorage.setItem('applyStyles' + tshirtId + userId , 'true');
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
      } else {
        var message = 'This item is already in your cart';
        var messageElement = document.querySelector('.wish-messages');
        messageElement.style.display = "block";
        messageElement.textContent = message;
        messageElement.classList.remove('wish-slide-up'); // Remove the class to allow the animation to run again
        setTimeout(function() {
          messageElement.classList.remove('wish-slide-up'); // Ensure the class is removed before adding it again
          messageElement.classList.add('wish-slide-up');
        }, 3000);
      }
    });    
  });
});
document.addEventListener('DOMContentLoaded', (event) => {
  let element = document.querySelector('.wish-messages');
  if (element) {
    element.addEventListener('animationend', function(event) {
      if (event.animationName === 'wish-slide-up') {
        this.classList.remove('wish-slide-up');
      }
    });
  }
});

document.addEventListener('DOMContentLoaded', function() {
  var removeIcons = document.querySelectorAll('.cart-remove-btn');
  if(removeIcons) {
    removeIcons.forEach(function(removeIcon) {
      var userId = removeIcon.getAttribute('data-user-id');
      var tshirtId = removeIcon.getAttribute('data-tshirt-id');  
      var state = localStorage.getItem('wishlist-' + tshirtId + userId);
      var cart = localStorage.getItem('cart-' + tshirtId + userId);
      console.log(localStorage);
      console.log(cart);
      removeIcon.addEventListener('click', function() {
        var itemInCart = localStorage.getItem('cart-' + tshirtId + userId);
        if (itemInCart === 'active') {
          var xhr = new XMLHttpRequest();
          var csrftoken = getCookie('csrftoken');
          // If the item is in the cart, remove it
          xhr.open('POST', 'remove_from_cart/' + tshirtId + '/');
          cart = null;
          localStorage.removeItem('cart-' + tshirtId + userId);
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

              // Remove the item from the page
              var itemElement = document.querySelector('.item-' + tshirtId + userId);
              if (itemElement) {
                  itemElement.remove();
              }
            } else {
              console.log('Error: ' + xhr.status);
            }
          }
        }
      });
    });
  }    
});
document.addEventListener('DOMContentLoaded', (event) => {
  let element = document.querySelector('.wish-messages');
  if (element) {
    element.addEventListener('animationend', function(event) {
      if (event.animationName === 'wish-slide-up') {
        this.classList.remove('wish-slide-up');
      }
    });
  }
});

document.addEventListener("DOMContentLoaded", function() {
  var addressBtn = document.querySelector(".address-btn");
  var bagBtn = document.querySelector(".bag-btn");
  var paymentBtn = document.querySelector(".payment-btn");
  if(addressBtn) {
    addressBtn.addEventListener("click", function() {
      setActiveClass('Address');
    });
  }
  if(bagBtn) {
    bagBtn.addEventListener("click", function() {
      setActiveClass('Bag');
    });
  }
  if(paymentBtn) {
    paymentBtn.addEventListener("click", function() {
      setActiveClass('Payment');
    });
  }
  function setActiveClass(textContent) {
    var activeItems = document.querySelectorAll(".cart-list-items.active");
    activeItems.forEach(function(item) {
      item.classList.remove("active");
    });
    var listItems = document.querySelectorAll(".cart-list-items");
    listItems.forEach(function(item) {
      if(item.textContent.includes(textContent)) {
        item.classList.add("active");
      }
    });
  }
});


document.addEventListener("DOMContentLoaded" , function() {
  var itemSelections = document.querySelectorAll('.cart-order-btn');
  var loadingSpinner = document.querySelector('.cart-loading-time');
    itemSelections.forEach(function(itemSelection) {
      itemSelection.addEventListener('click' , function() {
        loadingSpinner.style.display = "block"; // Show the loading spinner
        setTimeout(function() {
          loadingSpinner.style.display = "none"; // Hide the loading spinner after 3 seconds
        }, 600);
      });
    })
});

document.addEventListener("DOMContentLoaded" , function() {
  var itemRemoveBtns = document.querySelectorAll('.cartItem-remove');
  var removeModalContainers = document.querySelectorAll('.move-from-cart-container');
  var closeConfirmModals = document.querySelectorAll('.cart-remove-modal-close');
  var removeIcons = document.querySelectorAll('.cart-remove-btn');
  var moveToWislistIcons = document.querySelectorAll('.cart-moveTo-wishlist');
  itemRemoveBtns.forEach(function(itemRemoveBtn , index) {
    itemRemoveBtn.addEventListener('click' , function() {
      removeModalContainers[index].style.display = "block";
    });
  });
  closeConfirmModals.forEach(function(closeConfirmModal , index) {
    closeConfirmModal.addEventListener('click' , function() {
      removeModalContainers[index].style.display = "none";
    });
  });
  removeIcons.forEach(function(removeIcon , index) {
    removeIcon.addEventListener('click' , function() {
      removeModalContainers[index].style.display = "none";
    });
  });
  moveToWislistIcons.forEach(function(moveToWishlistIcon , index) {
    moveToWishlistIcon.addEventListener('click' , function() {
      removeModalContainers[index].style.display = "none";
    })
  })
});

document.addEventListener('DOMContentLoaded', function() {
  var moveToWislistIcons = document.querySelector('.cart-moveTo-wishlist');
  if (moveToWislistIcons) {
    var userId = moveToWislistIcons.getAttribute('data-user-id');
    var tshirtId = moveToWislistIcons.getAttribute('data-tshirt-id');  
    var tshirtTitle = moveToWislistIcons.getAttribute('data-title');
    var tshirtName = moveToWislistIcons.getAttribute('data-name');
    var state = localStorage.getItem('wishlist-' + tshirtId + userId);
    var cart = localStorage.getItem('cart-' + tshirtId + userId);
    console.log(localStorage);
    console.log(state);
    console.log(userId);
    moveToWislistIcons.addEventListener('click', function() {
      var itemInWishlist = localStorage.getItem('wishlist-' + tshirtId +userId);
      console.log(itemInWishlist);
      if (itemInWishlist !== 'active') {
        console.log("Hii");
        var xhr = new XMLHttpRequest();
        var csrftoken = getCookie('csrftoken');
        // If the item is in the cart, remove it
        xhr.open('POST', 'cart_to_wishlist/' + tshirtTitle + '/' + tshirtName + '/' + tshirtId + '/');
        state = 'active';
        cart = null;
        localStorage.setItem('wishlist-' + tshirtId + userId , state);
        localStorage.removeItem('cart-' + tshirtId + userId);
        localStorage.setItem('applyStyles' + tshirtId + userId, 'false');
        // Get the CSRF token and set it as a header
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
        xhr.send();
        xhr.onload = function() {
          if (xhr.status == 200) {
            var message = 'Item moved to wishlist';
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
      } else {
        console.log("Hello");
        var message = 'Item already in wishlist';
        var messageElement = document.querySelector('.wish-messages');
        messageElement.style.display = "block";
        messageElement.textContent = message;
        messageElement.classList.remove('wish-slide-up'); 
        setTimeout(function() {
          messageElement.classList.remove('wish-slide-up'); 
          messageElement.classList.add('wish-slide-up');
        }, 3000);
      }
    });
  }    
});
document.addEventListener('DOMContentLoaded', (event) => {
  let element = document.querySelector('.wish-messages');
  if (element) {
    element.addEventListener('animationend', function(event) {
      if (event.animationName === 'wish-slide-up') {
        this.classList.remove('wish-slide-up');
      }
    });
  }
});

document.addEventListener('DOMContentLoaded', function() {
  var icons = document.querySelectorAll('.product-wishlist'); 
  icons.forEach(function(icon) {
    var dsIcon1 = icon.querySelector('.ds-wish-icon-1'); 
    var dsIcon2 = icon.querySelector('.ds-wish-icon-2'); 
    var wishlistTxt = icon.querySelector('.ds-wish-txt');
    var tshirtId = icon.getAttribute('data-tshirt-id');
    var userId = icon.getAttribute('data-user-id');
    if (localStorage.getItem('applyStyles' + tshirtId + userId) === 'true') {
      var state = localStorage.getItem('wishlist-' + tshirtId + userId);
      state = null;
      localStorage.removeItem('wishlist-' + tshirtId + userId);
      icon.style.backgroundColor = "white";
      dsIcon1.style.display = "block";
      dsIcon2.style.display = "none";
      wishlistTxt.style.color = "black";
      localStorage.removeItem('applyStyles' + tshirtId + userId); 
    } else if (localStorage.getItem('applyStyles' + tshirtId + userId) === 'false') {
      var state = localStorage.getItem('wishlist-' + tshirtId + userId);
      state = 'active';
      localStorage.setItem('wishlist-' + tshirtId + userId, 'active');
      icon.style.backgroundColor = "rgb(71, 71, 71)";
      dsIcon1.style.display = "none";
      dsIcon2.style.display = "block";
      wishlistTxt.style.color = "white";
      localStorage.removeItem('applyStyles' + tshirtId + userId); 
    }
  });
});

document.addEventListener('DOMContentLoaded' , function() {
  var cartItems = document.querySelectorAll('.cart-items-list');
  var retailPriceDetail = document.querySelector('.total-retail-price-value');
  var teesItemCount = document.querySelector('.item-count');
  var discountPriceValue = document.querySelector('.discount-price-value');
  var shippingFee = document.querySelector('.shipping-fee');
  var lessThanMin = document.querySelector('.less-min');
  var greaterThanMin = document.querySelector('.greater-min');
  var totalAmount = document.querySelector('.total-amount-value');
  var totalPrice = 0;
  var totalRetailPrice = 0;
  var discountPrice = 0;
  if(cartItems) {
    cartItems.forEach(function(cartItem) {
      var itemPrice = parseFloat(cartItem.getAttribute('data-price'));
      var itemRetailPrice = parseFloat(cartItem.getAttribute('data-retail-price'));
      var itemCount = cartItem.getAttribute('data-item-count');
      totalPrice += itemPrice;
      totalRetailPrice += itemRetailPrice;
      discountPrice = totalRetailPrice - totalPrice;
      console.log(itemPrice);
      console.log(itemRetailPrice);
      console.log(totalPrice);
      console.log(totalRetailPrice);
      console.log(discountPrice);
      console.log(itemCount);
      if(teesItemCount !== null) {
        teesItemCount.textContent = itemCount;
      }
    })
    if(totalPrice < 500) {
      shippingFee.textContent = 40;
      shippingFee.style.color = 'rgb(5, 199, 5)';
      greaterThanMin.style.display = 'inline-block';
      lessThanMin.style.display = 'none';
      retailPriceDetail.textContent = totalRetailPrice.toLocaleString('en-IN', {style: 'currency', currency: 'INR'});
      discountPriceValue.textContent = discountPrice.toLocaleString('en-IN', {style: 'currency', currency: 'INR'});
      totalAmount.textContent = (totalPrice + 40).toLocaleString('en-IN', {style: 'currency', currency: 'INR'});
    }
    if (totalPrice >= 500){
      shippingFee.textContent = 'FREE';
      shippingFee.style.color = 'rgb(5, 199, 5)';
      greaterThanMin.style.display = 'none';
      lessThanMin.style.display = 'inline-block';
      retailPriceDetail.textContent = totalRetailPrice.toLocaleString('en-IN', {style: 'currency', currency: 'INR'});
      discountPriceValue.textContent = discountPrice.toLocaleString('en-IN', {style: 'currency', currency: 'INR'});
      totalAmount.textContent = totalPrice.toLocaleString('en-IN', {style: 'currency', currency: 'INR'});
    }
  }
});