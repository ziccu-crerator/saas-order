import json
import os

log_path = r"C:\Users\Shahi\.gemini\antigravity-ide\brain\27b15d33-bc95-481c-bdc5-861d387b6f1e\.system_generated\logs\transcript.jsonl"

css_content = ""
html_content = ""

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line.strip())
            if "tool_calls" in data:
                for call in data["tool_calls"]:
                    if call["name"] == "write_to_file":
                        target = call["args"]["TargetFile"]
                        if "styles.css" in target and not css_content:
                            css_content = call["args"]["CodeContent"]
                        if "index.html" in target and not html_content:
                            html_content = call["args"]["CodeContent"]
        except Exception:
            pass

with open(r"c:\Users\Shahi\Desktop\saas_new\styles_original.css", "w", encoding="utf-8") as f:
    f.write(css_content)

with open(r"c:\Users\Shahi\Desktop\saas_new\index_original.html", "w", encoding="utf-8") as f:
    f.write(html_content)
