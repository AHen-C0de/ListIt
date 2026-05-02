function openListEdit() {
    $("#modal-background").css("display", "flex"); // TODO: .show()
    let $template = $("#edit-template").contents();
    $template.attr("id", "edit");
    let $modal = $("#modal");
    $template.appendTo($modal);
    $template.find("input").on("input", getGroceries)
}

function getGroceries(e) {
    let $input = $(e.target)
    $.ajax({
        type: "GET",
        url: $input.attr("x-url"),
        data: {search: e.target.value.trim()},
    });
}