import React from 'react';
import type { VisualData } from '../types';

interface VisualDiagramProps {
  visualData?: VisualData;
  className?: string;
}

export default function VisualDiagram({ visualData, className = '' }: VisualDiagramProps) {
  if (!visualData || !visualData.data) return null;

  const { type, data, title } = visualData;

  return (
    <div className={`bg-slate-950/80 border border-slate-800 rounded-xl p-4 space-y-2 overflow-x-auto ${className}`}>
      {title && (
        <div className="text-[10px] font-bold uppercase tracking-wider text-indigo-400">
          {title}
        </div>
      )}

      {/* 1. BINARY TREE DIAGRAM */}
      {type === 'tree' && renderTreeDiagram(data)}

      {/* 2. GRAPH DIAGRAM */}
      {type === 'graph' && renderGraphDiagram(data)}

      {/* 3. 2D MATRIX / GRID DIAGRAM */}
      {type === 'matrix' && renderMatrixDiagram(data)}

      {/* 4. LINKED LIST DIAGRAM */}
      {type === 'linkedList' && renderLinkedListDiagram(data)}

      {/* 5. ARRAY / BLOCK DIAGRAM */}
      {(type === 'array' || type === 'blocks') && renderArrayDiagram(data)}
    </div>
  );
}

// Tree visual rendering using SVG or recursive layout
function renderTreeDiagram(data: any) {
  // If array format: [3, 9, 20, null, null, 15, 7]
  const arr = Array.isArray(data) ? data : data.nodes || [];
  if (arr.length === 0) return null;

  return (
    <div className="flex flex-col items-center py-2 select-none overflow-x-auto">
      <svg className="w-full max-w-[340px] h-[130px]" viewBox="0 0 340 130">
        <defs>
          <linearGradient id="treeNodeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#6366f1" />
            <stop offset="100%" stopColor="#4338ca" />
          </linearGradient>
        </defs>

        {/* Level 0: Root (idx 0) */}
        {arr[0] !== null && arr[0] !== undefined && (
          <>
            {/* Edge to Left child (idx 1) */}
            {arr[1] !== null && arr[1] !== undefined && (
              <line x1="170" y1="24" x2="100" y2="64" stroke="#475569" strokeWidth="2" />
            )}
            {/* Edge to Right child (idx 2) */}
            {arr[2] !== null && arr[2] !== undefined && (
              <line x1="170" y1="24" x2="240" y2="64" stroke="#475569" strokeWidth="2" />
            )}
            <circle cx="170" cy="24" r="15" fill="url(#treeNodeGrad)" stroke="#818cf8" strokeWidth="1.5" />
            <text x="170" y="28" fill="#ffffff" fontSize="11" fontWeight="bold" textAnchor="middle">
              {arr[0]}
            </text>
          </>
        )}

        {/* Level 1: Left (idx 1) & Right (idx 2) */}
        {arr[1] !== null && arr[1] !== undefined && (
          <>
            {/* Edge to Left child (idx 3) */}
            {arr[3] !== null && arr[3] !== undefined && (
              <line x1="100" y1="64" x2="60" y2="106" stroke="#475569" strokeWidth="2" />
            )}
            {/* Edge to Right child (idx 4) */}
            {arr[4] !== null && arr[4] !== undefined && (
              <line x1="100" y1="64" x2="140" y2="106" stroke="#475569" strokeWidth="2" />
            )}
            <circle cx="100" cy="64" r="14" fill="#1e293b" stroke="#6366f1" strokeWidth="1.5" />
            <text x="100" y="68" fill="#e2e8f0" fontSize="10" fontWeight="bold" textAnchor="middle">
              {arr[1]}
            </text>
          </>
        )}

        {arr[2] !== null && arr[2] !== undefined && (
          <>
            {/* Edge to Left child (idx 5) */}
            {arr[5] !== null && arr[5] !== undefined && (
              <line x1="240" y1="64" x2="200" y2="106" stroke="#475569" strokeWidth="2" />
            )}
            {/* Edge to Right child (idx 6) */}
            {arr[6] !== null && arr[6] !== undefined && (
              <line x1="240" y1="64" x2="280" y2="106" stroke="#475569" strokeWidth="2" />
            )}
            <circle cx="240" cy="64" r="14" fill="#1e293b" stroke="#6366f1" strokeWidth="1.5" />
            <text x="240" y="68" fill="#e2e8f0" fontSize="10" fontWeight="bold" textAnchor="middle">
              {arr[2]}
            </text>
          </>
        )}

        {/* Level 2: Leaves (idx 3, 4, 5, 6) */}
        {[
          { idx: 3, x: 60, y: 106 },
          { idx: 4, x: 140, y: 106 },
          { idx: 5, x: 200, y: 106 },
          { idx: 6, x: 280, y: 106 }
        ].map(({ idx, x, y }) => {
          if (arr[idx] === null || arr[idx] === undefined) return null;
          return (
            <React.Fragment key={idx}>
              <circle cx={x} cy={y} r="12" fill="#0f172a" stroke="#475569" strokeWidth="1.5" />
              <text x={x} y={y + 4} fill="#cbd5e1" fontSize="9" fontWeight="bold" textAnchor="middle">
                {arr[idx]}
              </text>
            </React.Fragment>
          );
        })}
      </svg>
    </div>
  );
}

