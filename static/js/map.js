function initMap() {
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 16,
        center: { lat: pins[0].latitude, lng: pins[0].longitude },
    });
    const maps = new google.maps.Map(document.getElementById("maps"), {
        zoom: 16,
        center: { lat: pins[0].latitude, lng: pins[0].longitude },
    });
    const markers = pins.map(pin => {
        return [new google.maps.Marker({ position: { lat: pin.latitude, lng: pin.longitude, post: pin.post }, map: map }), pin.post]
    });
    const marker = pins.map(pin => {
        return [new google.maps.Marker({ position: { lat: pin.latitude, lng: pin.longitude, post: pin.post }, map: maps }), pin.post]
    });
    // add event listener to each marker
    markers.forEach(marker => {
        marker[0].addListener("click", () => {
            const postdiv = document.getElementById("post");
            postdiv.innerHTML = "";

            if (marker[1].video == ''){
                postvisual = `<img src="/static${marker[1].img}" class="pinedpostimg">`;
            }else{
                postvisual = ` <iframe width="600px" height="315" src="${marker[1].video}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="margin-top:50px; margin-left:65px"></iframe>`;
            }
            postdiv.innerHTML = `
            <div class="pinpostdiv" id="pinponstdiv">
            <span class="pinpostclose" 
            onclick="document.getElementById('post').style.display = 'none'">
            დახურვა</span>
            <div class="postbkack">
            <span class="pinpostheader">${marker[1].title}</span>
            ${postvisual}
            <span class="pinedpostbody">${marker[1].body}</span>
            <a href="${marker[1].source}" target="_blank" style="margin-left:65px; display:block; color:black; margin-bottom: 50px">${marker[1].source}</a>

            </div>
            </div>`;
            console.log(marker);
            document.getElementById("post").style.display = "block";
            document.getElementById("pinponstdiv").style.display = "block";
            document.getElementById("postback").style.display = "block";
        })
    })
    marker.forEach(marker => {
        marker[0].addListener("click", () => {
            const postdiv = document.getElementById("postmobile");
            postdiv.innerHTML = "";

            if (marker[1].video == ''){
                postvisual = `<img src="/static${marker[1].img}" class="pinedpostimg">`;
            }else{
                postvisual = ` <iframe width="85%" height="170px" src="${marker[1].video}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="margin-top:50px; margin-left:25px"></iframe>`;
            }
            postdiv.innerHTML = `
            <div class="pinpostdiv" id="pinponstdiv">
            <span class="pinpostclose" 
            onclick="document.getElementById('postmobile').style.display = 'none'">
            დახურვა</span>
            <div class="postbkack">
            <span class="pinpostheader">${marker[1].title}</span>
            ${postvisual}
            <span class="pinedpostbody">${marker[1].body}</span>
            <a href="${marker[1].source}" target="_blank" style="margin-left:25px; display:block; color:black; margin-bottom: 50px">${marker[1].source}</a>

            </div>
            </div>`;
            console.log(marker);
            document.getElementById("postmobile").style.display = "block";
            document.getElementById("pinponstdiv").style.display = "block";
            document.getElementById("postback").style.display = "block";
        })
    })

}
window.initMap = initMap;