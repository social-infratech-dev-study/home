# 프로젝트 라벨 및 이슈 템플릿 자동화

## Article

[Github로 협업하는 방법 - repo 생성 시 할 일](https://didu-story.tistory.com/278)

[Github Label, Issue, Pull Request Template 적용하기](https://velog.io/@modolee/github-initial-settings)

---

## Setting

```bash

mkdir home

cd home

git clone https://github.com/social-infratech-dev-study/home.git

cd home/Round1/week2

npm install
```

### Label

[github-label-sync](https://www.npmjs.com/package/github-label-sync)

script

```
npm install

node labels/get.js

node labels/set.js
```

cli

```bash
npm install -g github-label-sync

github-label-sync --dry-run --access-token [액세스 토큰] --labels [라벨 json 파일명] [계정명]/[저장소 이름]
```

> --dry-run 옵션으로 단순히 라벨 확인만 할 수 있음

> 적용된 라벨 확인: https://github.com/social-infratech-dev-study/home/labels 



### Issue Template

`.github/ISSUE_TEMPLATE.md` 파일 생성

-

### Pull Request Template

`.github/PULL_REQUEST_TEMPLATE.md` 파일 생성

Keyword 커밋과 함께 이슈를 Close 할 수 있는 키워드

```
close
closes
closed
fix
fixes
fixed
resolve
resolves
resolved
```




## 레포 변경사항

[General](https://github.com/social-infratech-dev-study/home/settings)

squash merge 하나로만 적용, 제목 기본 설정 수정
- Allow squash merging 
- Default to pull request title ()

merge된 remote 브랜치 자동 삭제
- Automatically delete head branches 

[Branch protection rules](https://github.com/social-infratech-dev-study/home/settings/branches)

-

https://kth990303.tistory.com/317
https://hong-dev.github.io/bftest/master_branch/

merge전 PR 승인 필요
- Require a pull request before merging

## 참고

### Commit message

[커밋 템플릿](https://git-scm.com/book/ko/v2/Git%EB%A7%9E%EC%B6%A4-Git-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)

슬렉 참고

```
feat: The new feature you're adding to a particular application
fix: A bug fix
style: Feature and updates related to styling
refactor: Refactoring a specific section of the codebase
test: Everything related to testing
docs: Everything related to documentation
chore: Regular code maintenance.[ You can also use emojis to represent commit types]


# 테스트용
```
