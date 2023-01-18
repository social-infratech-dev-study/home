const fs = require("fs");
const githubLabelSync = require("github-label-sync");

fs.readFile(__dirname + "/labels.json", (err, data) => {
  if (err) throw err;
  const labels = JSON.parse(data);

  githubLabelSync({
    accessToken: "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", // "토큰",
    repo: "social-infratech-dev-study/home", // "계정명/저장소이름",
    labels: labels,
  })
    .then((_) => {
      console.log("Success");
    })
    .catch((_) => {
      console.log("Failure");
    });
});
