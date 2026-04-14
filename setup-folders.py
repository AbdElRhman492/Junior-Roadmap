#!/usr/bin/env python3
"""
Create folder structure for Junior Laravel Developer Roadmap
This script creates Phase folders with Topic subfolders
"""

import os
import sys
from pathlib import Path

def create_roadmap_structure():
    """Create the complete folder structure for the roadmap"""
    
    # Define all phases and their topics
    roadmap = {
        "Phase 00 - Fill the Critical Gaps": [
            "01 - OOP Pillars",
            "02 - SOLID Principles",
            "03 - Dependency Injection & IoC",
            "04 - N+1 Problem - Full Mastery",
            "05 - CSRF & XSS",
            "06 - SQL Injection",
            "Checkpoint",
        ],
        "Phase 01 - Laravel Deep Mastery": [
            "01 - Laravel Request Lifecycle",
            "02 - Eloquent ORM - Advanced",
            "03 - Queues & Jobs",
            "04 - Middleware - Write Your Own",
            "05 - REST API Best Practices",
            "06 - Authentication - Sanctum Deep Dive",
            "07 - Routing - Advanced",
            "08 - Laravel Architecture Patterns",
            "09 - Events & Listeners",
            "10 - Caching",
            "Checkpoint",
        ],
        "Phase 02 - Database & Performance": [
            "01 - MySQL Joins - All Types",
            "02 - Indexing - Deep Mastery",
            "03 - Transactions & Data Integrity",
            "04 - Query Optimization",
            "05 - Database Migrations - Advanced",
            "06 - Redis & Caching Strategy",
            "Checkpoint",
        ],
        "Phase 03 - Security, Testing & Clean Code": [
            "01 - Security - All Major Attacks",
            "02 - Testing - PHPUnit & Pest",
            "03 - Clean Code Practices",
            "04 - Error Handling & Logging",
            "05 - Git - Professional Level",
            "06 - API Documentation",
            "Checkpoint",
        ],
        "Phase 04 - Job-Ready Polish": [
            "01 - Portfolio Project - Exam Management API",
            "02 - Interview Preparation",
            "03 - Freelance Setup",
            "04 - Deployment Basics",
            "05 - PHP 8 Modern Features",
            "06 - What's Next After Junior",
            "Checkpoint",
        ],
    }
    
    # Create Learning directory
    learning_dir = Path("Learning")
    learning_dir.mkdir(exist_ok=True)
    
    print("🚀 Creating Junior Laravel Developer Roadmap folder structure...\n")
    
    # Create phase folders and topics
    for phase, topics in roadmap.items():
        phase_dir = learning_dir / phase
        print(f"📁 Creating {phase}...")
        
        for topic in topics:
            topic_dir = phase_dir / topic
            topic_dir.mkdir(parents=True, exist_ok=True)
            
            # Create a template notes file in each topic
            notes_file = topic_dir / "notes.md"
            if not notes_file.exists():
                notes_file.write_text(f"# {topic}\n\n## Understanding\n\n## Key Concepts\n\n## Code Examples\n\n## Resources\n\n## Checkpoint\n")
            
            # Create a code example file
            code_file = topic_dir / "code-examples.php"
            if not code_file.exists():
                code_file.write_text(f"<?php\n\n// {topic}\n// Add code examples here\n\n")
    
    print("\n✅ Folder structure created successfully!")
    print(f"\n📂 Location: {learning_dir.resolve()}")
    print("\n📋 Structure created:")
    print_tree(learning_dir, prefix="")
    
    print("\n💡 Features:")
    print("   ✓ 5 Phase folders")
    print("   ✓ 32 Topic subfolders")
    print("   ✓ notes.md template in each topic")
    print("   ✓ code-examples.php for each topic")
    print("\n💡 Next steps:")
    print("   1. Add your learning notes in notes.md")
    print("   2. Add code examples in code-examples.php")
    print("   3. Track your progress through index.html")
    print("   4. Export progress reports weekly")


def print_tree(directory, prefix="", max_depth=3, current_depth=0):
    """Print a tree structure of the directory"""
    if current_depth >= max_depth:
        return
    
    try:
        entries = sorted(directory.iterdir(), key=lambda x: x.name)
        dirs = [e for e in entries if e.is_dir()]
        
        for i, d in enumerate(dirs):
            is_last = i == len(dirs) - 1
            current_prefix = "└── " if is_last else "├── "
            print(f"{prefix}{current_prefix}{d.name}/")
            
            next_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(d, next_prefix, max_depth, current_depth + 1)
    except PermissionError:
        pass


if __name__ == "__main__":
    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        create_roadmap_structure()
        print("\n🎉 All done! Happy learning! 🚀\n")
    except KeyboardInterrupt:
        print("\n\n❌ Script interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
