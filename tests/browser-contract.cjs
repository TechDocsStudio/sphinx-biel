const http = require("node:http"),
  fs = require("node:fs"),
  path = require("node:path"),
  assert = require("node:assert/strict");
const puppeteer = require("puppeteer");
const widget = path.join(
  process.env.BIEL_WIDGET_DIR ||
    path.dirname(require.resolve("biel-search/package.json")),
  "dist/biel-search",
);
const site = path.resolve(process.argv[2]);
const expected = JSON.parse(fs.readFileSync(path.join(site, "expected.json")));
const prefix =
  "https://cdn.jsdelivr.net/npm/biel-search@0.1.94/dist/biel-search/";
const server = http.createServer((req, res) => {
  const url = new URL(req.url, "http://localhost");
  const file = path.resolve(
    site,
    url.pathname === "/" ? "index.html" : url.pathname.slice(1),
  );
  if (
    !file.startsWith(site + path.sep) ||
    !fs.existsSync(file) ||
    fs.statSync(file).isDirectory()
  ) {
    res.writeHead(404);
    res.end();
    return;
  }
  res.setHeader(
    "Content-Type",
    file.endsWith(".html")
      ? "text/html"
      : file.endsWith(".css")
        ? "text/css"
        : "text/javascript",
  );
  fs.createReadStream(file).pipe(res);
});
(async () => {
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  const url = `http://127.0.0.1:${server.address().port}`;
  const browser = await puppeteer.launch({
    executablePath: process.env.PUPPETEER_EXECUTABLE_PATH,
    headless: true,
    pipe: true,
    args: ["--no-sandbox"],
  });
  try {
    const page = await browser.newPage();
    page.on("pageerror", (error) => console.log("Pageerror", error.message));
    await page.evaluateOnNewDocument(() => {
      window.injected = 0;
      window.fetch = async () => ({
        ok: true,
        status: 200,
        json: async () => ({
          whitelabel: false,
          actions: [],
          suggested_questions: [],
          initial_message: "",
          filters: [],
        }),
      });
      window.WebSocket = class {
        constructor() {
          setTimeout(() => this.onopen?.(), 0);
        }
        close() {}
        send() {}
        addEventListener() {}
        removeEventListener() {}
      };
    });
    await page.setRequestInterception(true);
    page.on("request", (request) => {
      if (request.url().startsWith(url)) return request.continue();
      if (request.url().startsWith(prefix)) {
        const file = path.resolve(
          widget,
          request.url().slice(prefix.length).split("?")[0],
        );
        if (
          file.startsWith(widget + path.sep) &&
          fs.existsSync(file) &&
          !fs.statSync(file).isDirectory()
        )
          return request.respond({
            status: 200,
            headers: { "Access-Control-Allow-Origin": "*" },
            contentType: file.endsWith(".css") ? "text/css" : "text/javascript",
            body: fs.readFileSync(file),
          });
      }
      return request.abort();
    });
    await page.goto(url);
    await page.waitForFunction(() =>
      document.querySelector("biel-button")?.classList.contains("hydrated"),
    );
    const result = await page.evaluate(() => {
      const button = document.querySelector("biel-button");
      return {
        project: button.project,
        text: button.textContent,
        renderMath: button.renderMath,
        initialMessages: button.initialMessages,
        children: button.querySelectorAll("img,script").length,
        executed: window.injected,
      };
    });
    assert.equal(result.project, expected.project);
    assert.equal(result.text, expected.button_text ?? expected.bielButtonText);
    assert.equal(result.renderMath, false);
    assert.deepEqual(
      result.initialMessages,
      expected.initial_messages ?? expected.initialMessages,
    );
    assert.equal(result.children, 0);
    assert.equal(result.executed, 0);
    await page.evaluate(() =>
      document
        .querySelector("biel-button")
        .shadowRoot.querySelector("[part=button]")
        .click(),
    );
    await page.waitForFunction(() =>
      document.querySelector("biel-bot")?.classList.contains("hydrated"),
    );
    const bot = await page.evaluate(() => {
      const bot = document.querySelector("biel-bot");
      return {
        project: bot.project,
        disableInput: bot.disableInput,
        initialMessages: bot.initialMessages,
        renderMath: bot.renderMath,
      };
    });
    assert.equal(bot.project, expected.project);
    assert.equal(bot.disableInput, true);
    assert.equal(bot.renderMath, false);
    assert.deepEqual(
      bot.initialMessages,
      expected.initial_messages ?? expected.initialMessages,
    );
    console.log(
      `PASS installed integration actual built widget: ${site}, literal label/quotes/Unicode/close-script, false booleans, arrays, button event and bot props`,
    );
  } finally {
    await browser.close();
    server.close();
  }
})().catch((error) => {
  console.error(error);
  server.close();
  process.exitCode = 1;
});
