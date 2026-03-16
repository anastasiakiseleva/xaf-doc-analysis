# Setting Up Free Local AI (Ollama) for Relationship Classification

## What You'll Do:

Classify 5,000 high-value documentation relationships using a **free local AI model** on your PC instead of expensive cloud APIs.

---

## Step 1: Install Ollama (5 minutes)

1. **Download Ollama**:
   - Go to: https://ollama.com/download
   - Click "Download for Windows"
   - Run the installer

2. **Verify installation**:
   ```powershell
   ollama --version
   ```
   Should show version number (e.g., "ollama version 0.1.32")

---

## Step 2: Install a Model (10-15 minutes)

Choose **ONE** of these models:

### Option A: Llama 3.1 (8B) - Recommended
```powershell
ollama pull llama3.1:8b
```
- **Size**: 4.7 GB download
- **Speed**: ~2-3 pairs/second
- **Quality**: Good for relationship classification
- **Time**: ~2-3 hours for 5,000 pairs

### Option B: Mistral (7B) - Faster but less accurate
```powershell
ollama pull mistral:7b
```
- **Size**: 4.1 GB download
- **Speed**: ~3-4 pairs/second
- **Quality**: Decent, may need review
- **Time**: ~1.5-2 hours for 5,000 pairs

### Option C: Qwen 2.5 (7B) - Good balance
```powershell
ollama pull qwen2.5:7b
```
- **Size**: 4.4 GB download
- **Speed**: ~3 pairs/second
- **Quality**: Good reasoning ability
- **Time**: ~2 hours for 5,000 pairs

**Test the model**:
```powershell
ollama run llama3.1:8b "Explain what a property editor is"
```

---

## Step 3: Configure the Classification Script

Create a new file `scripts/06_classify_relationships_ollama.py` or modify the existing one to add Ollama support.

**Key changes needed**:
1. Add "ollama" as a provider option
2. Call local Ollama API instead of cloud services
3. Use http://localhost:11434/api/generate endpoint

---

## Step 4: Run Classification

```powershell
# Activate your virtual environment
.\.venv\Scripts\Activate.ps1

# Run classification on the filtered 5,000 pairs
python scripts/06_classify_relationships.py `
    --input outputs/semantic_pairs_high_value.parquet `
    --provider ollama `
    --model llama3.1:8b `
    --output outputs/classified_pairs_high_value.parquet `
    --delay 0
```

**Parameters explained**:
- `--input`: Your filtered 5,000 high-value pairs
- `--provider ollama`: Use local AI instead of cloud
- `--model llama3.1:8b`: Which model to use
- `--delay 0`: No delay needed for local calls
- `--output`: Where to save results

---

## What Happens During Classification:

```
Processing pair 1/5000:
  Source: "How to Create a Custom Property Editor" (tutorial)
  Target: "PropertyEditor Class" (API reference)
  
  AI Analysis: "explains" (confidence: 0.85)
  Rationale: Tutorial demonstrates practical implementation of API
  Evidence: "inherit from PropertyEditor", "override CreateControl"
  
✓ Saved checkpoint (every 50 pairs)
```

**Progress tracking**:
- Checkpoints saved every 50 pairs
- Can stop and resume anytime
- Terminal shows current pair and estimated time remaining

---

## Expected Results:

After 2-3 hours, you'll have:

✅ **5,000 classified relationships** with labels like:
- **"explains"**: 2,000+ pairs (tutorial → API)
- **"uses"**: 1,500+ pairs (code example → API)
- **"requires"**: 800+ pairs (prerequisite knowledge)
- **"extends"**: 400+ pairs (advanced topics)
- **"applies_to"**: 200+ pairs (platform-specific)

✅ **Confidence scores** (0.0 - 1.0) for each relationship

✅ **Evidence quotes** from actual documentation text

✅ **Bidirectional flags** (does relationship work both ways?)

---

## Cost Comparison:

| Method | Cost | Time | Quality |
|--------|------|------|---------|
| **Ollama (local)** | **$0** | 2-3 hours | Good |
| OpenAI GPT-4 | $25-50 | 30-60 min | Excellent |
| Anthropic Claude | $30-60 | 30-60 min | Excellent |

---

## Troubleshooting:

**"ollama: command not found"**
- Restart PowerShell after installation
- Check: `C:\Users\<YourName>\AppData\Local\Programs\Ollama\ollama.exe`

**"connection refused"**
- Ollama service not running
- Run: `ollama serve` in a separate terminal

**"model not found"**
- Model not downloaded
- Run: `ollama pull llama3.1:8b`

**Too slow?**
- Close other applications
- Use smaller model: `mistral:7b`
- Or process fewer pairs first (test with --limit 100)

---

## Next Steps After Classification:

1. **Analyze results**:
   ```python
   python tools/analyze_classified_relationships.py
   ```

2. **Generate reports**:
   - Which tutorials explain which APIs?
   - What prerequisites are missing?
   - Where are documentation gaps?

3. **Update documentation**:
   - Add missing cross-links
   - Create prerequisite sections
   - Reorganize learning paths

---

## Questions?

- **"Can I use multiple models?"** - Yes, test with different models and compare
- **"Can I stop and resume?"** - Yes, checkpoints saved every 50 pairs
- **"What if results are poor?"** - Try a larger model or switch to cloud API for subset
- **"How much RAM needed?"** - 8GB minimum, 16GB recommended

---

## Alternative: Cloud API (If Ollama Too Slow)

If 2-3 hours is too long, use cloud API for faster results:

```powershell
# With OpenAI (need API key)
python scripts/06_classify_relationships.py `
    --input outputs/semantic_pairs_high_value.parquet `
    --provider openai `
    --api-key "your-api-key" `
    --model gpt-4o-mini `
    --output outputs/classified_pairs_high_value.parquet

# Cost: ~$15-25 for 5,000 pairs with gpt-4o-mini
# Time: 20-30 minutes
```

---

**Ready to start? Install Ollama and let me know if you need help!**
