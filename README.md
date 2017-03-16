# 오픈아레나 웹사이트 설명
## Pycharm 명령어
맥 위주의 사용법이라서 윈도우는 커맨드가 다를 수 있음
```
# 가상환경 켜기
> source ~/myvenv/bin/activate
# 데이터베이스 연동
> python manage.py makemigrations
> python manage.py migrate
# static 파일 모으기
> python manage.py collectstatic
```

## Django의 구조
* `templates` = html 파일들의 모음
* `static` = img, js, css 파일들의 모음
* `views.py` = 백엔드 프로그래밍
* `urls.py` = url 할당
* `admin.py` = admin 페이지에서 데이터베이스를 볼 수 있도록
* `models.py` = 데이터베이스 구조 설정
* `forsm.py` = input 데이터를 쉽게 받을 수 있도록 (우리는 현재 미사용중)
* `settings.py` = 기본 설정들 변경

## 중요 파일들 설명
* `db.sqlite3` = local 데이터베이스 (나중에 클라우드화 필요)
* `openarena.pem` = AWS 서버 ssh 접속 시 필요
* `rootkey.csv` = AWS S3 클라우드 접속 시 필요
* `requirements.txt` = 가상환경에 설치된 app 리스트 목록 제공 (나중에 다른 곳에서 가상환경 설치 시 빠르게 설치 가능)
* `uwsgi.ini` = AWS 서버에서 서비스 상시 오픈 시 필요

## Models.py 구성
### Tournament
* `id` = 자동으로 key 숫자가 증가한다.
* `username` = 오픈아레나 닉네임
* `email` = 오픈아레나 이메일
* `created` = 대회 제출된 시간
#### tab1
* `tournament_name` = 대회명 (중복 검사)
* `tournament_game` = 게임 카테고리 (기타 입력 포함)
* `tournament_image` = AWS 업로드 후 URL 가져오기 (아직 이미지 사이즈는 따로 설정 안해뒀음)
> `no` 선택 시, 게임에 맞춰 우리가 이미지를 넣어줘야 함.
* `tournament_summary` = 대회 요약 (글자 제한은 없음, 나중 추가 필요)
* `tournament_url` = 대회 URL (openarena.kr/ 뒤 URL)
#### tab2
* `tournament_starttime` = 대회 시작 시간
* `tournament_endtime` = 대회 종료 시간
* `tournament_format` = 대회 포맷 (single_elimination, double_elimination, round_robin, swiss)
* `tournament_format_spec` = 대회 포맷에 대한 세부사항
> `single_elimination` =  3위 결정전을 치를지 말지
> `double_elimination` = 승자조에게 어드밴티지를 줄지 말지
> `round_robin` = 승점을 어떤 방식으로 설정할 것인지 (`custom_system`일 경우, 각 상황 별 포인트를 받는다.)
> `swiss` = 각 상황 별 포인트를 어떻게 설정할지
* `tournament_rule` = 대회 규칙
* `participation` = 대회 참가자 양식을 받을지 말지
> `no`  선택 시, `participation_custom_url`을 통해 오픈아레나 외 다른 플랫폼으로 참가하기 버튼을 연결시킬 수 있음.
> `yes` 선택 시, 아래 세부 사항들을 작성해야 함.
* `participation_type` = 개인 참가 혹은 팀 참가
* `participation_template_custom` = 제공 양식 외 추가 양식을 만들 것인지 여부
* `participation_template_format` = 참가자 양식을 글씨로 받을 것인지, 파일로 받을 것인지
* `participation_template` = 참가자 양식 항목 배열로 받기
* `participation_number` = 참가자를 몇 명이나 받을 것인지
* `participation_time` = 대회 참가 기간을 자동으로 설정되게 할 것인지 아니면 자기가 정할 것인지
> `default` 선택 시, `participation_starttime` = 대회 양식 제출 시간, `participation_endtime` = 대회 시작 시간으로 자동 설정.
> `custom` 선택 시, 자신이 `participation_starttime`, `participation_endtime`을 설정 가능.
* `participation_checkin` = 체크인 기능을 사용할 것인지 (`yes` or `no`)
> `yes` 선택 시, 선택된 시간이 입력됨.
#### tab3
* `funding_notice` = 후원 관련 정책을 읽었는지 (only `yes`)
* `account_notice` = 상금 지급 정책을 읽었는지 (only `yes`)
* `participation_fee` = 참가비를 받을 것인지
> `yes`를 선택한 경우, 금액이 입력됨
* `funding` = 후원비를 받을 것인지
> `yes` 선택 시 아래 사항들을 입력해야 함.
* `funding_goal` = 후원 목표 금액이 얼마인지
* `funding_time` = 후원 가능 기간 설정
> `default` 선택 시, `funding_starttime` = 대회 양식 제출 시간, `funding_endtime` = 대회 종료 시간으로 자동 설정.
> `custom` 선택 시, 자신이 `funding_starttime`, `funding_endtime`을 설정 가능.
* `reward` = 후원 보상을 할 것인지
> `yes`일 경우, `reward_number` = 후원 보상 금액, `reward_spec` = 후원 금액에 따른 보상 내용 입력 필요
* `promise` = 후원 공약을 할 것인지
> `yes`일 경우, `promise_number` = 후원 공약 금액, `promise_spec` = 공약 금액에 따른 공약 내용 입력 필요
#### tab4
* `profile_name` = 진행자명
> `default` 선택 시, 오픈아레나 닉네임을 사용
> `custom` 선택 시, 자신이 입력한 닉네임을 사용
* `profile_introduction` = 진행자 소개
* `profile_image` = 진행자 프로필 이미지
> `no` 선택 시, 기본 프로필 이미지 사용
* `streaming` = 방송을 진행할 주소
> `yes`  선택 시, `streaming_site` = 대회 방송 사이트 종류, `streaming_url` = 대회 방송 사이트 URL 입력 받는다.
* `profile_email` = 진행자 이메일
> `default` 선택 시, 오픈아레나 이메일을 사용
> `custom` 선택 시, 자신이 입력한 이메일을 사용
* `profile_phone` = 진행자의 연락처를 받는다.
* `profile_account` = 진행자가 참가비 혹은 후원비 기능을 사용할 경우, 입력을 받게 된다.
* `creator_enrollment` = 크리에이터 등록 여부
#### after submit
* `confirm` = 우리가 최종적으로 대회를 열지 말지를 선택
* `cover_image` = 따로 대회 이미지가 없는 경우 사용되는 이미지 URL
* `logo_image` = 각 대회에 따른 게임 카테고리 로고 이미지 URL
## SSH 접속
```
# 참고 코드
> ssh -i "openarena.pem" ubuntu@ec2-52-79-197-160.ap-northeast-2.compute.amazonaws.com
> git@github.com:kyounginbaek/Openarena_website.git
> uwsgi --ini uwsgi.ini
```
