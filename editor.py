
import subprocess
import sys
from pathlib import Path

if len(sys.argv) != 3:
    print("Uso: python editor.py entrada.mp4 saida.mp4")
    sys.exit(1)

entrada = Path(sys.argv[1])
saida = Path(sys.argv[2])

if not entrada.exists():
    print(f"Vídeo não encontrado: {entrada}")
    sys.exit(1)

filtros = (
    "scale=1080:1920:force_original_aspect_ratio=increase,"
    "crop=1080:1920,"
    "eq=contrast=1.08:saturation=1.15:brightness=-0.02,"
    "colorbalance=bs=0.08:rs=-0.03:gs=-0.01,"
    "format=yuv420p"
)

comando = [
    "ffmpeg", "-y",
    "-i", str(entrada),
    "-vf", filtros,
    "-map", "0:v:0",
    "-map", "0:a?",
    "-c:v", "libx264",
    "-preset", "ultrafast",
    "-crf", "23",
    "-c:a", "aac",
    "-b:a", "192k",
    "-movflags", "+faststart",
    str(saida)
]

subprocess.run(comando, check=True)
print(f"Vídeo editado: {saida}")
