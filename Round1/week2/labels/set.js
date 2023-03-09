const fs = require("fs");
const githubLabelSync = require("github-label-sync");

fs.readFile(__dirname + "/labels.json", (err, data) => {
  if (err) throw err;
  const labels = JSON.parse(data);

  githubLabelSync({
    accessToken: "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", // "토큰",
    repo: "ProtoconNet/protocon-explorer-v2", // "계정명/저장소이름",
    labels: labels,
  })
    .then((_) => {
      console.log("Success");
    })
    .catch((error) => {
      console.log("Failure", error);
    });
});
