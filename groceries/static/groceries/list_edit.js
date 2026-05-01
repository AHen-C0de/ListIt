function openListEdit() {
    $("#modal-background").css("display", "flex"); // TODO: .show()
    let $template = $("#edit-template").contents();
    $template.attr("id", "edit");
    let $modal = $("#modal");
    $template.appendTo($modal);
}