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
    $itemContainer = $("#item-options");

    $itemContainer.empty(); // rm currently rendered item buttons
    if ($input.val() === "") { return; } // no data -> no request

    $.ajax({
        type: "GET",
        url: $input.attr("x-url"),
        // param-name must align to expected one from SearchFilter class in viewset
        data: {search: $input.val().trim()},
        success: (data) => { // create items buttons from data
            for (item of data) {
                $itemButton = $(`<button>${item.name}</button>`).click(e => setItemOnList(e, item));
                $itemContainer.append($itemButton);
            };
        }
    });
}

function setItemOnList(e, item) {
    let storingInput = $("#select_item_url")
    const urlTemplate = storingInput.val()
    const url = urlTemplate.replace(storingInput.attr("x-pkPlaceholder"), item.id);
    // $.ajax({
    //     type: "POST",
    //     url: $input.attr("x-url"),
    //     // param-name must align to expected one from SearchFilter class in viewset
    //     data: {search: $input.val().trim()},
    //     success: (data) => { // create items buttons from data
    //         for (item of data) {
    //             $itemButton = $(`<button>${item.name}</button>`) //TODO: .click()
    //             $itemContainer.append($itemButton);
    //         };
    //     }
    // });
}