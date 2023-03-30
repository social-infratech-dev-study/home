# EB (Elastic Beanstalk)

AWS Beanstalk는 AWS의 PaaS 서비스입니다.

### PaaS(Platform-as-a-service) 서비스란?

사전 구성된 플랫폼 환경에 애플리케이션만 배포해서 실행할 수 있게 해주는 서비스입니다.

![이미지](https://www.redhat.com/rhdc/managed-files/iaas-paas-saas-diagram5.1-1638x1046.png)

`IaaS`는 가상 머신, 스토리지, 네트워크, 운영 체제 및 데이터베이스와 같은 인프라를 제공합니다.
사용자는 이러한 인프라를 제어하고 관리하며, 애플리케이션과 데이터를 위한 운영 체제와 프로그래밍 언어를 선택할 수 있습니다.
이러한 유연성으로 인해 IaaS는 대규모 웹 사이트, 애플리케이션 및 데이터베이스를 호스팅하고 실행하는 데 매우 적합합니다.

`PaaS`는 IaaS보다 더 많은 서비스를 제공합니다.
PaaS는 사용자에게 애플리케이션 및 데이터베이스를 개발, 실행 및 관리하는 데 필요한 플랫폼을 제공합니다.
이러한 플랫폼에는 런타임, 프레임워크, 개발 도구, 데이터베이스 및 보안 등의 서비스가 포함됩니다.
PaaS를 사용하면 사용자는 애플리케이션을 빠르게 개발하고 배포할 수 있으며, 인프라를 관리할 필요가 없습니다.
따라서 개발팀이나 비전문가들이 쉽게 애플리케이션을 개발하고 관리할 수 있습니다.

- 예: heroku, netlify, Azure App Service, Google App Engine 등

요약하면, IaaS는 인프라를 서비스로 제공하는 반면, PaaS는 애플리케이션 개발 및 관리를 위한 플랫폼을 서비스로 제공합니다.
IaaS는 유연성이 높고, PaaS는 개발 속도가 빠릅니다. 따라서 사용자가 원하는 서비스의 범위와 제어 수준에 따라 선택할 수 있습니다.

## Elastic Beanstalk이란 (AWS 공식 설명)

- 웹 애플리케이션 및 서비스를 개발, 배포, 운영하기 위한 서비스입니다.
- Elastic Beanstalk를 사용하면 애플리케이션 개발을 위한 AWS 리소스를 손쉽게 구성하고 배포할 수 있습니다.
- **EC2, S3, RDS, Elastic Load Balancing, Auto Scaling 등의 AWS 리소스를 자동으로 구성**, 애플리케이션 배포 및 운영을 간소화합니다.

- Elastic Beanstalk는 다양한 프로그래밍 언어 및 플랫폼을 지원합니다.
  - Java, .NET, PHP, Node.js, Python, Ruby, Go, Docker 등
- Elastic Beanstalk는 여러 개발자 도구와 연동하여 CI/CD 파이프라인을 구성할 수 있습니다.

AWS Elastic Beanstalk는 개발자가 애플리케이션 코드에만 집중할 수 있도록 기본 인프라를 관리하는 것을 목표로 합니다.
이를 통해 개발자는 애플리케이션 개발에 집중하여 생산성을 높일 수 있습니다.

### 구성요소

![구성요소](https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/images/clearbox-flow-00.png)

## [실습] Node.js 앱을 EB에 배포하기

### 🛠 Prequsition

- node
- [IAM (aws credential)](https://catalog.us-east-1.prod.workshops.aws/workshops/3fd6c80b-39f2-4534-b69c-c400aed50c67/ko-KR/workshop-setting/cli-setting)

### 1단계: 배포할 Express 앱 만들기

```shell
$ npx express-generator

$ express eb-express-app   ## 웹 애플리케이션 프로젝트 생성

$ cd eb-express-app
$ npm install   ## 의존성 패키지 설치

$ npm start ## 앱 실행
```

### 2단계: 로컬에 EB AWS CLI를 설치하기

```shell
### Mac OS
$ brew install awsebcli
```

- [참고: 다양한 OS에서 설치스크립트로 eb cli 설치](https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/eb-cli3-install.html)

### 3단계: EB에 웹 어플리케이션을 배포하기

Elastic Beanstalk 환경을 초기화 & 셋팅 합니다.

- 리전, 애플리케이션 이름, 플랫폼, EC2의 SSH 연결 여부 등을 설정 가능

```shell
$ eb init
```

Elastic Beanstalk 환경을 생성 후, 애플리케이션을 실행합니다.

```shell
$ eb create [환경 이름]

```

### 4단계: AWS 웹사이트에서 구동 확인하기

![이미지](https://d1tlzifd8jdoy4.cloudfront.net/wp-content/uploads/2021/08/7dbe76c356e38bcf9b03af617b340e3e-768x352.png)

### 5단계: 새 버전의 애플리케이션 배포해보기

소스코드를 부분 수정 후, 배포 합니다.
웹 링크를 통해 변경되었는지 확인합니다.

```shell
$ eb deploy

```

### 6단계: 셋팅 가능한 환경 확인하기

- [[공식 문서] EB 환경 구성](https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/customize-containers.html)

---

## 참고 링크

- [(AWS 워크샵) AWS Basic Deployment Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/3fd6c80b-39f2-4534-b69c-c400aed50c67/ko-KR)
- [(공식문서) AWS EB 개발자 안내서](https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/Welcome.html)
- [AWS Elastic Beanstalk을 사용해서 웹 애플리케이션 배포하기](https://dev.classmethod.jp/articles/deploy-express-application-to-elastic-beanstalk/)

```

```
