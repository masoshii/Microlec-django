$(document).ready(function() {
    $(document).on('click', '#register-submit', function( e ){
        var namesValue = $('#names-input').val();
        var lnamesValue = $('#lnames-input').val();
        var runValue = $('#run-input').val();
        var emailValue = $('#email-input').val();
        var pwdValue = $('#password-input').val();
        var repValue = $('#repeat-password-input').val();

        if (isBlank(emailValue)) {
            $('#weird-email').css('opacity', '0');
            $('#email-emsg').css('opacity', '1');
            $('#email-input').css('border-bottom', '1px solid red');
            alert('1')
            e.preventDefault();
        }
        
        if(!isEmailValid(emailValue) && !isBlank(emailValue)){
            $('#email-emsg').css('opacity', '0');
            $('#weird-email').css('opacity', '1');
            $('#email-input').css('border-bottom', '1px solid red');
            alert('2')
            e.preventDefault();
        }
        
        if(isBlank(pwdValue)){
            $('#password-emsg').css('opacity', '1');
            $('#password-input').css('border-bottom', '1px solid red');
            alert('3')
            e.preventDefault();
        }

        if(isBlank(repValue) || pwdValue != repValue){
            $('#repeat-password-emsg').css('opacity', '1');
            $('#repeat-password-input').css('border-bottom', '1px solid red');
            alert('4')
            e.preventDefault();
        }

        if(isBlank(namesValue)){
            $('#names-emsg').css('opacity', '1');
            $('#names-input').css('border-bottom', '1px solid red');
            alert('5')
            e.preventDefault();
        }
        if(isBlank(lnamesValue)){
            $('#lnames-emsg').css('opacity', '1');
            $('#lnames-input').css('border-bottom', '1px solid red');
            alert('6')
            e.preventDefault();
        }

        if (isBlank(runValue)) {
            $('#weird-run').css('opacity', '0');
            $('#run-emsg').css('opacity', '1');
            $('#run-input').css('border-bottom', '1px solid red');
            alert('7')
            e.preventDefault();
        }
        
        if(!isRunValid(runValue) && !isBlank(runValue)){
            $('#run-emsg').css('opacity', '0');
            $('#weird-run').css('opacity', '1');
            $('#run-input').css('border-bottom', '1px solid red');
            alert('8')
            e.preventDefault();
        }

    });
    $(document).on('input', '.form-control', function(){
        var object = $(this);
        object.css("border-bottom", "1px solid rgb(32, 32, 32)");

        if (object.attr('id') == 'email-input'){
            $('#weird-email').css('opacity', '0');
            $('#email-emsg').css('opacity', '0');
        } else if (object.attr('id') == 'password-input') {
            $('#password-emsg').css('opacity', '0');
        } else if (object.attr('id') == 'run-input'){   
            $('#weird-run').css('opacity', '0');
            $('#run-emsg').css('opacity', '0');
        } else if (object.attr('id') == 'names-input'){   
            $('#names-emsg').css('opacity', '0');
        } else if (object.attr('id') == 'lnames-input'){   
            $('#lnames-emsg').css('opacity', '0');
        }
        else {
            $('#repeat-password-emsg').css('opacity', '0');
        }
    })
});