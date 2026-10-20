"""Generate the Mazze docs visual system (SVG) in the mazzescan.io style.

Usage: python3 tools/gen_brand_assets.py .gitbook/assets/brand

Covers and cards are also published as 2x PNGs, rendered from the SVGs with
headless Chrome (--force-device-scale-factor=2).
"""
import os
import random
import sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

SANS = "Inter, 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'SF Mono', Menlo, Consolas, monospace"

THEMES = {
    "light": dict(bg="#fafaf9", surface="#ffffff", surface2="#f4f4f1", hair="#e8e8e6",
                  ink="#0a0a0a", ink2="#1f1f1f", muted="#737373", muted2="#a3a3a3",
                  native="#ff6600", native_soft="#fff0e6", evm="#6c24e0", evm_soft="#f0e9fd",
                  shield="#0a0a0a", shield_soft="#ededeb", on_shield="#ffffff", ok="#16a34a"),
    "dark": dict(bg="#0c0c0c", surface="#141414", surface2="#1a1a1a", hair="#2a2a2a",
                 ink="#f5f5f4", ink2="#e7e5e4", muted="#a3a3a3", muted2="#737373",
                 native="#ff7a26", native_soft="#2a1608", evm="#9b6bff", evm_soft="#1d1430",
                 shield="#f5f5f4", shield_soft="#262626", on_shield="#0a0a0a", ok="#22c55e"),
}


def svg(w, h, body, t):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" font-family="{SANS}">'
            f'<rect width="{w}" height="{h}" fill="{t["bg"]}"/>{body}</svg>\n')


def write(name, content):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)


def text(x, y, s, size, fill, weight=400, mono=False, anchor="start", ls=None, opacity=None):
    fam = f' font-family="{MONO}"' if mono else ""
    extra = f' letter-spacing="{ls}"' if ls is not None else ""
    op = f' opacity="{opacity}"' if opacity is not None else ""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}"'
            f' text-anchor="{anchor}"{fam}{extra}{op}>{s}</text>')


def chip(x, y, label, bg, fg, size=13):
    w = int(len(label) * size * 0.66 + 18)
    h = int(size * 1.75)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{bg}"/>'
            + text(x + 9, y + h * 0.69, label, size, fg, 500, mono=True, ls="0.06em")), w


def grid(w, h, t, step=40, opacity=0.6):
    lines = []
    for x in range(0, w + 1, step):
        lines.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}"/>')
    for y in range(0, h + 1, step):
        lines.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}"/>')
    return f'<g stroke="{t["hair"]}" stroke-width="1" opacity="{opacity}">{"".join(lines)}</g>'


def hatch_def(t, pid="hatch"):
    return (f'<defs><pattern id="{pid}" width="6" height="6" patternUnits="userSpaceOnUse" '
            f'patternTransform="rotate(45)"><rect width="6" height="6" fill="{t["shield_soft"]}"/>'
            f'<line x1="0" y1="0" x2="0" y2="6" stroke="{t["shield"]}" stroke-width="2"/></pattern></defs>')


