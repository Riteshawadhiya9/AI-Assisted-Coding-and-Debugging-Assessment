import json
import os
import sys

from bank_arrays import ARRAY_QUESTIONS
from bank_strings import STRING_QUESTIONS
from bank_hashmap import HASHMAP_QUESTIONS
from bank_trees import TREE_QUESTIONS
from bank_trees_missing import MISSING_TREE_QUESTIONS
from bank_bst_missing import MISSING_BST_QUESTIONS
from bank_recursion import RECURSION_QUESTIONS
from bank_dp import DP_QUESTIONS
from bank_dp_missing import MISSING_DP_QUESTIONS
from bank_2ddp import DP2D_QUESTIONS
from bank_2ddp_missing import MISSING_2DDP_QUESTIONS
from bank_graphs import GRAPH_QUESTIONS
from bank_graphs_missing import MISSING_GRAPH_QUESTIONS
from bank_advanced import ADVANCED_QUESTIONS

ALL_QUESTION_MODULES = [
    ("Arrays", ARRAY_QUESTIONS),
    ("Strings", STRING_QUESTIONS),
    ("HashMap/HashSet", HASHMAP_QUESTIONS),
    ("Trees/BST", TREE_QUESTIONS),
    ("Trees (Expanded)", MISSING_TREE_QUESTIONS),
    ("BST (Expanded)", MISSING_BST_QUESTIONS),
    ("Recursion/Backtracking", RECURSION_QUESTIONS),
    ("Dynamic Programming", DP_QUESTIONS),
    ("DP (Expanded)", MISSING_DP_QUESTIONS),
    ("2D DP / Matrix DP", DP2D_QUESTIONS),
    ("2D DP (Expanded)", MISSING_2DDP_QUESTIONS),
    ("Graphs", GRAPH_QUESTIONS),
    ("Graphs (Expanded)", MISSING_GRAPH_QUESTIONS),
    ("Advanced DSA", ADVANCED_QUESTIONS),
]

def validate_and_compile():
    compiled_questions = []
    seen_ids = set()
    seen_titles = set()
    
    topic_counts = {}
    difficulty_counts = {"easy": 0, "medium": 0, "hard": 0}
    lang_coverage = {"c": 0, "cpp": 0, "java": 0}
    
    print("==================================================")
    print("COMPILING & VALIDATING UNIVERSAL QUESTION BANK")
    print("==================================================")
    
    for category_name, questions in ALL_QUESTION_MODULES:
        print(f"\nProcessing category: {category_name} ({len(questions)} questions)")
        for q in questions:
            qid = q.get("id")
            title = q.get("title")
            
            # Validation: ID uniqueness
            if not qid:
                raise ValueError(f"Missing ID in question: {q}")
            if qid in seen_ids:
                raise ValueError(f"Duplicate Question ID detected: {qid}")
            seen_ids.add(qid)
            
            # Validation: Title uniqueness
            if title in seen_titles:
                raise ValueError(f"Duplicate Question Title detected: {title}")
            seen_titles.add(title)
            
            # Validation: Required fields
            required_fields = [
                "problemStatement", "topic", "subtopic", "difficulty",
                "estimatedTime", "primaryBugType", "bugConcept",
                "intendedApproach", "explanation", "constraints",
                "visibleTestCases", "hiddenTestCases", "expectedComplexity",
                "tags", "implementations"
            ]
            for field in required_fields:
                if field not in q or q[field] is None:
                    raise ValueError(f"Question {qid} is missing required field: {field}")
            
            # Validation: Implementations must include C, C++, and Java
            impls = q["implementations"]
            for lang in ["c", "cpp", "java"]:
                if lang not in impls:
                    raise ValueError(f"Question {qid} is missing {lang} implementation")
                if not impls[lang].get("buggyCode") or not impls[lang].get("buggyCode").strip():
                    raise ValueError(f"Question {qid} has empty buggyCode for {lang}")
                if not impls[lang].get("correctCode") or not impls[lang].get("correctCode").strip():
                    raise ValueError(f"Question {qid} has empty correctCode for {lang}")
                # Validation: Buggy code must NEVER contain bug-revealing comments
                buggy_code = impls[lang]["buggyCode"]
                banned_comment_patterns = [
                    r'//\s*(?:BUG|incorrect|fix|wrong|intentional|this causes|TODO)',
                    r'/\*.*?(?:BUG|incorrect|fix|wrong|intentional|this causes|TODO).*?\*/'
                ]
                import re
                for pat in banned_comment_patterns:
                    if re.search(pat, buggy_code, re.IGNORECASE | re.DOTALL):
                        raise ValueError(f"Question {qid} contains forbidden bug-revealing comments in {lang} buggyCode!")
                lang_coverage[lang] += 1
            
            # Set fallback legacy top-level buggyCode / correctCode / language
            q["language"] = "cpp"
            q["buggyCode"] = impls["cpp"]["buggyCode"]
            q["correctCode"] = impls["cpp"]["correctCode"]
            
            # Count statistics
            topic = q["topic"]
            topic_counts[topic] = topic_counts.get(topic, 0) + 1
            
            diff = q["difficulty"].lower()
            if diff in difficulty_counts:
                difficulty_counts[diff] += 1
            
            compiled_questions.append(q)
            
    print("\n--------------------------------------------------")
    print(f"Total Questions Compiled: {len(compiled_questions)}")
    print(f"Unique IDs: {len(seen_ids)}")
    print("--------------------------------------------------")
    print("\nTopic Breakdown:")
    for topic, count in sorted(topic_counts.items()):
        print(f"  - {topic:20s}: {count}")
        
    print("\nDifficulty Breakdown:")
    total = len(compiled_questions)
    for diff, count in difficulty_counts.items():
        pct = (count / total) * 100 if total > 0 else 0
        print(f"  - {diff.capitalize():10s}: {count:2d} ({pct:5.1f}%)")
        
    print("\nLanguage Support Coverage:")
    for lang, count in lang_coverage.items():
        pct = (count / total) * 100 if total > 0 else 0
        print(f"  - {lang.upper():6s}: {count}/{total} ({pct:.0f}%)")
        
    output_path = os.path.join(os.path.dirname(__file__), "questions.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(compiled_questions, f, indent=2, ensure_ascii=False)
        
    print(f"\nSuccessfully wrote {len(compiled_questions)} questions to {output_path}!")
    return compiled_questions

if __name__ == "__main__":
    validate_and_compile()
