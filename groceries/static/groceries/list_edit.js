function openListEdit() {
    // show modal
    $("#modal-background").css("display", "flex"); // TODO: .show()
    // copy edit template into it
    let $template = $("#edit-template").contents();
    $template.attr("id", "edit");
    $template.appendTo($("#modal"));
    // attach onInput event handler to the input field
    $template.find("input").on("input", getGroceries);
}

function getGroceries(e) {
    let $input = $(e.target);
    $.ajax({
        type: "GET",
        url: $input.attr("x-url"),
        data: {search: $input.value.trim()}, //* param-name must align to expected one from SearchFilter class in viewset
    });
}