def dag(t, x0, y0, cols, col_w, row_h, seed, size=26, label=True):
    """Epoch columns: one pivot (ink) per epoch plus uncles; parent + referee edges."""
    rnd = random.Random(seed)
    kinds = ["native", "native", "evm", "plain", "plain", "shield"]
    epochs = []
    for c in range(cols):
        n = rnd.choice([1, 2, 2, 3, 3, 4])
        pivot = rnd.randrange(n)
        blocks = []
        for r in range(n):
            bx = x0 + c * col_w
            by = y0 + r * row_h + (rnd.random() - 0.5) * 6
            blocks.append((bx, by, r == pivot, rnd.choice(kinds)))
        epochs.append(blocks)
    edges, nodes = [], []
    for c in range(1, cols):
        piv_prev = next(b for b in epochs[c - 1] if b[2])
        for b in epochs[c]:
            if b[2]:
                edges.append(f'<line x1="{piv_prev[0]+size}" y1="{piv_prev[1]+size/2}" x2="{b[0]}" '
                             f'y2="{b[1]+size/2}" stroke="{t["ink"]}" stroke-width="1.6"/>')
            else:
                edges.append(f'<line x1="{piv_prev[0]+size}" y1="{piv_prev[1]+size/2}" x2="{b[0]}" '
                             f'y2="{b[1]+size/2}" stroke="{t["muted2"]}" stroke-width="1"/>')
            for u in epochs[c - 1]:
                if not u[2] and rnd.random() < 0.7:
                    edges.append(f'<line x1="{u[0]+size}" y1="{u[1]+size/2}" x2="{b[0]}" y2="{b[1]+size/2}" '
                                 f'stroke="{t["muted2"]}" stroke-width="1" stroke-dasharray="3 4"/>')
    for blocks in epochs:
        for bx, by, piv, kind in blocks:
            if piv:
                nodes.append(f'<rect x="{bx}" y="{by}" width="{size}" height="{size}" rx="4" fill="{t["ink"]}"/>')
                dot = {"native": t["native"], "evm": t["evm"]}.get(kind)
                if dot:
                    nodes.append(f'<circle cx="{bx+size/2}" cy="{by+size/2}" r="{size*0.16}" fill="{dot}"/>')
            else:
                fill = {"native": t["native_soft"], "evm": t["evm_soft"], "shield": "url(#hatch)"}.get(kind, t["surface"])
                stroke = {"native": t["native"], "evm": t["evm"], "shield": t["shield"]}.get(kind, t["muted2"])
                nodes.append(f'<rect x="{bx}" y="{by}" width="{size}" height="{size}" rx="4" fill="{fill}" '
                             f'stroke="{stroke}" stroke-width="1.3"/>')
    lab = []
    if label:
        for c in range(cols):
            lab.append(text(x0 + c * col_w + size / 2, y0 - 16, f"E{c+1:02d}", 11, t["muted"], mono=True, anchor="middle"))
    return "".join(edges) + "".join(nodes) + "".join(lab)


# ---------------------------------------------------------------- home cover
def home_cover(mode):
    t = THEMES[mode]
    w, h = 1990, 480
    b = hatch_def(t) + grid(w, h, t, 48, 0.55)
    b += f'<rect x="0" y="{h-4}" width="{w/3:.0f}" height="4" fill="{t["native"]}"/>'
    b += f'<rect x="{w/3:.0f}" y="{h-4}" width="{w/3:.0f}" height="4" fill="{t["evm"]}"/>'
    b += f'<rect x="{2*w/3:.0f}" y="{h-4}" width="{w/3+1:.0f}" height="4" fill="{t["shield"]}"/>'
    x = 120
    c1, w1 = chip(x, 120, "NATIVE", t["native"], "#ffffff", 14)
    c2, w2 = chip(x + w1 + 10, 120, "ESPACE · EVM", t["evm"], "#ffffff", 14)
    c3, _ = chip(x + w1 + w2 + 20, 120, "SHIELDED", t["shield"], t["on_shield"], 14)
    b += c1 + c2 + c3
    b += text(x, 250, "Mazze", 112, t["ink"], 700, ls="-0.03em")
    b += text(x, 308, "Fast. Secure. Private.", 36, t["muted"], 400, ls="-0.01em")
    b += text(x, 372, "PoW · RandomX · DAG/DETS · post-quantum shielded space", 18, t["muted"], 400, mono=True)
    panel_x, panel_y, pw, ph = 1060, 70, 810, 340
    b += (f'<rect x="{panel_x}" y="{panel_y}" width="{pw}" height="{ph}" rx="8" fill="{t["surface"]}" '
          f'stroke="{t["hair"]}"/>'
          f'<line x1="{panel_x}" y1="{panel_y+48}" x2="{panel_x+pw}" y2="{panel_y+48}" stroke="{t["hair"]}"/>')
    b += text(panel_x + 22, panel_y + 30, "Live DAG", 16, t["ink"], 600)
    b += text(panel_x + 104, panel_y + 30, "last 7 epochs", 13, t["muted"], mono=True)
    b += f'<circle cx="{panel_x+pw-90}" cy="{panel_y+25}" r="5" fill="{t["ok"]}"/>'
    b += text(panel_x + pw - 78, panel_y + 30, "synced", 13, t["muted"], mono=True)
    b += dag(t, panel_x + 60, panel_y + 112, 7, 110, 52, seed=7, size=28)
    return svg(w, h, b, t)


