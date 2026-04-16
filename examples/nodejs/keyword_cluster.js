const keywords = [
  "text to video api",
  "ai video api",
  "cheapest text to video api",
  "sora vs veo api",
  "text to video api python example",
  "openai compatible api",
  "best ai video api in 2026",
  "suno api alternatives",
  "ai api keyword strategy github"
];

function classify(keyword) {
  const k = keyword.toLowerCase();
  if (k.includes("vs") || k.includes("comparison") || k.includes("best")) return "comparison";
  if (k.includes("cheapest") || k.includes("pricing") || k.includes("buy")) return "transactional";
  if (k.includes("example") || k.includes("how to") || k.includes("strategy")) return "informational";
  return "core";
}

const buckets = {
  core: [],
  informational: [],
  transactional: [],
  comparison: []
};

for (const kw of keywords) {
  buckets[classify(kw)].push(kw);
}

console.log("Keyword Clusters");
console.log("================");
for (const key of Object.keys(buckets)) {
  console.log(`\n[${key}]`);
  for (const kw of buckets[key]) {
    console.log(`- ${kw}`);
  }
}

