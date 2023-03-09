## AWS Cloudwatch란?
- Amazon CloudWatch는 모니터링 및 관찰 서비스
- CloudWatch는 애플리케이션 모니터링, 시스템 전체 성능 변경에 대응, 리소스에 대한 데이터와 실행 가능한 인사이트를 제공
- AWS에서 사용되는 다양한 서비스의 지표 및 로그를 통합하여 관리가능. 대시보드에 수집한 지표나 로그를 사용자가 원하는 형태로 표시
- 수집한 지표를 분석하거나 설정한 임계치를 넘길 시 AWS SNS와 연계하여 이메일로 통지할 수 있고 EC2나 Autoscaling Group 조작과 연계도 가능
- 지표나 로그의 패턴을 기반으로 다른 AWS 서비스와 연계하는 기능은 AWS Eventbridge를 활용하는 것을 추천

### Billing 알림 설정하기
- https://docs.aws.amazon.com/ko_kr/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html

### Cloudwatch Agent
- EC2에 기본적으로 다음 지표 기본적으로 수집함.
    - CPU 사용률(CPUUtilization)
    - 네트워크 사용률(NetworkIn, NetworkOut)
    - 디스크 성능(DiskReadOps, DiskWriteOps)
    - 디스크 읽기/쓰기(DiskReadBytes, DiskWriteBytes)
    - 상태 확인 지표(StatusCheckFailed, StatusCheckFailed_Instance, StatusCheckFailed_System)
    - Cloudwatch 콘솔에서 [모든 지표] > [EC2] 에서 원하는 인스턴스의 ID를 검색하며 다음과 같이 기본적으로 수집되고 있는 것을 확인가능.

- 단순히 인스턴스가 정상 가동되고 있는지를 확인하기에는 위의 지표를 감시하는 것만으로 충분 할 수도 있지만 확실한 모니터링을 위해서는 메모리나 디스크 여유 공간 등의 지표도 모니터링 할 필요가 있음.
- 또 로그나 프로세스 등을 수집하여 모니터링 해야하는 경우도 있음.
- Cloudwatch Agent를 인스턴스에 설치하고 구성 파일을 설정한 후 실행하면 더 많은 지표와 로그 등을 수집할 수 있음.

### Cloudwatch Agent 설치
- cli를 사용하여 cloudwatch agent 설치하기
  - https://docs.aws.amazon.com/ko_kr/AmazonCloudWatch/latest/monitoring/download-cloudwatch-agent-commandline.html

### Cloudwatch Agent 구성파일 설정
- 구성파일은 agent, metrics, logs의 블록으로 구성된 JSON파일.
- agent 블록은 필수이며, 나머지 블록은 선택.
  - agent 섹션 
    - agent 전체구성에 대한 필드
  - metric 섹션
    - 수집하여 Cloudwatch에 게시할 사용자 지정 지표
  - logs 섹션
    - Cloudwatch logs에 게시되는 로그파일을 지정
  - https://docs.aws.amazon.com/ko_kr/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html