# ---------------------------------------------------------------- card covers
def card(num, title, sub, motif, accent, mode="light"):
    t = THEMES[mode]
    w, h = 640, 360
    acc = t[accent] if accent in t else accent
    b = hatch_def(t) + grid(w, h, t, 32, 0.5)
    b += f'<rect x="0" y="0" width="{w}" height="4" fill="{acc}"/>'
    b += text(36, 58, f"{sub}", 14, t["muted"], 500, mono=True, ls="0.08em")
    b += text(36, 112, title, 44, t["ink"], 700, ls="-0.02em")
    b += motif(t)
    return svg(w, h, b, t)


def m_overview(t):
    return dag(t, 60, 200, 6, 96, 40, seed=3, size=22, label=False)


def m_spaces(t):
    out = ""
    specs = [("NATIVE", t["native"], t["native_soft"], "#fff"), ("ESPACE", t["evm"], t["evm_soft"], "#fff"),
             ("SHIELDED", t["shield"], "url(#hatch)", t["on_shield"])]
    for i, (lab, col, soft, fg) in enumerate(specs):
        x = 36 + i * 194
        out += f'<rect x="{x}" y="170" width="178" height="150" rx="6" fill="{t["surface"]}" stroke="{t["hair"]}"/>'
        c, _ = chip(x + 14, 186, lab, col, fg, 12)
        out += c
        out += f'<rect x="{x+14}" y="236" width="150" height="66" rx="4" fill="{soft}" stroke="{col}" stroke-opacity="0.35"/>'
        if i < 2:
            out += text(x + 89, 275, ["mazze:aak2…", "0x5aF3…9c1"][i], 14, col, 500, mono=True, anchor="middle")
    return out


def m_architecture(t):
    out = ""
    layers = ["RPC · jsonrpsee", "Consensus · DETS", "Execution · revm 40", "Storage · MDBX / ParityDB"]
    for i, lab in enumerate(layers):
        y = 160 + i * 44
        out += f'<rect x="{36+i*14}" y="{y}" width="{560-i*28}" height="36" rx="5" fill="{t["surface"]}" stroke="{t["hair"]}"/>'
        out += f'<rect x="{36+i*14}" y="{y}" width="5" height="36" rx="2" fill="{t["ink"] if i % 2 else t["native"]}"/>'
        out += text(56 + i * 14, y + 23, lab, 14, t["ink2"], 500, mono=True)
    return out


def m_privacy(t):
    out = ""
    rows = [(160, [1, 1, 0, 1, 1, 1, 0, 1]), (206, [0, 1, 1, 1, 0, 1, 1, 1]), (252, [1, 1, 1, 0, 1, 1, 1, 0])]
    for y, pat in rows:
        for i, on in enumerate(pat):
            x = 36 + i * 72
            if on:
                out += f'<rect x="{x}" y="{y}" width="62" height="32" rx="4" fill="url(#hatch)" stroke="{t["shield"]}"/>'
            else:
                out += f'<rect x="{x}" y="{y}" width="62" height="32" rx="4" fill="{t["surface"]}" stroke="{t["hair"]}"/>'
                out += text(x + 31, y + 21, "nf", 13, t["muted"], mono=True, anchor="middle")
    out += text(36, 322, "STARK · Poseidon2 · KoalaBear · 128-bit", 14, t["muted"], mono=True)
    return out


