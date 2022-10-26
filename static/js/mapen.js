function initMap() {
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: { lat: pins[0].latitude, lng: pins[0].longitude },
    });
    const maps = new google.maps.Map(document.getElementById("maps"), {
        zoom: 15,
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
                postvisual = ` <iframe width="64%" height="280px" src="${marker[1].video_en}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="margin-top:30px; margin-left:65px"></iframe>`;
            }
            postdiv.innerHTML = `
            <div class="pinpostdiv" id="pinponstdiv">
            <span class="pinpostclose" 
            onclick="document.getElementById('post').style.display = 'none'">
            close</span>
            <div class="postbkack">
            <span class="pinpostheader">${marker[1].title_en}</span>
            <a class="pinpostlocation" href="${marker[1].location_link}">${marker[1].location}</a>
            <span onclick="copy()">
<div class="post_social_divs" style=" margin-left:8%; background-color:#F1F1E6;"><img src="/static/icons/Iconlink.svg" style="width: 20px; height: 20px; margin-left: 14px; margin-top: 14px; float: left;"></div>
</span>

<a href="https://www.facebook.com/dialog/share?app_id=87741124305&href={{ request.build_absolute_uri }}
"><div class="post_social_divs" style=" background-color:#F1F1E6;"><img src="/static/icons/Vectorfb.svg" style="width: 22px; height: 22px; margin-left: 13.5px; margin-top: 13px; float: left;"></div></a>

<div class="post_social_divs" style=" background-color:#F1F1E6;"><img src="/static/icons/vectortw.svg" style="width: 20px; height: 20px; margin-left: 14px; margin-top: 14px; float: left;"></div>
            <div class="post_line" style="width:70%; margin-left: 7%"></div>
            ${postvisual}
            <span class="pinedpostbody">${marker[1].body_en}</span>
            <a href="${marker[1].source}" target="_blank" style="margin-left:65px; display:block; color:black; margin-bottom: 50px; width: 60%; word-wrap: break-word;"> Source</a>

            </div>
            </div>`;
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
                postvisual = ` <iframe width="100%" height="170px" src="${marker[1].video}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="margin-top:50px"></iframe>`;
            }
            postdiv.innerHTML = `
            <div class="pinpostdiv" id="pinponstdiv">
            <span class="pinpostclose" 
            onclick="document.getElementById('postmobile').style.display = 'none'">
            close</span>
            <div class="postbkack">
            <span class="pinpostheader">${marker[1].title_en}</span>
           <a class="pinpostlocation" href="${marker[1].location_link}">${marker[1].location}</a>
            <span onclick="copy()">
<div class="post_social_divs" style=" margin-left:8%; background-color:#F1F1E6;"><img src="/static/icons/Iconlink.svg" style="width: 20px; height: 20px; margin-left: 14px; margin-top: 14px; float: left;"></div>
</span>

<a href="https://www.facebook.com/dialog/share?app_id=87741124305&href={{ request.build_absolute_uri }}
"><div class="post_social_divs" style=" background-color:#F1F1E6;"><img src="/static/icons/Vectorfb.svg" style="width: 22px; height: 22px; margin-left: 13.5px; margin-top: 13px; float: left;"></div></a>

<div class="post_social_divs" style=" background-color:#F1F1E6;"><img src="/static/icons/vectortw.svg" style="width: 20px; height: 20px; margin-left: 14px; margin-top: 14px; float: left;"></div>
            ${postvisual}
            <span class="pinedpostbody">${marker[1].body_en}</span>
            <a href="${marker[1].source}" target="_blank" style="margin-left:25px; display:block; color:black; margin-bottom: 50px">Source</a>

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