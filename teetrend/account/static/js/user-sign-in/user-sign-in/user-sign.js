$(document).ready(function() {
  $('input[type=password]').each(function(index) {
      $(this).after('<input type="checkbox" id="show-password' + index + '" class="password-checkbox"><label for="show-password' + index + '"> Show password</label>');
      $('#show-password' + index).change(function() {
          var passwordField = $(this).prev('input[type=password]');
          var passwordFieldType = passwordField.attr('type');
          
          if (this.checked) {
              passwordField.attr('type', 'text');
          } else if (!this.checked) {
            passwordField.attr('type', 'password');
          }
      });
  });
});