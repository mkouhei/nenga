$(function() {
    function select_year() {
        $("select#year").bind("change", function() {
            var target_url = "/nenga/plan_actual/" + $("select#year").val() + "/";
            location.href = target_url;
        });
    }

    $("input").addClass("form-control");
    $("select").addClass("form-control");

    select_year();
});
