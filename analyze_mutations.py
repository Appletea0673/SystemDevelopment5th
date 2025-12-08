#!/usr/bin/env python
"""Analyze cosmic-ray mutation testing results."""

import json
import subprocess
import sys

# Run cosmic-ray dump and parse results
result = subprocess.run(
    ["cosmic-ray", "dump", "cosmic-ray.sqlite"],
    capture_output=True,
    text=True
)

if result.returncode != 0:
    print(f"Error running cosmic-ray dump: {result.stderr}")
    sys.exit(1)

# Parse JSON lines
data = []
for line in result.stdout.strip().split('\n'):
    if line.strip():
        try:
            entry = json.loads(line)
            # Each line is a list with 2 elements: [job_info, result_info]
            if isinstance(entry, list) and len(entry) >= 2:
                data.append(entry[1])  # Get the result part
        except json.JSONDecodeError:
            continue

# Count outcomes
killed = sum(1 for d in data if d.get('test_outcome') == 'killed')
survived = sum(1 for d in data if d.get('test_outcome') == 'survived')
incompetent = sum(1 for d in data if d.get('test_outcome') == 'incompetent')
timeout = sum(1 for d in data if d.get('test_outcome') == 'timeout')
total = len(data)

# Print results
print("\n" + "="*50)
print("🧬 Cosmic Ray Mutation Testing Results")
print("="*50)
print(f"\n📊 Total mutations tested: {total}")
print(f"\n✅ Killed (テストが検出):     {killed:3d}  ({killed/total*100:.1f}%)" if total > 0 else "")
print(f"❌ Survived (テストが未検出):  {survived:3d}  ({survived/total*100:.1f}%)" if total > 0 else "")
print(f"💀 Incompetent (コード破損):   {incompetent:3d}  ({incompetent/total*100:.1f}%)" if total > 0 else "")
if timeout > 0:
    print(f"⏰ Timeout:                    {timeout:3d}  ({timeout/total*100:.1f}%)")

if total > 0:
    kill_rate = killed / total * 100
    print(f"\n🎯 Mutation Kill Rate: {kill_rate:.1f}%")
    print("\n" + "="*50)
    
    if kill_rate >= 80:
        print("素晴らしい！テストの品質が非常に高いです！")
    elif kill_rate >= 60:
        print("良好です。さらにテストを追加することで改善できます。")
    else:
        print("⚠️  テストカバレッジを改善する必要があります。")
    
    if survived > 0:
        print(f"\n⚠️  {survived}個のミューテーションが生き残りました。")
        print("   追加のテストが必要な可能性があります。")
