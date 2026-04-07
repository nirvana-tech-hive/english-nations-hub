import ZAI from 'z-ai-web-dev-sdk';

const args = process.argv.slice(2);
const url = args[0];

if (!url) {
  console.error('Usage: node extract_emails.mjs <url>');
  process.exit(1);
}

try {
  const zai = await ZAI.create();
  const result = await zai.functions.invoke('page_reader', { url });
  console.log(JSON.stringify({
    title: result.data.title,
    html: result.data.html,
    url: result.data.url,
    publishedTime: result.data.publishedTime,
    text: (result.data.html || '').replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim().substring(0, 5000)
  }));
} catch (error) {
  console.error(JSON.stringify({ error: error.message }));
  process.exit(1);
}