def m_tokenomics(t):
    out = ""
    vals = [0.9, 0.62, 0.48, 0.38, 0.31, 0.27, 0.24, 0.22, 0.21, 0.2]
    for i, v in enumerate(vals):
        bh = 150 * v
        out += f'<rect x="{36+i*56}" y="{320-bh}" width="40" height="{bh}" rx="3" fill="{t["native"] if i == 0 else t["ink"]}" opacity="{1 if i == 0 else 0.85}"/>'
    out += f'<line x1="36" y1="321" x2="604" y2="321" stroke="{t["hair"]}"/>'
    return out


def m_developers(t):
    out = f'<rect x="36" y="150" width="568" height="176" rx="6" fill="{t["surface"]}" stroke="{t["hair"]}"/>'
    lines = [("$", " cast chain-id --rpc-url $ESPACE", t["muted"]),
             ("", "eth_call → revm 40 · Prague", t["evm"]),
             ("", "mazze_call → native interpreter", t["native"]),
             ("", "34036 / 34036 state tests ✓", t["ok"])]
    for i, (p, s, col) in enumerate(lines):
        out += text(58, 188 + i * 36, (p + s) if p else "  " + s, 16, col if i else t["ink2"], 500 if i else 400, mono=True)
    return out


def m_node(t):
    out = f'<rect x="36" y="150" width="568" height="176" rx="6" fill="{t["ink"]}"/>'
    lines = ["$ docker compose up -d", "$ ./run/mazze-cli.sh summary",
             "  epoch 182 340 · peers 12 · synced", "  miner: stratum · RandomX"]
    for i, s in enumerate(lines):
        col = t["bg"] if i < 2 else t["muted2"]
        out += text(58, 190 + i * 36, s, 16, col, 500 if i < 2 else 400, mono=True)
    out += f'<circle cx="580" cy="172" r="5" fill="{t["ok"]}"/>'
    return out


def m_knowledge(t):
    out = ""
    terms = [("Epoch", "pivot block + its past"), ("Nullifier", "spent-note marker"), ("Anchor", "a recorded tree root")]
    for i, (k, v) in enumerate(terms):
        y = 160 + i * 54
        out += f'<rect x="36" y="{y}" width="568" height="44" rx="5" fill="{t["surface"]}" stroke="{t["hair"]}"/>'
        out += text(56, y + 28, k, 16, t["ink"], 600)
        out += text(200, y + 28, v, 15, t["muted"], mono=True)
    return out


def m_community(t):
    rnd = random.Random(11)
    pts = [(60 + rnd.random() * 520, 170 + rnd.random() * 150) for _ in range(22)]
    out = ""
    for i, (x, y) in enumerate(pts):
        for (x2, y2) in pts[i + 1:i + 3]:
            out += f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{t["muted2"]}" stroke-width="1"/>'
    for i, (x, y) in enumerate(pts):
        col = [t["native"], t["evm"], t["ink"]][i % 3]
        out += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{5 if i % 4 else 8}" fill="{col}"/>'
    return out


def m_roadmap(t):
    out = f'<line x1="56" y1="250" x2="584" y2="250" stroke="{t["hair"]}" stroke-width="2"/>'
    out += f'<line x1="56" y1="250" x2="352" y2="250" stroke="{t["ink"]}" stroke-width="2"/>'
    for i, lab in enumerate(["A", "B", "C", "D"]):
        x = 56 + i * 176
        done = i < 2
        out += f'<circle cx="{x}" cy="250" r="12" fill="{t["ink"] if done else t["surface"]}" stroke="{t["ink"]}" stroke-width="2"/>'
        out += text(x, 292, f"PHASE {lab}", 13, t["ink"] if done else t["muted"], 500, mono=True, anchor="middle")
    out += f'<circle cx="352" cy="250" r="6" fill="{t["native"]}"/>'
    return out


