#!/usr/bin/env python3
"""Render the Qwen Tris MemoryAgent commercial.

This is a public-safe three-minute announcement asset that carries the Hermes
Trismegistus arc into the Qwen Cloud MemoryAgent lane without modifying the
Hermes build.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil
import subprocess
import textwrap

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


REPO = Path("/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30")
TRIS = Path("/Users/renaissancefieldlite1.0/Documents/Playground/trismegistus")
TRIS_ASSETS = TRIS / "TRISMEGISTUS_HERMES_CONTEST_LANDING_PAGE" / "assets"
OUT_DIR = REPO / "commercial_exports" / "2026-07-02_QWEN_TRIS_MEMORYAGENT_COMMERCIAL"
WORK = OUT_DIR / "work"
UI_CAPTURE_DIR = OUT_DIR / "ui_captures"

BG = TRIS_ASSETS / "listharmonicsbackground.png"
RFL_LOGO_SYSTEM = TRIS_ASSETS / "rfl-logo-system-grid-public-2026-06-30.png"
TRIS_LOGO = TRIS_ASSETS / "trismegistus-logo-transparent.png"
BEAT = TRIS / "NEWARCHITECTDBEATFORNEWTRIS.wav"
UI_HOME = UI_CAPTURE_DIR / "qwen_tris_ui_home_20260702.png"
UI_CHAT = UI_CAPTURE_DIR / "qwen_tris_ui_memory_lanes_chat_20260702.png"
UI_CHAT_FALLBACK = UI_CAPTURE_DIR / "qwen_tris_ui_running_chat_20260702.png"

KOKORO_MODEL = Path("/Volumes/Samsung SSD 990 2TB/Playground/STOIC.CORE/models/kokoro/kokoro-v1.0.int8.onnx")
KOKORO_VOICES = Path("/Volumes/Samsung SSD 990 2TB/Playground/STOIC.CORE/models/kokoro/voices-v1.0.bin")
VOICE_NAME = "bm_daniel"
VOICE_SPEED = 1.0
VOICE_GAIN = 10 ** (1.8 / 20.0)
MUSIC_GAIN = 0.15

OUT_BASE = "USE_THIS_QWEN_TRIS_MEMORYAGENT_COMMERCIAL_2026-07-02_v06_SSP_MEMORY_EXPLAINER"
OUT_VIDEO = OUT_DIR / f"{OUT_BASE}.mp4"
OUT_AUDIO = OUT_DIR / f"{OUT_BASE}_AUDIO_MIX.wav"
OUT_VOICE = OUT_DIR / f"{OUT_BASE}_VOICE.wav"
OUT_SCRIPT = OUT_DIR / f"{OUT_BASE}_SCRIPT.md"
OUT_CAPTION = OUT_DIR / f"{OUT_BASE}_CAPTION.md"
OUT_RECEIPT = OUT_DIR / f"{OUT_BASE}_RECEIPT.md"

W, H = 1920, 1080
BAND_TOP = 792
WHITE = (246, 247, 251)
MUTED = (183, 190, 207)
QWEN_BLUE = (40, 105, 255)
QWEN_CYAN = (74, 230, 255)
QWEN_PURPLE = (143, 87, 255)
GOLD = (245, 214, 95)
GREEN = (126, 226, 142)
PANEL = (4, 7, 15, 225)


@dataclass
class Scene:
    title: str
    subtitle: str
    narration: str
    kind: str
    min_duration: float = 7.0


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def font(size: int, bold: bool = False, mono: bool = False) -> ImageFont.FreeTypeFont:
    if mono:
        candidates = [
            "/System/Library/Fonts/SFNSMono.ttf",
            "/System/Library/Fonts/Menlo.ttc",
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
        p = Path(candidate)
        if p.exists():
            return ImageFont.truetype(str(p), size=size)
    return ImageFont.load_default()


F_TITLE = font(82, bold=True)
F_H1 = font(62, bold=True)
F_H2 = font(42, bold=True)
F_H3 = font(31, bold=True)
F_BODY = font(29)
F_SMALL = font(22)
F_TINY = font(18)
F_MONO = font(25, mono=True)
F_MONO_BIG = font(54, bold=True, mono=True)


def cover(img: Image.Image) -> Image.Image:
    img = img.convert("RGB")
    scale = max(W / img.width, H / img.height)
    resized = img.resize((int(img.width * scale), int(img.height * scale)), Image.Resampling.LANCZOS)
    left = (resized.width - W) // 2
    top = (resized.height - H) // 2
    return resized.crop((left, top, left + W, top + H))


def fit(img: Image.Image, max_w: int, max_h: int) -> Image.Image:
    img = img.convert("RGBA")
    scale = min(max_w / img.width, max_h / img.height)
    return img.resize((max(1, int(img.width * scale)), max(1, int(img.height * scale))), Image.Resampling.LANCZOS)


def trim_alpha(img: Image.Image) -> Image.Image:
    img = img.convert("RGBA")
    bbox = img.getbbox()
    return img.crop(bbox) if bbox else img


def base_bg() -> Image.Image:
    if BG.exists():
        img = cover(Image.open(BG))
    else:
        img = Image.new("RGB", (W, H), (0, 0, 0))
    img = ImageEnhance.Brightness(img).enhance(0.33)
    bg = img.convert("RGBA")
    bg = Image.alpha_composite(bg, Image.new("RGBA", (W, H), (1, 4, 15, 156)))
    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid)
    for x in range(0, W, 80):
        gd.line((x, 0, x, H), fill=(*QWEN_BLUE, 22), width=1)
    for y in range(0, H, 80):
        gd.line((0, y, W, y), fill=(*QWEN_CYAN, 13), width=1)
    for x in range(-200, W + 200, 160):
        gd.line((x, 0, x + 520, H), fill=(*QWEN_PURPLE, 10), width=1)
    return Image.alpha_composite(bg, grid)


def wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill=WHITE,
    max_width: int = 900,
    line_spacing: int = 8,
    center: bool = False,
) -> int:
    x, y = xy
    lines: list[str] = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        current = ""
        for word in words:
            test = f"{current} {word}".strip()
            if not current or draw.textlength(test, font=fnt) <= max_width:
                current = test
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)
        if not words:
            lines.append("")
    for line in lines:
        xx = x
        if center:
            bbox = draw.textbbox((0, 0), line, font=fnt)
            xx = x + (max_width - (bbox[2] - bbox[0])) // 2
        draw.text((xx, y), line, font=fnt, fill=fill)
        y += fnt.size + line_spacing
    return y


def panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int = 14, outline=QWEN_CYAN) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=PANEL, outline=outline, width=2)


def paste_shadow(canvas: Image.Image, img: Image.Image, xy: tuple[int, int], blur: int = 18, alpha: int = 125) -> None:
    x, y = xy
    rgba = img.convert("RGBA")
    mask = rgba.getchannel("A")
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    shadow.paste(Image.new("RGBA", rgba.size, (0, 0, 0, alpha)), (x + 10, y + 12), mask)
    canvas.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(blur)))
    canvas.alpha_composite(rgba, (x, y))


def header(draw: ImageDraw.ImageDraw) -> None:
    draw.rounded_rectangle((44, 36, 925, 94), radius=8, fill=(0, 0, 0, 230), outline=QWEN_CYAN, width=2)
    draw.text((66, 53), "RENAISSANCE FIELD LITE / QWEN TRIS", font=font(27, bold=True), fill=QWEN_CYAN)
    draw.rounded_rectangle((1448, 36, 1810, 94), radius=8, fill=(0, 0, 0, 230), outline=QWEN_PURPLE, width=2)
    draw.text((1470, 53), "MEMORYAGENT TRACK", font=font(27, bold=True), fill=QWEN_PURPLE)


def caption_band(img: Image.Image, text: str) -> None:
    if not text.strip():
        return
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, BAND_TOP, W, H), fill=(0, 0, 0, 255))
    draw.rectangle((0, BAND_TOP, W, BAND_TOP + 3), fill=QWEN_CYAN)
    draw.rectangle((0, H - 5, W, H), fill=QWEN_PURPLE)
    wrapped(draw, (170, BAND_TOP + 40), text, font(38, bold=True), WHITE, max_width=1580, line_spacing=10, center=True)


def draw_open(scene: Scene) -> Image.Image:
    img = base_bg()
    draw = ImageDraw.Draw(img)
    header(draw)
    if RFL_LOGO_SYSTEM.exists():
        logo = fit(Image.open(RFL_LOGO_SYSTEM), 660, 548)
        paste_shadow(img, logo, (115, 158), blur=24, alpha=150)
    if TRIS_LOGO.exists():
        mark = fit(trim_alpha(Image.open(TRIS_LOGO)), 610, 190)
        paste_shadow(img, mark, (1095, 250), blur=20, alpha=140)
    draw.text((1110, 504), "QWEN TRIS RECALL", font=F_H1, fill=WHITE)
    draw.text((1114, 578), "Memory AI Expert Partner", font=F_H2, fill=QWEN_CYAN)
    wrapped(draw, (1118, 638), "Trismegistus carried into Qwen Cloud: same spine, new memory track.", F_BODY, MUTED, max_width=650)
    caption_band(img, scene.narration)
    return img


def draw_bridge(scene: Scene) -> Image.Image:
    img = base_bg()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((86, 118), scene.title, font=F_H1, fill=WHITE)
    wrapped(draw, (92, 198), scene.subtitle, F_BODY, MUTED, max_width=1080)
    cards = [
        ("TRIS", "Hermes / Nemo route", QWEN_PURPLE),
        ("SPINE", "SQLite + JSONL + RAG", QWEN_CYAN),
        ("SSP", "Stable-State Path", GOLD),
        ("QWEN", "Cloud MemoryAgent", QWEN_BLUE),
        ("RECEIPT", "500-turn run", GREEN),
    ]
    for i, (head, sub, color) in enumerate(cards):
        x = 112 + i * 345
        y = 405
        panel(draw, (x, y, x + 282, y + 160), radius=16, outline=color)
        draw.text((x + 28, y + 26), head, font=F_H3, fill=color)
        wrapped(draw, (x + 28, y + 76), sub, F_SMALL, MUTED, max_width=225)
        if i < len(cards) - 1:
            draw.line((x + 290, y + 80, x + 330, y + 80), fill=QWEN_CYAN, width=4)
            draw.polygon([(x + 330, y + 80), (x + 314, y + 69), (x + 314, y + 91)], fill=QWEN_CYAN)
    caption_band(img, scene.narration)
    return img


def draw_stack(scene: Scene) -> Image.Image:
    img = base_bg()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((86, 116), scene.title, font=F_H1, fill=WHITE)
    wrapped(draw, (92, 194), scene.subtitle, F_BODY, MUTED, max_width=900)
    rows = [
        ("FRONTEND", "static Qwen Tris Recall UI"),
        ("BACKEND", "Python API + provider abstraction"),
        ("MODEL", "Qwen Cloud / qwen-plus"),
        ("MEMORY", "SQLite store + JSONL audit"),
        ("RAG", "SQLite FTS + LangChain when available"),
        ("FALLBACK", "local Qwen / Ollama route for dry runs"),
    ]
    for i, (head, body) in enumerate(rows):
        col = i % 2
        row = i // 2
        x = 116 + col * 840
        y = 302 + row * 138
        panel(draw, (x, y, x + 748, y + 104), radius=12, outline=QWEN_CYAN if i < 4 else QWEN_PURPLE)
        draw.text((x + 28, y + 18), head, font=F_H3, fill=QWEN_CYAN)
        wrapped(draw, (x + 28, y + 58), body, F_SMALL, MUTED, max_width=680)
    caption_band(img, scene.narration)
    return img


def draw_conditions(scene: Scene) -> Image.Image:
    img = base_bg()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((86, 116), scene.title, font=F_H1, fill=WHITE)
    wrapped(draw, (92, 194), scene.subtitle, F_BODY, MUTED, max_width=1040)
    cards = [
        ("A", "BASELINE QWEN", "prompt-only answer discipline", MUTED),
        ("B", "QWEN TRIS", "Mirror Architecture memory / RAG / SSP", QWEN_CYAN),
        ("C", "TUNED SSP", "gated until real adapter or internal-layer receipt", GOLD),
    ]
    for i, (tag, head, body, color) in enumerate(cards):
        x = 120 + i * 580
        y = 378
        panel(draw, (x, y, x + 495, y + 180), radius=16, outline=color)
        draw.text((x + 30, y + 30), tag, font=F_MONO_BIG, fill=color)
        draw.text((x + 112, y + 38), head, font=F_H3, fill=WHITE)
        wrapped(draw, (x + 112, y + 88), body, F_SMALL, MUTED, max_width=330)
    caption_band(img, scene.narration)
    return img


def draw_500(scene: Scene) -> Image.Image:
    img = base_bg()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((86, 116), scene.title, font=F_H1, fill=WHITE)
    wrapped(draw, (92, 194), scene.subtitle, F_BODY, MUTED, max_width=1050)
    metrics = [
        ("500 / 500", "hosted Qwen Cloud turns"),
        ("2168 / 2168", "checks passed"),
        ("0", "prompt spills"),
        ("0", "raw receipt spills"),
    ]
    for i, (big, label) in enumerate(metrics):
        x = 124 + (i % 2) * 840
        y = 330 + (i // 2) * 155
        panel(draw, (x, y, x + 748, y + 118), radius=16, outline=GREEN if i == 0 else QWEN_CYAN)
        draw.text((x + 32, y + 16), big, font=font(48, bold=True, mono=True), fill=GREEN if i == 0 else QWEN_CYAN)
        wrapped(draw, (x + 36, y + 76), label, F_SMALL, WHITE, max_width=660)
    caption_band(img, scene.narration)
    return img


def draw_bench(scene: Scene) -> Image.Image:
    img = base_bg()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((86, 116), scene.title, font=F_H1, fill=WHITE)
    wrapped(draw, (92, 194), scene.subtitle, F_BODY, MUTED, max_width=980)
    cards = [
        ("LongBench-E", "offset 0", "+0.092", "299 scored / 1 skipped"),
        ("LongBench-E", "held-out offset 50", "+0.110", "299 scored / 1 skipped"),
        ("Qasper", "lm-eval full", "+0.00135", "224 / 224"),
        ("Qasper", "lm-eval 100", "+0.0179", "matched slice"),
    ]
    for i, (head, sub, delta, foot) in enumerate(cards):
        x = 112 + (i % 2) * 850
        y = 320 + (i // 2) * 152
        panel(draw, (x, y, x + 760, y + 118), radius=14, outline=QWEN_CYAN if i < 2 else QWEN_PURPLE)
        draw.text((x + 28, y + 18), head, font=F_H3, fill=QWEN_CYAN)
        draw.text((x + 282, y + 18), sub, font=F_SMALL, fill=MUTED)
        draw.text((x + 28, y + 54), delta, font=font(44, bold=True, mono=True), fill=GREEN)
        wrapped(draw, (x + 242, y + 62), foot, F_SMALL, WHITE, max_width=455)
    caption_band(img, scene.narration)
    return img


def draw_lanes(scene: Scene) -> Image.Image:
    img = base_bg()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((86, 116), scene.title, font=F_H1, fill=WHITE)
    lanes = [
        "C5B / 500 SSP memory",
        "Mirror Architecture source pack",
        "SWE code memory",
        "WebArena browser memory",
        "Long-session coherence",
        "External work receipts",
    ]
    for i, lane in enumerate(lanes):
        x = 112 + (i % 2) * 850
        y = 232 + (i // 2) * 138
        panel(draw, (x, y, x + 760, y + 100), radius=12, outline=QWEN_CYAN)
        draw.text((x + 28, y + 24), f"{i + 1}", font=F_MONO_BIG, fill=QWEN_PURPLE)
        wrapped(draw, (x + 112, y + 28), lane, F_H3, WHITE, max_width=610)
    caption_band(img, scene.narration)
    return img


def draw_cloud(scene: Scene) -> Image.Image:
    img = base_bg()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((86, 116), scene.title, font=F_H1, fill=WHITE)
    wrapped(draw, (92, 194), scene.subtitle, F_BODY, MUTED, max_width=1000)
    lines = [
        ("API proof file", "src/qwen_agent_buildout/trini_recall/alibaba_qwen_cloud_client.py"),
        ("Endpoint", "dashscope-intl.aliyuncs.com/compatible-mode/v1"),
        ("Model route", "qwen-plus, hosted Qwen Cloud"),
        ("Deploy gate", "record backend running on Alibaba Cloud"),
    ]
    for i, (head, body) in enumerate(lines):
        y = 328 + i * 100
        panel(draw, (128, y, 1788, y + 72), radius=12, outline=QWEN_CYAN if i < 3 else GOLD)
        draw.text((154, y + 20), head, font=F_H3, fill=QWEN_CYAN if i < 3 else GOLD)
        draw.text((530, y + 22), body, font=F_MONO, fill=WHITE)
    caption_band(img, scene.narration)
    return img


def draw_ui(scene: Scene) -> Image.Image:
    img = base_bg()
    draw = ImageDraw.Draw(img)
    header(draw)
    draw.text((86, 116), scene.title, font=F_H1, fill=WHITE)
    wrapped(draw, (92, 194), scene.subtitle, F_BODY, MUTED, max_width=1060)

    shot_path = UI_CHAT if scene.kind == "ui_chat" and UI_CHAT.exists() else None
    if shot_path is None and scene.kind == "ui_chat" and UI_CHAT_FALLBACK.exists():
        shot_path = UI_CHAT_FALLBACK
    if shot_path is None and UI_HOME.exists():
        shot_path = UI_HOME

    if shot_path and shot_path.exists():
        shot = Image.open(shot_path).convert("RGBA")
        if shot.height > 900:
            shot = shot.crop((0, 0, shot.width, 900))
        shot = fit(shot, 1420, 500)
        x = (W - shot.width) // 2
        y = 278
        draw.rounded_rectangle((x - 16, y - 16, x + shot.width + 16, y + shot.height + 16), radius=16, fill=(0, 0, 0, 235), outline=QWEN_CYAN, width=2)
        paste_shadow(img, shot, (x, y), blur=12, alpha=100)
        draw.text((x, y + shot.height + 28), f"capture: {shot_path.name}", font=F_TINY, fill=MUTED)
    else:
        panel(draw, (180, 300, 1740, 690), radius=16, outline=QWEN_CYAN)
        wrapped(draw, (260, 432), "Live UI capture missing. Render kept this gate explicit.", F_H2, WHITE, max_width=1380, center=True)

    caption_band(img, scene.narration)
    return img


def draw_close(scene: Scene) -> Image.Image:
    img = base_bg()
    draw = ImageDraw.Draw(img)
    header(draw)
    if TRIS_LOGO.exists():
        mark = fit(trim_alpha(Image.open(TRIS_LOGO)), 590, 190)
        paste_shadow(img, mark, ((W - mark.width) // 2, 164), blur=24, alpha=145)
    draw.text((W // 2, 438), "QWEN TRIS RECALL", font=F_TITLE, fill=WHITE, anchor="mm")
    draw.text((W // 2, 522), "Memory AI Expert Partner", font=F_H2, fill=QWEN_CYAN, anchor="mm")
    wrapped(draw, (388, 598), scene.subtitle, F_BODY, MUTED, max_width=1140, center=True)
    caption_band(img, scene.narration)
    return img


SCENES = [
    Scene(
        "Qwen Tris Recall",
        "Memory AI Expert Partner.",
        "Qwen Tris Recall is the next version of Trismegistus: the same Renaissance Field Lite spine, rebuilt around Qwen Cloud memory.",
        "open",
        8.2,
    ),
    Scene(
        "From Tris to Qwen Tris.",
        "The Hermes contest build gave us the operator. This version asks how far memory can carry it.",
        "The Hermes build gave us the operator: chat, source checks, outreach, coding work, Stripe gates, and saved receipts. Qwen Tris keeps that shape and asks one question: can memory make it better?",
        "bridge",
        11.5,
    ),
    Scene(
        "The stack is running.",
        "Frontend, backend, cloud model, memory store, audit trail, and fallback route.",
        "This is the running app: a local Qwen Tris UI, Python backend, SQLite memory, JSONL audit log, LangChain RAG, Qwen Cloud path, and local Qwen fallback for dry runs.",
        "stack",
        11.2,
    ),
    Scene(
        "Live local surface.",
        "Captured from the Qwen Tris app running on this machine.",
        "Here is the app running locally: chat, memory, model status, voice controls, and source fetch on one surface.",
        "ui_home",
        8.8,
    ),
    Scene(
        "Live memory chat.",
        "Local Qwen route, saved chat state, and visible next gate.",
        "This screenshot shows the live chat path: Qwen local online, LangChain RAG online, memory stored, and the next Qwen Cloud gate still visible.",
        "ui_chat",
        9.2,
    ),
    Scene(
        "Three-condition test.",
        "Baseline, architecture-on, and the future tuned SSP lane.",
        "We test it simply. First, plain Qwen. Second, Qwen with Mirror Architecture memory and SSP. Third, the tuned lane stays gated until a real adapter receipt exists.",
        "conditions",
        12.4,
    ),
    Scene(
        "SSP is the memory stabilizer.",
        "Stable-State Path keeps the job, evidence, memory, route, and next gate lined up.",
        "SSP means Stable-State Path. It is the reason the memory gets stronger: Qwen Tris is not just holding more text. It keeps the right state of the work, so recall stays tied to the mission instead of drifting with the last prompt.",
        "bridge",
        14.0,
    ),
    Scene(
        "Five hundred turns.",
        "Hosted Qwen Cloud memory run, no public-safe receipt spill.",
        "The hosted Qwen run completed five hundred memory turns. Across the checks, it kept the target memories clean and did not spill private prompts or raw receipts.",
        "500",
        12.0,
    ),
    Scene(
        "Six memory lanes.",
        "Not toy recall. Collapse-prone working memory across real project lanes.",
        "The memory work is not trivia recall. It tracks project memory across C5B, Mirror Architecture sources, SWE code work, browser tasks, long sessions, and real external work receipts.",
        "lanes",
        10.4,
    ),
    Scene(
        "Public benchmark receipts.",
        "LongBench-E and Qasper show architecture-on gains over the baseline route.",
        "Then we checked it against public benchmark-style slices. LongBench-E improved over baseline on two windows, and Qasper stayed net positive under the same scoring path.",
        "bench",
        13.2,
    ),
    Scene(
        "Why this matters.",
        "The claim is not leaderboard theater. It is model-agnostic memory discipline.",
        "The point is not one lucky prompt. The point is that the same method moved from Hermes and Nemo into Qwen, and the receipts still improved against the baseline.",
        "bridge",
        11.6,
    ),
    Scene(
        "Alibaba Cloud proof lane.",
        "The code path is ready. The deployment recording is the next required gate.",
        "The Qwen API client is in the repo. The next hard gate is the Alibaba Cloud recording: backend live on Alibaba, calling Qwen Cloud, without exposing secrets.",
        "cloud",
        12.0,
    ),
    Scene(
        "Public-safe package.",
        "Repo, license, run instructions, architecture diagram, and receipt index.",
        "The repo package has the license, source, run steps, Docker path, architecture diagram, deployment runbook, benchmark receipts, and submission checklist.",
        "stack",
        10.6,
    ),
    Scene(
        "The product arc.",
        "Tris is not just chat. Qwen Tris is continuity infrastructure for an AI expert partner.",
        "This is the product direction: an AI expert partner that remembers the work, checks evidence, keeps receipts, and turns each gap into the next step.",
        "conditions",
        11.0,
    ),
    Scene(
        "Qwen Tris Recall.",
        "Renaissance Field Lite is carrying Trismegistus into Qwen Cloud: memory first, receipts always, model agnostic.",
        "Qwen Tris is the Qwen version of Trismegistus. It remembers the work, checks the receipts, and carries the build forward.",
        "close",
        10.0,
    ),
]


def render_scene(scene: Scene) -> Image.Image:
    return {
        "open": draw_open,
        "bridge": draw_bridge,
        "stack": draw_stack,
        "conditions": draw_conditions,
        "500": draw_500,
        "lanes": draw_lanes,
        "bench": draw_bench,
        "cloud": draw_cloud,
        "ui_home": draw_ui,
        "ui_chat": draw_ui,
        "close": draw_close,
    }[scene.kind](scene)


def synth_voice() -> tuple[np.ndarray, int, list[float]]:
    if not KOKORO_MODEL.exists() or not KOKORO_VOICES.exists():
        raise SystemExit("Kokoro model/voice files missing")
    pipeline = Kokoro(str(KOKORO_MODEL), str(KOKORO_VOICES))
    if VOICE_NAME not in pipeline.get_voices():
        raise SystemExit(f"Missing Kokoro voice {VOICE_NAME}")

    parts: list[np.ndarray] = []
    durations: list[float] = []
    sr_out = 24000
    for idx, scene in enumerate(SCENES, 1):
        audio, sr = pipeline.create(scene.narration, voice=VOICE_NAME, speed=VOICE_SPEED)
        sr_out = int(sr)
        audio = audio.astype(np.float32).reshape(-1) * VOICE_GAIN
        audio = np.clip(audio, -0.94, 0.94)
        spoken = len(audio) / sr_out
        duration = max(scene.min_duration, spoken + 0.8)
        lead = np.zeros(int(0.14 * sr_out), dtype=np.float32)
        tail = np.zeros(max(0, int(round((duration - spoken) * sr_out))), dtype=np.float32)
        parts.append(np.concatenate([lead, audio, tail]))
        durations.append(duration + 0.14)
        sf.write(str(WORK / f"voice_scene_{idx:02d}.wav"), audio, sr_out)
    return np.concatenate(parts), sr_out, durations


def make_music(duration: float, sample_rate: int) -> np.ndarray:
    music_path = WORK / "music_bed_processed.wav"
    run([
        "ffmpeg",
        "-y",
        "-stream_loop",
        "-1",
        "-i",
        str(BEAT),
        "-t",
        f"{duration:.3f}",
        "-ac",
        "1",
        "-ar",
        str(sample_rate),
        "-af",
        f"volume={MUSIC_GAIN}",
        str(music_path),
    ])
    music, _ = sf.read(str(music_path), always_2d=False)
    return music.astype(np.float32)


def mix_audio() -> tuple[float, int, list[float]]:
    voice, sr, durations = synth_voice()
    total = len(voice) / sr
    music = make_music(total, sr)
    if len(music) < len(voice):
        music = np.pad(music, (0, len(voice) - len(music)))
    music = music[: len(voice)]
    mix = voice + music
    peak = float(np.max(np.abs(mix))) or 1.0
    if peak > 0.98:
        mix = mix / peak * 0.98
    sf.write(str(OUT_VOICE), voice, sr)
    sf.write(str(OUT_AUDIO), mix, sr)
    (WORK / "durations.txt").write_text("\n".join(f"{d:.3f}" for d in durations) + "\n", encoding="utf-8")
    return total, sr, durations


def render_video(total_duration: float, durations: list[float]) -> None:
    concat = WORK / "slides.concat.txt"
    lines: list[str] = []
    slide_paths: list[Path] = []
    for idx, (scene, duration) in enumerate(zip(SCENES, durations), 1):
        slide = render_scene(scene)
        path = WORK / f"slide_{idx:02d}.png"
        slide.save(path)
        slide_paths.append(path)
        lines.append(f"file '{path}'")
        lines.append(f"duration {duration:.3f}")
    lines.append(f"file '{slide_paths[-1]}'")
    concat.write_text("\n".join(lines) + "\n", encoding="utf-8")

    silent = WORK / "silent_video.mp4"
    run([
        "ffmpeg",
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(concat),
        "-vf",
        "fps=30,format=yuv420p",
        "-c:v",
        "libx264",
        "-crf",
        "18",
        str(silent),
    ])
    run([
        "ffmpeg",
        "-y",
        "-i",
        str(silent),
        "-i",
        str(OUT_AUDIO),
        "-shortest",
        "-t",
        f"{total_duration:.3f}",
        "-c:v",
        "libx264",
        "-crf",
        "18",
        "-preset",
        "medium",
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        str(OUT_VIDEO),
    ])


def write_docs(duration: float, sample_rate: int) -> None:
    transcript = "# Qwen Tris MemoryAgent Commercial Script\n\n"
    for idx, scene in enumerate(SCENES, 1):
        transcript += f"## Scene {idx}: {scene.title}\n\n"
        transcript += f"**Subtitle:** {scene.subtitle}\n\n"
        transcript += f"{scene.narration}\n\n"
    OUT_SCRIPT.write_text(transcript, encoding="utf-8")

    caption = textwrap.dedent(
        f"""\
        # Qwen Tris MemoryAgent Commercial Caption

        Qwen Tris Recall is the Qwen Cloud memory build of the RFL Trismegistus stack.

        The commercial shows the bridge from Tris into Qwen Tris: the Hermes/Nemo-era operator spine, SQLite memory, JSONL audit receipts, RAG retrieval, Mirror Architecture / SSP, hosted Qwen Cloud route, live UI screenshots, and public benchmark receipts.

        Public-safe receipts highlighted:
        - Hosted Qwen Cloud 500-turn run: 500/500 turns, 2168/2168 checks, zero prompt spills, zero raw receipt spills.
        - LongBench-E offset 0: +0.092 architecture-on delta across 299 scored rows.
        - Held-out LongBench-E offset 50: +0.110 architecture-on delta across 299 scored rows.
        - Qasper EleutherAI lm-eval: full 224-row net positive, matched 100-row +0.0179.

        Track: Qwen Cloud MemoryAgent.

        Boundary: this is not an official leaderboard claim. It is a public-safe demo and receipt package showing baseline Qwen versus Qwen Tris architecture-on memory discipline. Alibaba Cloud backend deployment recording remains the next submission gate.
        """
    )
    OUT_CAPTION.write_text(caption, encoding="utf-8")

    receipt = textwrap.dedent(
        f"""\
        # Qwen Tris MemoryAgent Commercial Receipt

        Created: 2026-07-02

        Video:
        `{OUT_VIDEO}`

        Audio mix:
        `{OUT_AUDIO}`

        Voice:
        `{OUT_VOICE}`

        Music bed:
        `{BEAT}`

        Music treatment:
        - user-made Qwen Tris beat source
        - no added EQ
        - volume {MUSIC_GAIN}

        Voice:
        - Kokoro `{VOICE_NAME}`
        - speed {VOICE_SPEED}
        - pitch unmodified

        Duration:
        - {duration:.2f} seconds

        Sample rate:
        - {sample_rate}

        Evidence referenced:
        - `docs/QWEN_TRIS_PUBLIC_SUBMISSION_PACKET_2026-07-01.md`
        - `docs/ARCHITECTURE.md`
        - `docs/SUBMISSION_CHECKLIST_QWEN.md`
        - `data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T054449Z.md`
        - `data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T195427Z.md`
        - `data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T214036Z.md`
        - `data/third_party_eval_runs/QWEN_TRIS_LM_EVAL_QASPER_RECEIPT_20260701T180343Z.md`

        Public boundary:
        - MemoryAgent commercial/demo asset.
        - No official leaderboard claim.
        - No private prompts, keys, raw private memory, or proprietary internals included.
        - Alibaba Cloud backend deployment recording is still the next required gate.
        """
    )
    OUT_RECEIPT.write_text(receipt, encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if WORK.exists():
        shutil.rmtree(WORK)
    WORK.mkdir(parents=True, exist_ok=True)
    total, sr, durations = mix_audio()
    render_video(total, durations)
    write_docs(total, sr)
    print(OUT_VIDEO)
    print(OUT_RECEIPT)


if __name__ == "__main__":
    main()
