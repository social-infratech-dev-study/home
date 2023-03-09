const githubLabelSync = require("github-label-sync");

githubLabelSync({
  accessToken: "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",
  repo: "ProtoconNet/pepper-fi-admin", // "계정명/저장소이름",
  labels: [],
  dryRun: true,
}).then((diff) => {
  const labals = diff.map((label) => label.actual);
  console.log(labals);
});
