## VPC(Virtual Private Cloud)
### VPC란?
- Amazon Virtual Private Cloud(Amazon VPC)에서는 사용자가 정의한 가상 네트워크로 AWS 리소스를 시작할 수 있습니다.
- 이 가상 네트워크는 AWS의 확장 가능한 인프라를 사용한다는 이점과 함께 고객의 자체 데이터 센터에서 운영하는 기존 네트워크와 매우 유사합니다.
- Private Network를 활용하여 네트워크망을 구성하고 내부에 각종 Resource를 탑재할 수 있는 서비스를 VPC라 합니다. 
- VPC에 들어가는 대표적인 서비스는 EC2, ELB, RDS, Security Group, Network ACL 등이 있습니다. - VPC에 들어 가는 Resource(EC2 등)들은 고유의 사설 IP와 Interface를 반드시 갖게 되며 외부에 공개될 Resource의 경우, 공인 IP를 보유할 수 있습니다. 그리고 AWS 사용자 정의 네트워크 VPC에서 사용하는 사설 IP에 대해 살펴보면 다음과 같습니다.
- VPC를 생성하는 경우, RFC 1918규격에 따라 프라이빗(비공개적으로 라우팅 가능) IPv4 주소 범위에 속하는 CIDR 블록( 또는 이하)을 지정할 수 있음.

  - RFC 1918은 사설 IP 주소 범위를 정의하는 인터넷 표준 문서입니다. 이 문서는 인터넷에서 사용되는 공용 IP 주소 공간을 보호하기 위해 사설 네트워크에서 사용할 수 있는 IP 주소 범위를 정의합니다.
  - RFC 1918은 세 가지 사설 IP 주소 범위를 정의합니다. 이 범위는 다음과 같습니다.
    ```
    10.0.0.0 - 10.255.255.255 (10/8 prefix)
    172.16.0.0 - 172.31.255.255 (172.16/12 prefix)
    192.168.0.0 - 192.168.255.255 (192.168/16 prefix)
    ```
  - 이러한 사설 IP 주소는 인터넷에서 라우팅되지 않으므로, 사설 네트워크에서만 사용되며 인터넷을 통해 액세스할 수 없습니다. 따라서 이러한 사설 IP 주소를 사용하여 내부 네트워크를 구성할 수 있습니다. 

- 하지만 VPC 생성시 허용되는 블록 크기는 /28 넷마스크 ~ /16 넷마스크입니다. 
<div align="center">
<img width="500" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbwch2X%2FbtqDwFqChJF%2FHhxVC5xmuPCjaH6AMb9Jf0%2Fimg.png">
</div>

### 서브넷
- VPC 내에서 IP주소를 분할한 네트워크가 서브넷
  - 서브넷을 사용하면 리소스를 분리하고 보안을 강화할 수 있음.
  - 서브넷은 가용영역(Availability Zone)내에 생성할 수 있음.
  - 서브넷은 VPC의 IP주소범위 안에서 고유한 IP주소범위를 가짐.
  - 외부 인터넷과 통신이 가능한 퍼블릭 서브넷과 그렇지 않은 프라이빗 서브넷을 만들 수도 있음.
<div align="center">
<img width="400" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FrJ54b%2FbtqEADe4aGD%2FIGXACgdsilnQKo2UeSUueK%2Fimg.png">
</div>

### 라우팅 테이블
- 라우팅 테이블(영어: routing table)은 컴퓨터 네트워크에서 목적지 주소를 목적지에 도달하기 위한 네트워크 노선으로 변환시키는 목적으로 사용된다.  
- 각 라우터의 라우팅 테이블은 모든 목적지 정보에 대해 해당 목적지에 도달하기 위해서 거쳐야 할 다음 라우터의 정보를 가지고 있다. 
  
### 인터넷 게이트웨이
- VPC에서 인터넷으로의 통신을 가능하게 해주는 구성 요소입니다. 인터넷 게이트웨이를 VPC에 연결하면 VPC의 인스턴스 및 다른 리소스가 인터넷에 직접 액세스할 수 있습니다.
- VPC는 기본적으로 인터넷과 완전히 격리되어 있으며, VPC 내에서 인스턴스 간 통신이나 인터넷과의 통신을 위해서는 IGW를 사용해야 합니다. I
- VPC에서 Resource(EC2 등)가 인터넷 게이트웨이를 통해서 외부 인터넷과 통신하고자 할 경우 다음과 같은 조건을 갖추어야 함.
  - 1. Internet 통신하고자 하는 Resource가 공인 IP를 보유할 것
  - 2. Resource가 소속된 Subnet의 Routing Table에 '0.0.0.0/0' 목적지로 갖는 Routing 'Internet Gateway'이 있을 것
  - 3. Network ACL과 Security Group 규칙에서 허용할 것

<div align="center">
<img width="800" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F8PjiK%2FbtqDEZ92HAB%2FXbkqKnZ3ItUNfPZ7kJ51O1%2Fimg.png">
</div>

### 참고자료
- https://aws-hyoh.tistory.com/49