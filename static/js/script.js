$(document).ready(function(){
    $('button').on('click', function(){

        $donor_id = $(this).attr('data-donor-id');

        console.log($donor_id)
        // donor_id = document.querySelector(donor-id)

        $.ajax({
            type: "POST",
            url: "../addbookmarks/",

            data:{
                donor_id: $donor_id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },

            success: function(){
                // window.location = "../";
            }
        });

    });
});