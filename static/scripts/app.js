$(function () {

    $('#myTab li:first-child a').tab('show')

    setTimeout(() => {
        $("#flash-messages-content").fadeOut("slow")
    }, 3000);

})