CARDS = [
    ("card-overview.svg", "01", "Overview", "START HERE", m_overview, "native"),
    ("card-architecture.svg", "03", "Architecture", "NODE INTERNALS", m_architecture, "ink"),
    ("card-privacy.svg", "04", "Shielded space", "PRIVACY", m_privacy, "shield"),
    ("card-tokenomics.svg", "05", "Tokenomics", "MAZZE TOKEN", m_tokenomics, "native"),
    ("card-developers.svg", "06", "Developers", "BUILD", m_developers, "evm"),
    ("card-node.svg", "07", "Run a node", "TESTNET · OPERATORS", m_node, "ink"),
    ("card-knowledge.svg", "08", "Knowledge base", "FAQ · GLOSSARY", m_knowledge, "muted"),
    ("card-community.svg", "09", "Community", "ECOSYSTEM", m_community, "evm"),
    ("card-roadmap.svg", "10", "Roadmap", "PHASES", m_roadmap, "native"),
]


# ---------------------------------------------------------------- diagrams
def box(x, y, w, h, t, title, sub=None, accent=None, fill=None, title_size=17):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill or t["surface"]}" stroke="{t["hair"]}"/>'
    if accent:
        out += f'<rect x="{x}" y="{y}" width="4" height="{h}" rx="2" fill="{accent}"/>'
    out += text(x + 18, y + 30, title, title_size, t["ink"], 600)
    if sub:
        for i, s in enumerate(sub if isinstance(sub, list) else [sub]):
            out += text(x + 18, y + 56 + i * 22, s, 13.5, t["muted"], mono=True)
    return out


def arrow(x1, y1, x2, y2, t, label=None, color=None, dash=False, lx=None, ly=None):
    col = color or t["muted"]
    d = ' stroke-dasharray="5 5"' if dash else ""
    out = (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="1.6"{d} '
           f'marker-end="url(#arr-{col.strip("#")})"/>')
    out = (f'<defs><marker id="arr-{col.strip("#")}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" '
           f'markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker></defs>') + out
    if label:
        out += text(lx if lx is not None else (x1 + x2) / 2, ly if ly is not None else (y1 + y2) / 2 - 8,
                    label, 12.5, t["muted"], mono=True, anchor="middle")
    return out


def header(t, w, eyebrow, title):
    return (text(48, 58, eyebrow, 13, t["muted"], 500, mono=True, ls="0.08em")
            + text(48, 96, title, 28, t["ink"], 700, ls="-0.01em")
            + f'<line x1="48" y1="120" x2="{w-48}" y2="120" stroke="{t["hair"]}"/>')


def d_three_spaces(mode):
    t = THEMES[mode]
    w, h = 1400, 620
    b = hatch_def(t) + header(t, w, "MAZZE · ONE CHAIN, THREE SPACES", "Native, eSpace and the Shielded space share one DAG and one state root")
    cols = [
        ("NATIVE", t["native"], "#ffffff", t["native_soft"], "Native space",
         ["base32 addresses (mazze:…)", "Mazze interpreter", "sponsorship · collateral", "internal contracts", "mazze_* RPC"]),
        ("ESPACE · EVM", t["evm"], "#ffffff", t["evm_soft"], "eSpace",
         ["0x… addresses, MetaMask", "revm 40 · Prague spec", "34036/34036 state tests", "KZG 0x0a, standard precompiles", "eth_* RPC"]),
        ("SHIELDED", t["shield"], t["on_shield"], "url(#hatch)", "Shielded space",
         ["mzs1… addresses", "2-in × 2-out notes", "STARK proofs (PS-1)", "nullifiers · anchors", "shielded_* RPC"]),
    ]
    cw, gap, x0, y0 = 416, 28, 48, 150
    for i, (ch, col, fg, soft, title, items) in enumerate(cols):
        x = x0 + i * (cw + gap)
        b += f'<rect x="{x}" y="{y0}" width="{cw}" height="300" rx="8" fill="{t["surface"]}" stroke="{t["hair"]}"/>'
        c, _ = chip(x + 20, y0 + 20, ch, col, fg, 12)
        b += c + text(x + 20, y0 + 84, title, 24, t["ink"], 700)
        for j, it in enumerate(items):
            b += f'<circle cx="{x+26}" cy="{y0+120+j*34}" r="3.5" fill="{col}"/>'
            b += text(x + 40, y0 + 125 + j * 34, it, 15, t["ink2"], 400, mono=True)
    by = 500
    b += f'<rect x="48" y="{by}" width="{w-96}" height="70" rx="8" fill="{t["ink"]}"/>'
    b += text(72, by + 30, "Shared base layer", 17, t["bg"], 600)
    b += text(72, by + 54, "PoW (RandomX) · DAG/DETS ordering · epochs · one state root over the three spaces", 14, t["muted2"], mono=True)
    for i in range(3):
        cx = x0 + i * (cw + gap) + cw / 2
        b += f'<line x1="{cx}" y1="{y0+300}" x2="{cx}" y2="{by}" stroke="{t["muted2"]}" stroke-width="1.5" stroke-dasharray="4 4"/>'
    b += text(x0 + cw + gap / 2, 478, "cross-space bridge", 12, t["muted"], mono=True, anchor="middle")
    b += text(x0 + 2 * cw + 1.5 * gap, 478, "shield-in / shield-out", 12, t["muted"], mono=True, anchor="middle")
    return svg(w, h, b, t)


