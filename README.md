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
<img src="https://user-images.githubusercontent.com/104615408/200173223-76d4cfb9-c148-4507-b909-d2e52f472524.png" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615408/200173273-a457242c-8b2f-479e-8fe9-a59932128925.png" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615408/200173283-b7727600-4de6-44cd-b39c-53aae555cfb9.png" width="60%" height="60%">

### T-검정, 상관관계분석
<img src="https://user-images.githubusercontent.com/104615408/200173320-6d4c338e-5d0d-4e98-b321-164b8b7fcf1a.png" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615408/200173346-ed6d59b2-8134-4f32-bf90-ee6711030d66.png" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615408/200173359-1f552b6e-7fc4-4d10-bb0d-25c256d51cdc.png" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615408/200173388-80a37d03-0cfd-4535-a371-f823bb9e7158.png" width="60%" height="60%">

## ・Power BI 
[File Download](https://github.com/sujinbang/02_MINIPROJECT/tree/main/BI) >> file_name : BI_이륜차사고분석.pbix <br>
<br>
<img src="https://user-images.githubusercontent.com/104615408/200173536-9fff4208-c9cb-44b4-a26d-d0fd28cac65d.png" width="60%" height="60%">




## ・웹사이트 구현
[영상 미리보기](https://github.com/sujinbang/02_MINIPROJECT/tree/main/%EC%8B%9C%EC%97%B0%EC%98%81%EC%83%81)<br>
<br>
<img src="https://user-images.githubusercontent.com/104615408/200173844-c7db5ec3-8853-4a6e-83c8-262023516e8b.png" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615408/200173932-0ff23756-aee6-41c4-8395-9857ccc83298.png" width="60%" height="60%">
<img src="https://user-images.githubusercontent.com/104615408/200173957-a0bafc7f-51cb-4388-b240-d0d6c9230c98.png" width="60%" height="60%">


