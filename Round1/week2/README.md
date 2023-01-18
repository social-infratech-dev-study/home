# 프로젝트 라벨 및 이슈 템플릿 자동화

## 타겟 article(?)

[Github Label, Issue, Pull Request Template 적용하기](https://velog.io/@modolee/github-initial-settings)

### setting

```bash

mkdir home

cd home

git clone https://github.com/social-infratech-dev-study/home.git

cd home/Round1/week2

npm install

```

### label

[github-label-sync](https://www.npmjs.com/package/github-label-sync)

```
npm install

node labels/get.js

node labels/set.js

```

```bash
npm install -g github-label-sync
```

`--dry-run`옵션으로 단순히 라벨 확인만 할 수 있음

```bash
github-label-sync --dry-run --access-token [액세스 토큰] --labels [라벨 json 파일명] [계정명]/[저장소 이름]
```

### Issue template

`.github/ISSUE_TEMPLATE` 하위에 md 파일로 생성

### PR template

`.github/PULL_REQUEST_TEMPLATE.md` 파일로 생성
