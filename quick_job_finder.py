#!/usr/bin/env python3
"""
Quick AI Trainer Job Finder
Display current opportunities with basic filtering
"""

import json
from typing import List, Dict
from datetime import datetime


class QuickJobFinder:
    """Quick lookup for AI trainer jobs"""
    
    def __init__(self):
        self.jobs = self.load_jobs()
    
    def load_jobs(self) -> List[Dict]:
        """Load jobs from JSON file or return hardcoded list"""
        jobs = [
            {
                "company": "OpenAI",
                "position": "AI Trainer / Contractor",
                "site": "https://openai.com/careers",
                "pay_range": "$30-80/hour",
                "description": "Train and evaluate AI models",
                "remote": True,
                "experience_level": "Intermediate"
            },
            {
                "company": "Anthropic",
                "position": "AI Safety Researcher / Trainer",
                "site": "https://www.anthropic.com/careers",
                "pay_range": "$50-100/hour",
                "description": "Constitutional AI training and evaluation",
                "remote": True,
                "experience_level": "Intermediate-Advanced"
            },
            {
                "company": "Scale AI",
                "position": "AI Trainer / Data Annotator",
                "site": "https://scale.com/careers",
                "pay_range": "$25-60/hour",
                "description": "Label and train machine learning models",
                "remote": True,
                "experience_level": "Beginner-Intermediate"
            },
            {
                "company": "Outlier AI",
                "position": "AI Trainer",
                "site": "https://www.outlier.ai",
                "pay_range": "$15-50/hour",
                "description": "Train and evaluate AI models",
                "remote": True,
                "experience_level": "Beginner"
            },
            {
                "company": "Hugging Face",
                "position": "ML Engineer / Trainer",
                "site": "https://huggingface.co/join",
                "pay_range": "$80-150k",
                "description": "Build and train language models",
                "remote": True,
                "experience_level": "Advanced"
            },
            {
                "company": "Google Cloud AI",
                "position": "AI Trainer",
                "site": "https://cloud.google.com/careers",
                "pay_range": "$100-180k",
                "description": "Train and evaluate AI models for Google Cloud",
                "remote": True,
                "experience_level": "Advanced"
            },
            {
                "company": "AWS AI",
                "position": "ML Training Specialist",
                "site": "https://www.amazon.jobs",
                "pay_range": "$90-160k",
                "description": "Machine learning training and development",
                "remote": True,
                "experience_level": "Advanced"
            },
            {
                "company": "Cohere",
                "position": "Model Trainer / Evaluator",
                "site": "https://cohere.com/careers",
                "pay_range": "$45-90/hour",
                "description": "Train large language models",
                "remote": True,
                "experience_level": "Intermediate"
            },
            {
                "company": "Kaggle",
                "position": "Course Instructor / Trainer",
                "site": "https://www.kaggle.com",
                "pay_range": "Variable (course revenue)",
                "description": "Create and teach AI/ML courses",
                "remote": True,
                "experience_level": "Beginner-Advanced"
            },
            {
                "company": "DataCamp",
                "position": "Course Instructor",
                "site": "https://www.datacamp.com/instructor",
                "pay_range": "$5-20k per course",
                "description": "Teach data science and AI courses",
                "remote": True,
                "experience_level": "Beginner-Advanced"
            },
        ]
        return jobs
    
    def filter_by_pay(self, min_hourly: int = 0) -> List[Dict]:
        """Filter jobs by minimum hourly rate"""
        filtered = []
        for job in self.jobs:
            if '/hour' in job['pay_range']:
                try:
                    rate = int(job['pay_range'].split('-')[0].replace('$', ''))
                    if rate >= min_hourly:
                        filtered.append(job)
                except:
                    filtered.append(job)
        return filtered
    
    def filter_by_experience(self, level: str) -> List[Dict]:
        """Filter jobs by experience level"""
        return [j for j in self.jobs if level.lower() in j['experience_level'].lower()]
    
    def filter_by_company(self, company_name: str) -> List[Dict]:
        """Filter jobs by company name"""
        return [j for j in self.jobs if company_name.lower() in j['company'].lower()]
    
    def display_job(self, job: Dict) -> None:
        """Display a single job in formatted way"""
        print(f"\n{'='*80}")
        print(f"🏢 {job['company']}")
        print(f"{'='*80}")
        print(f"📌 Position: {job['position']}")
        print(f"💰 Pay: {job['pay_range']}")
        print(f"📝 Description: {job['description']}")
        print(f"🌐 Remote: {'Yes' if job['remote'] else 'No'}")
        print(f"📊 Experience Level: {job['experience_level']}")
        print(f"🔗 Apply: {job['site']}")
    
    def display_all(self) -> None:
        """Display all jobs"""
        print(f"\n{'='*80}")
        print(f"🤖 AI TRAINER JOBS FOR SOFTWARE ENGINEERS - {len(self.jobs)} Opportunities")
        print(f"{'='*80}")
        
        for i, job in enumerate(self.jobs, 1):
            print(f"\n{i}. {job['company']} - {job['position']}")
            print(f"   💰 {job['pay_range']} | 📊 {job['experience_level']}")
            print(f"   {job['description']}")
            print(f"   🔗 {job['site']}")
    
    def search(self, query: str) -> List[Dict]:
        """Search jobs by company or position"""
        query = query.lower()
        return [j for j in self.jobs if query in j['company'].lower() or query in j['position'].lower()]
    
    def print_stats(self) -> None:
        """Print statistics about available jobs"""
        hourly_jobs = [j for j in self.jobs if '/hour' in j['pay_range']]
        salary_jobs = [j for j in self.jobs if 'k' in j['pay_range'].lower() or j['pay_range'].count('-') == 1]
        remote_jobs = [j for j in self.jobs if j['remote']]
        
        print(f"\n📊 JOB STATISTICS")
        print(f"{'='*50}")
        print(f"Total Positions: {len(self.jobs)}")
        print(f"Hourly Contracts: {len(hourly_jobs)}")
        print(f"Salary Positions: {len(salary_jobs)}")
        print(f"Remote Positions: {len(remote_jobs)}")
        
        # Calculate average hourly rates
        hourly_rates = []
        for job in hourly_jobs:
            try:
                low = int(job['pay_range'].split('-')[0].replace('$', '').replace('/hour', ''))
                high = int(job['pay_range'].split('-')[1].replace('$', '').replace('/hour', ''))
                hourly_rates.append((low + high) / 2)
            except:
                pass
        
        if hourly_rates:
            avg_rate = sum(hourly_rates) / len(hourly_rates)
            print(f"Average Hourly Rate: ${avg_rate:.2f}/hour")
        
        # Experience level distribution
        print(f"\n📈 By Experience Level:")
        levels = {}
        for job in self.jobs:
            level = job['experience_level']
            levels[level] = levels.get(level, 0) + 1
        
        for level, count in sorted(levels.items()):
            print(f"  • {level}: {count} positions")


