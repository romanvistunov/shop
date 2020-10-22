$(document).ready(function () {
  $("#order_select").change(function () {
    var value = $("#order_select option:selected").val();
    $.ajax({
      url: "/ajax/filter_products/",
      data: {
        ordering: value,
      },
      dataType: "json",
      success: function (data) {
        $('#productrow').html(data.qset);
      },
    });
  });
});

$("#product").change(function () {
  var product = $(this).val();
  $.ajax({
    url: "/ajax/validate_product/",
    data: {
      product: product,
    },
    dataType: "json",
    success: function (data) {
      if (data.is_taken) {
        notie.alert({ type: "success", text: product + " exists" });
      } else {
        notie.alert({ type: "warning", text: product + " does not exists" });
      }
    },
    error: function (jqXHR, exception) {
      var msg = "";
      if (jqXHR.status === 0) {
        msg = "Not connect.\n Verify Network.";
      } else if (jqXHR.status == 404) {
        msg = "Requested page not found [404]";
      } else if (jqXHR.status == 500) {
        msg = "Internal Server Error [500]";
      } else if (exception === "parsererror") {
        msg = "Requested JSON parse failed";
      } else if (exception === "timeout") {
        msg = "Time out error.";
      } else if (exception === "abort") {
        msg = "Ajax request aborted";
      } else {
        msg = "Uncaught Error.\n" + jqXHR.responseText;
      }
      //$('#output').html(msg);
      notie.alert({ type: "error", text: msg });
    },
  });
});