def d_node_pipeline(mode):
    t = THEMES[mode]
    w, h = 1400, 560
    b = hatch_def(t) + header(t, w, "NODE PIPELINE", "From a transaction to an executed epoch")
    y = 170
    steps = [
        ("RPC / P2P", ["mazze_* · eth_*", "shielded_*"], t["muted"]),
        ("Transaction pool", ["account lanes", "shielded lane"], t["native"]),
        ("Block generator", ["pack · slot heights"], t["native"]),
        ("PoW · RandomX", ["local or Stratum"], t["ink"]),
        ("Sync graph", ["stage A: proofs", "header · body checks"], t["evm"]),
        ("Consensus", ["DETS · pivot chain", "epochs"], t["evm"]),
    ]
    bw, gap = 196, 22
    for i, (title, sub, acc) in enumerate(steps):
        x = 48 + i * (bw + gap)
        b += box(x, y, bw, 108, t, title, sub, acc, title_size=16)
        if i < len(steps) - 1:
            b += arrow(x + bw + 2, y + 54, x + bw + gap - 2, y + 54, t)
    y2 = 360
    low = [
        ("Executor", ["native: interpreter", "eSpace: revm 40", "stage B: shielded engine"], t["ink"], 48, 380),
        ("Block data manager", ["receipts · witnesses", "checkpoints"], t["ink"], 48 + 380 + 60, 330),
        ("Storage", ["MDBX hot tier", "ParityDB cold tier"], t["ink"], 48 + 380 + 60 + 330 + 60, 300),
    ]
    for title, sub, acc, x, bw2 in low:
        b += box(x, y2, bw2, 126, t, title, sub, acc, title_size=16)
    last_x = 48 + 5 * (bw + gap) + bw / 2
    b += f'<path d="M{last_x} {y+108} L{last_x} {y2-40} L{48+190} {y2-40} L{48+190} {y2-4}" fill="none" stroke="{t["muted"]}" stroke-width="1.6"/>'
    b += arrow(48 + 190, y2 - 12, 48 + 190, y2 - 2, t)
    b += text(last_x - 200, y2 - 50, "ordered epoch", 12.5, t["muted"], mono=True, anchor="middle")
    b += arrow(48 + 380 + 2, y2 + 63, 48 + 380 + 58, y2 + 63, t)
    b += arrow(48 + 380 + 60 + 330 + 2, y2 + 63, 48 + 380 + 60 + 330 + 58, y2 + 63, t)
    b += text(1352, 530, "deferred state / receipts / logs roots → later headers", 12.5, t["muted"], mono=True, anchor="end")
    return svg(w, h, b, t)