def main():
    """Interactive menu"""
    finder = QuickJobFinder()
    
    while True:
        print("\n" + "="*50)
        print("🔍 AI TRAINER JOB FINDER")
        print("="*50)
        print("1. View all jobs")
        print("2. Search by company")
        print("3. Filter by minimum pay (hourly)")
        print("4. Filter by experience level")
        print("5. View statistics")
        print("6. Exit")
        print("="*50)
        
        choice = input("Select option (1-6): ").strip()
        
        if choice == "1":
            finder.display_all()
        
        elif choice == "2":
            company = input("Enter company name to search: ").strip()
            results = finder.search(company)
            if results:
                for job in results:
                    finder.display_job(job)
            else:
                print(f"No jobs found for '{company}'")
        
        elif choice == "3":
            try:
                min_pay = int(input("Enter minimum hourly rate: $"))
                results = finder.filter_by_pay(min_pay)
                if results:
                    print(f"\n✅ Found {len(results)} jobs paying ${min_pay}+/hour:\n")
                    for job in results:
                        print(f"• {job['company']} - {job['pay_range']}")
                        print(f"  {job['position']}")
                        print(f"  {job['site']}\n")
                else:
                    print(f"No jobs found paying ${min_pay}+/hour")
            except ValueError:
                print("Invalid amount")
        
        elif choice == "4":
            print("\nExperience levels: Beginner, Intermediate, Advanced")
            level = input("Enter experience level: ").strip()
            results = finder.filter_by_experience(level)
            if results:
                print(f"\n✅ Found {len(results)} jobs for {level} level:\n")
                for job in results:
                    print(f"• {job['company']} - {job['pay_range']}")
                    print(f"  {job['position']}\n")
            else:
                print(f"No jobs found for {level} level")
        
        elif choice == "5":
            finder.print_stats()
        
        elif choice == "6":
            print("👋 Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
