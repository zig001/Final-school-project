$(document).ready( function() {
   $(document).on("change", "select", function() {
      let img = $(this).find("option:selected").attr("data-img-src");
      $("#preview").empty().append("<image src=" + img + "/>");
   });
});