// Graph visual rendering using SVG coordinates
function renderGraphDiagram(data: any) {
  const nodes = data.nodes || [];
  const edges = data.edges || [];
  const directed = !!data.directed;

  // Compute circular layout for nodes
  const count = nodes.length;
  const radius = 45;
  const cx = 140;
  const cy = 60;

  const nodePositions: Record<string, { x: number; y: number }> = {};
  nodes.forEach((node: any, i: number) => {
    const id = typeof node === 'object' ? node.id : String(node);
    const angle = (i * 2 * Math.PI) / Math.max(1, count) - Math.PI / 2;
    nodePositions[id] = {
      x: cx + radius * Math.cos(angle),
      y: cy + radius * Math.sin(angle)
    };
  });

  return (
    <div className="flex justify-center py-2 select-none">
      <svg className="w-[280px] h-[130px]" viewBox="0 0 280 130">
        <defs>
          <marker
            id="arrow"
            viewBox="0 0 10 10"
            refX="20"
            refY="5"
            markerWidth="6"
            markerHeight="6"
            orient="auto-start-reverse"
          >
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#818cf8" />
          </marker>
        </defs>

        {/* Edges */}
        {edges.map(([u, v, weight]: [any, any, any?], i: number) => {
          const uPos = nodePositions[String(u)];
          const vPos = nodePositions[String(v)];
          if (!uPos || !vPos) return null;

          const midX = (uPos.x + vPos.x) / 2;
          const midY = (uPos.y + vPos.y) / 2;

          return (
            <React.Fragment key={i}>
              <line
                x1={uPos.x}
                y1={uPos.y}
                x2={vPos.x}
                y2={vPos.y}
                stroke="#6366f1"
                strokeWidth="1.8"
                strokeOpacity="0.75"
                markerEnd={directed ? 'url(#arrow)' : undefined}
              />
              {weight !== undefined && (
                <text x={midX} y={midY - 4} fill="#a5b4fc" fontSize="9" fontWeight="bold" textAnchor="middle">
                  {weight}
                </text>
              )}
            </React.Fragment>
          );
        })}

        {/* Nodes */}
        {nodes.map((node: any) => {
          const id = typeof node === 'object' ? node.id : String(node);
          const label = typeof node === 'object' ? node.label || node.id : String(node);
          const pos = nodePositions[id];
          if (!pos) return null;

          return (
            <React.Fragment key={id}>
              <circle cx={pos.x} cy={pos.y} r="14" fill="#1e293b" stroke="#818cf8" strokeWidth="2" />
              <text x={pos.x} y={pos.y + 4} fill="#ffffff" fontSize="10" fontWeight="bold" textAnchor="middle">
                {label}
              </text>
            </React.Fragment>
          );
        })}
      </svg>
    </div>
  );
}

// 2D Matrix / Grid visual rendering
function renderMatrixDiagram(data: any) {
  const grid: any[][] = Array.isArray(data) ? data : data.grid || [];
  if (!grid || grid.length === 0) return null;

  return (
    <div className="flex justify-center py-2 select-none overflow-x-auto">
      <div className="inline-block border border-slate-700 bg-slate-900 rounded-lg overflow-hidden shadow-lg">
        <table className="border-collapse text-xs font-mono text-center">
          <tbody>
            {grid.map((row, r) => (
              <tr key={r}>
                {row.map((cell, c) => (
                  <td
                    key={c}
                    className="border border-slate-800 px-3.5 py-2 font-bold text-slate-200 hover:bg-indigo-600/20 transition-colors"
                  >
                    {String(cell)}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

// Linked List visual rendering
function renderLinkedListDiagram(data: any) {
  const list: any[] = Array.isArray(data) ? data : data.nodes || [];
  if (list.length === 0) return null;

  return (
    <div className="flex items-center gap-1.5 py-3 overflow-x-auto select-none">
      {list.map((node, i) => (
        <React.Fragment key={i}>
          <div className="bg-[#1e293b] border border-indigo-500/50 rounded-lg px-3 py-1.5 text-xs font-bold text-white font-mono shadow-[0_0_10px_rgba(99,102,241,0.15)] shrink-0">
            {String(node)}
          </div>
          <span className="text-indigo-400 font-bold text-xs shrink-0 select-none">──&gt;</span>
        </React.Fragment>
      ))}
      <div className="bg-slate-900 border border-slate-800 rounded-lg px-2.5 py-1.5 text-[11px] font-semibold text-slate-500 font-mono shrink-0">
        NULL
      </div>
    </div>
  );
}

// Array / Blocks visual rendering
function renderArrayDiagram(data: any) {
  const arr = Array.isArray(data) ? data : data.elements || [];
  if (arr.length === 0) return null;

  return (
    <div className="flex flex-wrap items-center gap-2 py-2 overflow-x-auto select-none">
      {arr.map((item: any, i: number) => (
        <div key={i} className="flex flex-col items-center">
          <div className="bg-slate-900 border border-indigo-500/40 hover:border-indigo-400 rounded-lg min-w-[36px] h-9 px-2 flex items-center justify-center font-mono font-bold text-xs text-white shadow-sm transition-all">
            {String(item)}
          </div>
          <span className="text-[9px] text-slate-500 font-mono mt-0.5">[{i}]</span>
        </div>
      ))}
    </div>
  );
}
