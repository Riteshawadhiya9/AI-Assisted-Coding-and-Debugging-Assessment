

export default function BackgroundGrid() {
  return (
    <div className="pointer-events-none fixed inset-0 z-0 overflow-hidden">
      {/* Grid Pattern Overlay */}
      <div 
        className="absolute inset-0 opacity-[0.04]"
        style={{
          backgroundImage: `
            linear-gradient(to right, #6366f1 1px, transparent 1px),
            linear-gradient(to bottom, #6366f1 1px, transparent 1px)
          `,
          backgroundSize: '40px 40px',
        }}
      ></div>

      {/* Abstract Glowing Blobs */}
      <div className="absolute -top-[10%] -left-[20%] w-[60%] h-[60%] rounded-full bg-indigo-700/10 blur-[120px] opacity-70"></div>
      <div className="absolute top-[40%] -right-[10%] w-[50%] h-[50%] rounded-full bg-purple-700/10 blur-[100px] opacity-60"></div>
      <div className="absolute -bottom-[10%] left-[10%] w-[40%] h-[40%] rounded-full bg-blue-700/10 blur-[90px] opacity-50"></div>
    </div>
  );
}
