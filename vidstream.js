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
        let img = "<img class=\"picture img-thumbnail\" src=" + cdata["image"] + "></img>"
        let name = "<h3>" + cdata["name"] + "</h3>"
        let time = "<h5>" + cdata["time"] + "</h5>"
        $("#main-content").append("" + img + name + time + "<hr>");
    }
}
