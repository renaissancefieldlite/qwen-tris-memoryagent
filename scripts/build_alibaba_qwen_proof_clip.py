#!/usr/bin/env python3
"""Build the short Alibaba/Qwen Cloud backend proof clip.

The clip is separate from the main demo video. It shows:

- the Qwen Cloud account/free-tier screen capture;
- the public-safe source file that calls Alibaba Cloud Model Studio/Qwen Cloud;
- a masked live API receipt from the Qwen-compatible chat/completions route;
- the Qwen Tris MemoryAgent result receipts that sit behind the submission.
"""

from __future__ import annotations

from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
import time

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


REPO = Path("/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30")
SRC = REPO / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from qwen_agent_buildout.trini_recall.alibaba_qwen_cloud_client import (  # noqa: E402
    complete_with_qwen_cloud,
    qwen_cloud_chat_completions_endpoint,
)
from qwen_agent_buildout.trini_recall import MemoryStore, QwenCloudProvider  # noqa: E402
from qwen_agent_buildout.trini_recall.bootstrap import build_offline_agent, seed_default_memories  # noqa: E402


PROOF_DIR = REPO / "docs" / "qwen_cloud_deployment_proof"
EXPORT_DIR = REPO / "commercial_exports" / "2026-07-04_ALIBABA_QWEN_CLOUD_PROOF"
WORK = EXPORT_DIR / "work"
SITE_ASSET_DIR = Path("/Users/renaissancefieldlite1.0/Documents/Playground/renaissancefieldlite.github.io/assets")

QWEN_SCREENSHOT = PROOF_DIR / "qwen_cloud_free_tier_active_20260701T040738Z.png"
SOURCE_FILE = REPO / "src" / "qwen_agent_buildout" / "trini_recall" / "alibaba_qwen_cloud_client.py"
ARCH_FILE = REPO / "docs" / "ARCHITECTURE.md"
SUBMISSION_PACKET = REPO / "docs" / "QWEN_TRIS_PUBLIC_SUBMISSION_PACKET_2026-07-01.md"

OUT_BASE = "USE_THIS_ALIBABA_QWEN_CLOUD_PROOF_2026-07-04_v02_RUNNING_TRIS"
OUT_VIDEO = EXPORT_DIR / f"{OUT_BASE}.mp4"
OUT_CONTACT_SHEET = EXPORT_DIR / f"{OUT_BASE}_CONTACT_SHEET.jpg"
OUT_RECEIPT_MD = PROOF_DIR / f"{OUT_BASE}_RECEIPT.md"
OUT_RECEIPT_JSON = PROOF_DIR / f"{OUT_BASE}_RECEIPT.json"
OUT_SITE_VIDEO = SITE_ASSET_DIR / "qwen-tris-alibaba-qwen-cloud-proof-20260704-v02-running-tris.mp4"
OUT_SITE_CONTACT = SITE_ASSET_DIR / "qwen-tris-alibaba-qwen-cloud-proof-20260704-v02-running-tris.jpg"

W, H = 1920, 1080
QWEN_BLUE = (38, 112, 255)
QWEN_CYAN = (0, 216, 255)
QWEN_VIOLET = (112, 92, 255)
WHITE = (246, 248, 255)
MUTED = (185, 194, 211)
PANEL = (3, 8, 18, 232)


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        clean = line.strip()
        if not clean or clean.startswith("#") or "=" not in clean:
            continue
        key, value = clean.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def font(size: int, bold: bool = False, mono: bool = False) -> ImageFont.FreeTypeFont:
    if mono:
        candidates = [
            "/System/Library/Fonts/Menlo.ttc",
            "/System/Library/Fonts/SFNSMono.ttf",
        ]
    elif bold:
        candidates = [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
        ]
    else:
        candidates = [
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
        ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default()


F_TITLE = font(76, bold=True)
F_H1 = font(58, bold=True)
F_H2 = font(40, bold=True)
F_BODY = font(31)
F_SMALL = font(24)
F_TINY = font(20)
F_MONO = font(24, mono=True)
F_MONO_BIG = font(34, mono=True)


def wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill=WHITE,
    max_width: int = 900,
    line_spacing: int = 8,
) -> int:
    x, y = xy
    for para in text.split("\n"):
        words = para.split()
        line = ""
        if not words:
            y += fnt.size + line_spacing
            continue
        for word in words:
            candidate = f"{line} {word}".strip()
            if not line or draw.textlength(candidate, font=fnt) <= max_width:
                line = candidate
            else:
                draw.text((x, y), line, font=fnt, fill=fill)
                y += fnt.size + line_spacing
                line = word
        if line:
            draw.text((x, y), line, font=fnt, fill=fill)
            y += fnt.size + line_spacing
    return y


