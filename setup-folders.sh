#!/bin/bash

# Create folder structure for Junior Laravel Developer Roadmap
# This script creates Phase folders with Topic subfolders

set -e

echo "🚀 Creating Junior Laravel Developer Roadmap folder structure..."
echo ""

# Create main Learning directory
mkdir -p Learning
cd Learning

# ======================== PHASE 00 ========================
echo "📁 Creating Phase 00: Fill the Critical Gaps..."
mkdir -p "Phase 00 - Fill the Critical Gaps"/{
  "01 - OOP Pillars",
  "02 - SOLID Principles",
  "03 - Dependency Injection & IoC",
  "04 - N+1 Problem - Full Mastery",
  "05 - CSRF & XSS",
  "06 - SQL Injection",
  "Checkpoint"
}

# ======================== PHASE 01 ========================
echo "📁 Creating Phase 01: Laravel Deep Mastery..."
mkdir -p "Phase 01 - Laravel Deep Mastery"/{
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
  "Checkpoint"
}

# ======================== PHASE 02 ========================
echo "📁 Creating Phase 02: Database & Performance..."
mkdir -p "Phase 02 - Database & Performance"/{
  "01 - MySQL Joins - All Types",
  "02 - Indexing - Deep Mastery",
  "03 - Transactions & Data Integrity",
  "04 - Query Optimization",
  "05 - Database Migrations - Advanced",
  "06 - Redis & Caching Strategy",
  "Checkpoint"
}

# ======================== PHASE 03 ========================
echo "📁 Creating Phase 03: Security, Testing & Clean Code..."
mkdir -p "Phase 03 - Security, Testing & Clean Code"/{
  "01 - Security - All Major Attacks",
  "02 - Testing - PHPUnit & Pest",
  "03 - Clean Code Practices",
  "04 - Error Handling & Logging",
  "05 - Git - Professional Level",
  "06 - API Documentation",
  "Checkpoint"
}

# ======================== PHASE 04 ========================
echo "📁 Creating Phase 04: Job-Ready Polish..."
mkdir -p "Phase 04 - Job-Ready Polish"/{
  "01 - Portfolio Project - Exam Management API",
  "02 - Interview Preparation",
  "03 - Freelance Setup",
  "04 - Deployment Basics",
  "05 - PHP 8 Modern Features",
  "06 - What's Next After Junior",
  "Checkpoint"
}

echo ""
echo "✅ Folder structure created successfully!"
echo ""
echo "📂 Directory tree:"
tree -L 2 || find . -type d | sort | sed 's|^\./||' | awk '
  BEGIN { FS = "/" }
  {
    depth = NF - 1
    for (i = 0; i < depth; i++) printf "  "
    print "├── " $NF
  }
'

echo ""
echo "📍 Location: $(pwd)"
echo ""
echo "💡 Next steps:"
echo "   1. Create notes files in each topic folder"
echo "   2. Add code examples and practice projects"
echo "   3. Track your progress through each phase"
echo ""
