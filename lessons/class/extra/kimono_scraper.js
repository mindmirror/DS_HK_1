var kimono = (function($){
  var api = 'd2nkn824',
      apikey = '7cb169974fbeaf8b1fd22e7d961f7cc7',
      beaches = [],
      data = [];

  function handleBeaches(data) {
    data.results.beaches.forEach(function(e, i){
      e.beach['id'] = e.beach.href.split('beachid=')[1]
      beaches.push(e.beach)
    })
  }

  function getBeaches(){
    var req = $.ajax({
          "url": "http://www.kimonolabs.com/api/82r2lbeu",
          "crossDomain":true,
          "dataType":"jsonp",
          "data": {
            "apikey" : apikey,
          }
      });

    req.done(handleBeaches).done(getBeachData)
  }

  function handleBeachData(resp){
    console.log(resp);
    r = resp.results
    url = r.index.rating['src']
    data.push({
      "title" : r.index.title,
      "index": url.charAt(url.length - 5),
      "tides": r.tides.tides,
      "weather": r.forecase.weather,
      "wind": r.forecase.wind.text
    })
  }

  function getBeachData(){
    for (beach in beaches){
      (function(id){
        var req = $.ajax({
          "url": "http://www.kimonolabs.com/api/" + api,
          "crossDomain":true,
          "dataType":"jsonp",
          "data": {
            apikey : apikey,
            beachid : id
          }
        })
        req.done(handleBeachData)
      })(beaches[beach]['id']);
    }
  }

  return {
    set_api : function(api){api=api},
    set_apikey : function(key){apikey=apikey},
    load_beaches : function(){
      return beaches.length ? beaches : getBeaches()
    },
    beaches : beaches,
    data : data
  }

}(jQuery))
