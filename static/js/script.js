$(document).ready(function(){
    $('.add-bookmark').on('click', function(){

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
                $('#add-bookmark').addClass('hidden')
                $('#remove-bookmark').removeClass('hidden')
            }
        });

    });

    $('.remove-bookmark').on('click', function(){

        $donor_id = $(this).attr('data-donor-id');

        console.log($donor_id)
        // donor_id = document.querySelector(donor-id)

        $.ajax({
            type: "POST",
            url: "../removebookmarks/",

            data:{
                donor_id: $donor_id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },

            success: function(){
                // window.location = "../";
                $('#remove-bookmark').addClass('hidden')
                $('#add-bookmark').removeClass('hidden')
            }
        });
    });
});