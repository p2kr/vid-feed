$(function () {
    var url = "https://gogo-stream.com/";
    $.get(url, data => {
        console.log(data);
        var vid_names = $(data).find($("div .name"));
        console.log(vid_names);
    });
});
