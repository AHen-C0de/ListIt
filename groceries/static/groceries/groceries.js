$( document ).ready(() => {
      $("#list").find("li").click(toggleItem);
    }
)

function toggleItem(e) {
    let $item = $(e.target).detach();
    if ($item[0].classList.contains("active")) {
        $("#list").append($item);
        $($item).removeClass("active");
        $($item).addClass("finished");
    } else {
        $("#list").prepend($item);
        $($item).removeClass("finished");
        $($item).addClass("active");
    }
}