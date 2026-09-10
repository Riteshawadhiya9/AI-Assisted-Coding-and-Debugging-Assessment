import json
import re

def parse_visual_data_from_input(topic, subtopic, input_str, title_prefix="Test Case"):
    # Try parsing matrix: [[...], [...]]
    matrix_match = re.search(r'\[\s*\[.*?\]\s*\]', input_str, re.DOTALL)
    if matrix_match:
        try:
            # clean single quotes to double quotes for json
            cleaned = matrix_match.group(0).replace("'", '"')
            parsed = json.loads(cleaned)
            if isinstance(parsed, list) and len(parsed) > 0 and isinstance(parsed[0], list):
                return {
                    "type": "matrix",
                    "title": f"{title_prefix} Grid Matrix",
                    "data": parsed
                }
        except Exception:
            pass

    # Try parsing tree input: [3,9,20,null,null,15,7] or root = [...]
    if topic == 'trees' or 'tree' in subtopic:
        tree_match = re.search(r'\[([0-9,\s\-nullNULL]+)\]', input_str)
        if tree_match:
            try:
                raw_items = [x.strip() for x in tree_match.group(1).split(',')]
                parsed = []
                for item in raw_items:
                    if item.lower() == 'null' or item == '':
                        parsed.append(None)
                    else:
                        parsed.append(int(item))
                if len(parsed) > 0:
                    return {
                        "type": "tree",
                        "title": f"{title_prefix} Binary Tree",
                        "data": parsed
                    }
            except Exception:
                pass

    # Try parsing graph input: V = 4, E = 4\n0 1\n1 2... or edges = [[...]]
    if topic == 'graphs' or 'graph' in subtopic:
        # Check for edge list in text format
        lines = [l.strip() for l in input_str.strip().split('\n') if l.strip()]
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
        
        if len(edges) > 0:
            nodes = sorted(list(nodes_set), key=lambda x: int(x))
            return {
                "type": "graph",
                "title": f"{title_prefix} Graph Topology",
                "data": {
                    "nodes": nodes,
                    "edges": edges,
                    "directed": "directed" in subtopic or "cycle" in subtopic or "topo" in subtopic or "dijkstra" in subtopic
                }
            }

    # Try parsing linked list or array: [1,2,3,4,5] or nums = [...]
    arr_match = re.search(r'\[([0-9,\s\-\"\'a-zA-Z]+)\]', input_str)
    if arr_match:
        try:
            raw_items = [x.strip().strip('"\'') for x in arr_match.group(1).split(',') if x.strip()]
            if 'list' in subtopic or 'link' in subtopic:
                return {
                    "type": "linkedList",
                    "title": f"{title_prefix} Linked List",
                    "data": raw_items[:8]
                }
            elif len(raw_items) > 0:
                return {
                    "type": "array",
                    "title": f"{title_prefix} Array Elements",
                    "data": raw_items[:10]
                }
        except Exception:
            pass

    # Fallback general block diagram
    return {
        "type": "blocks",
        "title": f"{title_prefix} Data Input",
        "data": [input_str.replace('\n', ' ')[:30]]
    }

def main():
    path = "server/src/data/questions.json"
    with open(path, "r", encoding="utf-8") as f:
        questions = json.load(f)

    for q in questions:
        topic = q.get("topic", "")
        subtopic = q.get("subtopic", "")

        # 1. Ensure question-level visualData
        if not q.get("visualData"):
            first_input = q["visibleTestCases"][0]["input"] if q.get("visibleTestCases") else ""
            q["visualData"] = parse_visual_data_from_input(topic, subtopic, first_input, f"{q['title']} Structure")

        # 2. Ensure every visible test case has visualData
        for i, tc in enumerate(q.get("visibleTestCases", [])):
            tc["visualData"] = parse_visual_data_from_input(topic, subtopic, tc["input"], f"Example {i+1}")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2)

    print(f"Successfully enriched {len(questions)} questions and their visible test cases with visual diagrams!")

if __name__ == "__main__":
    main()
