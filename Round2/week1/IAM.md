# IAM

## AWS Identity and Access Management
IAM은 AWS 리소스에 대한 액세스를 안전하게 제어할 수 있는 웹 서비스

AWS 계정을 생성할 때는 해당 계정의 모든 권한이 단일 로그인 ID로 시작 = AWS 계정 루트 사용자

그러니까 결국, `인증 제어`

## IAM 작동 방식

- 인증
- 승인
- 작업 또는 연산
- 리소스

![iam-work](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/images/intro-diagram%20_policies_800.png)


## RABC & ABAC

### RBAC(Role-Based access Control)
- 접근이나 작업에 대한 권한을 역할에 따라 결정
- 요리사, 경찰관, 교사 라는 Role
![RBAC](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/images/tutorial-abac-concept.png)

### ABAC(Attribute-Based Access Control)
- 접근이나 작업에 대한 권한을 사용자, 리소스 속성 또는 환경에 따라 결정
- 가장 많은 연봉

![ABAC](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/images/tutorial-abac-rbac-concept.png)

### IAM Policy JSON

```json
/* 하나의 정책에 다수의 Statements가 사용된 예 */
{
  "Version": "2012-10-17", // “2012–10–17”, “2008–10–17” 값을 가질 수 있다.
  "Statement": [
    {
      "Sid": "FirstStatement", // Statement ID로 statement 를 구분하기 위해서 사용
      "Effect": "Allow", // 해당 설정 적용을 Allow / Deny
      "Action": [ // 허용할 행위(액션)
      	"s3:List*",
        "s3:Get*"
      ], 
      "Resource": [ // Action이 영향을 미치는 리소스 리스트를 지정
        "arn:aws:s3:::confidential-data",
        "arn:aws:s3:::confidential-data/*"
      ], 
      "Condition": {
      	"Bool": {"aws:MultiFactorAuthPresent": "true"}
      } // 조건을 충족되는 경우에만 해당 정책을 적용
    }
  ]
}
```


## 마치며
<!-- ![understand](https://cdn.ppomppu.co.kr/zboard/data3/2019/0424/20190424221842_alwsmiwa.jpg) -->
<img src="https://cdn.ppomppu.co.kr/zboard/data3/2019/0424/20190424221842_alwsmiwa.jpg" width="200"/>

## 참조

- https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/introduction.html
- https://hello-backend.tistory.com/175
- https://inpa.tistory.com/entry/AWS-%F0%9F%93%9A-IAM-Policy-JSON-%EA%B5%AC%EC%A1%B0-ARN-%EB%AC%B8%EB%B2%95-%EC%A0%95%EB%A6%AC