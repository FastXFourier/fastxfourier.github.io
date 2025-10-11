# How to Add New Problems

This guide explains how to add new problems to your website. The new system uses a simple YAML file instead of manual HTML editing.

## Quick Start

To add a new problem, simply edit the `problems.yaml` file and add a new entry. That's it! 🎉

## Step-by-Step Guide

### 1. Open `problems.yaml`

Located in the root directory of your project.

### 2. Add Your Problem Entry

Add a new entry following this template:

```yaml
  - id: your_problem_id
    title: Problem Title in Thai or English
    link: https://url-to-problem-statement.com
    difficulty: Very Easy | Easy | Medium | Hard
    source: TOI | POSN1 | Codeforces | etc.
    topics:
      - Topic 1
      - Topic 2
      - Topic 3
    solution: /problems/your_problem_id  # Optional - defaults to /problems/{id}
```

### 3. Example - Adding a New Problem

Let's say you want to add a new TOI problem:

```yaml
  - id: toi21_quartet
    title: toi21_quartet
    link: https://api.otog.in.th/problem/doc/1091
    difficulty: Medium
    source: TOI
    topics:
      - Dynamic Programming
      - Graph Theory
```

### 4. Build Your Site

Run MkDocs to see your changes:

```bash
mkdocs serve
```

The problem will automatically appear on your problems page with:

- ✅ Proper difficulty badge (colored based on difficulty)
- ✅ Source tag
- ✅ Filterable by difficulty, source, and topics
- ✅ Link to problem statement
- ✅ Link to your solution page

## Field Reference

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `id` | ✅ Yes | Unique identifier for the problem | `toi21_quartet` |
| `title` | ✅ Yes | Display title | `ข้อสอบ POSN1 2567 ข้อ 1` |
| `link` | ✅ Yes | URL to problem statement | `https://grader.gchan.moe/...` |
| `difficulty` | ✅ Yes | One of: `Very Easy`, `Easy`, `Medium`, `Hard` | `Medium` |
| `source` | ✅ Yes | Problem source/contest | `TOI`, `POSN1`, `Codeforces` |
| `topics` | ✅ Yes | List of topic tags | `[Dynamic Programming, Math]` |
| `solution` | ❌ No | Custom solution URL (defaults to `/problems/{id}`) | `/problems/custom_path` |

## Difficulty Levels

Choose one of these difficulty levels:

- **Very Easy** - Basic problems, fundamental concepts (Green badge)
- **Easy** - Simple applications of concepts (Light green badge)
- **Medium** - Requires combining multiple concepts (Orange badge)
- **Hard** - Advanced problems, complex algorithms (Red badge)

## Common Topics

Here are some commonly used topic tags:

**Basics:**

- `C/C++ Basics`
- `Arrays`
- `Strings`
- `Math`
- `Sorting`

**Data Structures:**

- `Data Structures`
- `Stack`
- `Queue`
- `Heap`
- `Disjoint Set Union`

**Algorithms:**

- `Dynamic Programming`
- `Greedy`
- `Graph Theory`
- `Tree`
- `Binary Search`
- `Two Pointers`

**Advanced:**

- `Bitmask`
- `Segment Tree`
- `Fenwick Tree`

> **Tip:** You can create new topics as needed! The filter system will automatically include them.

## Creating the Solution Page

After adding a problem to `problems.yaml`, create the solution file:

1. Create a new markdown file in `docs/problems/` named `{id}.md`
   - Example: `docs/problems/toi21_quartet.md`

2. Write your solution in the file (see existing solutions for examples)

3. The "View Solution" link will automatically point to this page!

## Benefits of This System

✨ **Before:** Manual HTML editing, copy-pasting div tags, careful attribute management  
✨ **After:** 7 lines of clean YAML

✨ **Before:** Filters needed manual updating  
✨ **After:** Filters automatically update based on YAML data

✨ **Before:** 300+ lines of repetitive HTML  
✨ **After:** 7 lines per problem, everything auto-generated

## Troubleshooting

### Problem doesn't appear?

1. Check YAML syntax (indentation matters!)
2. Ensure all required fields are present
3. Run `mkdocs serve` and check for errors in terminal

### Filters not working?

The JavaScript and CSS are auto-generated. If filters don't work:

1. Clear your browser cache
2. Check browser console for JavaScript errors

### Want to change the order?

Problems appear in the order they're listed in `problems.yaml`. Simply reorder them in the file!

## Questions?

If you have questions about adding problems, check the existing entries in `problems.yaml` for examples, or refer to the generated `docs/problems/index.md` to see how problems are displayed.

---

**Happy problem adding! 🚀**
