const MESSAGE_BODY = require("./const");
const axios = require("axios");

const postChat = async (body) => {
  if (!body.username || !body.message) {
    throw Error("이름과 메시지를 작성해주세요.");
  }
  await axios({
    method: "post",
    url: "https://github-action-page2.vercel.app/api/pusher/chat-update",
    data: body,
  });
};

postChat(MESSAGE_BODY);
