function initMap() {
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 16,
        center: { lat: pins[0].latitude, lng: pins[0].longitude },
    });
    const markers = pins.map(pin => {
        return [new google.maps.Marker({ position: { lat: pin.latitude, lng: pin.longitude, post: pin.post }, map: map }), pin.post]
    });
    // add event listener to each marker
    markers.forEach(marker => {
        marker[0].addListener("click", () => {
            const postdiv = document.getElementById("post");
            postdiv.innerHTML = "";
            postdiv.innerHTML = `
            <div class="pinpostdiv" id="pinponstdiv">
            <span class="pinpostclose" 
            onclick="document.getElementById('post').style.display = 'none'">
            დახურვა</span>
            <div class="postbkack">
            <span class="pinpostheader">${marker[1].title}</span>

            <span class="pinedpostbody">${marker[1].body}</span>
            </div></div>`;
            console.log(pins)
            console.log(marker)
            document.getElementById("post").style.display = "block";
            document.getElementById("pinponstdiv").style.display = "block";
            document.getElementById("postback").style.display = "block";
        })
    })
}

window.initMap = initMap;