def background() -> Image.Image:
    img = Image.new("RGBA", (W, H), (1, 4, 13, 255))
    draw = ImageDraw.Draw(img)
    for x in range(0, W, 80):
        draw.line((x, 0, x, H), fill=(*QWEN_BLUE, 24), width=1)
    for y in range(0, H, 80):
        draw.line((0, y, W, y), fill=(*QWEN_CYAN, 14), width=1)
    for x in range(-260, W + 260, 150):
        draw.line((x, 0, x + 520, H), fill=(*QWEN_VIOLET, 12), width=1)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((1200, -250, 2240, 750), fill=(38, 112, 255, 42))
    gd.ellipse((-320, 520, 760, 1320), fill=(0, 216, 255, 26))
    img = Image.alpha_composite(img, glow.filter(ImageFilter.GaussianBlur(80)))
    return img


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], outline=QWEN_CYAN) -> None:
    draw.rounded_rectangle(box, radius=18, fill=PANEL, outline=outline, width=2)


def fit_image(path: Path, max_w: int, max_h: int) -> Image.Image:
    img = Image.open(path).convert("RGBA")
    scale = min(max_w / img.width, max_h / img.height)
    resized = img.resize((max(1, int(img.width * scale)), max(1, int(img.height * scale))), Image.Resampling.LANCZOS)
    return resized


def paste_shadow(canvas: Image.Image, img: Image.Image, xy: tuple[int, int]) -> None:
    x, y = xy
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    shadow.paste(Image.new("RGBA", img.size, (0, 0, 0, 150)), (x + 12, y + 16), img.getchannel("A"))
    canvas.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(18)))
    canvas.alpha_composite(img, (x, y))


def header(draw: ImageDraw.ImageDraw) -> None:
    draw.rounded_rectangle((42, 38, 820, 92), radius=8, fill=(0, 0, 0, 220), outline=QWEN_CYAN, width=2)
    draw.text((64, 53), "RENAISSANCE FIELD LITE / QWEN TRIS", font=font(26, bold=True), fill=QWEN_CYAN)
    draw.rounded_rectangle((1360, 38, 1835, 92), radius=8, fill=(0, 0, 0, 220), outline=QWEN_VIOLET, width=2)
    draw.text((1382, 53), "ALIBABA QWEN CLOUD PROOF", font=font(26, bold=True), fill=QWEN_VIOLET)


def slide_title() -> Image.Image:
    img = background()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((95, 185), "Qwen Cloud proof clip", font=F_TITLE, fill=WHITE)
    wrapped(
        draw,
        (100, 288),
        "This separate clip shows the backend/API route that connects Qwen Tris Recall to Alibaba Cloud Model Studio / Qwen Cloud.",
        F_H2,
        MUTED,
        max_width=1180,
        line_spacing=12,
    )
    y = 455
    for label, value in [
        ("Endpoint", "dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions"),
        ("Model", os.getenv("QWEN_MODEL", "qwen-plus")),
        ("Secret handling", "API key loaded from runtime env, never printed"),
        ("Proof file", "src/qwen_agent_buildout/trini_recall/alibaba_qwen_cloud_client.py"),
    ]:
        panel(draw, (120, y, 1800, y + 88), outline=QWEN_CYAN)
        draw.text((150, y + 18), label, font=F_SMALL, fill=QWEN_CYAN)
        wrapped(draw, (420, y + 18), value, F_SMALL, WHITE, max_width=1290, line_spacing=4)
        y += 112
    return img


