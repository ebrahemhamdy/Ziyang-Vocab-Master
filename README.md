# Ziyang Vocab Master (公益开源版)

**Author:** Ziyang Xu 
**Grade:** 10th Grade (High School Affiliated to Beijing Normal University - BNU)
**License:** Open Source & 100% Free (Public Welfare Software)

---

## 🌟 The Problem I Wanted to Solve

As a high school student, I frequently encounter a major problem with existing English vocabulary apps: **they force you to use their pre-defined word lists.** 

In the real world, students study from specific textbooks, read custom materials, or tackle past exam papers (like GRE or SAT). We have our own reading materials with the exact vocabulary we need to master. However, importing a custom vocabulary list from a textbook into existing apps is either impossible, incredibly tedious, or locked behind a paywall. 

That is why I created **Ziyang Vocab Master**. 

This is a **public welfare, open-source, and entirely free** software designed by a student, for students. My goal is to empower anyone to turn their own PDFs and textbooks into a fully interactive, AI-enriched vocabulary course in just a few clicks.

---

## 🚀 Features

Ziyang Vocab Master is a self-contained, all-in-one HTML application that runs entirely in your local browser (no data is uploaded to my servers). It is divided into a three-step pipeline:

### 1. 📄 PDF Vocabulary Extractor (PDF 词库提取器)
Instead of typing words manually, you can upload any textbook or study guide PDF (e.g., GRE 24 Sets).
- Automatically scans the PDF and extracts target vocabulary words.
- Filters out "noisy" stop words.
- Exports a clean CSV list of the vocabulary found in your specific material.

### 2. 🤖 AI Word Factory (AI 单词加工厂)
Once you have your custom word list, Ziyang Vocab Master uses AI to do the heavy lifting of looking up definitions!
- **Gemini API Integration:** Automatically fetches phonetic symbols (IPA), concise Chinese meanings, root etymologies, English definitions, synonyms, antonyms, and example sentences.
- **Pexels API Integration:** Automatically fetches a high-quality visual memory aid (image) for the word.
- Processes your list safely with rate-limiting and exports a comprehensive, enriched CSV database.

### 3. 🧠 Immersive Flashcard Study (沉浸背单词测验)
The ultimate study tool to actually memorize the words you processed.
- **Interactive Flashcards:** Uses spaced repetition logic (Unknown/Known tracking) to ensure you focus on the words you get wrong.
- **Multi-dimensional Testing:** 
  - **[1] Association:** Think of the root, synonyms, and antonyms.
  - **[2] Context:** Review the example sentence and associated scenes.
  - **[3] Spelling:** Type out the word from memory.
  - **[4] Pronunciation:** Uses your microphone and Web Speech API to test your English pronunciation!
- **Mac Dictionary Integration:** Right-click on any English word to instantly pop up the native macOS Dictionary.

---

## 💻 How to Use

1. **Download the App:** Simply download the `Ziyang_Vocab_Master.html` file.
2. **Open in Browser:** Double-click the file to open it in Chrome, Safari, or Edge.
3. **Navigate the Tabs:** 
   - Go to **Tab 1** to extract words from your textbook PDF.
   - Go to **Tab 2** to import the extracted CSV, plug in your Gemini/Pexels API keys, and let the AI generate the study material.
   - Go to **Tab 3** to load the final enriched CSV and start your personalized study session!

---

## 🤝 Contribution & Public Welfare

Education should not be restricted by expensive software. If you are a student, teacher, or developer who finds this tool useful, feel free to use, modify, and share it. Let's make learning more efficient together!
