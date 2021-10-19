import $ from "jquery";


$(document).ready(function(){
    $('button').on('click', function(){
        var username = $("input[name='username']").attr('value');
        $.ajax({
            type: 'POST',
            url: 'inSession.php',
            data: {
                current_user: username
            },
            success : function(data){
                alert(data);
            }
        });
    });
});