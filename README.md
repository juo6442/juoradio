# juoradio
주오 대학생 시절, KBS 라디오 방송을 Mac OS X에서도 듣고싶은데 KBS에서는 [콩](http://www.kbs.co.kr/radio/kong/)이라는 앱을 통한 듣기만 지원하고 있었다. 주오는 크아아아아 울부짓었고 요래조래 콩을 까 보고 ~~ㅋㄲㅈㅁ~~ 해서 만들어 보았음. 그리고 주오는 이걸 만들고 나서부터 라디오를 듣지 않고 있다.

## 사용법
아래 주소에서 [Google App Engine](https://cloud.google.com)을 통해 서비스되고 있다. 들어가면 방송별 주소가 나올 것이며, mms를 지원하는 플레이어(VLC 등)으로 재생이 가능하다고 전해들었다. 하지만 redirection 지원 안 하면 재생 안 되는 듯. 근데 요새 그런 게 있나...

https://juoradio.appspot.com

## 원리
콩 앱을 들쑤셔 보니 아래 주소를 사용하고 있는 것을 알았다.

http://kong.kbs.co.kr/live_player/channelMini.php?id=[아이디]&channel=[채널]

아이디는 아무거나 쓰면 되고, 채널은 1 ~ 8 중 한 개. 이 주소를 입력해 보면 html body에 0과 mms 주소가 적혀 있다. 그런데 이 주소의 parameter가 일정 시간마다 변하는 수법을 사용하고 있다. 간단히 파싱해서 이 주소로 redirect시켜주는 게 전부.

Google App Engine을 이용해 2013년부터 구동된 이후 평화롭게 돌고 있었으나, 2017년 옛날 버전의 파이썬은 더 이상 지원을 하지 않겠다는 구글의 최후통첩을 받고 2.7로 migration하는 김에 깃헙에도 올림.

# TODO
주소 안내 페이지 이쁘게 꾸미기. 하지만 아마 안 할 거야...
타임아웃 발생시 3회쯤 retry
