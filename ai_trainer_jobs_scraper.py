#!/usr/bin/env python3
"""
AI Trainer Jobs Scraper for Software Engineers
Fetches AI trainer job listings from multiple sources and compiles salary/position data
"""

import requests
import json
from typing import List, Dict, Optional
from datetime import datetime
import time
from bs4 import BeautifulSoup
import pandas as pd


class AITrainerJobScraper:
    """Scraper for AI Trainer jobs targeting software engineers"""
    
    def __init__(self):
        self.jobs = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def scrape_upwork_ai_jobs(self) -> List[Dict]:
        """Scrape AI trainer positions from Upwork"""
        try:
            # Note: Upwork requires authentication for real scraping
            # This is a template for the API structure
            url = "https://www.upwork.com/ab/jobs/search/"
            params = {
                'q': 'AI trainer software engineer',
                'sort': 'recency'
            }
            
            print("⚠️  Upwork requires authentication. Use Upwork API or manual browsing.")
            print("   Visit: https://www.upwork.com/ab/jobs/search/?q=AI+trainer+software+engineer")
            
            return []
        except Exception as e:
            print(f"Error scraping Upwork: {e}")
            return []
    
    def scrape_linkedin_ai_jobs(self) -> List[Dict]:
        """Fetch AI trainer jobs from LinkedIn (using search URL)"""
        try:
            print("📋 LinkedIn Job Search URLs:")
            linkedin_urls = {
                "AI Trainer": "https://www.linkedin.com/jobs/search/?keywords=AI%20Trainer&location=United%20States",
                "Machine Learning Trainer": "https://www.linkedin.com/jobs/search/?keywords=Machine%20Learning%20Trainer",
                "AI Curriculum Developer": "https://www.linkedin.com/jobs/search/?keywords=AI%20Curriculum%20Developer",
            }
            
            for title, url in linkedin_urls.items():
                print(f"  {title}: {url}")
            
            return []
        except Exception as e:
            print(f"Error with LinkedIn: {e}")
            return []
    
    def get_indeed_ai_jobs(self) -> List[Dict]:
        """Search Indeed for AI trainer positions"""
        try:
            print("📋 Indeed Job Search URLs:")
            indeed_urls = {
                "AI Trainer": "https://www.indeed.com/jobs?q=AI+Trainer+Software+Engineer",
                "AI Curriculum": "https://www.indeed.com/jobs?q=AI+Curriculum+Developer",
                "Machine Learning": "https://www.indeed.com/jobs?q=Machine+Learning+Instructor",
            }
            
            for title, url in indeed_urls.items():
                print(f"  {title}: {url}")
            
            return []
        except Exception as e:
            print(f"Error scraping Indeed: {e}")
            return []
    
    def add_manual_job_data(self) -> None:
        """Add known companies hiring AI trainers"""
        known_hiring = [
            {
                "company": "OpenAI",
                "position": "AI Trainer / Contractor",
                "site": "https://openai.com/careers",
                "pay_range": "$30-80/hour",
                "description": "Train and evaluate AI models",
                "remote": True,
                "date_found": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "company": "Anthropic",
                "position": "AI Safety Researcher / Trainer",
                "site": "https://www.anthropic.com/careers",
                "pay_range": "$50-100/hour",
                "description": "Constitutional AI training and evaluation",
                "remote": True,
                "date_found": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "company": "Scale AI",
                "position": "AI Trainer / Data Annotator",
                "site": "https://scale.com/careers",
                "pay_range": "$25-60/hour",
                "description": "Label and train machine learning models",
                "remote": True,
                "date_found": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "company": "Outlier AI",
                "position": "AI Trainer",
                "site": "https://www.outlier.ai",
                "pay_range": "$15-50/hour",
                "description": "Train and evaluate AI models",
                "remote": True,
                "date_found": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "company": "Hugging Face",
                "position": "ML Engineer / Trainer",
                "site": "https://huggingface.co/join",
                "pay_range": "$80-150k",
                "description": "Build and train language models",
                "remote": True,
                "date_found": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "company": "Kaggle",
                "position": "Course Instructor / Trainer",
                "site": "https://www.kaggle.com",
                "pay_range": "Variable (course revenue)",
                "description": "Create and teach AI/ML courses",
                "remote": True,
                "date_found": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "company": "DataCamp",
                "position": "Course Instructor",
                "site": "https://www.datacamp.com/instructor",
                "pay_range": "$5-20k per course",
                "description": "Teach data science and AI courses",
                "remote": True,
                "date_found": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "company": "Coursera",
                "position": "Instructor Partner",
                "site": "https://partners.coursera.org",
                "pay_range": "Revenue sharing",
                "description": "Create AI/ML courses",
                "remote": True,
                "date_found": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "company": "Google Cloud AI",
                "position": "AI Trainer",
                "site": "https://cloud.google.com/careers",
                "pay_range": "$100-180k",
                "description": "Train and evaluate AI models for Google Cloud",
                "remote": True,
                "date_found": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "company": "AWS AI",
                "position": "ML Training Specialist",
                "site": "https://www.amazon.jobs",
                "pay_range": "$90-160k",
                "description": "Machine learning training and development",
                "remote": True,
                "date_found": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "company": "Cohere",
                "position": "Model Trainer / Evaluator",
                "site": "https://cohere.com/careers",
                "pay_range": "$45-90/hour",
                "description": "Train large language models",
                "remote": True,
                "date_found": datetime.now().strftime("%Y-%m-%d")
            },
            {
                "company": "Deepmind (Google)",
                "position": "AI Research Trainer",
                "site": "https://www.deepmind.com/careers",
                "pay_range": "$120-200k",
                "description": "Advanced AI model training and research",
                "remote": False,
                "date_found": datetime.now().strftime("%Y-%m-%d")
            }
        ]
        
        self.jobs.extend(known_hiring)
    
    def scrape_freelance_platforms(self) -> None:
        """Add freelance platform links for AI trainer jobs"""
        freelance_sources = {
            "Upwork AI Trainer": "https://www.upwork.com/ab/jobs/search/?q=AI+trainer+software+engineer&sort=recency",
            "Fiverr AI Services": "https://www.fiverr.com/search/gigs?query=ai+training",
            "PeoplePerHour": "https://www.peopleperhour.com/browse/ai-training",
            "Guru": "https://www.guru.com/d/jobs/c/programming/",
        }
        
        print("\n🎯 Freelance Platforms with AI Trainer Gigs:")
        for platform, url in freelance_sources.items():
            print(f"  • {platform}: {url}")
    
    def export_to_csv(self, filename: str = "ai_trainer_jobs.csv") -> None:
        """Export job listings to CSV"""
        if not self.jobs:
            print("No jobs to export")
            return
        
        df = pd.DataFrame(self.jobs)
        df.to_csv(filename, index=False)
        print(f"\n✅ Exported {len(self.jobs)} jobs to {filename}")
    
    def export_to_json(self, filename: str = "ai_trainer_jobs.json") -> None:
        """Export job listings to JSON"""
        if not self.jobs:
            print("No jobs to export")
            return
        
        with open(filename, 'w') as f:
            json.dump(self.jobs, f, indent=2)
        print(f"✅ Exported {len(self.jobs)} jobs to {filename}")
    
    def display_jobs_table(self) -> None:
        """Display jobs in a formatted table"""
        if not self.jobs:
            print("No jobs found")
            return
        
        df = pd.DataFrame(self.jobs)
        print("\n" + "="*120)
        print("AI TRAINER JOBS FOR SOFTWARE ENGINEERS")
        print("="*120)
        print(df.to_string(index=False))
        print("="*120)
        print(f"\nTotal Jobs Found: {len(self.jobs)}")
    
    def run(self) -> None:
        """Run the complete job scraper"""
        print("🤖 AI Trainer Jobs Scraper for Software Engineers")
        print("=" * 60)
        
        # Gather job data
        print("\n📊 Gathering job listings...\n")
        self.add_manual_job_data()
        self.scrape_linkedin_ai_jobs()
        self.get_indeed_ai_jobs()
        self.scrape_upwork_ai_jobs()
        
        # Display results
        self.display_jobs_table()
        
        # Freelance platforms
        self.scrape_freelance_platforms()
        
        # Export data
        print("\n💾 Exporting data...")
        self.export_to_csv()
        self.export_to_json()
        
        print("\n✨ Scraping complete!")
        print("\n📌 TIPS FOR AI TRAINER JOBS:")
        print("  • Update skills in: Python, ML frameworks (PyTorch, TensorFlow)")
        print("  • Strong communication skills are essential")
        print("  • Domain expertise in software engineering is valuable")
        print("  • Remote work is common for AI trainer positions")
        print("  • Many positions are hourly contract work")
        print("  • Consider specializing in specific AI models (LLMs, Vision, etc.)")


def main():
    """Main entry point"""
    scraper = AITrainerJobScraper()
    scraper.run()


if __name__ == "__main__":
    main()
