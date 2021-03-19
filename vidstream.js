$(function () {
    $.getJSON("gogo-stream.json", data => {
        sessionStorage.setItem("my_data", JSON.stringify(data))
        console.log("data = ", data);
        process_data(data);
    })
});
var x; // for testing only
function process_data(data) {
    x = data; // for testing only

    var gogostreamData = data["gogo-stream"];

    for (let i = 0; i < gogostreamData.length; i++) {
        let cdata = gogostreamData[i]; // currentData;
        let img_attr = "class=\"center-picture img-thumbnail\""
        let name_attr = "class=\"text-center\""
        let time_attr = "class=\"text-center\""
        let img = "<img " + img_attr + " src=" + cdata["image"] + "></img>"
        let name = "<h3 " + name_attr + " >" + cdata["name"] + "</h3>"
        let time = "<h5 " + time_attr + " >" + cdata["time"] + "</h5>"
        $("#main-content").append("" + img + name + time + "<hr>");
    }
}
