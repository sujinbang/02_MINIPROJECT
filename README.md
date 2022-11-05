# 이륜차 사고 정보 제공
<br>

## ・프로젝트 개요
본 프로젝트는 배달 수요 증가와 이륜차 사고가 어떤 연관성이 있는지에 대한 아이디어로 시작하여 사고 다발 지점 정보를 제공하는 프로젝트 입니다.<br>
EDA 기반의 데이터 분석 및 시각화를 진행하였으며. Scikit-learn 라이브러리를 활용하여 이륜차 사고와 배달 사용량을 T-검정으로 확인 후 다항회귀분석 및 상관관계 분석으로 연관성을 확인하였습니다.<br>
분석 내용은 django를 활용하여 구현한 웹페이지에 이미지로 시각화하였으며, 배달 사용량이 가장 많은 서울지역을 대상으로 사고 다발 지점 정보를 제공하는 웹 페이지를 구현하였습니다.<br>
이 때 사용된 기술은 pandas, matplotlib, seaborn, folium, Scikit-learn, django 입니다.

## ・데이터 출처
・ 국가교통부 통계누리 <br>
・ 교통안전정보관리시스템 <br>
・ 통계청 <br>
・ 공공데이터포털 <br>
・ 질병관리청 <br>
## ・분석 내용
### 현황 분석
<img src="https://user-images.githubusercontent.com/104615408/200115699-90ffb4a3-5792-419e-9e0f-fa61831911f1.png" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615408/200115921-f7211ecc-c686-4a9e-99d3-6a8916fe79df.png" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615408/200115932-bdc5007b-08a7-4311-b9fa-5e9d64a9d695.png" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615408/200115939-823313d6-7ad4-42e8-924b-37a0ba68cd33.png" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615408/200115958-67de8269-5b27-49b9-aaaa-654233fca5e3.png" width="60%" height="60%">

### 문제점 분석
<img src="https://user-images.githubusercontent.com/104615408/200116235-745bce21-2876-4d79-8a1e-8ac1447b5b51.png" width="60%" height="60%">




## ・웹사이트 구현
[영상](
