# google place



## 참고자료

https://github.com/yariksav/vue-google-places>

<https://developers.google.com/places/web-service/details>

<https://github.com/Akryum/vue-googlemaps/blob/master/README.md>

<https://github.com/Akryum/vue-googlemaps>

<https://stackoverflow.com/questions/54411989/problem-with-cors-google-directions-api-get-request-vue-js>

<https://developers.google.com/maps/documentation/javascript/examples/place-details>

<https://developers.google.com/places/place-id>

<https://developers.google.com/places/web-service/autocomplete>

<https://developers.google.com/maps/documentation/javascript/importing_data>>

<https://developers.google.com/maps/documentation/javascript/places>

<https://developers.google.com/maps/documentation/javascript/tutorial>

<https://developers.google.com/maps/documentation/javascript/get-api-key>

<https://developers.google.com/places/place-id>

<https://developers.google.com/maps/documentation/geocoding/start>

<https://markus.oberlehner.net/blog/using-the-google-maps-api-with-vue/>

<http://jeonghwan-kim.github.io/2018/04/07/vue-router.html>

<https://bumcrush.tistory.com/168>

<https://pro-self-studier.tistory.com/76>

<https://stackoverflow.com/questions/49944760/pass-dynamic-data-to-router-link>

<https://developers.google.com/places/web-service/details#PlaceDetailsResults>

<https://m.blog.naver.com/PostView.nhn?blogId=ksh81850&logNo=220277104894&proxyReferer=https%3A%2F%2Fwww.google.com%2F>

<https://developers.google.com/maps/documentation/javascript/examples/infowindow-simple>



## 실행원리

1. 장소아이디 받는방법

2. 지도에 표시될때 상세정보 및 좌표에 마커 찍어주기?

   1. geocoding을 이용하여 거리주소를 경도, 위도로 변환하여 찍어준다.

3. 장소검색

4. 음식점으로 필터링

5. 음식점 마커

6. 음식점이름을 ID로 변환하여 정보 뽑아내기

   

## issue 정리

Google place를 이용하면서 발생했던 문제는 다음과 같습니다.



##### 1. google place autocomplete 모듈을 이용

<https://www.npmjs.com/package/vue-place-autocomplete>를 통해 google 지역 자동완성 시스템을 구축하고자 하였으나 Failed to resolve loader: sass-loader 문제가 발생하였다.

<https://github.com/MikeCheng1208/vue-metamask/issues/1>의 해결방법에 의해 해결되었다.

```
npm i sass-loader
npm i node-sass
```



##### 2. 장소 검색을 위해 장소의 위도, 경도로 좌표변환

평범하게 우리가 흔히 알고있는 '서울특별시 강남구' 와 같은 주소가 아닌 위도 : xxx 경도:xxx로 검색해야하는 문제가 발생하였다. 이를 해결하기 위해 geocoding이라는 google에서 지원해주는 방법을 통해 해결하였다.

```js
async Search() {
    const google = await gmapsInit();
    const geocoder = new google.maps.Geocoder();
    var address = this.field1 // autocomplete 과 v-model로 연결되어있다.
    geocoder.geocode( { 'address': address}, function(results, status) {
          if (status == 'OK') {
            vm.centerlat = results[0].geometry.location.lat()     // 위도
            vm.centerlng = results[0].geometry.location.lng()     // 경도
              
...

}
```



##### 3. axios를 통해 위치기준으로 1.5Km 반경 음식점 검색

여기서는 두가지 문제가 발생하였다.

	1. CORS error
 	2. axios로 받은 데이터가 data 안에 들어가지 않는 error



CORS error의 경우 https://cors-anywhere.herokuapp.com/ 를 이용하여 다음과 같이 하여 문제를 해결하였다

```js
data () {
      return {
          ....
        places:[],
          ....
      },

methods: {
    async Search() {
        ....
        geocoder.geocode( { 'address': address}, function(results, status) {
            const PROXY_URL = 'https://cors-anywhere.herokuapp.com/';
            const PLACE_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
            const LAST_URL ='&radius=1500&type=restaurant&key====Your Key==='
            const URL = PROXY_URL + PLACE_URL + vm.centerlat + ',' + vm.centerlng + LAST_URL
            axios.get(URL)
                  .then((response) => {
                        vm.places = response.data.results
....
```



##### 4.  상세페이지 이동

상세페이지로 이동하는데  place_id값과 함께 보내주기 위해 router-link 를 다음과 같이 이용하였다.

```vue
<router-link :to="{ name: 'Detail', params: { id: place.place_id }}">{{ place.name }} {{ place.rating }}</router-link>
```

 예제는 다음과 같다

```js
// route.js

import Vue from 'vue'
import Router from 'vue-router'

import Home from './view/Home'
import Detail from './view/Detail'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/:id',
            name: 'Detail',
            component: Detail,
            // 데이터 받이 귀해 props를 true로 설정해야한다.
            props: true
        }
    ]
})
```

```vue
<template>
  <div id="home">
    <!-- <core-maps/> -->
    <div v-if="field1" class="alert alert-info">
      Current Value: {{ field1 }}
    </div>
    <place-autocomplete-field v-model="field1" placeholder="Enter an an address, zipcode, or location" label="Address" name="field1" api-key="===Your Key"></place-autocomplete-field>
    <a @click="Search">검색</a>
    <ul>
      <li v-for="place in places">
          <router-link :to="{ name: 'Detail', params: { id: place.place_id }}">{{ place.name }} {{ place.rating }}</router-link>
      </li>
    </ul>
  </div>
</template>


<script>
import axios from 'axios'
import https from 'https';
import gmapsInit from '@/utils/gmaps';

  export default {
    name: "home",
    data () {
      return {
        field1 : '',
        places:[],
        centerlat:0,
        centerlng:0,
      }
    },
    ....
```

