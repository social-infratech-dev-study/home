const MESSAGE_BODY = require("../src/const");

test("message body check", () => {
  expect(!!MESSAGE_BODY.username).not.toBe(false);
  expect(!!MESSAGE_BODY.message).not.toBe(false);
});