def d_shielded_lifecycle(mode):
    t = THEMES[mode]
    w, h = 1400, 640
    b = hatch_def(t) + header(t, w, "SHIELDED SPACE · VALUE FLOW", "Shield-in, pay privately, claim, shield-out — the backing always equals the notes")
    # public row
    b += text(48, 168, "PUBLIC · NATIVE SPACE", 12.5, t["native"], 600, mono=True, ls="0.06em")
    b += box(48, 182, 300, 100, t, "Your native account", ["signed tx, value = A"], t["native"])
    b += box(1052, 182, 300, 100, t, "Any native / eSpace", ["address receives v_out"], t["native"])
    b += f'<rect x="540" y="172" width="320" height="120" rx="8" fill="{t["surface"]}" stroke="{t["native"]}" stroke-width="1.5"/>'
    b += text(560, 204, "ShieldedBridge 0x0888…09", 16, t["ink"], 600, mono=True)
    b += text(560, 232, "backing balance (native)", 13.5, t["muted"], mono=True)
    b += text(560, 258, "= Σ value of all notes", 13.5, t["native"], 600, mono=True)
    b += text(560, 280, "fees are burned", 13, t["muted"], mono=True)
    b += arrow(350, 232, 536, 232, t, "shieldIn(bodyHash)", t["native"])
    b += arrow(862, 232, 1048, 232, t, "v_public_out", t["native"])
    # shielded row
    sy = 380
    b += f'<rect x="48" y="{sy-28}" width="{w-96}" height="176" rx="10" fill="url(#hatch)" opacity="0.35"/>'
    b += text(48, sy - 40, "PRIVATE · SHIELDED SPACE", 12.5, t["ink"], 600, mono=True, ls="0.06em")
    nodes = [
        (72, "1 · Shield-in", ["consumes deposit credit", "→ self-note (seed)"]),
        (408, "2 · Pay", ["2 in × 2 out, STARK", "opening sent off-chain"]),
        (744, "3 · Claim", ["received note + self-note", "→ one recoverable note"]),
        (1080, "4 · Shield-out", ["v_public_out > 0", "to a public address"]),
    ]
    for x, title, sub in nodes:
        b += box(x, sy, 270, 120, t, title, sub, t["shield"])
    for i in range(3):
        x = nodes[i][0] + 272
        b += arrow(x, sy + 60, nodes[i + 1][0] - 2, sy + 60, t, None, t["ink"])
    b += f'<line x1="700" y1="294" x2="700" y2="{sy-30}" stroke="{t["muted2"]}" stroke-dasharray="4 4"/>'
    b += text(712, 336, "credit recorded for bodyHash", 12.5, t["muted"], mono=True)
    b += text(48, 604, "Every shielded transaction has the same public shape: 2 nullifiers, 2 commitments, a recovery slot, one constant fee.", 15, t["ink2"])
    return svg(w, h, b, t)


