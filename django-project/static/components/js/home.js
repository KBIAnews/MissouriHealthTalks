function resizeCards(){
    $(".home-card").css("height", $(window).height() - 50 + "px")
}

var homeMap = {};
var markers= L.markerClusterGroup();

$(document).ready(function(){
    this.resizeCards();
    this.homeMap = L.map('home-map',{
        center: [38.9517, -92.3341],
        zoom: 7,
        dragging: true,
        doubleClickZoom: false,
        zoomControl: true,
        scrollWheelZoom: false
    });

    var storyIcon = L.icon({
        iconUrl: '/static/marker-icon-red.png',
        iconSize: [28, 44] //38,57
    });

    L.tileLayer('https://api.mapbox.com/styles/v1/nathanlawrence/cj59z9ndw6f212rmkcx0rkilr/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoibmF0aGFubGF3cmVuY2UiLCJhIjoiY2l5dzl5NDA4MDAxeTJxcWU3NTVwaHBsMyJ9.kNUj23zWfRJNLl2W8hsAyA', {
        maxZoom: 18
    }).addTo(this.homeMap);


    console.log(this.markers);

    for (var i = 0, len = this.stories.length; i < len; i++) {
        story = stories[i];
        marker = L.marker([story.lat,story.long], {icon: storyIcon});

        this.markers.addLayer(marker);

        marker.bindPopup('<a href="' + story.url + '"><h3>' + story.title + '</h3></a><p class="description">' +
            story.description + '</p><p class="readmore"><a href="'
            + story.url + '">Read More</a></p>');
    }

    this.homeMap.addLayer(markers);
});
