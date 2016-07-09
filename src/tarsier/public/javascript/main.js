$(document).ready(function() {

    // Initial date-pickers
    $("#start_date").pDatepicker({
        altField : "#start_date_mask",
        altFormat: 'unix',
        format: "YYYY-MM-DD"
    });

    $("#end_date").pDatepicker({
        altField : "#end_date_mask",
        altFormat: 'unix',
        format: "YYYY-MM-DD"
    });

    // Set query string of url if exist for start_date and end_date.
    var queryString = getQueryString();

    // If url contains querystring, set them to input fields.
    if (queryString.start_date != undefined && queryString.start_date != '') {
        var startDate = persianDate(parseInt(queryString.startDate));
        var endDate = persianDate(parseInt(queryString.endDate));

        $("#start_date").val(startDate.year() + '-' + startDate.month() + '-' + startDate.date());
        $("#start_date_mask").val(queryString.startDate);
        $("#end_date").val(endDate.year() + '-' + endDate.month() + '-' + endDate.date());
        $("#ens_date_mask").val(queryString.endDate);
    }
    // Else set end_date one day later start_date by default.
    else {
        var tomorrow = new Date(new Date().getTime() + 24 * 60 * 60 * 1000);
        var endDate = persianDate(parseInt(tomorrow.getTime()));
        $("#end_date").val(endDate.year() + '-' + endDate.month() + '-' + endDate.date());
        $("#ens_date_mask").val(tomorrow.getTime());
    }
});

// Separate query params of urls.
function getQueryString() {
    var queryString = {};
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i=0;i<vars.length;i++) {
    var pair = vars[i].split("=");
        // If first entry with this name
        if (typeof queryString[pair[0]] === "undefined") {
          queryString[pair[0]] = decodeURIComponent(pair[1]);
            // If second entry with this name
        } else if (typeof queryString[pair[0]] === "string") {
          var arr = [ queryString[pair[0]],decodeURIComponent(pair[1]) ];
          queryString[pair[0]] = arr;
            // If third or later entry with this name
        } else {
          queryString[pair[0]].push(decodeURIComponent(pair[1]));
        }
    }
    return queryString;
}
