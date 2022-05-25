$(document).ready(function() {
 $('#district').change(function() {
            var district_id = $('#district').val();
            if (district_id != '') {
                $.ajax({
                    url: "/get_centers",
                    type: "POST",
                    data: {
                        district_id: district_id,
                        csrfmiddlewaretoken: '{{ csrf_token }}',
                    },

                    success: function(data) {
                      $('#center').html(data);
                    }
                });
            } else {
                $('#center').empty();
                $("#center").append("<option value=''>--Select Center--</option>");
            }
        });

 $('#center').change(function() {
            var center_id = $('#center').val();
            if (center_id != '') {
                $.ajax({
                    url: "/get_flowers",
                    type: "POST",
                    data: {
                        center_id: center_id,
                    },

                    success: function(data) {
                      $('#flower').html(data);
                    }
                });
            } else {
                $('#flower').empty();
                $("#flower").append("<option value=''>--Select Flower--</option>");
            }
        });

    $('#flower').change(function() {
            var flower_id = $('#flower').val()
            price=$(this).find(':selected').data('price')
            if (flower_id != '') {
            $('#price').val(price);
            } else {
            $('#price').val("");
            }
        });


         $('#quantity').on('input', function() {
          var qty = $('#quantity').val()
          var price = $('#price').val()
          if (qty != "" && price != "") {
          var total=qty*price
          $('#total').val(total);
          } else {
            $('#total').val("");
            }
        });



    });
