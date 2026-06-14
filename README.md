# AI Trainer Jobs for Software Engineers

A Python-based scraper to find AI trainer job opportunities and their compensation across multiple platforms.

## 📋 Overview

This project helps software engineers find AI trainer positions, including:
- **Direct Positions**: Full-time and part-time roles at AI companies
- **Contract Work**: Hourly contractor positions for model training/evaluation
- **Freelance Opportunities**: Gig-based work on major platforms
- **Course Teaching**: Revenue-sharing educational opportunities

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/KarringtonLeonard/AI-Trainer-Jobs.git
cd AI-Trainer-Jobs

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
# Run the scraper
python ai_trainer_jobs_scraper.py
```

This will:
1. Collect AI trainer job listings from multiple sources
2. Display a formatted table of current opportunities
3. Export data to CSV and JSON formats

## 📊 Job Sources

### Direct Companies Hiring AI Trainers
- **OpenAI** - $30-80/hour | AI Model Training
- **Anthropic** - $50-100/hour | Constitutional AI Training
- **Scale AI** - $25-60/hour | Data Labeling & Model Training
- **Outlier AI** - $15-50/hour | AI Model Evaluation
- **Hugging Face** - $80-150k | ML Engineer roles
- **Google Cloud AI** - $100-180k | AI Training Specialist
- **AWS AI** - $90-160k | ML Training Specialist
- **Cohere** - $45-90/hour | Language Model Training
- **Deepmind** - $120-200k | AI Research Training

### Freelance Platforms
- [Upwork](https://www.upwork.com/ab/jobs/search/?q=AI+trainer)
- [Fiverr](https://www.fiverr.com/search/gigs?query=ai+training)
- [PeoplePerHour](https://www.peopleperhour.com/browse/ai-training)
- [Guru](https://www.guru.com/d/jobs/c/programming/)

### Job Boards
- [LinkedIn](https://www.linkedin.com/jobs/search/?keywords=AI%20Trainer)
- [Indeed](https://www.indeed.com/jobs?q=AI+Trainer+Software+Engineer)
- [Kaggle](https://www.kaggle.com/jobs)

### Course Platforms (Revenue Sharing)
- [Kaggle](https://www.kaggle.com) - Create AI/ML courses
- [DataCamp](https://www.datacamp.com/instructor) - $5-20k per course
- [Coursera](https://partners.coursera.org) - Revenue sharing model
- [Udemy](https://www.udemy.com/teaching/) - Course revenue sharing

## 💰 Salary Ranges

| Role | Range | Type |
|------|-------|------|
| AI Trainer (Contract) | $15-80/hour | Hourly |
| ML Model Evaluator | $25-60/hour | Hourly |
| AI Research Trainer | $120-200k | Full-time |
| ML Engineer | $80-150k | Full-time |
| Cloud AI Specialist | $90-180k | Full-time |
| Course Instructor | $5-20k/course | Per course |

## 📂 Output Files

The scraper generates:
- `ai_trainer_jobs.csv` - Spreadsheet format
- `ai_trainer_jobs.json` - JSON format for programmatic access

## 🎯 Required Skills

✅ **Essential**
- Python programming
- Machine Learning fundamentals (PyTorch, TensorFlow)
- Understanding of LLMs and AI model evaluation
- Technical communication skills

✅ **Beneficial**
- Software engineering background
- Data science experience
- Domain expertise (NLP, Computer Vision, etc.)
- Teaching/mentoring experience
- Experience with specific AI frameworks

## 💡 Tips for Success

1. **Update Your LinkedIn** with keywords: "AI Trainer", "Model Trainer", "AI Evaluator"
2. **Build a Portfolio** - Create AI projects on GitHub showcasing your skills
3. **Start with Contracts** - Many companies prefer contract workers before full-time
4. **Specialize** - Focus on LLMs, Vision Models, or specific domains
5. **Network** - Join AI communities on Discord, Reddit, and Slack channels
6. **Stay Current** - Keep up with latest AI developments and tools

## 🔧 Customization

To modify the scraper:

1. **Add new companies** - Edit `add_manual_job_data()` method
2. **Change filters** - Modify job search parameters
3. **Adjust pay ranges** - Update compensation values
4. **Add new sources** - Create new scraping methods for additional platforms

## ⚠️ Notes

- Some platforms (LinkedIn, Indeed, Upwork) require authentication or have scraping restrictions
- Pay ranges are estimates and vary by experience level and location
- Remote work is common; local positions are less frequent
- Always verify job postings on official company websites

## 📝 Contributing

Contributions welcome! To add new job sources or companies:

1. Fork the repository
2. Add your job source to the scraper
3. Test the code
4. Submit a pull request

## 📧 Contact

Questions or suggestions? Feel free to open an issue or discuss in the repository.

## 📜 License

This project is open source and available under the MIT License.

---

**Last Updated**: 2026-06-14
**Total Companies Listed**: 12+
**Platforms Covered**: 10+
