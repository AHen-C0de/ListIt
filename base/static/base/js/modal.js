$(function() { // = $( document ).ready()
    // make modal close when clicking on background
    $("#modal-background").on("click", (e) => {
        $("#modal-background").hide();
    });
    // prevent closing modal when clicking on it
    $("#modal").on("click", (e) => {
        e.stopPropagation();
    });
});