def slide_alibaba_screen() -> Image.Image:
    img = background()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((85, 125), "Alibaba / Qwen Cloud account route", font=F_H1, fill=WHITE)
    wrapped(draw, (90, 195), "The account has Qwen Cloud quota visible in the Alibaba/Qwen console. The backend calls Qwen through the official compatible endpoint.", F_BODY, MUTED, max_width=1260)
    shot = fit_image(QWEN_SCREENSHOT, 1500, 690)
    paste_shadow(img, shot, ((W - shot.width) // 2, 330))
    return img


def slide_source_code() -> Image.Image:
    img = background()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((85, 120), "Public-safe Qwen API code", font=F_H1, fill=WHITE)
    wrapped(draw, (90, 190), "Judges can inspect the exact source file that builds the payload, masks the key by environment, and calls Alibaba/Qwen chat completions.", F_BODY, MUTED, max_width=1400)
    source = SOURCE_FILE.read_text(encoding="utf-8", errors="replace").splitlines()
    excerpt_lines = []
    for idx, line in enumerate(source, start=1):
        if 17 <= idx <= 81:
            excerpt_lines.append(f"{idx:>3}: {line}")
    panel(draw, (90, 310, 1830, 890), outline=QWEN_VIOLET)
    y = 334
    for line in excerpt_lines[:22]:
        draw.text((125, y), line[:118], font=F_MONO, fill=(220, 231, 255))
        y += 24
    draw.text((125, 920), str(SOURCE_FILE), font=F_TINY, fill=QWEN_CYAN)
    return img


def slide_live_receipt(receipt: dict[str, object]) -> Image.Image:
    img = background()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((85, 125), "Live API receipt", font=F_H1, fill=WHITE)
    wrapped(draw, (90, 198), "One low-token request was sent through the backend proof client. The API key is masked; the response proves the request reached Qwen Cloud.", F_BODY, MUTED, max_width=1320)
    lines = [
        f"created_at_utc: {receipt['created_at_utc']}",
        f"api_key_loaded: {receipt['api_key_loaded']}",
        f"api_base: {receipt['api_base']}",
        f"endpoint: {receipt['endpoint']}",
        f"model: {receipt['model']}",
        f"latency_seconds: {receipt['latency_seconds']}",
        "model_response:",
        f"  {receipt['model_response']}",
    ]
    panel(draw, (125, 350, 1795, 785), outline=QWEN_CYAN)
    y = 390
    for line in lines:
        draw.text((165, y), line, font=F_MONO_BIG if line == "model_response:" else F_MONO, fill=WHITE if line != "model_response:" else QWEN_CYAN)
        y += 52 if line == "model_response:" else 42
    draw.text((130, 830), f"Receipt: {OUT_RECEIPT_MD}", font=F_TINY, fill=QWEN_CYAN)
    return img


def slide_tris_turn(receipt: dict[str, object]) -> Image.Image:
    img = background()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((85, 118), "Qwen Cloud running Tris", font=F_H1, fill=WHITE)
    wrapped(
        draw,
        (90, 190),
        "This is the actual Qwen Tris Recall agent path: seeded memory, SSP packet, RAG evidence, Qwen Cloud provider, and a saved response.",
        F_BODY,
        MUTED,
        max_width=1370,
    )
    rows = [
        ("provider", receipt["tris_provider"]),
        ("model", receipt["tris_model"]),
        ("latency", f"{receipt['tris_latency_seconds']} seconds"),
        ("retrieved memories", ", ".join(receipt["tris_retrieval_ids"][:4])),
        ("evidence docs", ", ".join(receipt["tris_evidence_ids"][:3])),
    ]
    y = 315
    for key, value in rows:
        panel(draw, (115, y, 1805, y + 70), outline=QWEN_CYAN)
        draw.text((145, y + 19), str(key), font=F_SMALL, fill=QWEN_CYAN)
        wrapped(draw, (520, y + 18), str(value), F_SMALL, WHITE, max_width=1180, line_spacing=4)
        y += 84
    panel(draw, (115, 750, 1805, 980), outline=QWEN_VIOLET)
    draw.text((145, 778), "Tris response excerpt", font=F_SMALL, fill=QWEN_VIOLET)
    wrapped(draw, (145, 820), str(receipt["tris_response_excerpt"]), F_SMALL, WHITE, max_width=1560, line_spacing=6)
    return img


def slide_results() -> Image.Image:
    img = background()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((85, 120), "Why this matters for Qwen Tris", font=F_H1, fill=WHITE)
    wrapped(draw, (90, 195), "The cloud route is the runtime lane. The MemoryAgent result is the architecture lane: same model family, stable memory spine, receipts, and baseline comparison.", F_BODY, MUTED, max_width=1350)
    rows = [
        ("Hosted Qwen Cloud memory", "500/500", "architecture-on turns passed"),
        ("Qwen second model slice", "24/24", "hosted architecture-on slice"),
        ("LongBench public slice", "+0.105", "baseline 0.571 -> Qwen Tris 0.676"),
        ("MBPP coding repair", "+4", "67/100 -> 71/100"),
        ("Hermes vs Qwen packet", "20/20 each", "same Mirror Architecture / SSP packet"),
    ]
    y = 340
    for name, score, note in rows:
        panel(draw, (130, y, 1790, y + 104), outline=QWEN_CYAN)
        draw.text((165, y + 24), name, font=F_SMALL, fill=MUTED)
        draw.text((700, y + 14), score, font=F_H2, fill=QWEN_CYAN)
        wrapped(draw, (1000, y + 22), note, F_SMALL, WHITE, max_width=700)
        y += 124
    return img


def write_receipt(receipt: dict[str, object]) -> None:
    PROOF_DIR.mkdir(parents=True, exist_ok=True)
    OUT_RECEIPT_JSON.write_text(json.dumps(receipt, indent=2, sort_keys=True), encoding="utf-8")
    body = f"""# Alibaba / Qwen Cloud Proof Receipt

Created: `{receipt['created_at_utc']}`

## Live API Route

- API key loaded: `{receipt['api_key_loaded']}`
- API base: `{receipt['api_base']}`
- Endpoint: `{receipt['endpoint']}`
- Model: `{receipt['model']}`
- Latency seconds: `{receipt['latency_seconds']}`
- Source code: `{SOURCE_FILE}`

## Model Response

```text
{receipt['model_response']}
```

## Qwen Cloud Running Qwen Tris

- Provider: `{receipt['tris_provider']}`
- Model: `{receipt['tris_model']}`
- Latency seconds: `{receipt['tris_latency_seconds']}`
- Retrieved memory IDs: `{", ".join(receipt['tris_retrieval_ids'])}`
- Retrieved evidence IDs: `{", ".join(receipt['tris_evidence_ids'])}`

```text
{receipt['tris_response_excerpt']}
```

## Public-Safe Boundary

The raw API key is not printed or stored in this receipt. This receipt proves
the Qwen Tris backend proof client reached the Alibaba/Qwen Cloud compatible
chat/completions route at render time.

## Clip

- Proof clip: `{OUT_VIDEO}`
- Contact sheet: `{OUT_CONTACT_SHEET}`
"""
    OUT_RECEIPT_MD.write_text(body, encoding="utf-8")


def call_qwen() -> dict[str, object]:
    load_env_file(REPO / ".env.local")
    api_base = os.getenv("QWEN_API_BASE", "https://dashscope-intl.aliyuncs.com/compatible-mode/v1")
    model = os.getenv("QWEN_MODEL", "qwen-plus")
    endpoint = qwen_cloud_chat_completions_endpoint(api_base)
    created = now_utc()
    start = time.time()
    response = complete_with_qwen_cloud(
        "Return one short sentence confirming this request reached Qwen Cloud for the Qwen Tris MemoryAgent proof clip. Include the words Qwen Cloud and MemoryAgent.",
        timeout=90,
    )
    latency = round(time.time() - start, 2)
    receipt = {
        "created_at_utc": created,
        "api_key_loaded": bool(os.getenv("QWEN_API_KEY")),
        "api_base": api_base,
        "endpoint": endpoint,
        "model": model,
        "latency_seconds": latency,
        "model_response": response.replace("\n", " ").strip(),
        "source_file": str(SOURCE_FILE),
        "architecture_file": str(ARCH_FILE),
        "submission_packet": str(SUBMISSION_PACKET),
    }
    tris = call_qwen_tris_agent()
    receipt.update(tris)
    return receipt


def call_qwen_tris_agent() -> dict[str, object]:
    """Run an actual Qwen Tris Recall architecture-on turn through Qwen Cloud."""

    proof_db = Path(tempfile.gettempdir()) / "qwen_tris_cloud_agent_proof.sqlite3"
    if proof_db.exists():
        proof_db.unlink()
    store = MemoryStore(proof_db)
    seed_default_memories(store)
    agent = build_offline_agent(store)
    provider = QwenCloudProvider.from_env()
    agent.provider = provider
    message = (
        "For the proof clip, identify yourself as Qwen Tris Recall running through "
        "Qwen Cloud, explain what memory/SSP lane you are using, and name the next "
        "gate in two concise paragraphs."
    )
    start = time.time()
    result = agent.answer(message, architecture_on=True)
    latency = round(time.time() - start, 2)
    return {
        "tris_provider": result.provider_name,
        "tris_model": provider.model,
        "tris_latency_seconds": latency,
        "tris_prompt_type": "architecture_on_stable_state_packet",
        "tris_retrieval_ids": [retrieval.item.id for retrieval in result.retrievals],
        "tris_evidence_ids": [hit.doc.id for hit in result.evidence_hits],
        "tris_response_excerpt": result.response.replace("\n", " ").strip()[:900],
        "tris_proof_db": str(proof_db),
    }


def render_video(slides: list[Image.Image]) -> None:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)
    frame_paths: list[Path] = []
    for idx, slide in enumerate(slides, start=1):
        path = WORK / f"slide_{idx:02d}.png"
        slide.convert("RGB").save(path, quality=95)
        frame_paths.append(path)
    list_path = WORK / "slides.txt"
    durations = [4.0, 5.0, 5.0, 5.5, 7.0, 5.0]
    lines: list[str] = []
    for path, duration in zip(frame_paths, durations, strict=True):
        lines.append(f"file '{path}'")
        lines.append(f"duration {duration}")
    lines.append(f"file '{frame_paths[-1]}'")
    list_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    run([
        "ffmpeg",
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(list_path),
        "-vf",
        "fps=30,format=yuv420p",
        "-movflags",
        "+faststart",
        str(OUT_VIDEO),
    ])
    sheet = Image.new("RGB", (W, H), (0, 0, 0))
    thumbs = [slide.convert("RGB").resize((W // 3, H // 3), Image.Resampling.LANCZOS) for slide in slides]
    for idx, thumb in enumerate(thumbs):
        x = (idx % 3) * (W // 3)
        y = (idx // 3) * (H // 3)
        sheet.paste(thumb, (x, y))
    sheet.save(OUT_CONTACT_SHEET, quality=92)
    SITE_ASSET_DIR.mkdir(parents=True, exist_ok=True)
    OUT_SITE_VIDEO.write_bytes(OUT_VIDEO.read_bytes())
    OUT_SITE_CONTACT.write_bytes(OUT_CONTACT_SHEET.read_bytes())


def main() -> None:
    receipt = call_qwen()
    write_receipt(receipt)
    slides = [
        slide_title(),
        slide_alibaba_screen(),
        slide_source_code(),
        slide_live_receipt(receipt),
        slide_tris_turn(receipt),
        slide_results(),
    ]
    render_video(slides)
    print(f"proof_video={OUT_VIDEO}")
    print(f"proof_contact_sheet={OUT_CONTACT_SHEET}")
    print(f"proof_receipt={OUT_RECEIPT_MD}")
    print(f"site_video={OUT_SITE_VIDEO}")
    print(f"site_contact_sheet={OUT_SITE_CONTACT}")


if __name__ == "__main__":
    main()