def d_shielded_tx(mode):
    t = THEMES[mode]
    w, h = 1400, 600
    b = hatch_def(t) + header(t, w, "ANATOMY OF A SHIELDED TRANSACTION", "A 441-byte body in the block, a proof up to 192 KiB beside it")
    fields = [
        ("version", "u8 · u8", 1.0),
        ("anchor", "48 B", 1.5),
        ("nf ×2", "2 × 48 B", 1.9),
        ("cm_out ×2", "2 × 48 B", 1.9),
        ("recovery", "32+64+16 B", 2.0),
        ("v_in · v_out · dest", "u64 · u64 · opt", 2.6),
        ("fee", "u64", 1.0),
        ("proof_hash", "64 B", 1.7),
    ]
    total = sum(f[2] for f in fields)
    x, y, W = 48, 170, w - 96
    for name, size, wt in fields:
        fw = W * wt / total
        is_proof = name == "proof_hash"
        b += (f'<rect x="{x:.1f}" y="{y}" width="{fw-4:.1f}" height="86" rx="5" '
              f'fill="{t["evm_soft"] if is_proof else t["surface"]}" stroke="{t["evm"] if is_proof else t["hair"]}"/>')
        b += text(x + 10, y + 34, name, 13.5, t["ink"], 600, mono=True)
        b += text(x + 10, y + 62, size, 12.5, t["muted"], mono=True)
        x += fw
    b += text(48, 290, "BODY · in the block's shielded section · committed by transactions_root", 12.5, t["muted"], 500, mono=True, ls="0.04em")
    px = w - 48 - 520
    b += f'<rect x="{px}" y="350" width="520" height="150" rx="8" fill="{t["surface"]}" stroke="{t["evm"]}" stroke-width="1.5"/>'
    b += text(px + 22, 384, "Witness sidecar · STARK proof", 17, t["ink"], 600)
    for i, s in enumerate(["PS-1: KoalaBear⁸ · FRI · Keccak-256", "≈185–189 KB measured · cap 192 KiB",
                           "sent on the wire, never stored in the block DB"]):
        b += text(px + 22, 414 + i * 26, s, 13.5, t["muted"], mono=True)
    b += f'<path d="M{w-48-120} 258 L{w-48-120} 346" stroke="{t["evm"]}" stroke-width="1.6" stroke-dasharray="5 5" fill="none"/>'
    b += text(w - 48 - 132, 312, "commits to", 12.5, t["evm"], mono=True, anchor="end")
    b += box(48, 350, 560, 150, t, "What an observer learns", ["that a valid 2×2 spend happened", "public amounts in / out (shield-in, shield-out)",
                                                                 "the constant fee — and nothing else"], t["shield"])
    b += text(48, 556, "No sender, nonce, signature or gas. Shield-in, payment and claim are indistinguishable by size and fee.", 15, t["ink2"])
    return svg(w, h, b, t)


def d_storage(mode):
    t = THEMES[mode]
    w, h = 1400, 520
    b = hatch_def(t) + header(t, w, "STORAGE", "Two tiers: MDBX for hot state, ParityDB for history and snapshots")
    b += box(48, 160, 620, 220, t, "MDBX · hot tier", ["state_db_type = \"mdbx\" (default)", "mmap, RAM-speed reads",
                                                        "current state · delta MPTs", "ShieldedWitness column (pruned an era behind)"], t["native"])
    b += box(732, 160, 620, 220, t, "ParityDB · cold tier", ["blocks · receipts · traces", "history",
                                                             "snapshots: storage_db/snapshot/paritydb_<epoch>/",
                                                             "fallback state DB (\"paritydb\")"], t["ink"])
    b += arrow(670, 270, 728, 270, t)
    b += text(48, 430, "Checkpoint cadence  era_epoch_count = 20 000 epochs  ·  consensus says “this era is final”", 14.5, t["ink2"], mono=True)
    b += text(48, 462, "Snapshot cadence    snapshot_epoch_count ≈ 2 000 epochs  ·  disk says “this state can ship to a peer”", 14.5, t["ink2"], mono=True)
    return svg(w, h, b, t)


if __name__ == "__main__":
    for mode in ("light", "dark"):
        suffix = "" if mode == "light" else "-dark"
        write(f"cover-home{suffix}.svg", home_cover(mode))
        write(f"diagram-three-spaces{suffix}.svg", d_three_spaces(mode))
        write(f"diagram-node-pipeline{suffix}.svg", d_node_pipeline(mode))
        write(f"diagram-shielded-flow{suffix}.svg", d_shielded_lifecycle(mode))
        write(f"diagram-shielded-tx{suffix}.svg", d_shielded_tx(mode))
        write(f"diagram-storage{suffix}.svg", d_storage(mode))
    for fname, num, title, sub, motif, accent in CARDS:
        accent_key = {"ink": "ink", "shield": "shield", "muted": "muted"}.get(accent, accent)
        write(fname, card(num, title, sub, motif, accent_key))
    print("ok", len(os.listdir(OUT)))
