$(document).ready(function() {
    $(document).on('click', '#login-submit', function( e ){
        var emailValue = $('#email-input').val();
        var pwdValue = $('#password-input').val();

        if (isBlank(emailValue)) {
            $('#weird-email').css('opacity', '0');
            $('#email-emsg').css('opacity', '1');
            $('#email-input').css('border-bottom', '1px solid red');
            e.preventDefault();
        }
        
        if(!isEmailValid(emailValue) && !isBlank(emailValue)){
            $('#email-emsg').css('opacity', '0');
            $('#weird-email').css('opacity', '1');
            $('#email-input').css('border-bottom', '1px solid red');
            e.preventDefault();
        }
        
        if(isBlank(pwdValue)){
            $('#password-emsg').css('opacity', '1');
            $('#password-input').css('border-bottom', '1px solid red');
            e.preventDefault();
        }
    });
    $(document).on('input', '.form-control', function(){
        var object = $(this);
        object.css("border-bottom", "1px solid rgb(32, 32, 32)");

        if (object.attr('id') == 'email-input'){
            $('#weird-email').css('opacity', '0');
            $('#email-emsg').css('opacity', '0');
        } else {
            $('#password-emsg').css('opacity', '0');
        }
    })
});