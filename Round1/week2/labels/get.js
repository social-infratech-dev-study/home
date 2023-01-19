const githubLabelSync = require("github-label-sync");

githubLabelSync({
  // accessToken: "토큰", (private)
  repo: "social-infratech-dev-study/home", // "계정명/저장소이름",
  labels: [],
  dryRun: true,
}).then((diff) => {
  const labals = diff.map((label) => label.actual);
  console.log(labals);
});
