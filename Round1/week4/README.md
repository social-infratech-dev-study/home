## 1. 개요

- GitHub Action은 빌드, 테스트 및 배포 파이프라인을 자동화할 수 있는 CI/CD 플랫폼
  - CI : 지속적인 통합 - 어플리케이션 코드의 새로운 변경 사항이 정기적으로 빌드 및 테스트를 거쳐 공유 리포지토리에 병합됩니다
  - CD : 지속적인 서비스 제공(Continuous Delivery) 및/또는 지속적인 배포
- 레포지토리에서 다른 이벤트가 발생할 때 workflow를 실행할 수 있도록 해준다.

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4af78527-1a24-4933-9fef-50d065fb0995/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230202T073327Z&X-Amz-Expires=86400&X-Amz-Signature=322380eb3a3bc4c744ecf0b340bede03512cce8b97798c262d559952275d6177&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

## 2. Work Flow

- 하나 이상의 작업을 실행하는 구성 가능한 자동화된 프로세스
- 레포지토리의 이벤트로 트리거될 때 실행되거나 수동으로 또는 정의된 일정에 따라 트리거될 수 있다.
- `.github/workflows` 디렉토리에 정의

## 3. Event

- 깃허브에서 일어날 수 있을 대부분의 이벤트를 지정 가능
- work flow의 실행시킬 트리거
- 이벤트 리스트 - [링크](https://docs.github.com/ko/actions/using-workflows/events-that-trigger-workflows)
  - `push`
  - \***\*`issues`\*\***
  - \***\*`pull_request`\*\***
  - \***\*`schedule`\*\***

## 4. Jobs

- `jobs.<job_id>`를 사용하여 작업에 고유 식별자를 지정합니다
  - `<job_id>`는 문자 또는 `_`로 시작해야 하며 영숫자, `-` 또는 `_`만 포함해야 합니다.

```yaml
jobs:
  my_first_job:
    name: My first job
  my_second_job:
    name: My second job
```

- `jobs.<job_id>.runs-on`을 사용하여 작업을 실행할 머신 형식을 정의합니다.
  - GitHub 호스팅 실행기 - [링크](https://docs.github.com/ko/actions/using-jobs/choosing-the-runner-for-a-job#github-%ED%98%B8%EC%8A%A4%ED%8C%85-%EC%8B%A4%ED%96%89%EA%B8%B0-%EC%84%A0%ED%83%9D)

```yaml
runs-on: ubuntu-latest
```

- `jobs.<job_id>.strategy.matrix` 을 사용하여 다양한 작업 구성 행렬을 정의

  - `os`
  - `version`

  ```yaml
  jobs:
    example_matrix:
      strategy:
        matrix:
          version: [10, 12, 14]
          os: [ubuntu-latest, windows-latest]

  {version: 10, os: ubuntu-latest}
  {version: 10, os: windows-latest}
  {version: 12, os: ubuntu-latest}
  {version: 12, os: windows-latest}
  {version: 14, os: ubuntu-latest}
  {version: 14, os: windows-latest}
  ```

- 작업의 종속성 부여
  - 이 예제에서 `job1`은 `job2`가 시작되기 전에 성공적으로 완료해야 하며 `job3`은 `job1`
    및 `job2`모두 완료되기를 기다립니다.

```yaml
jobs:
  job1:
  job2:
    needs: job1
  job3:
    needs: [job1, job2]
```

- 작업의 조건 부여
  - if 를 사용하여 작업을 실행할 수 있는 시기 제어
  ```yaml
  name: example-workflow
  on: [push]
  jobs:
    production-deploy:
      if: github.repository == 'octo-org/octo-repo-prod'
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - uses: actions/setup-node@v3
          with:
            node-version: "14"
        - run: npm install -g bats
  ```
- 동시성
  - `jobs.<job_id>.concurrency` 를 사용하여 동일한 동시성 그룹을 사용하는 단일 작업 또는 워크플로만 한 번에 실행되도록 할 수 있다.
  - 동일한 동시성 그룹에서 현재 실행 중인 작업 또는 워크플로도 취소하려면 `cancel-in-progress: true` 를 지정
  ```yaml
  concurrency:
    group: ${{ github.ref }}
    cancel-in-progress: true
  ```
- 컨테이너
  - `jobs.<job_id>.container` 를 사용하여 컨테이너를 아직 지정하지 않는 작업에서 모든 단계를 실행하는 컨테이너를 생성
  - 컨테이너를 설정하지 않으면 단계가 컨테이너에서 실행되도록 구성된 작업을 참조하지 않는 한, 모든 단계가 runs-on으로 지정된 호스트에서 직접 실행
  ```yaml
  name: CI
  on:
    push:
      branches: [main]
  jobs:
    container-test-job:
      runs-on: ubuntu-latest
      container:
        image: node:14.16
        env:
          NODE_ENV: development
        ports:
          - 80
        volumes:
          - my_docker_volume:/volume_mount
        options: --cpus 1
      steps:
        - name: Check for dockerenv file
          run: (ls /.dockerenv && echo Found dockerenv) || (echo No dockerenv)
  ```
- 작업의 기본 값
  - `jobs.<job_id>.defaults.run` 을 사용해 워크플로의 모든 run 단계의 기본 shell 및 working-directory 옵션을 제공할 수 있다.
  ```yaml
  defaults:
    run:
      shell: bash
      working-directory: scripts
  ```

## 5. 동작

### 5.1 동작 유형

- github-actions-repository - [링크](https://github.com/actions/)
- github-market-place - [링크](https://github.com/marketplace?type=actions)
- Docker ( linux )
- Javascript ( linux, macOS, windows )
- 복합 작업 ( linux, macOS, windows )

## 참고

- GitHub Actions Docs - [링크](https://docs.github.com/ko/actions)
- GitHub Actions 요금 - [링크](https://docs.github.com/ko/billing/managing-billing-for-github-actions/about-billing-for-github-actions)
