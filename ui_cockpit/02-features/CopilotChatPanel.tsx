import React, { useState } from 'react';

export const CopilotChatPanel: React.FC<{ apiEndpoint: string }> = ({ apiEndpoint }) => {
  const [messages, setMessages] = useState<Array<{ sender: string; text: string }>>([
    { sender: 'copilot', text: "Bonjour, je suis votre assistant Copilot Sommelier & Accords Vins. Comment puis-je vous aider ?" }
  ]);

  return (
    <div style={ display: 'flex', flexDirection: 'column', height: '100%', border: '1px solid #e5e7eb', borderRadius: 8 }>
      <div style={ padding: 12, borderBottom: '1px solid #e5e7eb', fontWeight: 'bold' }>
        Copilot Sommelier & Accords Vins
      </div>
      <div style={ flex: 1, padding: 12, overflowY: 'auto' }>
        {messages.map((m, idx) => (
          <div key={idx} style={ marginBottom: 8, textAlign: m.sender === 'user' ? 'right' : 'left' }>
            <span style={ background: m.sender === 'user' ? '#3b82f6' : '#f3f4f6', color: m.sender === 'user' ? '#fff' : '#000', padding: '6px 12px', borderRadius: 12, display: 'inline-block' }>
              {m.text}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
