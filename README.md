## Deep Learning based Automatic Risk Recognition and Navigation System for the Visually Impaired, Navi-Ro
## 시각장애인을 위한 안전 내비게이션 시스템, 내비로(Navi-Ro)

**프로젝트 소개**  

‘내비로(Navi-Ro)’는 실내에서 시각장애인이 원하는 장소로 안내해주고, 보행 중에 나타나는 장애물을 인공지능으로 인식하여 안전하게 이동할 수 있도록 도와줍니다. 
 
**개발 배경 및 필요성**  

GPS 사용이 불가한 실내에서 시각장애인이 누군가의 도움 없이 이동하는 것은 어렵습니다. 또한 이동 중에 마주치는 각종 장애물에 대한 정보가 없어 위험에 노출되어 있습니다. 이러한 위험과 불편함을 줄이고자 자동 위험인식 내비게이션 시스템을 개발하였습니다.

**주요 기능**  

- 문자정보와 feature extraction을 통한 경로 안내: RGB Camera 이미지를 분석하여 알아낸 사용자의 현재 위치와 사용자가 지정한 목적지를 토대로 탐색한 최단경로로 길을 안내합니다. 시각장애인의 특성을 고려하여, 모든 과정은 natural language processing을 이용해 음성으로 이뤄집니다.  
- LiDAR와 vision model의 융합을 통한 장애물 안내: 딥러닝 기반의 object detection algorithm을 이용하여 장애물의 종류를 파악합니다. 직접 개발한 이미지 기반의 위험 인식 인공지능 모델을 통해 그 장애물에 해당되는 LiDAR의 거리데이터를 추출하여 시각장애인에게 안내합니다. 

**수상 내역**  

- 2020 프로보노 공모전 동상  
- 2020 이화 도전학기제 대표 사례 선정  
- University of San Diego 주최 GSIC (Global Social Innovation Challenge) Global finalist 선정  

**관련 기사**  

https://inews.ewha.ac.kr/news/articleView.html?idxno=32454  
http://www.dhnews.co.kr/news/articleView.html?idxno=135341  

**관련 영상**  

https://www.youtube.com/watch?v=TtiyApOsPcE&list=LL&index=16  
