# 🧠 DECODE.IT – A Self-Replicating NFT

> “This NFT holds the key to itself.”

DECODE.IT is a one-of-a-kind NFT that *contains a compressed version of the code that can regenerate itself*. It's not just an image — it's a functioning recursive program embedded in pixels. Once decoded, it can reproduce the script that originally created the image, making it a digital ouroboros — a snake eating its own tail.

Built using Python, Pillow, NumPy, zlib, and base64 — this NFT represents a fusion of **art, cryptography, and code**.

---

## 🔍 How It Works

- **encode_it.py**: Takes the source code and encodes it **into an image**, pixel by pixel, hiding characters in grayscale values. It also stores the black pixel positions in a compressed format.
- **decode_it.py**: Reads the encoded image and **reconstructs the original source code** from the pixel data.

---

## 🧬 Files Included

| File           | Purpose                                                    |
|----------------|------------------------------------------------------------|
| `encode_it.py` | Embeds the Python source code into an image                |
| `decode_it.py` | Extracts the Python source code back from the image        |
| `DECODE.IT.png`| The NFT image that contains the encoded version of itself  |

---

## 🧪 Requirements

To run either script, install the following Python packages:

```bash
pip install pillow numpy
```

---

## 🚀 Usage

### 🔁 To Regenerate the NFT Image (From Code):
1. Ensure `encode_it.py` is your main code.
2. Run:

```bash
python encode_it.py
```

➡️ This creates an image: `DECODE.IT.png` containing the embedded code.

---

### 🧩 To Decode the NFT Image Back Into Code:

1. Place `DECODE.IT.png` in the same directory as `decode_it.py`
2. Run:

```bash
python decode_it.py
```

➡️ This regenerates the file `encode_it.py` — a replica of the original encoder.

---

## 📐 Technical Structure

- **File size**: 512x512 (262,144 pixels)
- **Pixel Encoding**:
  - `Black (0)` pixels: Fixed locations stored via compressed `BLACK_PIXEL_LOCS`
  - `White (255)` pixels: Used to store source code as ASCII grayscale values
- **Compression**: zlib + base64 to compress the black pixel map

---

## 👨‍💻 Author

**Anurag Pandey**  
- 💼 [LinkedIn](https://www.linkedin.com/in/-anurag-pandey-/)  
- 🧠 Creator of DECODE.IT  
- 📍 B.Tech AIML, GGSIPU

---

## 📢 Message from the Creator

```
Hi Decoder,

    FIRST OF ALL, I WANT TO CONGRATULATE YOU FOR SUCCESSFULLY DECODING THE DECODE.IT NFT.
    THIS NFT PROJECT WAS FUN TO BUILD AND INSPIRED ME TO LEARN MORE ABOUT THE METAVERSE AND BLOCKCHAIN.

    ABOUT 180 LINES ARE CODE-FREE INSIDE THE GENERATED encode_it.py FILE.
    YOU CAN MODIFY THE LOGIC THERE TO BUILD SOMETHING NEW AND ENCODE THAT BACK INTO THE IMAGE.

    THIS ISN’T JUST AN NFT.
    IT’S AN IDEA – A TOOL – A LOOP – A CHALLENGE.

    ENJOY & STAY CURIOUS!
```

---

## 📎 License

This project is released under the [MIT License](LICENSE) — feel free to fork, experiment, and create your own version of recursive NFTs!

---

## 💡 Ideas to Extend

- Make it web-based (in-browser decoder)
- Add steganography techniques
- Integrate with blockchain for auto-verification
- Add QR-encoded URLs inside the image

---

🌀 **DECODE.IT** — Code. Compress. Loop.  

