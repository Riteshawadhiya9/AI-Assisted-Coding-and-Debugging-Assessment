import json
import re

def create_visual_for_question_and_cases(q):
    qid = q["id"]
    topic = q.get("topic", "")
    subtopic = q.get("subtopic", "")
    title = q.get("title", "")

    # 1. SPECIFIC CUSTOM VISUAL DATA GENERATION PER QUESTION ID / TOPIC
    # =========================================================================

    # --- 1. TREES ---
    if topic == "trees":
        # Check if we can parse tree array
        for i, tc in enumerate(q.get("visibleTestCases", [])):
            inp = tc["input"]
            tree_match = re.search(r'\[([0-9,\s\-nullNULL]+)\]', inp)
            if tree_match:
                items = [None if x.strip().lower() in ('null', '') else int(x.strip()) for x in tree_match.group(1).split(',')]
                tc["visualData"] = {
                    "type": "tree",
                    "title": f"Example {i+1}: Tree Hierarchy",
                    "data": items
                }
            else:
                tc["visualData"] = {
                    "type": "tree",
                    "title": f"Example {i+1}: Tree Nodes",
                    "data": [3, 9, 20, None, None, 15, 7]
                }
        if not q.get("visualData"):
            q["visualData"] = q["visibleTestCases"][0].get("visualData")

    # --- 2. GRAPHS ---
    elif topic == "graphs":
        for i, tc in enumerate(q.get("visibleTestCases", [])):
            inp = tc["input"]
            # Check for grid matrix in graph (e.g. number of islands, flood fill)
            matrix_match = re.search(r'\[\s*\[.*?\]\s*\]', inp, re.DOTALL)
            if matrix_match and ("island" in qid or "flood" in qid or "grid" in subtopic):
                try:
                    cleaned = matrix_match.group(0).replace("'", '"')
                    parsed_grid = json.loads(cleaned)
                    tc["visualData"] = {
                        "type": "matrix",
                        "title": f"Example {i+1}: Graph Grid Map",
                        "data": parsed_grid
                    }
                    continue
                except Exception:
                    pass

            # Otherwise graph topology with nodes & edges
            lines = [l.strip() for l in inp.split('\n') if l.strip()]
            edges = []
            nodes_set = set()
            for line in lines:
                parts = line.split()
                if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
                    u, v = parts[0], parts[1]
                    w = int(parts[2]) if len(parts) >= 3 and parts[2].isdigit() else None
                    if w is not None:
                        edges.append([u, v, w])
                    else:
                        edges.append([u, v])
                    nodes_set.add(u)
                    nodes_set.add(v)
            
            if edges:
                nodes = sorted(list(nodes_set), key=lambda x: int(x))
                tc["visualData"] = {
                    "type": "graph",
                    "title": f"Example {i+1}: Graph Network",
                    "data": {
                        "nodes": nodes,
                        "edges": edges,
                        "directed": "directed" in qid or "cycle" in qid or "topo" in qid or "course" in qid
                    }
                }
            elif "0 1" in inp or "edges" in inp:
                tc["visualData"] = {
                    "type": "graph",
                    "title": f"Example {i+1}: Graph Structure",
                    "data": {
                        "nodes": ["0", "1", "2", "3"],
                        "edges": [["0", "1"], ["1", "2"], ["2", "3"]],
                        "directed": True
                    }
                }
            else:
                tc["visualData"] = {
                    "type": "graph",
                    "title": f"Example {i+1}: Graph Topology",
                    "data": {
                        "nodes": ["0", "1", "2", "3"],
                        "edges": [["0", "1"], ["0", "2"], ["1", "3"], ["2", "3"]],
                        "directed": False
                    }
                }
        if not q.get("visualData"):
            q["visualData"] = q["visibleTestCases"][0].get("visualData")

    # --- 3. 2D DYNAMIC PROGRAMMING ---
    elif topic == "2ddp":
        if "unique_paths" in qid:
            q["visualData"] = {
                "type": "matrix",
                "title": "3x7 Robot Path Matrix",
                "data": [
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 2, 3, 4, 5, 6, 7],
                    [1, 3, 6, 10, 15, 21, 28]
                ]
            }
            if len(q.get("visibleTestCases", [])) >= 1:
                q["visibleTestCases"][0]["visualData"] = {
                    "type": "matrix",
                    "title": "Case 1: 3x7 Grid Path Matrix (Result = 28)",
                    "data": [
                        [1, 1, 1, 1, 1, 1, 1],
                        [1, 2, 3, 4, 5, 6, 7],
                        [1, 3, 6, 10, 15, 21, 28]
                    ]
                }
            if len(q.get("visibleTestCases", [])) >= 2:
                q["visibleTestCases"][1]["visualData"] = {
                    "type": "matrix",
                    "title": "Case 2: 3x2 Grid Path Matrix (Result = 3)",
                    "data": [
                        [1, 1],
                        [1, 2],
                        [1, 3]
                    ]
                }
        elif "min_path_sum" in qid:
            q["visualData"] = {
                "type": "matrix",
                "title": "Grid Cost Matrix (Min Path = 1 -> 3 -> 1 -> 1 -> 1 = 7)",
                "data": [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
            }
            if len(q.get("visibleTestCases", [])) >= 1:
                q["visibleTestCases"][0]["visualData"] = {
                    "type": "matrix",
                    "title": "Case 1: 3x3 Cost Grid",
                    "data": [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
                }
            if len(q.get("visibleTestCases", [])) >= 2:
                q["visibleTestCases"][1]["visualData"] = {
                    "type": "matrix",
                    "title": "Case 2: 2x3 Cost Grid",
                    "data": [[1, 2, 3], [4, 5, 6]]
                }
        else:
            for i, tc in enumerate(q.get("visibleTestCases", [])):
                inp = tc["input"]
                matrix_match = re.search(r'\[\s*\[.*?\]\s*\]', inp, re.DOTALL)
                if matrix_match:
                    try:
                        cleaned = matrix_match.group(0).replace("'", '"')
                        parsed_grid = json.loads(cleaned)
                        tc["visualData"] = {
                            "type": "matrix",
                            "title": f"Example {i+1}: DP Table",
                            "data": parsed_grid
                        }
                        continue
                    except Exception:
                        pass
                tc["visualData"] = {
                    "type": "matrix",
                    "title": f"Example {i+1}: 2D DP State Matrix",
                    "data": [
                        [0, 0, 0, 0],
                        [0, 1, 1, 1],
                        [0, 1, 2, 3]
                    ]
                }
            if not q.get("visualData"):
                q["visualData"] = q["visibleTestCases"][0].get("visualData")

    # --- 4. ADVANCED DSA / ARRAYS / LINKED LISTS ---
    else:
        for i, tc in enumerate(q.get("visibleTestCases", [])):
            inp = tc["input"]
            arr_match = re.search(r'\[([0-9,\s\-\"\'a-zA-Z]+)\]', inp)
            if "list" in qid or "link" in subtopic:
                items = [x.strip().strip('"\'') for x in arr_match.group(1).split(',') if x.strip()] if arr_match else ["1", "2", "3", "4", "5"]
                tc["visualData"] = {
                    "type": "linkedList",
                    "title": f"Example {i+1}: Linked Node Chain",
                    "data": items[:7]
                }
            elif arr_match:
                items = [x.strip().strip('"\'') for x in arr_match.group(1).split(',') if x.strip()]
                tc["visualData"] = {
                    "type": "array",
                    "title": f"Example {i+1}: Memory Block Array",
                    "data": items[:8]
                }
            else:
                tc["visualData"] = {
                    "type": "blocks",
                    "title": f"Example {i+1}: Input Block Values",
                    "data": [inp.replace('\n', ' ')[:24]]
                }
        if not q.get("visualData"):
            q["visualData"] = q["visibleTestCases"][0].get("visualData")

def main():
    path = "server/src/data/questions.json"
    with open(path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    for q in questions:
        create_visual_for_question_and_cases(q)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2)

    print(f"Successfully generated high-resolution visual diagrams for all {len(questions)} questions and test cases!")

if __name__ == "__main__":
    main()
