
const workShop = function(){
    const axios = require('axios')
    const data = {
        "post": {
            "title": "Sample POST request",
            "content": "Send this request via XMLHTTPRequest",
            "author": "Master Tester!!",
        }
        
    }
    url = 'http://13.125.249.144:8080/ssafy/daejeon/2/posts/'
    axios.get(url)
        .then(function (response) {
            console.log(response);
        })
    axios.post(url, data)
        .then(function (response) {
            console.log(response);
        })
}
const workShopButton = document.querySelector('#button')
workShopButton.addEventListener('click', workShop)